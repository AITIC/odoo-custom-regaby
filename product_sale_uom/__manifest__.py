# -*- coding: utf-8 -*-
{
    'name': 'Produc Sale UOM',
    'version': '19.0.0.1.0',
    'author': 'Ing. Gabriela Rivero',
    'license': 'LGPL-3',
    'category': 'Product',
    'website': 'www.galup.com.ar',
    'description': 'Este módulo permite elegir una unidad de venta en el producto',
    'depends': ['product', 'sale_management', 'stock', 'account'],
    'data': [
        'views/product_template_view.xml',
        'views/sale_view.xml',
        'views/stock_view.xml',
        'views/invoice_view.xml',
    ],
    'installable': False,
}
