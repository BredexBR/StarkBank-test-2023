import starkbank
from apscheduler.schedulers.background import BackgroundScheduler

class receiveUser():
    def starkBankUser():
        private_key_content = """
        CONTEUDO DA CHAVE PRIVADA
        """

        # for project users:
        project = starkbank.Project(
            environment="sandbox",
            id="id do sandbox",
            private_key=private_key_content
        )
        starkbank.user = project


class backgroundTime():    
    def schedule_time():
        schedule_manager = BackgroundScheduler()
        schedule_manager.remove_all_jobs()
        schedule_manager.add_job("função que vai rodar em background", "interval", hours=3)
        schedule_manager.start()