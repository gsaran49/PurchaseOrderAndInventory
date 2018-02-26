from openerp import tools
from openerp.osv import osv, fields
from openerp.tools.translate import _
import time
from datetime import date
from datetime import datetime


class sales_invoice(osv.osv):
	_name = "sales.invoice"
	_description = "sales.invoice"
	_columns = {
	'Bill_no': fields.integer('Bill No',required=True),
	'customer_name':fields.many2one('res.partner','Customer Name',required=True),
	'state':fields.selection([('draft','draft'),('confirmed','Confirmed')],'Status'),
	'date': fields.date('Date',required=True),
	}
	_defaults = {
	'state':'draft',
	'date' : lambda * a: time.strftime('%Y-%m-%d'),
	}
	
	
		
		
		
	
sales_invoice()


