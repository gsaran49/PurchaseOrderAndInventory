from openerp import tools
from openerp.osv import osv, fields
from openerp.tools.translate import _
import time
import openerp.addons.decimal_precision as dp
import openerp.tools as tools

class kite_purchaseamendment(osv.osv):

	_name = "kite.purchaseamendment"
	_description = "Kite purchaseamendment"
	_order = "Amendment_date desc"
	
	_columns = {
		'supplier': fields.char('Supplier',size=128, select=True,required=True,readonly=True,states={'draft': [('readonly', False)]}),
		'Amendment_date':fields.date('Amendment Date',readonly=True),
		'Amendment_No':fields.float('Amendment No',size=128),
		'state': fields.selection([('draft', 'Draft'),('cancel', 'Cancelled'),('confirm', 'Confirmed')],'Status',readonly=False),
		'line_id':fields.one2many('kite.purchaseamendment.line','Product','product line',readonly=True,states={'draft': [('readonly', False)]}),
		'Bill_type':fields.char('Bill type',readonly=True),
		'Payment': fields.char('Payment',size=128, select=True,required=True,readonly=True,states={'draft': [('readonly', False)]}),
	}
	_defaults = {
		'Amendment_date': fields.date.context_today,
		#~ 'status':'draft',
	   }
	def create(self, cr, uid, vals,context=None):		
		if vals.get('name','/')=='/':
			vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'kite.purchaseamendment') or '/'
		order =  super(kite_purchaseamendment, self).create(cr, uid, vals, context=context)
		return order
	def confirm_purchase(self,cr,uid,ids,context=None):
		#~ purchase_plan_obj = self.pool.get('kite.general.planning')
		rec = self.browse(cr,uid,ids[0])
		rec.write({'state':'confirm'})
	

kite_purchaseamendment()
class kite_purchaseamendment_line(osv.osv):
	_name = "kite.purchaseamendment.line"
	_description = "Kite purchaseamendment line"
	
	_columns = {
		
		'Product':fields.char('Product',size=128,required=True),
		'Amendment Quantity':fields.integer('Quantity',size=128),
		'Amend Price':fields.integer('Price unit',size=128),
		'Amount':fields.integer('Amount',size=128),
		'total':fields.integer('total',size=128),
		'product_line':fields.many2one('kite.purchaseamendment','Product line'),
	}

	#~ '''def onchange_product(self, cr, uid, ids,product_name,unit_price,context=None):
		#~ price = ""
		#~ value = {'unit_price':''}
		#~ partner_obj = self.pool.get('product.product')
		#~ result = partner_obj.browse(cr, uid, product_name)
		#~ if result:
			#~ price = result.list_price 
			#~ value={'unit_price':price}
			#~ return {'value': value} 
			
	#~ def onchange_result(self, cr, uid, ids,unit_price,required_qty, context=None):
		#~ res = {}
		#~ if unit_price and required_qty :
			#~ res['total_price'] = unit_price * required_qty
		#~ return {'value': res}'''
kite_purchaseamendment_line()
