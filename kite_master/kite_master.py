from openerp import tools
from openerp.osv import osv, fields
from openerp.tools.translate import _
import time
import openerp.addons.decimal_precision as dp
import openerp.tools as tools

class kite_master(osv.osv):

	_name = "kite.master"
	_description = "Kite master"
	
	_columns = {
		'customer': fields.char('Number',size=128, select=True,required=True,readonly=True,states={'draft': [('readonly', False)]}),
		'date':fields.date('Date',readonly=True),
		'invoice_address': fields.char('invoice_address',size=128, select=True,required=True,readonly=False,states={'draft': [('readonly', False)]}),
		'delivary_address': fields.char('delivary_address',size=128, select=True,required=True,readonly=False,states={'draft': [('readonly', False)]}),
		'shop': fields.char('shop',size=128, select=True,required=True,readonly=False,states={'draft': [('readonly', False)]}),
		'line_id':fields.one2many('kite.master.line','product','product line',readonly=True,states={'draft': [('readonly', False)]}),
	}
	_defaults = {
		'date': fields.date.context_today,
		#'state':'draft',
		#'active':True,
		
	   }
	def create(self, cr, uid, vals,context=None):		
		if vals.get('name','/')=='/':
			vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'kite.master') or '/'
		order =  super(kite_master, self).create(cr, uid, vals, context=context)
		return order
	def confirm_purchase(self,cr,uid,ids,context=None):
		purchase_plan_obj = self.pool.get('kite.master.planning')
		rec = self.browse(cr,uid,ids[0])
		rec.write({'state':'confirm'})
	

kite_master()
class kite_master_line(osv.osv):
	_name = "kite.master.line"
	_description = "Kite master line"
	
	_columns = {
		
		'product':fields.char('Product',size=128,required=True),
		'Descrption':fields.many2one('product.product','customer',required=True),
		#'type_product':fields.many2one('kg.purchase','Product Type',readonly=True,invisible=True),
		'Quantity':fields.float('Quantity',size=128),
		'unit_measure':fields.float('unit_measure',size=128),
		'unit_price':fields.float('unit_price',size=128),
		'sub_total':fields.float('sub_total',size=128),
		 
	}
	_defaults = {
		#'pro_type' : 'direct',
		}
	'''def onchange_product(self, cr, uid, ids,product_name,unit_price,context=None):
		price = ""
		value = {'unit_price':''}
		partner_obj = self.pool.get('product.product')
		result = partner_obj.browse(cr, uid, product_name)
		if result:
			price = result.list_price 
			value={'unit_price':price}
			return {'value': value} 
			
	def onchange_result(self, cr, uid, ids,unit_price,required_qty, context=None):
		res = {}
		if unit_price and required_qty :
			res['total_price'] = unit_price * required_qty
		return {'value': res}'''
kite_master_line()
