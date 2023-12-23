from flask import Flask
from Adapters.invoiceController import invoiceController

def invoiceDomain():
    app = Flask(__name__)

    invoiceController.controller() 

    #if __name__ == "__main__":
     #   app.run(debug=True)