## Double Ledger Management

App to accommodate parties that act as both customers and suppliers in ERPNEXT

Many times we see that a we buy from the same customer we sell our products to and vice versa. In that case it becomes tedious to operate two different ledgers and put adjustment entries manually. Adding manual entries leads to human error. This app will will take care of such accounts. 

### Stucture of the app
Each party has a dominent side either it is primarily our customer and we buy products from it sometimes. Or is it primarily our supplier and we sell products to it sometimes. User will be able to add parties of such character and select its primary nature. 

#### In case of primary customer:  
When ever a product is purchased from such customer and purchase invoice is made. On submission of the purchase invoice an automatic Journal entry is created to that debits the supplier side and credits the customer side. If purchase invoice is "is paid" then no journal entry will be created. On cancelation of the purchase invoice the corresponding Journal entry will automatically get cancelled as well.  

#### In case of primary supplier:
When ever a product is sold to such supplier and sales invoice is made. On submission of the sales invoice an automatic Journal entry is created to that debits the supplier side and credits the customer side. If sales invoice is "is pos" than no journal entry will be created. On cancelation of the sales invoice the corresponding Journal entry will automatically get cancelled as well. 

#### License

MIT