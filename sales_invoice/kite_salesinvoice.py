from openerp import tools
from openerp.osv import osv, fields
from openerp.tools.translate import _
import time
import openerp.addons.decimal_precision as dp
import openerp.tools as tools

class kite_salesinvoice(osv.osv):

	_name = "kite.salesinvoice"
	_description = "Kite salesinvoice"
	
	_columns = {
		'Bill_No': fields.char('Bill Number',size=128, select=True,required=True,readonly=True,states={'draft': [('readonly', False)]}),
		'Date':fields.date('Date',readonly=True),
		'Phone_No':fields.integer('Phone number',size=128),
		'line_id':fields.one2many('kite.salesinvoice.line','Item_Name','product line',readonly=True,states={'draft': [('readonly', False)]}),
		'Amount':fields.integer('amount',size=128),
		'Tax':fields.integer('Tax',size=128),
		'state': fields.selection([('draft', 'Draft'),('cancel', 'Cancelled'),('confirm', 'Confirmed')],'Status',readonly=False),

	}
	_defaults = {
		'Date': fields.date.context_today,
		#~ 'status':'draft',
	   }
	def create(self, cr, uid, vals,context=None):		
		if vals.get('name','/')=='/':
			vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'kite.salesinvoice') or '/'
		order =  super(kite_salesinvoice, self).create(cr, uid, vals, context=context)
		return order
	def confirm_purchase(self,cr,uid,ids,context=None):
		#~ purchase_plan_obj = self.pool.get('kite.general.planning')
		rec = self.browse(cr,uid,ids[0])
		rec.write({'state':'confirm'})
	

kite_salesinvoice()
class kite_salesinvoice_line(osv.osv):
	_name = "kite.salesinvoice.line"
	_description = "Kite salesinvoice line"
	
	_columns = {
		
		'Item_Name':fields.char('Item_Name',size=128,required=True),
		#'UCN':fields.many2one('product.product','',required=True),
		#'type_product':fields.many2one('kg.purchase','Product Type',readonly=True,invisible=True),
		'Quantity':fields.float('Quantity',size=128),
		'Price_unit':fields.float('Price unit',size=128),
		'Amount':fields.float('Amount',size=128),
		'product_line':fields.many2one('kite.salesinvoice','Product line'),
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
kite_salesinvoice_line()
