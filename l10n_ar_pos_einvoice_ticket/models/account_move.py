from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    l10n_ar_include_vat = fields.Boolean(
        compute='_compute_l10n_ar_include_vat',
        store=True,
    )

    @api.depends('l10n_latam_use_documents', 'journal_id',
                 'company_id', 'partner_id', 'l10n_latam_document_type_id')
    def _compute_l10n_ar_include_vat(self):
        for move in self:
            move.l10n_ar_include_vat = move._l10n_ar_include_vat()