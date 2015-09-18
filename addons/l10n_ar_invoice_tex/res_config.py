# -*- coding: utf-8 -*-
from openerp import models, fields, api


class invoice_tex_config_settings(models.TransientModel):
    _name = 'l10n_ar_invoice_tex.config.settings'
    _inherit = 'res.config.settings'

    invtex_show_bonif = fields.Boolean(
        string="Show bonification",
        default=True
    )
    invtex_lines_size = fields.Selection(
        selection=[('small', 'Small'),
                   ('normal', 'Normal'),
                   ('big', 'Big')],
        string="Line sizes",
        default='normal',
        required=True
    )

    @api.model
    def get_default_company_values(self, fields):
        company = self.env.user.company_id
        return {
            'invtex_show_bonif': company.invtex_show_bonif,
            'invtex_lines_size': company.invtex_lines_size,
        }

    @api.one
    def set_company_values(self):
        company = self.env.user.company_id
        company.invtex_show_bonif = self.invtex_show_bonif
        company.invtex_lines_size = self.invtex_lines_size

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: