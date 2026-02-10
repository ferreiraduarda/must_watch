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
    item = None

    if request.method == 'POST':
        titulo = request.form['titulo']
        tipo = request.form['tipo']
        indicado = request.form['indicado']

        item = Midia(titulo, tipo, indicado)
        item.salvar()

    lista = Midia.obter_todos()

    return render_template(
        'lista.html',
        titulo='Lista de Desejos',
        lista=lista
    )

@app.route('/delete/<int:id>')
def delete(id):
    item = Midia.id(id)
    item.excluir()

    return redirect(url_for('lista'))


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):

    if request.method == 'POST':
        titulo = request.form['titulo']
        tipo = request.form['tipo']
        indicado = request.form['indicado']

        item = Midia(titulo, tipo, indicado, id)
        item.atualizar()

        return redirect(url_for('lista'))

    lista = Midia.obter_todos()
    item = Midia.id(id)

    return render_template(
        'lista.html',
        titulo=f'Editando ID: {id}',
        lista=lista,
        item=item
    )


if __name__ == '__main__':
    app.run(debug=True)
