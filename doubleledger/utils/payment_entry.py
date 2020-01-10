import frappe


@frappe.whitelist()
def get_party_primary_role(party_type, party):
    doc = frappe.get_list('Double Ledger Parties',
                         filters={
                             party_type: party
                         },
                         fields= "primary_role")
    if doc:
        return doc[0].primary_role
