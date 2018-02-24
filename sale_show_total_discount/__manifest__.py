# -*- coding: utf-8 -*-
# Copyright 2018 Uakami - Manuel Marquez <buzondemam@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Show Total Discount in Sales Orders',
    'version': '11.0.1.0.1',
    'category': 'Sale',
    'author': 'Uakami',
    'website': "https://uakami.com/",
    'license': 'AGPL-3',
    'depends': [
        'sale',
    ],
    'data': [
        'views/sale_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
