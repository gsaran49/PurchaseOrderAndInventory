from openerp import tools
from openerp.osv import osv, fields
from openerp.tools.translate import _
import time
import openerp.addons.decimal_precision as dp
import openerp.tools as tools

class kite_supplier(osv.osv):

	_name = "kite.supplier"
	_description = "Kite supplier"
	
	
	_columns = {
		'Name': fields.char('Name',size=128, select=True,required=True,readonly=True,states={'draft': [('readonly', False)]}),
		'Email':fields.char('Email',size=128),
		'state': fields.selection([('draft', 'Draft'),('cancel', 'Cancelled'),('confirm', 'Confirmed')],'Status',readonly=False),
		#'line_id':fields.one2many('kite.departmentmaster.line','Item_Name','product line',readonly=True,states={'draft': [('readonly', False)]}),
		'Phone_No':fields.integer('Phone No',readonly=False),
		'Website': fields.char('Website',size=128, select=True,required=True,readonly=False,states={'draft': [('readonly', False)]}),
	    'job_position':fields.char('job position',size=128),
	}
	'''_defaults = {
		#'GRN_date': fields.date.context_today,
		#~ 'status':'draft',
	   }'''
	def create(self, cr, uid, vals,context=None):		
		if vals.get('name','/')=='/':
			vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'kite.supplier') or '/'
		order =  super(kite_supplier, self).create(cr, uid, vals, context=context)
		return order
	def confirm_purchase(self,cr,uid,ids,context=None):
		#~ purchase_plan_obj = self.pool.get('kite.general.planning')
		rec = self.browse(cr,uid,ids[0])
		rec.write({'state':'confirm'})
	

kite_supplier()
