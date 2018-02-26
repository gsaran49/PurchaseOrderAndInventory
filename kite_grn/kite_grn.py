from openerp import tools
from openerp.osv import osv, fields
from openerp.tools.translate import _
import time
import openerp.addons.decimal_precision as dp
import openerp.tools as tools

class kite_grn(osv.osv):

	_name = "kite.grn"
	_description = "Kite grn"
	_order = "GRN_date desc"
	
	_columns = {
		'supplier': fields.char('Number',size=128, select=True,required=True,readonly=True,states={'draft': [('readonly', False)]}),
		'GRN_date':fields.date('GRN Date',readonly=True),
		'GRN_No':fields.float('GRN No',size=128),
		'state': fields.selection([('draft', 'Draft'),('cancel', 'Cancelled'),('confirm', 'Confirmed')],'Status',readonly=False),
		'line_id':fields.one2many('kite.grn.line','product_id','product line',readonly=True,states={'draft': [('readonly', False)]}),
		'active':fields.boolean('Active'),
		'GRN_type':fields.selection([('direct','Direct'),('fromcp','From Purchase Planning')],'GRN Type',readonly=True,states={'draft': [('readonly', False)]}),
		'Inward_Type':fields.selection([('direct','Direct'),('fromcp','From Purchase Planning')],'Inward Type',readonly=True,states={'draft': [('readonly', False)]}),
		'InvoiceDC_Date':fields.date('InvoiceDC Date',readonly=False),
		'LR_Date':fields.date('LR Date',readonly=False),
	}
	_defaults = {
		'GRN_date': fields.date.context_today,
		'state':'draft',
		'active':True,
		
	   }
	def create(self, cr, uid, vals,context=None):		
		if vals.get('name','/')=='/':
			vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'kite.grn') or '/'
		order =  super(kite_grn, self).create(cr, uid, vals, context=context)
		return order
	def confirm_purchase(self,cr,uid,ids,context=None):
		purchase_plan_obj = self.pool.get('kite.grn.planning')
		rec = self.browse(cr,uid,ids[0])
		rec.write({'state':'confirm'})
	

kite_grn()
class kite_grn_line(osv.osv):
	_name = "kite.grn.line"
	_description = "Kite grn line"
	
	_columns = {
		
		'po_Qty':fields.char('Product Qty',size=128,required=True),
		'product':fields.many2one('product.product','Product',required=True),
		#'type_product':fields.many2one('kg.purchase','Product Type',readonly=True,invisible=True),
		'challen_Qty':fields.float('Challen Qty',size=128),
		'Required_qty':fields.float('Required Qty',size=128),
		'Accepted_Qty':fields.float('Accepted Qty',size=128),
		'product_id':fields.many2one('kite.grn','Product line'),
		'pro_type':fields.selection([('direct','Direct'),('fromcp','From purchase Plan')],'Production Type'),
	}
	_defaults = {
		'pro_type' : 'direct',
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
kite_grn_line()
