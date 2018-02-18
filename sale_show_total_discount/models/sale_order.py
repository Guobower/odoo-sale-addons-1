# -*- coding: utf-8 -*-
# Copyright 2018 Uakami - Manuel Marquez <buzondemam@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_discount = fields.Float(compute='_compute_total_discount')

    @api.depends('order_line')
    def _compute_total_discount(self):
        """Computes value of field total_discount"""

        for record in self:
            record.total_discount = sum([
                line.price_unit * line.product_uom_qty
                for line in record.order_line
            ]) - record.amount_untaxed
