# -*- coding: utf-8 -*-
{
    'name': 'POS einvoice ticket',
    'version': '19.0.0.1.0',
    'author': 'Ing. Gabriela Rivero',
    'license': 'LGPL-3',
    'category': 'Point Of Sale',
    'website': 'www.galup.com.ar',
    'depends': [
        'point_of_sale',
        'l10n_ar',
    ],
    'data': [
        'views/pos_config.xml',
    ],
    'assets': {
        "point_of_sale._assets_pos": [
            "/l10n_ar_pos_einvoice_ticket/static/src/js/pos_model.js",
            "/l10n_ar_pos_einvoice_ticket/static/src/css/pos_receipts.css",
            "l10n_ar_pos_einvoice_ticket/static/src/xml/pos_ticket.xml",
        ],
    },
    'installable': True,
}
