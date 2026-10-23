# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, exceptions


class StockMove(models.Model):
    _inherit = "stock.move"

    product_uom_original = fields.Many2one('uom.uom', 'Unit of Measure Sale', required=False)
    product_qty_original = fields.Float(
        string='Quantity',
        digits='Product Unit of Measure',
        required=False,
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'sale_line_id' in vals:
                order_line = self.env['sale.order.line'].browse(vals['sale_line_id'])
                vals['product_uom_original'] = order_line.product_uom_original.id
                vals['product_qty_original'] = order_line.product_uom_qty_original
        return super(StockMove, self).create(vals_list)
