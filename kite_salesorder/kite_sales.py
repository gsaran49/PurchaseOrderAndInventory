from openerp import tools
from openerp.osv import osv, fields
from openerp.tools.translate import _
import time
import openerp.addons.decimal_precision as dp
import openerp.tools as tools

class kite_sales(osv.osv):

	_name = "kite.sales"
	_description = "Kite sales"
	
	_columns = {
		'customer': fields.char('Number',size=128, select=True,required=True,readonly=True,states={'draft': [('readonly', False)]}),
		'date':fields.date('Date',readonly=True),
		'invoice_address': fields.char('invoice_address',size=128, select=True,required=True,readonly=False,states={'draft': [('readonly', False)]}),
		'delivery_address': fields.char('delivary_address',size=128, select=True,required=True,readonly=False,states={'draft': [('readonly', False)]}),
		'shop': fields.char('shop',size=128, select=True,required=True,readonly=False,states={'draft': [('readonly', False)]}),
		'line_id':fields.one2many('kite.sales.line','product','product line',readonly=True,states={'draft': [('readonly', False)]}),
	    'state': fields.selection([('draft', 'Draft'),('cancel', 'Cancelled'),('confirm', 'Confirmed')],'State',readonly=False),
	}
	_defaults = {
		'date': fields.date.context_today,
		
		 }
	
	

kite_sales()
class kite_sales_line(osv.osv):
	_name = "kite.sales.line"
	_description = "Kite sales line"
	
	_columns = {
		
		'product':fields.char('Product',size=128,required=True),
		'Descrption':fields.many2one('product.product','Product Qty',required=True),
		#'type_product':fields.many2one('kg.purchase','Product Type',readonly=True,invisible=True),
		'Quantity':fields.float('Quantity',size=128),
		'unit_measure':fields.float('unit_measure',size=128),
		'unit_price':fields.float('unit_price',size=128),
		'sub_total':fields.float('sub_total',size=128),
		 
	}
	
	
kite_sales_line()
