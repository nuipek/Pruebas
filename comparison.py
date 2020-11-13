

class Prueba:
   def __init__(self, name, edad=26):
      self.nombre = name
      self.edad = edad
      self.apellido = "Paco"

   def __eq__(self, other):
      if not isinstance(other, Prueba):
         # don't attempt to compare against unrelated types
         return NotImplemented
      if self is other:
         return True
      else:
         return self.__dict__ == other.__dict__

if __name__ == "__main__":
   prueba1 = Prueba("Paco", 26)
   prueba2 = Prueba("Manolo")
   prueba3 = Prueba("Manolo")
   prueba4 = Prueba("Manolo")

   print(repr(prueba1))
   print(repr(prueba2))
   lista = list()
   lista.extend([prueba1,prueba2, prueba3])

   if prueba4 in lista:
      print(True)

   # print(prueba1 == prueba3)