import starkbank
import random
from ..Domain.people import people
from ..Application.addPeople import addPeople

class AddInvoice:
    def addInvoice():
        try:
            for x in range(0,random.randint(8, 12)): 
                numberRandom = random.randint(1, 12)
                people = addPeople.addPeople(numberRandom)
                
                invoices = [starkbank.Invoice(
                        amount=random.randint(1000, 5000),  
                        name=people.name,
                        tax_id=people.cpf
                    ) 
                    ]

                starkbank.invoice.create(invoices)
        except Exception as e:
            print("erro: " , e)
    