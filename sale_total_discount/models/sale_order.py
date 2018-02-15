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
