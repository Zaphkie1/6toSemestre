from pymongo import MongoClient
import certifi


MONGO_URI = "mongodb+srv://l21450213Apache0136H*@cluster0.yiyx2bq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


ca=certifi.where()
def dbConnection():
    try:
        client=MongoClient(MONGO_URI, tlsCAFile=ca)
        db=client=["db_product_gpoA"]
    except ConnectionError as e:
        print("Error al conector a la BD!")
    else:
        print("Conexion establecida")
        return db