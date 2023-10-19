# Cria a máquina virtual Python
# python -m venv nomeDaMaquina

# Ativa a máquina virtual
# .\nomeDaMaquina\Scripts\Activate.ps1

# Instala o Flask
# pip install Flask

from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []

@app.route('/')
def lista_de_tarefas():
    return render_template('lista_de_tarefas.html', tasks=tasks)

@app.route('/adicionar-tarefa', methods=['GET', 'POST'])
def adicionar_tarefa():
    if request.method == 'POST':
        nova_tarefa = request.form.get('nova_tarefa')
        if nova_tarefa:
            tasks.append(nova_tarefa)
    return render_template('adicionar_tarefa.html')

if __name__ == '__main__':
    app.run(debug=True)
