from odoo import models, fields


class custom_accounting(models.Model):
    _inherit = 'res.partner'
    
    invoice_list = fields.One2many('account.move', 'partner_id',
                                    string="Invoice Details",
                                    readonly=True,
                                    domain=(
                                    [('payment_state', '=', 'not_paid'),
                                        ('move_type', '=', 'out_invoice'),
                                        # ('move_type', '=', 'out_invoice'),
                                        ('state','=','posted')]))