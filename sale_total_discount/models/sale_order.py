# -*- coding: utf-8 -*-
# Copyright 2018 Uakami - Manuel Marquez <buzondemam@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    discount_rate_id = fields.Many2one('discount.rate', 'Discount Rate')

    @api.onchange('partner_id')
    def update_discount_rate(self):
        """Updates value of discount rate when customer changes"""

        self.discount_rate_id = self.partner_id.discount_rate_id

    @api.multi
    def _update_discount(self):
        """Updates value of discount when product quantity changes"""

        products_qty = sum(self.order_line.mapped('product_uom_qty'))

        discount_rate = self.discount_rate_id
        discount_rate_lines = discount_rate.line_ids.sorted(
            key=lambda line: line.min_qty
        )

        last_line = discount_rate_lines[-1]
        for line_pos in range(len(discount_rate_lines)):

            line = discount_rate_lines[line_pos]

            if line != last_line:
                next_line = discount_rate_lines[line_pos + 1]

                if products_qty >= line.min_qty and \
                   products_qty < next_line.min_qty:

                    # FIXME: consider cases where the discount rate is a fixed
                    # amount
                    if line.discount_type == 'percentage' and \
                       line.percentage > 0:

                        for sale_line in self.order_line:
                            sale_line.discount = line.percentage

                        break

            else:

                if products_qty >= line.min_qty:

                    # FIXME: consider cases where the discount rate is a fixed
                    # amount
                    if line.discount_type == 'percentage' and \
                       line.percentage > 0:

                        for sale_line in self.order_line:
                            sale_line.discount = line.percentage

    @api.onchange('order_line', 'discount_rate_id')
    def onchange_order_line(self):

        if self.order_line and self.discount_rate_id:
            self._update_discount()
