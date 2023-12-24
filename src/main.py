from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

import starkbank
from flask import request, Flask
from Adapters.invoiceController import invoiceController

app = Flask(__name__)

if __name__ == "__main__":
    invoiceController.controller()
    app.run(debug=True)