# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class AccountJournal(models.Model):
    _inherit = "account.journal"

    use_manual_number = fields.Boolean(
        'Use Manual Number?',
    )
