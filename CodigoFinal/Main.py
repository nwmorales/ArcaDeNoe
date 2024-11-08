from Arca import Arca
from Animal import Perro, Gato
from Alimento import Croquetas, Heno

# Crear una instancia de Arca con capacidad máxima de 10
arca = Arca(10)

# Crear algunos animales
perro1 = Perro("Firulais")
gato1 = Gato("Michi")

# Crear algunos alimentos
croquetas = Croquetas(50)
heno = Heno(30)

# Agregar los animales y alimentos al arca
try:
    arca.agregar_animal(perro1)
    arca.agregar_animal(gato1)
    arca.agregar_alimento(croquetas)
    arca.agregar_alimento(heno)
except ValueError as e:
    print(e)

# Agregar agua al arca
arca.agregar_agua(100)

# Alimentar y dar agua a los animales
arca.alimentar_animal(perro1)
arca.dar_agua(perro1)
arca.alimentar_animal(gato1)
arca.dar_agua(gato1)

# Ver el estado del arca
estado = arca.estado_arca()
print(f"Estado del Arca: {estado}")

# Mostrar el estado de todos los animales
arca.mostrar_estado_animales()