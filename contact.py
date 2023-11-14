class AgendaContactos:
    def __init__(self):
        self.lista_contactos = ["Juan Perez", "Maria Lopez", "Carlos Rodriguez"]

    def agregar_contacto(self, nombre_apellido):
        self.lista_contactos.append(nombre_apellido)
        print(f'Contacto {nombre_apellido} agregado correctamente.')

    def borrar_contacto(self, nombre_apellido):
        if nombre_apellido in self.lista_contactos:
            self.lista_contactos.remove(nombre_apellido)
            print(f'Contacto {nombre_apellido} borrado correctamente.')
        else:
            print(f'Error: Contacto {nombre_apellido} no encontrado en la lista.')

    def imprimir_contactos(self):
        if not self.lista_contactos:
            print('La lista de contactos está vacía.')
        else:
            print('Lista de contactos:')
            for contacto in self.lista_contactos:
                print(contacto)

# Ejemplo de uso
agenda = AgendaContactos()

# Agregar contactos
agenda.agregar_contacto("Laura Martinez")

# Imprimir contactos
agenda.imprimir_contactos()

# Borrar un contacto
agenda.borrar_contacto("Maria Lopez")

# Imprimir contactos después de borrar
agenda.imprimir_contactos()
