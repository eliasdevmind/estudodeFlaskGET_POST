# Cria a máquina virtual Python
# python -m venv nomeDaMaquina

# Ativa a máquina virtual
# .\nomeDaMaquina\Scripts\Activate.ps1

# Instala o Flask
# pip install Flask

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Task:
    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

tasks = []

@app.route('/')
def lista_de_tarefas():
    return render_template('lista_de_tarefas.html', tasks=tasks)

@app.route('/adicionar-tarefa', methods=['GET', 'POST'])
def adicionar_tarefa():
    if request.method == 'POST':
        nova_tarefa = request.form.get('nova_tarefa')
        if nova_tarefa:
            task = Task(nova_tarefa)
            tasks.append(task)
    return render_template('adicionar_tarefa.html')

@app.route('/marcar-como-concluida/<int:task_index>')
def marcar_como_concluida(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index].completed = True
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
