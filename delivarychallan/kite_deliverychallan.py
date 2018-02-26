from openerp import tools
from openerp.osv import osv, fields
from openerp.tools.translate import _
import time
import openerp.addons.decimal_precision as dp
import openerp.tools as tools

class kite_deliverychallan(osv.osv):

	_name = "kite.deliverychallan"
	_description = "Kite deliverychallan"
	
	_columns = {
		'customer_name': fields.char('customer name',size=128, select=True,required=True,readonly=True,states={'draft': [('readonly', False)]}),
		'entry_date':fields.date('entry Date',readonly=True),
		'Phone_No':fields.float('Phone No',size=128),
		'state': fields.selection([('draft', 'Draft'),('cancel', 'Cancelled'),('confirm', 'Confirmed')],'Status',readonly=False),
		'DC_Date':fields.date('DC Date',readonly=True),
		'user_id': fields.char('user id',size=128),
	}
	'''_defaults = {
		'entry_date': fields.date.context_today,
		#~ 'status':'draft',
	   }'''
	def create(self, cr, uid, vals,context=None):		
		if vals.get('name','/')=='/':
			vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'kite.deliverychallan') or '/'
		order =  super(kite_deliverychallan, self).create(cr, uid, vals, context=context)
		return order
	def confirm_purchase(self,cr,uid,ids,context=None):
		#~ purchase_plan_obj = self.pool.get('kite.general.planning')
		rec = self.browse(cr,uid,ids[0])
		rec.write({'state':'confirm'})
	

kite_deliverychallan()
