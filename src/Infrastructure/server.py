import starkbank
import os
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from ..Application.addInvoice import AddInvoice

class receiveUser():
    def starkBankUser():
        private_key_content = """
        Informação da chave privada
        """

        print("id do sandbox: ",os.getenv('idSandbox'))
        # for project users:
        project = starkbank.Project(
            environment="sandbox",
            #id="id do ambiente sandbox",
            id= os.getenv('idSandbox'),
            private_key=private_key_content
        )
        starkbank.user = project

class backgroundTime():    
    def schedule_time():
        schedule_manager = BackgroundScheduler()
        schedule_manager.remove_all_jobs()
        #schedule_manager.add_job(AddInvoice.addInvoice, trigger=IntervalTrigger(hours=3)) # A cada 3 horas fara 8 a 12 faturas
        schedule_manager.add_job(AddInvoice.addInvoice, trigger=IntervalTrigger(seconds=30)) # A cada 30 segs fara 8 a 12 faturas(mais facil para testar)
        schedule_manager.start()
        try:
            #schedule_manager._thread.join(timeout=24*60*60) # depois de 24 horas encerrara a função
            schedule_manager._thread.join(timeout=60) # depois de 1 minuto encerrara a função (mais facil para testar)

        finally:
            schedule_manager.shutdown() # encerra