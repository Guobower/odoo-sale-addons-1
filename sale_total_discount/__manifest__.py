# -*- coding: utf-8 -*-
# Copyright 2018 Uakami - Manuel Marquez <buzondemam@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Discounts over total of sales orders',
    'version': '11.0.0.1.0',
    'category': 'Sale',
    'author': 'Uakami',
    'website': "https://uakami.com/",
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'sales_team',
    ],
    'data': [
        'data/res_config_settings.xml',
        'views/discount_rate_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
