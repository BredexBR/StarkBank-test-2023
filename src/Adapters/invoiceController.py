from Infrastructure.server import receiveUser
from Application.checkWebHook import webHook
from Application.addInvoice import AddInvoice
#from Application import  transfer

class invoiceController:
    def controller():
        receiveUser.starkBankUser()
        verifyUser = webHook.checkWebHook()

        if verifyUser != "erro":
            #server.schedule_time()
            starkInvoice = AddInvoice.addInvoice()
            for invoice in starkInvoice:
                print(invoice)
  
        else:
            print("Não foi possível encontrar webhook válido")
    
