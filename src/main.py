from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from flask import Flask
from Adapters.invoiceController import invoiceController

app = Flask(__name__)

if __name__ == "__main__":
    invoiceController.controller(app)
    app.run(debug=True)