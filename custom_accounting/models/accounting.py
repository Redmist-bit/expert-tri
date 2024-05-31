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
    
class ModelName(models.Model):
    
    _inherit = 'account.move'

    to_check = fields.Boolean(
    string='To Check',
    default=True,
    tracking=True,
    help="testitng",
)