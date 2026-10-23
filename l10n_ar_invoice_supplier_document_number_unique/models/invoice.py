# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = "account.move"

    @api.onchange('l10n_latam_document_type_id', 'l10n_latam_document_number')
    def validate_document_number(self):
        for rec in self.filtered(
                lambda x: not x.l10n_latam_sequence_id and x.l10n_latam_document_type_id):
            super(AccountMove, rec).validate_document_number()
            rec.ref = rec.l10n_latam_document_number
