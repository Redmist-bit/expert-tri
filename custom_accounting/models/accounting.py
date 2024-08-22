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

class NamaModel(models.Model):
    _inherit = 'stock.move'

    sale_line_id = fields.Many2one('sale.order.line', string='Sale Order Line')
    description_picking = fields.Text('Description of Picking', related='sale_line_id.name')

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    stock_move_ids = fields.One2many('stock.move', 'sale_line_id', string='Stock Moves')

    
    

    