from Infrastructure.server import receiveUser, backgroundTime
from Application.checkWebHook import webHook

class invoiceController:
    def controller():
        try:
            receiveUser.starkBankUser()
            verifyUser = webHook.checkWebHook()

            if verifyUser != "erro":
                backgroundTime.schedule_time()
                #for invoice in starkInvoice:
                #    print(invoice)
                #StarkTransfer.transfer()
    
            else:
                print("Não foi possível encontrar webhook válido")
        except Exception as e:
            print ("erro: ", e)
