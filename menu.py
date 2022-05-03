from ClaseManejadorRegistros import ManejadorRegistros
from clase import Registro

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.salir
                          }
    def opcion(self, unManejadorRegistros, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=="3":
            func(unManejadorRegistros)
        else:
            func()
    def salir(self):
        print('Usted salio del programa')


    def opcion1(self, unManejadorRegistros):
            unManejadorRegistros.mostrarTodosMayorMenor()


    def opcion2(self, unManejadorRegistros):
            unManejadorRegistros.mostrarTemperaturaPromedioTodasHoras()


    def opcion3(self, unManejadorRegistros):
            unManejadorRegistros.listarValoresUnDia()
