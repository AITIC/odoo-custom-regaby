# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = "account.move"

    use_manual_number = fields.Boolean(
        related='journal_id.use_manual_number',
        string='Use Manual Number?',
    )
    manual_number = fields.Char(
        string='Invoice Manual Number',
        copy=False,
        readonly=False,
        tracking=True,
        index=True,
    )

    @api.constrains('manual_number')
    def _check_unique_supplier_invoice_number_insensitive(self):
        """
        Check if another customer invoice has the same manual_number
        and the same commercial_partner_id as the current instance.
        """
        for rec in self:
            if rec.manual_number and \
                    rec.move_type in ('out_invoice', 'out_refund'):
                same_inv = rec.search([
                    ('commercial_partner_id', '=',
                     rec.commercial_partner_id.id),
                    ('move_type', 'in', ('out_invoice', 'out_refund')),
                    ('manual_number', '=ilike', rec.manual_number),
                    ('id', '!=', rec.id)
                ], limit=1)
                if same_inv:
                    raise ValidationError(_(
                        "The invoice/refund with manual number '%s' "
                        "already exists in Odoo under the number '%s' "
                        "for partner '%s'.") % (
                            same_inv.manual_number,
                            same_inv.name or '-',
                            same_inv.partner_id.display_name))

    @api.depends(
        'name',
        'l10n_latam_document_number',
        'l10n_latam_document_type_id.doc_code_prefix',
        'manual_number',
        'use_manual_number',
    )
    def _compute_display_name(self):
        TYPES = {
            'out_invoice': _('Invoice'),
            'in_invoice': _('Vendor Bill'),
            'out_refund': _('Credit Note'),
            'in_refund': _('Vendor Credit note'),
        }
        for rec in self:
            if rec.l10n_latam_document_number and rec.l10n_latam_document_type_id \
                    and not rec.use_manual_number:
                display_name = ("%s%s" % (
                    rec.l10n_latam_document_type_id.doc_code_prefix or '',
                    rec.l10n_latam_document_number))
            elif rec.use_manual_number and rec.manual_number and rec.l10n_latam_document_type_id:
                display_name = ("%s%s" % (
                    rec.l10n_latam_document_type_id.doc_code_prefix or '',
                    rec.manual_number))
            else:
                display_name = rec.name or TYPES.get(rec.move_type, '')
            rec.display_name = display_name
