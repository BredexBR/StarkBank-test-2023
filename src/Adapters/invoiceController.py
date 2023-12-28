from flask import Response
from Infrastructure.server import receiveUser, backgroundTime
from Infrastructure.conDatabase import conDatabase
from Application.checkWebHook import webHook
from Application.transfer import StarkTransfer

class invoiceController:
    def controller(app):
        try:
            receiveUser.starkBankUser()
            check = webHook.checkWebHook()

            if check != "erro":
                conn = conDatabase.conDatabase()
                if conn != "erro":
                    backgroundTime.schedule_time(conn)
                    conDatabase.closeDatabase(conn)
                else:
                    print("Não foi possível realizar a conexão com o banco de dados")
            else:
                print("Não foi possível encontrar webhook válido")
        except Exception as e:
            print ("erro invoiceController: ", e)
    
        @app.route('/webhook/transfer', methods=['POST'])
        def transfer_handle():
            StarkTransfer.makeTransfer()
            return Response(status=200)
    