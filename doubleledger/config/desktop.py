from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Double Ledger Management",
			"category": "Modules",
			"label": _("Double Ledger Management"),
			"color": "blue",
			"icon": "octicon octicon-book",
			"type": "module",
			"onboard_present": 1
			
		}
	]