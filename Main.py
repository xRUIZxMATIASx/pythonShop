import pyrebase
from Eatable import Eatable
from NonEatable import NonEatable

# Configuracion de la base de datos
config = {
    "apiKey": "AIzaSyCqPxQdvl2Yx0zHckcPudemSQq7hZu0xpk",
    "authDomain": "pythonshop-63009.firebaseapp.com",
    "databaseURL": "https://pythonshop-63009.firebaseio.com/",
    "storageBucket": "pythonshop-63009.appspot.com"
}

# Instancia de la base de datos
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def login():
    email = input('Ingrese su correo: ')
    password = input('Ingrese su contraseña: ')
    print('Ingresando...\n')
    user = auth.sign_in_with_email_and_password(email, password)
    main(user['localId'])

def signup():
    email = input('Ingrese su correo: ')
    name = input('Ingrese su nombre: ')
    phone = input('Ingrese su numero de telefono: ')
    address = input('Ingrese su domicilio: ')
    password = input('Ingrese su contraseña: ')
    user = auth.create_user_with_email_and_password(email, password)
    db = firebase.database()
    data = {
        "name": name,
        "phone": phone,
        "address": address,
        "id": user['localId']
    }
    db.child("users").child(user['localId']).set(data)
    print('Usuario Creado!!!\n\n')
    print('Por favor inicie sesion\n')
    login()

def main(user):
    exit = False
    while not exit:
        # print('Ver lista de productos: 1')
        print('Hacer pedido: 1')
        print('Ver pedido: 2')
        print('Salir: 3')
        selection = 0
        while not selection:
            try:
                selection = int(input(''))
                if not 1 <= selection <= 3:
                    raise ValueError
            except ValueError:
                print("Wrong input. Try again")
        if selection == 1:
            makeOrder(user)
        elif selection == 2:
            code = input('Ingrese el codigo del pedido: ')
            requestOrder(code)
        elif selection == 3:
            exit = True
        else:
            print('Error')

def requestOrder(code):
    all_products = []
    db = firebase.database()  # Se instancia la base de datos
    eatables = db.child("products").child("eatable").get()  # Se obtiene la lista de productos comestibles de la base de datos
    for products in eatables.each():  # Recorro con for para almacenarla en una lista
        params = products.val().split('&')  # Los atributos de los productos estan almacenados en un string separados por '&'
        all_products.append(Eatable("eatable", products.key(), params[0], params[1].replace(',', '.'), params[2], params[3], params[4], params[6], params[5]))  # Completo una lista de todos los productos
    noneatables = db.child("products").child("noneatable").get()  # Se obtiene la lista de productos No comestibles de la base de datos
    for products in noneatables.each():  # Recorro con for para almacenarla en una lista
        params = products.val().split('&')  # Los atributos de los productos estan almacenados en un string separados por '&'
        all_products.append(NonEatable("noneatable", products.key(), params[0], params[1].replace(',', '.'), params[2], params[3], params[4], params[6], params[5]))  # Completo una lista de todos los productos

    dir = db.child('order').child(code).child('listProducts').get()
    print('Nombre\t----------\tMarca\t-----\tPrecio\t-----\tCantidad')
    for product in all_products:
        if product.getIdProduct() in set(dir.val()):
            print(product.getName(), '\t----------\t'+product.getBrand(), '\t-----\t', product.getPrice(), '\t-----\t', dir.val().count(product.getIdProduct()))



def makeOrder(user):
    exit = False
    print('Cargando...\n\n\n')
    eatable = []
    noneatable = []
    all_products = []
    db = firebase.database() # Se instancia la base de datos
    eatables = db.child("products").child("eatable").get() # Se obtiene la lista de productos comestibles de la base de datos
    for products in eatables.each(): # Recorro con for para almacenarla en una lista
        params = products.val().split('&') # Los atributos de los productos estan almacenados en un string separados por '&'
        eatable.append(Eatable("eatable", products.key(), params[0], params[1].replace(',', '.'), params[2], params[3], params[4], params[6], params[5])) # Completo la lista de alimentos comestibles instanciando la clase
        all_products.append(Eatable("eatable", products.key(), params[0], params[1].replace(',', '.'), params[2], params[3], params[4], params[6], params[5])) # Completo una lista de todos los productos
    noneatables = db.child("products").child("noneatable").get()  # Se obtiene la lista de productos No comestibles de la base de datos
    for products in noneatables.each(): # Recorro con for para almacenarla en una lista
        params = products.val().split('&') # Los atributos de los productos estan almacenados en un string separados por '&'
        noneatable.append(NonEatable("noneatable", products.key(), params[0], params[1].replace(',', '.'), params[2], params[3], params[4], params[6], params[5])) # Completo la lista de alimentos No comestibles instanciando la clase
        all_products.append(NonEatable("noneatable", products.key(), params[0], params[1].replace(',', '.'), params[2], params[3], params[4], params[6], params[5])) # Completo una lista de todos los productos

    print('Lista\t-----\tNombre\t-----\tMarca\t-----\tCantidad\t-----\tDescripcion\t-----\tFecha de Vencimiento\t-----\tStock\t-----\tPrecio') # Cabecera de la lista de comestibles
    count = 0
    for x in eatable: # for para imprimir la lista de productos comestibles
        count += 1
        print(str(count)+'-----'+x.getName()+'-----'+x.getBrand()+'-----'+x.getUnitMeasure()+'-----'+x.getDescription()+'-----'+x.getExpirationDate()+'-----'+x.getStock()+'-----'+x.getPrice())
    print('\nNo comestibles\n')
    print('Lista\t-----\tNombre\t-----\tMarca\t-----\tCantidad\t-----\tDescripcion\t-----\tColor\t-----\tStock\t-----\tPrecio')  # Cabecera de la lista de no comestibles
    for x in noneatable: # for para imprimir la lista de productos No comestibles
        count += 1
        print(str(count)+'-----'+x.getName()+'-----'+x.getBrand()+'-----'+x.getUnitMeasure()+'-----'+x.getDescription()+'-----'+x.getColour()+'-----'+x.getStock()+'-----'+x.getPrice())
    print('\n')
    cart = [] # Carrito de compras
    while not exit:
        print('Agregar producto: 1')
        print('Pagar: 2')
        print('Mostrar pedido: 3')
        print('Volver atras: 4')
        selection = 0
        while not selection:
            try:
                selection = int(input(''))
                if not 1 <= selection <= 4:
                    raise ValueError
            except ValueError:
                print("Wrong input. Try Again")
        if selection == 1:
            product = input('Ingrese numero de lista: ')
            cantidad = int(input('Ingrese cantidad a agregar al carrito: '))
            if cantidad <= int(all_products[int(product) - 1].getStock()):
                all_products[int(product)-1].setStock(int(all_products[int(product)- 1].getStock()) - cantidad)
                for _ in range(cantidad):
                    cart.append(int(product)-1) # Agrego los indices de productos al carrito de compras
            else:
                print("No hay suficiente stock diponible para comprar esa cantidad. (stock disponible: ", all_products[int(product) - 1].getStock(), ")")
        elif selection == 2:
            if len(cart) != 0:
                pay(cart, all_products, user) # Llamo al metodo pay para realizar la orden
                exit = True
            else:
                print('El carrito esta vacio')
        elif selection == 3:
            if len(cart) == 0:
                print("El carrito esta vacio")
            else:
                showOrder(cart, all_products)
        elif selection == 4:
            exit = True


def pay(cart, all_products, user):
    pay_products = [] # Lista de productos a pagar
    print('Total a pagar:')
    count = 0
    for i in range(len(cart)):
        pay_products.append(all_products[int(cart[i])])
        count = count + float(all_products[int(cart[i])].getPrice())  # Calcular el precio total
    print('$'+str(count))
    print('¿Desea continuar?')
    print('Si: 1')
    print('No: 2')
    selection = 0
    while not selection:
        try:
            selection = int(input(''))
            if not 1 <= selection <= 2:
                raise ValueError
        except ValueError:
            print("Wrong input. Try again")
    if selection == 1:
        print('Realizando pedido...')
        db = firebase.database()
        if count == 0 or len(pay_products) == 0:
            print('No se pudo realizar la compra')
        else:
            for update in pay_products:
                if update.getType() == 'eatable': # Actualizar el stock de la base de datos segun el tipo de producto comprado
                    db.child("products").child("eatable").update({update.getName(): update.getIdProduct()+'&'+update.getPrice().replace('.', ',')+'&'+update.getUnitMeasure()+'&'+update.getBrand()+'&'+update.getDescription()+'&'+update.getExpirationDate()+'&'+str(int(update.getStock()))})
                elif update.getType() == 'noneatable':
                    db.child("products").child("noneatable").update({update.getName(): update.getIdProduct()+'&'+update.getPrice().replace('.', ',')+'&'+update.getUnitMeasure()+'&'+update.getBrand()+'&'+update.getDescription()+'&'+update.getColour()+'&'+str(int(update.getStock()))})
                else:
                    print('Error')
            print('¿Desea pagar el envio? Costo de $20')
            print('Si: 1')
            print('No: 2')
            send = int(input(''))
            if send == 1:
                send = True
                count = count + 20
            else:
                send = False
            idProducts = []
            for product in pay_products:
                idProducts.append(product.getIdProduct())
            data = {
                "clientId": user,
                "listProducts": idProducts,
                "shipping": send
            }
            code = db.child("order").push(data) # Guardar la orden en la base de datos
            print('La compra se ha realizado con exito!!!')
            print('El codigo para retirar es: ', code['name'])
            print('Total a pagar: ', count)
    elif selection == 2:
        print('Compra cancelada\n\n')
    else:
        print('Error')

def showOrder(cart, all_products):
    ids = list(set(cart))
    ids.sort()
    cantidad = []
    count = 0
    print('Lista\t-----\tNombre\t----------\tMarca\t-----\tUnidad\t-----\tDescripcion\t-----\tStock\t-----\tPrecio\t-----\tCantidad')
    for x in ids:
        cantidad.append(cart.count(x))
    for x in ids:
        print(str(int(x) + 1), '-----', all_products[int(x)].getName(), '-----', all_products[int(x)].getBrand(), '-----', all_products[int(x)].getUnitMeasure(), '-----', all_products[int(x)].getStock(), '-----', all_products[int(x)].getPrice(), "----", cantidad[count])
        count += 1
    return


print('Bienvenido a -------- PythonShop ---------')

print('Ingresar: 1')
print('Registrarse: 2')
print('Exit: 3')
selection = 0

while not selection:
    try:
        selection = int(input('Seleccione: '))
        if not 1 <= selection <= 3:
            selection = 0
            raise ValueError
    except ValueError:
        print("Error. Valor ingresado distinto de '1', '2', o '3'")
        pass
    
if selection == 1:
    login()
elif selection == 2:
    signup()
elif selection == 3:
    exit
