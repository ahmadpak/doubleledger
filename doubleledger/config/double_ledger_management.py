from __future__ import unicode_literals
import frappe
from frappe import _

def get_data():
    return[
        {
            "label": ("Setup"),
            "items": [
				{
					"type": "doctype",
					"name": "Double Ledger Parties",
					"onboard": 1,
					"label": _("Double Ledger Parties"),
					"description": _(" Managing Parties that act as both customers and suppliers"),
				}
			]
        }
    ]
