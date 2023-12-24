import starkbank
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from Application.addInvoice import AddInvoice

class receiveUser():
    def starkBankUser():
        private_key_content = """
        Informação da chave privada
        """

        # for project users:
        project = starkbank.Project(
            environment="sandbox",
            id="id do ambiente sandbox",
            private_key=private_key_content
        )
        starkbank.user = project

class backgroundTime():    
    def schedule_time():
        schedule_manager = BackgroundScheduler()
        schedule_manager.remove_all_jobs()
        #schedule_manager.add_job(Domain.invoice.invoiceDomain, trigger=IntervalTrigger(hours=3))
        schedule_manager.add_job(AddInvoice.addInvoice(), trigger=IntervalTrigger(seconds=30))
        schedule_manager.start()
        try:
            #schedule_manager._thread.join(timeout=24*60*60)
            schedule_manager._thread.join(timeout=60)

        finally:
            schedule_manager.shutdown()