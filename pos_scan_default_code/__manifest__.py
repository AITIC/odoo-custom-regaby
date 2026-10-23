# -*- coding: utf-8 -*-
{
    'name': 'POS Scan Default Code',
    'version': '19.0.0.1.0',
    'author': 'Ing. Gabriela Rivero',
    'license': 'LGPL-3',
    'category': 'Point Of Sale',
    'website': 'www.galup.com.ar',
    'summary': 'This module allows scan default code in POS and by a new product field modelo_articulo',
    'depends': ['point_of_sale'],
    'data': [
        'views/product_view.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            '/pos_scan_default_code/static/src/js/pos_scan.js',
        ],
    },
    'installable': False,
}
