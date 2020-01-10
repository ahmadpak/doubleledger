# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "doubleledger"
app_title = "Double Ledger Management"
app_publisher = "Havenir"
app_description = "App to accommodate parties that act as both customers and suppliers in ERPNEXT"
app_icon = "octicon octicon-book"
app_color = "blue"
app_email = "info@havenir.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/doubleledger/css/doubleledger.css"
# app_include_js = "/assets/doubleledger/js/doubleledger.js"

# include js, css files in header of web template
# web_include_css = "/assets/doubleledger/css/doubleledger.css"
# web_include_js = "/assets/doubleledger/js/doubleledger.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
    "Payment Entry": "public/js/payment_entry.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}


fixtures = [{
    'dt': 'Custom Field', 'filters':[
        [
            'name', 'in', [
                "Sales Invoice-no_double_ledger",
                "Purchase Invoice-no_double_ledger",
                "Payment Entry-primary_role"
            ]
        ]
    ]
}]


# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "doubleledger.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "doubleledger.install.before_install"
# after_install = "doubleledger.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "doubleledger.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
    "Sales Invoice" :{
        "on_submit" : "doubleledger.double_ledger_management.doctype.double_ledger_parties.double_ledger_parties.create_invoice_adj_jv",
        "on_cancel" : "doubleledger.double_ledger_management.doctype.double_ledger_parties.double_ledger_parties.cancel_adjusted_jv"
    },
    "Purchase Invoice" :{
        "on_submit" : "doubleledger.double_ledger_management.doctype.double_ledger_parties.double_ledger_parties.create_invoice_adj_jv",
        "on_cancel" : "doubleledger.double_ledger_management.doctype.double_ledger_parties.double_ledger_parties.cancel_adjusted_jv"
    },
    "Journal Entry" :{
        "on_cancel" : "doubleledger.double_ledger_management.doctype.double_ledger_parties.double_ledger_parties.prevent_linked_jv_cancellation"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"doubleledger.tasks.all"
# 	],
# 	"daily": [
# 		"doubleledger.tasks.daily"
# 	],
# 	"hourly": [
# 		"doubleledger.tasks.hourly"
# 	],
# 	"weekly": [
# 		"doubleledger.tasks.weekly"
# 	]
# 	"monthly": [
# 		"doubleledger.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "doubleledger.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "doubleledger.event.get_events"
# }

