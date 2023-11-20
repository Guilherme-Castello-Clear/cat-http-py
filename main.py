from flask import Flask, render_template
import requests

app = Flask(__name__)

HTTP_RESPONSES = [200, 201, 204, 400, 401, 403, 404, 500, 503]
HTTP_CATSCRIPTION = [
    "Tudo está indo bem! A solicitação foi bem-sucedida, e o servidor está respondendo com os dados solicitados. O cliente pode começar a ronronar de satisfação.",
    "A solicitação foi bem-sucedida, e algo novo foi criado. Como um novo filhote de gato, a entidade foi criada com sucesso.",
    "A solicitação foi bem-sucedida, mas não há conteúdo para enviar de volta. Parece que o gato desapareceu momentaneamente.",
    "O servidor não pode entender a solicitação, provavelmente devido a um erro do cliente. Parece que há uma bola de pelos no código.",
    "O acesso está negado devido à falta de credenciais válidas. O cliente não tem a senha certa para a caixa de areia.",
    "O servidor entende a solicitação, mas o acesso é proibido. O cliente não tem permissão para brincar com o catnip.",
    "O recurso solicitado não pôde ser encontrado no servidor. Parece que o gato se aventurou e está fora de alcance.",
    "O servidor encontrou uma situação inesperada que o impediu de atender à solicitação. Há uma bola de pelos atrapalhando as engrenagens do servidor.",
    "O servidor não está pronto para lidar com a solicitação. Talvez esteja na hora de uma soneca, e o servidor está temporariamente indisponível."
]

MAIN_URL = 'https://http.cat/'

@app.route("/")
def home():
    catsponses = []
    for http in HTTP_RESPONSES:
        current_cat = f'{MAIN_URL}{http}'
        res = requests.get(current_cat)
        catsponses.append(res.url)
    return render_template("index.html", cats=catsponses, catscription=HTTP_CATSCRIPTION)


if __name__ == '__main__':
    app.run(debug=True)
