from openerp import tools
from openerp.osv import osv, fields
from openerp.tools.translate import _
import time
import openerp.addons.decimal_precision as dp

class kite_inventory_GRN(osv.osv):

	_name = "kite.inventory.GRN"
	_description = "kite Inventory GRN"
	
	_columns = {
		'supplier': fields.char('Supplier',size=128,required=True,readonly=False),
		'Invoice/DC date':fields.date('Invoice/DC date',readonly=True),
		'state': fields.selection([('draft', 'Draft'),('cancel', 'Cancelled'),('confirm', 'Confirmed')],'Status',readonly=False),
		'active':fields.boolean('Active'),
		'grn_no': fields.char('GRN NO',size=128,required=True,readonly=False),
		'line_id':fields.one2many('module.inventory.line','product_id','module line'),
		
		
	}
	_defaults = {
		'creation_date': fields.date.context_today,
		'state':'draft',
		'active':True,
		
	   }
	def create(self, cr, uid, vals,context=None):		
		if vals.get('name','/')=='/':
			vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'module.inventory') or '/'
		order =  super(kg_module, self).create(cr, uid, vals, context=context)
		return order
	def confirm_module(self,cr,uid,ids,context=None):
		module_plan_obj = self.pool.get('module.inventory')
		rec = self.browse(cr,uid,ids[0])
		rec.write({'state':'confirm'})
	
module_inventory()
class kite_inventory_GRN_line(osv.osv):
	_name = "kite.inventory.GRN.line"
	_description = "kite Inventory GRN line"
	
	_columns = {
		
		'product':fields.char('product',size=128,required=True),
		'unit_price':fields.float('Unit Price'),
		'required_qty':fields.float('Required Qty'),
		'total_price':fields.float('Total price'),
		'product_id':fields.many2one('kite.inventory.GRN','Product line'),
	}
module_inventory_line()
