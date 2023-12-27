import starkbank
import os

class webHook:
    def checkWebHook():
        try:
            #webHookSandbox = "id do webhook sandbox"
            webHookSandbox = os.getenv('idWebhook')
            webhook = starkbank.webhook.get(webHookSandbox)
            return webhook

        except Exception as e:
            print("erro: ", e )
            webhook = "erro" 
            return webhook
            
        

        