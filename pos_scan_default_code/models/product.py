# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    modelo_articulo = fields.Char('Modelo Artículo')

    def _load_pos_data_fields(self, config_id):
        fields = super()._load_pos_data_fields(config_id)
        if 'modelo_articulo' not in fields:
            fields.append('modelo_articulo')
        return fields
