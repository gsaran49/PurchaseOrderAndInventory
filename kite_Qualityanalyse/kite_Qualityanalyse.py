from openerp import tools
from openerp.osv import osv, fields
from openerp.tools.translate import _
import time
import openerp.addons.decimal_precision as dp
import openerp.tools as tools

class kite_Qualityanalyse(osv.osv):

	_name = "kite.Qualityanalyse"
	_description = "Kite Qualityanalyse"
	_order = "GRN_date desc"
	
	_columns = {
		'supplier': fields.char('Number',size=128, select=True,required=True,readonly=True,states={'draft': [('readonly', False)]}),
		'GRN_date':fields.date('GRN Date',readonly=True),
		'GRN_No':fields.integer('GRN No',size=128),
		'state': fields.selection([('draft', 'Draft'),('cancel', 'Cancelled'),('confirm', 'Confirmed')],'Status',readonly=False),
		'line_id':fields.one2many('kite.Qualityanalyse.line','Item_Name','product line',readonly=True,states={'draft': [('readonly', False)]}),
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
			vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'kite.Qualityanalyse') or '/'
		order =  super(kite_Qualityanalyse, self).create(cr, uid, vals, context=context)
		return order
	def confirm_purchase(self,cr,uid,ids,context=None):
		#~ purchase_plan_obj = self.pool.get('kite.general.planning')
		rec = self.browse(cr,uid,ids[0])
		rec.write({'state':'confirm'})
	

kite_Qualityanalyse()
class kite_Qualityanalyse_line(osv.osv):
	_name = "kite.Qualityanalyse.line"
	_description = "Kite Qualityanalyse line"
	
	_columns = {
		
		'Item_Name':fields.char('Item_Name',size=128,required=True),
		'Quantity':fields.integer('Quantity',size=128),
		'Price_unit':fields.integer('Price unit',size=128),
		'Amount':fields.integer('Amount',size=128),
		'product_line':fields.many2one('kite.Qualityanalyse','Product line'),
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
kite_Qualityanalyse_line()
