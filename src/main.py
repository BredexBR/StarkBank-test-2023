from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from flask import Flask         
import Domain.invoice

app = Flask(__name__)

if __name__ == "__main__":
    Domain.invoice.invoiceDomain()
    app.run(debug=True)