from flask import Flask, render_template, request
from product import Product  # Asegúrate de que estás importando la clase Product correctamente
import db as dbase

app = Flask(__name__)

# Conexión a la base de datos
db = dbase.dbConnection


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/add_product', methods=['POST'])
def add_product():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']

        # Crear instancia de la clase Product
        product = Product(nombre, precio, cantidad)
        # Obtener los datos formateados para la base de datos
        data = product.toDBCollection()

        # Aquí deberías insertar 'data' en tu base de datos

        return "Producto agregado exitosamente"


@app.route('/edit_product')
def edit_product():
    return "Editar producto"


@app.route('/delete_product')
def delete_product():
    return "Eliminar producto"


if __name__ == '__main__':
    app.run(port=5000, debug=True)
