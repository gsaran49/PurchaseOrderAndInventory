from openerp import tools
from openerp.osv import osv, fields
from openerp.tools.translate import _
import time
import openerp.addons.decimal_precision as dp

class module_inventory(osv.osv):

	_name = "module.inventory"
	_description = "Module Inventory"
	
	_columns = {
		'suppiler': fields.char('Supplier',size=128,required=True,readonly=False),
		'creation_date':fields.date('Creation Date',readonly=True),
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
class module_inventory_line(osv.osv):
	_name = "module.inventory.line"
	_description = "Module Inventory line"
	
	_columns = {
		
		'item_name':fields.char('Item name',size=128,required=True),
		'unit_price':fields.float('Unit Price'),
		'required_qty':fields.float('Required Qty'),
		'total_price':fields.float('Total price'),
		'product_id':fields.many2one('module.inventory','Product line'),
	}
module_inventory_line()
