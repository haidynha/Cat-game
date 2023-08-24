from backend.geral.config import *
from backend.geral.testar import *

# inserindo a aplicação em um contexto :-/
with app.app_context():

    testar_jogador.run()