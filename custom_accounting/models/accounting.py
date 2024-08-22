from odoo import Command, _, api, fields, models
from odoo.exceptions import UserError,ValidationError
import math
import logging
import math
import numpy_financial 
from datetime import datetime
from dateutil.relativedelta import relativedelta



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
    purchase_line_ids = fields.One2many('purchase.order.line', 'sale_line_id', string='Purchase Order Lines', readonly=True, copy=False)
    # purchase_ids = fields.One2many('purchase.order.line', 'sale_line_id', string='Stock Moves')


class Pruchase(models.Model):
    _inherit = 'purchase.order.line'
    # purchase_line_ids = fields.Many2one('sale.order.line', string='Sale Order Line')

    name = fields.Text(string='Description', related='sale_line_id.name', required=True, compute='_compute_price_unit_and_date_planned_and_name', store=True, readonly=False)
    
    
        
    

    @api.onchange('name')
    def _onchange_field(self):
        self.name = self.sale_line_id


    
    


   

    
    

    