from openerp import tools
from openerp.osv import osv, fields
from openerp.tools.translate import _
import time
import openerp.addons.decimal_precision as dp
import openerp.tools as tools

class kite_deliverymaster(osv.osv):

	_name = "kite.deliverymaster"
	_description = "Kite deliverymaster"

	
	_columns = {
		'Customer_name': fields.char('Customer name',size=128, select=True,required=True,readonly=True,states={'draft': [('readonly', False)]}),
		'Delivery_date':fields.date('Delivery date',readonly=True),
		'Delivery_No':fields.float('Delivery No',size=128),
		'Delivery_time': fields.float('Delivery time',size=128),
		'line_id':fields.one2many('kite.deliverymaster.line','Item_Name','product line',readonly=True,states={'draft': [('readonly', False)]}),
		'GRN_type':fields.selection([('direct','Direct'),('fromcp','From Purchase Planning')],'GRN Type',readonly=True,states={'draft': [('readonly', False)]}),
		'DC_Date':fields.date('DC Date',readonly=True),
		'creation_Date':fields.date('creation Date',readonly=True),
		'Created_By': fields.char('Created By',size=128, select=True,required=True,readonly=True,states={'draft': [('readonly', False)]}),
	}
	_defaults = {
		'GRN_date': fields.date.context_today,
		#~ 'status':'draft',
	   }
	def create(self, cr, uid, vals,context=None):		
		if vals.get('name','/')=='/':
			vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'kite.deliverymaster') or '/'
		order =  super(kite_deliverymaster, self).create(cr, uid, vals, context=context)
		return order
	def confirm_purchase(self,cr,uid,ids,context=None):
		#~ purchase_plan_obj = self.pool.get('kite.general.planning')
		rec = self.browse(cr,uid,ids[0])
		rec.write({'state':'confirm'})
	

kite_deliverymaster()
class kite_deliverymaster_line(osv.osv):
	_name = "kite.customermaster.line"
	_description = "Kite deliverymaster line"
	
	_columns = {
		
		'Item_Name':fields.char('Item_Name',size=128,required=True),
		#'UCN':fields.many2one('product.product','',required=True),
		#'type_product':fields.many2one('kg.purchase','Product Type',readonly=True,invisible=True),
		'Quantity':fields.float('Quantity',size=128),
		'Price_unit':fields.float('Price unit',size=128),
		'Amount':fields.float('Amount',size=128),
		'product_line':fields.many2one('kite.deliverymaster','Product line'),
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
kite_deliverymaster_line()
