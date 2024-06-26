class Curso:
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self, nombre):
        self.alumnos.append(nombre)
        print(f"Alumno '{nombre}' agregado al curso.")

    def eliminar_alumno(self, nombre):
        if nombre in self.alumnos:
            self.alumnos.remove(nombre)
            print(f"Alumno '{nombre}' eliminado del curso.")
        else:
            print(f"El alumno '{nombre}' no está en la lista.")

    def listar_alumnos(self):
        if self.alumnos:
            print("Lista de alumnos en el curso:")
            for alumno in self.alumnos:
                print(f"- {alumno}")
        else:
            print("No hay alumnos en el curso.")

    def guardar_datos(self, archivo):
        with open(archivo, 'w') as file:
            json.dump(self.alumnos, file)
        print(f"Datos guardados en {archivo}")

    def cargar_datos(self, archivo):
        try:
            with open(archivo, 'r') as file:
                self.alumnos = json.load(file)
            print(f"Datos cargados desde {archivo}")
        except FileNotFoundError:
            print(f"No se encontró el archivo {archivo}. Iniciando con lista vacía.")


# Ejemplo de uso
curso = Curso()
archivo_guardado = "alumnos_curso.json"

# Intentamos cargar datos previos si existen
curso.cargar_datos(archivo_guardado)

while True:
    print("\n=== Menú ===")
    print("1. Agregar alumno")
    print("2. Eliminar alumno")
    print("3. Ver listado de alumnos")
    print("4. Guardar y salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        nombre = input("Ingrese el nombre del alumno a agregar: ")
        curso.agregar_alumno(nombre)
    elif opcion == '2':
        nombre = input("Ingrese el nombre del alumno a eliminar: ")
        curso.eliminar_alumno(nombre)
    elif opcion == '3':
        curso.listar_alumnos()
    elif opcion == '4':
        curso.guardar_datos(archivo_guardado)
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
