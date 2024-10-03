from flask import Flask
from secrets import token_hex

def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.secret_key = token_hex(16)
    
    from react_server.server.routes import server
    app.register_blueprint(server)
    
    return app
