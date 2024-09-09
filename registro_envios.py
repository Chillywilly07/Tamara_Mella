class Envio:
    def __init__(self, numero_guia, destinatario, direccion, fecha_envio, estado_entrega):
        self.numero_guia = numero_guia
        self.destinatario = destinatario
        self.direccion = direccion
        self.fecha_envio = fecha_envio
        self.estado_entrega = estado_entrega
        self.siguiente = None

class ListaEnlazadaEnvios:
    def __init__(self):
        self.cabeza = None

    def agregar_inicio(self, envio):
        envio.siguiente = self.cabeza
        self.cabeza = envio

    def agregar_final(self, envio):
        if self.cabeza is None:
            self.cabeza = envio
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = envio

    def eliminar_envio(self, numero_guia):
        actual = self.cabeza
        anterior = None
        encontrado = False
        while actual is not None and not encontrado:
            if actual.numero_guia == numero_guia:
                encontrado = True
            else:
                anterior = actual
                actual = actual.siguiente
        if actual is None:
            print("Envío no encontrado.")
            return
        if anterior is None:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente

    def buscar_envio(self, clave, valor):
        actual = self.cabeza
        encontrados = []
        while actual is not None:
            if clave == 'numero_guia' and actual.numero_guia == valor:
                encontrados.append(actual)
            elif clave == 'destinatario' and actual.destinatario == valor:
                encontrados.append(actual)
            actual = actual.siguiente
        return encontrados

# Función para mostrar el menú y gestionar las operaciones
def menu():
    lista_envios = ListaEnlazadaEnvios()
    while True:
        print("\nMenu de Operaciones:")
        print("1. Agregar Envío al Inicio")
        print("2. Agregar Envío al Final")
        print("3. Eliminar Envío")
        print("4. Buscar Envío")
        print("5. Mostrar Todos los Envíos")
        print("6. Salir")
        opcion = int(input("Ingrese el número de la operación que desea realizar: "))
        if opcion == 1:
            envio = crear_envio()
            lista_envios.agregar_inicio(envio)
        elif opcion == 2:
            envio = crear_envio()
            lista_envios.agregar_final(envio)
        elif opcion == 3:
            numero_guia = input("Ingrese el número de guía del envío a eliminar: ")
            lista_envios.eliminar_envio(numero_guia)
        elif opcion == 4:
            clave = input("Ingrese la clave de búsqueda (numero_guia o destinatario): ")
            valor = input("Ingrese el valor a buscar: ")
            encontrados = lista_envios.buscar_envio(clave, valor)
            if len(encontrados) > 0:
                for envio in encontrados:
                    mostrar_envio(envio)
            else:
                print("No se encontraron envíos con los criterios especificados.")
        elif opcion == 5:
            mostrar_todos_envios(lista_envios)
        elif opcion == 6:
            break
        else:
            print("Opción no válida.")

# Función para crear un objeto Envio con los datos ingresados por el usuario
def crear_envio():
    numero_guia = input("Ingrese el número de guía del envío: ")
    destinatario = input("Ingrese el nombre del destinatario: ")
    direccion = input("Ingrese la dirección de envío: ")
    fecha_envio = input("Ingrese la fecha de envío (dd/mm/aaaa): ")
    estado_entrega = input("Ingrese el estado de entrega (entregado, en tránsito, etc.): ")
    return Envio(numero_guia, destinatario, direccion, fecha_envio, estado_entrega)

# Función para mostrar la información de un envío
def mostrar_envio(envio):
    print("\nInformación del Envío:")
    print("Número de Guía:", envio.numero_guia)
    print("Destinatario:", envio.destinatario)
    print("Dirección de Envío:", envio.direccion)
    print("Fecha de Envío:", envio.fecha_envio)
    print("Estado de Entrega:", envio.estado_entrega)

# Función para mostrar todos los envíos en la lista
def mostrar_todos_envios(lista_envios):
    print("\nTodos los Envíos:")
    actual = lista_envios.cabeza
    while actual is not None:
        mostrar_envio(actual)
        actual = actual.siguiente

# Ejecutar el programa
if __name__ == "__main__":
    menu()
