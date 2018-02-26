from openerp import tools
from openerp.osv import osv, fields
from openerp.tools.translate import _
import time
import openerp.addons.decimal_precision as dp
import openerp.tools as tools

class kg_purchase(osv.osv):

	_name = "kg.purchase"
	_description = "KG Purchase"
	_order = "creation_date desc"
	
	_columns = {
		'name': fields.char('Number',size=128, select=True,required=True,readonly=True,states={'draft': [('readonly', False)]}),
		'creation_date':fields.date('Creation Date',readonly=True),
		'state': fields.selection([('draft', 'Draft'),('cancel', 'Cancelled'),('confirm', 'Confirmed')],'Status',readonly=False),
		'line_id':fields.one2many('kg.purchase.line','product_id','product line',readonly=True,states={'draft': [('readonly', False)]}),
		'active':fields.boolean('Active'),
		'plan_type':fields.selection([('direct','Direct'),('fromcp','From Purchase Planning')],'Product Type',readonly=True,states={'draft': [('readonly', False)]}),

		
	}
	_defaults = {
		'creation_date': fields.date.context_today,
		'state':'draft',
		'active':True,
		
	   }
	def create(self, cr, uid, vals,context=None):		
		if vals.get('name','/')=='/':
			vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'kg.purchase') or '/'
		order =  super(kg_purchase, self).create(cr, uid, vals, context=context)
		return order
	def confirm_purchase(self,cr,uid,ids,context=None):
		purchase_plan_obj = self.pool.get('kg.purchase.planning')
		rec = self.browse(cr,uid,ids[0])
		rec.write({'state':'confirm'})
	

kg_purchase()
class kg_purchase_line(osv.osv):
	_name = "kg.purchase.line"
	_description = "KG Purchase line"
	
	_columns = {
		
		'product_code':fields.char('Product Code',size=128,required=True),
		'product_name':fields.many2one('product.product','Product Name',required=True),
		#'type_product':fields.many2one('kg.purchase','Product Type',readonly=True,invisible=True),
		'unit_price':fields.float('Unit Price'),
		'required_qty':fields.float('Required Qty'),
		'total_price':fields.float('Total price'),
		'product_id':fields.many2one('kg.purchase','Product line'),
		'pro_type':fields.selection([('direct','Direct'),('fromcp','From purchase Plan')],'Production Type'),
	}
	_defaults = {
		'pro_type' : 'direct',
		}
	def onchange_product(self, cr, uid, ids,product_name,unit_price,context=None):
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
		return {'value': res}
kg_purchase_line()
