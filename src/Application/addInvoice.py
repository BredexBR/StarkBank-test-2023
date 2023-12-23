import starkbank
import random

class AddInvoice:
    def addInvoice():
        try:
            invoices = [starkbank.Invoice(
                    amount=random.randint(500, 5000),  
                    name="Arya Stark",
                    tax_id="012.345.678-90"
                ) 
                for x in range(0,random.randint(8, 12))
                ]
        
            #invoiceFinal = starkbank.invoice.create(invoices)
            #for invoice in invoiceFinal:
            #    print(invoice)

            return starkbank.invoice.create(invoices)
        except:
            return "erro"
    