from odoo import Command, _, api, fields, models
from odoo.exceptions import UserError,ValidationError
# import math
# import logging
import math
# import numpy_financial 
from datetime import datetime
from dateutil.relativedelta import relativedelta
# import locale



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
    
    def set_invoice_date(self,date):
            indonesian_month  = ['NN'
            , 'Januari'
            , 'Februari'
            , 'Maret'
            , 'April'
            , 'Mei'
            , 'Juni'
            , 'Juli'
            , 'Agustus'
            , 'September'
            , 'Oktober'
            , 'November'
            , 'Desember']
           
            date_format = datetime.strptime(str(date), '%d %B %Y')
            day = '{:02}'.format(date_format.day)
            date_return = day+' '+str(indonesian_month[int(date_format.month)])+' '+str(date_format.year)
            return date_return

class NamaModel(models.Model):
    _inherit = 'stock.move'

    sale_line_id = fields.Many2one('sale.order.line', string='Sale Order Line')
    description_picking = fields.Text('Description of Picking', related='sale_line_id.name')

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    stock_move_ids = fields.One2many('stock.move', 'sale_line_id', string='Stock Moves')
    purchase_line_ids = fields.One2many('purchase.order.line', 'sale_line_id', string='Purchase Order Lines', readonly=True, copy=False)

class Pruchase(models.Model):
    _inherit = 'purchase.order.line'

    
    sale_line_id = fields.Many2one('sale.order.line', string='Sale Order Line')

class purdchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button(self):
        for a in self.order_line:
            if a.sale_line_id.name:
                a.name = a.sale_line_id.name



    


   

    
    

    