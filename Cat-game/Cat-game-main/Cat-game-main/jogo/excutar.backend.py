from backend.geral.config import *
from backend.geral.rotas.listar import *

# rota padrão
@app.route("/")
def inicio():
    return 'backend com rotas generalizadas de listagem'

# inserindo a aplicação em um contexto :-/
with app.app_context():

    app.run(debug=True)