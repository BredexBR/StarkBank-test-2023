import starkbank
from flask import request

class StarkTransfer:
    
    def transfer():    
        event = starkbank.event.parse(
            content=request.data.decode("utf-8"),
            signature=request.headers["Digital-Signature"],
        )

        if event.subscription == "invoice" and event.log.type == "credited":
            transfers = starkbank.transfer.create([
                starkbank.Transfer(
                    amount=event.log.invoice.amount,
                    tax_id="20.018.183/0001-80",
                    name="Stark Bank S.A.",
                    bank_code="20018183",
                    branch_code="0001",
                    account_number="6341320293482496",
                )
            ])
            print (transfers)        
