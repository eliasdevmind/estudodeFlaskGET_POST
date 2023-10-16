# Cria a máquina virtual Python
# python -m venv nomeDaMaquina

# Ativa a máquina virtual
# .\nomeDaMaquina\Scripts\Activate.ps1

# Instala o Flask
# pip install Flask

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dicionário para armazenar os dados enviados
data = {"nome": "", "mensagem": ""}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Se o método for POST, atualize os dados com os valores do formulário
        data['nome'] = request.form['nome']
        data['mensagem'] = request.form['mensagem']
        return redirect(url_for('index'))
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
