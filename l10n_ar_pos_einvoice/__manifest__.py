# -*- coding: utf-8 -*-
{
    'name': 'POS einvoice AR',
    'version': '19.0.0.1.0',
    'author': 'Ing. Gabriela Rivero',
    'license': 'LGPL-3',
    'category': 'Point Of Sale',
    'website': 'www.galup.com.ar',
    'description': 'Este módulo permite imprimir opcionalmente la factura desde el POS.',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_config.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            '/l10n_ar_pos_einvoice/static/src/js/pos.js',
            '/l10n_ar_pos_einvoice/static/src/xml/pos_payment.xml',
        ],
    },
    'installable': False,
}
