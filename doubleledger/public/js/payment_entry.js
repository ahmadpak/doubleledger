frappe.ui.form.on('Payment Entry',{
	party: function(frm){
		frappe.call({
			method: "doubleledger.utils.payment_entry.get_party_primary_role",
			args: {
				party_type: frm.doc.party_type,
				party: frm.doc.party 
			},
			callback:function(r){
				frm.doc.primary_role = r.message
				frm.refresh_field('primary_role')
			}
		})
	}
})