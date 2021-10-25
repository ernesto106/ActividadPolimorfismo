from polimorfismo.Animal import Animal
from polimorfismo.Especies import Perro, Gato

# Instanciamos la clase
animal1=Animal()
perro1=Perro()
gato1 = Gato()

#Ulizamos los metodos de la clase
print("Animal:------")
animal1.hablar()
animal1.correr()

print("Perro:-------")
perro1.hablar()
perro1.correr()

print("Gato:--------")
gato1.hablar()
gato1.correr()