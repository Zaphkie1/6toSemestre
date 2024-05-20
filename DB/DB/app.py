from bson import ObjectId
from flask import Flask, flash, render_template, request, url_for, redirect
import db as datase
from product import Product

db = datase.dbConnection()
app_secret_key = 'secret_key'
app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    products = db['products']
    data = products.find()
    return render_template('index.html', dataProduct=data)

# Ruta productor
@app.route('/add_product', methods=['POST'])
def add_product():
    if request.method == 'POST':
        products = db['products']
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']

        if nombre and precio and cantidad:
            product = Product(nombre, precio, cantidad)
            products.insert_one(product.toDBCollection())
            flash('Producto Agregado')
        else:
            flash('Todos los campos son requeridos')
    return redirect(url_for('index'))

# Ruta Editar producto
@app.route('/edit_product/<id>')
def edit_product(id):
    products = db['products']
    data = products.find_one({'_id': ObjectId(id)})
    if data:
        return render_template('edit_product.html', dataProduct=data)
    else:
        return "Producto no encontrado"

# Ruta eliminar producto
@app.route('/delete_product/<id>')
def delete_product(id):
    products = db['products']
    result = products.delete_one({'_id': ObjectId(id)})
    if result.deleted_count > 0:
        flash('Producto eliminado exitosamente')
    else:
        flash('Producto no encontrado')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
