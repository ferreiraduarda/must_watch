from flask import Flask, render_template, request, redirect, url_for
from models.midia import Midia
from models.database import init_db

app = Flask(__name__)

init_db()

@app.route('/')
def home():
    return render_template('home.html', titulo='Home')

@app.route('/lista', methods=['GET', 'POST'])
def lista():
    if request.method == 'POST':
        titulo, tipo, indicado_por = request.form['titulo'], request.form['tipo'], request.form['indicado_por']
        item = Midia(titulo, tipo, indicado_por)
        item.salvar()
        return redirect(url_for('lista'))

    lista = Midia.obter_todos()
    return render_template('lista.html', titulo='Lista de Desejos', lista=lista)

@app.route('/delete/<int:id>')
def delete(id):
    item = Midia.id(id)
    if item:
        item.excluir()
    return redirect(url_for('lista'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    item = Midia.id(id)
    if not item:
        return redirect(url_for('lista'))

    if request.method == 'POST':
        item.titulo = request.form['titulo']
        item.tipo = request.form['tipo']
        item.indicado_por = request.form['indicado_por']
        item.atualizar()
        return redirect(url_for('lista'))

    lista_total = Midia.obter_todos()
    return render_template('lista.html', titulo=f'Editando ID: {id}', lista=lista_total, item=item)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
