import starkbank
import os

class webHook:
    def checkWebHook():
        try:
            webHookSandbox = "id do webhook sandbox"
            webhook = starkbank.webhook.get(webHookSandbox)
            return webhook

        except Exception as e:
            print("erro Webhook: ", e )
            webhook = "erro" 
            return webhook
            
        

        