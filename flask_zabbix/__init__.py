import sys
from flask import Flask
sys.path.append("./api")
from api import pesquisa_items_por_key




app = Flask(__name__)

@app.route('/')
def hello():
        return items_por_key("vfs.fs.size[F:,used]")



