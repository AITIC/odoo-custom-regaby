# -*- coding: utf-8 -*-
{
    'name': 'Journal Invoice Manual Number',
    'version': '19.0.0.1.0',
    'author': 'Ing. Gabriela Rivero',
    'license': 'LGPL-3',
    'category': 'Product',
    'website': 'www.galup.com.ar',
    'description': """Este módulo está pensando para poder asentar facturas de clientes viejas o anteriores a tener odoo implementado. \
    Es requisito poder asentar el número de factura en la factura de venta.
    Por lo tanto, se agrega en el journal un tilde Número manual (manual_number). Luego en la factura si está seteado ese tilde se muestra \
    un campo llamado igual.
    """,
    'depends': ['l10n_latam_invoice_document'],
    'data': [
        'views/journal_view.xml',
        'views/invoice_view.xml',
    ],
    'installable': False,
}
