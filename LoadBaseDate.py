import pyrebase
# Configuracion de la base de datos
config = {
    "apiKey": "AIzaSyCqPxQdvl2Yx0zHckcPudemSQq7hZu0xpk",
    "authDomain": "pythonshop-63009.firebaseapp.com",
    "databaseURL": "https://pythonshop-63009.firebaseio.com/",
    "storageBucket": "pythonshop-63009.appspot.com"
}

# Instancia de la base de datos
firebase = pyrebase.initialize_app(config)

db = firebase.database()


eatable = []
eatable.append("AGUA SABORIZADA&SER&2000&Agua saborizada muy rica&20/12/19&10&70")
eatable.append("BATATA&SIN MARCA&1&Batata podrida&12/02/94&12&25")
eatable.append("CEBOLLA COMERCIAL BOLSITA&SIN MARCA&1&Cebolla con olor a culo&23/12/32&123&45")
eatable.append("FLAN DULCE DE LECHE ROYAL X 40 GRS&ROYAL&40&Flan de San Martin&23/04/1830&5&78")
eatable.append("MARGARINA REPOSTERA DANICA PAN X 200 GRS&DANICA&200&Margarina&23/05/86&45&34")

noneatable = []
noneatable.append("MAQUINA DE AFEITAR EXCEL GILLETTE X 2 UNI&GILLETTE&2&Maquinita para afeitarse&gris&14&150")
noneatable.append("LIMPIADOR MULTIUSO DOY PACK MR MUSCULO X 500 CC&MR MUSCULO&500&Limpiador, es re persa&naranja&34&90")
noneatable.append("PANALES TALLE XXG PREMIUM CARE PAMPERS X 48 UNI&PAMPERS&48&Pañales para la bendicion&blanco&678&200")
noneatable.append("ACONDICIONADOR RESTAURACION PANTENE X 750 CC&PANTENE&750&Acondicionador para la pelada&blanco&45&100")
noneatable.append("CERA DEPILATORIA PARA MICROONDAS VEET X 200 GRS&VEET&200&Cera para sacarse la selva de encima&verde&56&120")


db.child("products").child("eatable").set(eatable)
db.child("products").child("noneatable").set(noneatable)
