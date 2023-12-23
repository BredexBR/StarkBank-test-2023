import starkbank

class webHook:
    def checkWebHook():
        try:
            webHookSandbox = "id do webhook criado no ambiente sandbox"
            webhook = starkbank.webhook.get(webHookSandbox)
            return webhook

        except:
            webhook = "erro"
            return webhook
            
        

        