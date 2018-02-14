# -*- coding: utf-8 -*-
# Copyright 2018 Uakami - Manuel Marquez <buzondemam@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sale_validity_date = fields.Boolean(
        'Set validity date automatically in sale orders')
    sale_validity_date_based_on = fields.Selection(
        [('payment_deadline', 'Payment Deadline'),
         ('time', 'Time (days)')], 'Based on', default='payment_deadline')
    sale_validity_date_cancel_inv_sp = fields.Boolean(
        'Cancel invoice and stock picking')
