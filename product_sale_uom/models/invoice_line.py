# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    product_uom_original = fields.Many2one('uom.uom', 'Unit of Measure Sale', required=False)
    product_qty_original = fields.Float(string='Quantity', digits='Product Unit of Measure', required=False)
