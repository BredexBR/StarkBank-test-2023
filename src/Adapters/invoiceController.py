from Infrastructure.server import receiveUser
from Application.checkWebHook import webHook
from Application.addInvoice import AddInvoice

class invoiceController:
    def controller():
        receiveUser.starkBankUser()
        verifyUser = webHook.checkWebHook()

        if verifyUser != "erro":
            
            #server.schedule_time()
            AddInvoice.addInvoice()
            #for invoice in starkInvoice:
            #    print(invoice)
            #StarkTransfer.transfer()
  
        else:
            print("Não foi possível encontrar webhook válido")
    
