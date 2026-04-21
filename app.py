# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_db_connection

app = Flask(__name__)
app.secret_key = 'clave_secreta_inventario'

@app.route('/')
def index():
    conn = get_db_connection()
    productos = conn.execute('SELECT * FROM productos').fetchall()
    conn.close()
    return render_template('index.html', productos=productos)

@app.route('/registrar')
def registrar():
    return render_template('registrar.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    categoria = request.form['categoria']
    precio = request.form['precio']
    stock = request.form['stock']

    if not nombre or not categoria or not precio or not stock:
        flash('Todos los campos son obligatorios.')
        return redirect(url_for('registrar'))

    conn = get_db_connection()
    conn.execute('INSERT INTO productos (nombre, categoria, precio, stock) VALUES (?, ?, ?, ?)',
                 (nombre, categoria, precio, stock))
    conn.commit()
    conn.close()
    flash('Producto guardado con exito.')
    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    conn = get_db_connection()
    producto = conn.execute('SELECT * FROM productos WHERE id = ?', (id,)).fetchone()
    conn.close()
    if producto is None:
        return redirect(url_for('index'))
    return render_template('editar.html', producto=producto)

@app.route('/actualizar', methods=['POST'])
def actualizar():
    id = request.form['id']
    nombre = request.form['nombre']
    categoria = request.form['categoria']
    precio = request.form['precio']
    stock = request.form['stock']

    conn = get_db_connection()
    conn.execute('UPDATE productos SET nombre = ?, categoria = ?, precio = ?, stock = ? WHERE id = ?',
                 (nombre, categoria, precio, stock, id))
    conn.commit()
    conn.close()
    flash('Producto actualizado con exito.')
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM productos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Producto eliminado con exito.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
