# -*- coding: utf-8 -*-
# Copyright 2018 Uakami - Manuel Marquez <buzondemam@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class DiscountRate(models.Model):
    _name = 'discount.rate'

    name = fields.Char(required=True)
    line_ids = fields.One2many(
        'discount.rate.line', 'discount_rate_id', 'Items')
    company_id = fields.Many2one('res.company')
    active = fields.Boolean('Active', default=True)


class DiscountRateLine(models.Model):
    _name = 'discount.rate.line'

    min_qty = fields.Float('Minimum Quantity', required=True)
    discount_type = fields.Selection([
        ('percentage', 'Percentage'), ('fixed', 'Amount Fixed')
    ], 'Discount Type', required=True)
    percentage = fields.Float('Percentage')
    amount = fields.Float('Amount')
    discount_rate_id = fields.Many2one('discount.rate', 'Discount Rate')
