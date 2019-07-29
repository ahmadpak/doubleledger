# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"color": "blue",
			"icon": "octicon octicon-book",
			"label": _("Double Ledger Management"),
			"items": [
				{
					"type": "doctype",
					"name": "Double Ledger Parties",
					"lable": _("Double Ledger Parties"),
					"description": _(" Managing Parties that act as both customers and suppliers")
				}
			]
		}
	]
