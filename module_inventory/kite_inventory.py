from openerp import tools
from openerp.osv import osv, fields
from openerp.tools.translate import _
import time
import openerp.addons.decimal_precision as dp

class kite_inventory(osv.osv):

	_name = "kite.inventory"
	_description = "Kite Inventory"
	
	_columns = {
		'supplier': fields.char('Supplier',size=128,required=True,readonly=False),
		'creation_date':fields.date('Creation Date',readonly=True),
		'state': fields.selection([('draft', 'Draft'),('cancel', 'Cancelled'),('confirm', 'Confirmed')],'Status',readonly=False),
		'active':fields.boolean('Active'),
		'grn_no': fields.char('GRN NO',size=128,required=True,readonly=False),
		'line_id':fields.one2many('kite.inventory.line','product_id','module line'),
		
		
	}
	_defaults = {
		'creation_date': fields.date.context_today,
		'state':'draft',
		'active':True,
		
	   }
	def create(self, cr, uid, vals,context=None):		
		if vals.get('name','/')=='/':
			vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'kite.inventory') or '/'
		order =  super(kite_inventory, self).create(cr, uid, vals, context=context)
		return order
	def confirm_module(self,cr,uid,ids,context=None):
		module_plan_obj = self.pool.get('kite.inventory')
		rec = self.browse(cr,uid,ids[0])
		rec.write({'state':'confirm'})
	
kite_inventory()
class kite_inventory_line(osv.osv):
	_name = "kite.inventory.line"
	_description = "Kite Inventory line"
	
	_columns = {
		
		'item_name':fields.char('Item name',size=128,required=True),
		'unit_price':fields.float('Unit Price',size=128),
		'required_qty':fields.float('Required Qty',size=128),
		'total_price':fields.float('Total price',size=128),
		'product_id':fields.many2one('kite.inventory','Product line'),
	}
	
kite_inventory_line()
