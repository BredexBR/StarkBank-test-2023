from flask import Response
from ..Infrastructure.server import receiveUser, backgroundTime
from ..Application.checkWebHook import webHook
from ..Application.transfer import StarkTransfer

class invoiceController:
    def controller(app):
        try:
            receiveUser.starkBankUser()
            check = webHook.checkWebHook()

            if check != "erro":
                backgroundTime.schedule_time()                    
            else:
                print("Não foi possível encontrar webhook válido")
        except Exception as e:
            print ("erro: ", e)
    
        @app.route('/webhook/transfer', methods=['POST'])
        def transfer_handle():
            StarkTransfer.makeTransfer()
            return Response(status=200)
    