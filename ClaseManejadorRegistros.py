from ClaseRegistro import Registro
import csv

class ManejadorRegistros:
    __lista = [[None for j in range(24)] for i in range(30)]
    def __init__(self):
        self.__lista = [[None for j in range(24)] for i in range(30)]
    def agregarRegistro(self, unRegistro, dia, hora):
        self.__lista[dia-1][hora] = unRegistro

    def cargarCSV(self, nombreArchivo):
        with open(nombreArchivo) as archivo:
            reader = csv.reader(archivo, delimiter=";")
            primera = True
            for fila in reader:
                if primera:
                    primera = False
                else:
                    unRegistro = Registro(float(fila[2]), float(fila[3]), float(fila[4]))
                    self.agregarRegistro(unRegistro, int(fila[0]), int(fila[1]))
    def getDiaHoraMenorTemperatura(self):
        dia = 0
        hora = 0
        for i in range(30):
            for j in range(24):
                if self.__lista[dia][hora].getTemperatura() > self.__lista[i][j].getTemperatura():
                    dia = i
                    hora = j
        return (dia+1, hora)

    def getDiaHoraMayorTemperatura(self):
        dia = 0
        hora = 0
        for i in range(30):
            for j in range(24):
                if self.__lista[dia][hora].getTemperatura() < self.__lista[i][j].getTemperatura():
                    dia = i
                    hora = j
        return (dia+1, hora)

    def getDiaHoraMenorHumedad(self):
        dia = 0
        hora = 0
        for i in range(30):
            for j in range(24):
                if self.__lista[dia][hora].getHumedad() > self.__lista[i][j].getHumedad():
                    dia = i
                    hora = j
        return (dia+1, hora)

    def getDiaHoraMayorHumedad(self):
        dia = 0
        hora = 0
        for i in range(30):
            for j in range(24):
                if self.__lista[dia][hora].getHumedad() < self.__lista[i][j].getHumedad():
                    dia = i
                    hora = j
        return (dia+1, hora)

    def getDiaHoraMenorPresion(self):
        dia = 0
        hora = 0
        for i in range(30):
            for j in range(24):
                if self.__lista[dia][hora].getPresion() > self.__lista[i][j].getPresion():
                    dia = i
                    hora = j
        return (dia+1, hora)

    def getDiaHoraMayorPresion(self):
        dia = 0
        hora = 0
        for i in range(30):
            for j in range(24):
                if self.__lista[dia][hora].getPresion() < self.__lista[i][j].getPresion():
                    dia = i
                    hora = j
        return (dia+1, hora)

    def mostrarTodosMayorMenor(self):
        diaMayorTemp, horaMayorTemp = self.getDiaHoraMayorTemperatura()
        diaMenorTemp, horaMenorTemp = self.getDiaHoraMenorTemperatura()
        diaMayorHumedad, horaMayorHumedad = self.getDiaHoraMayorHumedad()
        diaMenorHumedad, horaMenorHumedad = self.getDiaHoraMenorHumedad()
        diaMayorPresion, horaMayorPresion = self.getDiaHoraMayorPresion()
        diaMenorPresion, horaMenorPresion = self.getDiaHoraMenorPresion()
        print("Valores extremos".center(120, "-"))
        print("Dia y hora con mayor temperatura: {0} a las {1}hs con {2}°C".format(diaMayorTemp, horaMayorTemp, self.__lista[diaMayorTemperatura-1][horaMayorTemperatura].getTemperatura()))
        print("Dia y hora con menor temperatura: {0} a las {1}hs con {2}°C".format(diaMenorTemp, horaMenorTemp, self.__lista[diaMenorTemperatura-1][horaMenorTemperatura].getTemperatura()))
        print("Dia y hora con mayor humedad: {0} a las {1}hs con {2}%".format(diaMayorHumedad, horaMayorHumedad, self.__lista[diaMayorHumedad-1][horaMayorHumedad].getHumedad()))
        print("Dia y hora con menor humedad: {0} a las {1}hs con {2}%".format(diaMenorHumedad, horaMenorHumedad, self.__lista[diaMenorHumedad-1][horaMenorHumedad].getHumedad()))
        print("Dia y hora con mayor presion: {0} a las {1}hs con {2}mmHg".format(diaMayorPresion, horaMayorPresion, self.__lista[diaMayorPresion-1][horaMayorPresion].getPresion()))
        print("Dia y hora con menor presion: {0} a las {1}hs con {2}mmHg".format(diaMenorPresion, horaMenorPresion, self.__lista[diaMenorPresion-1][horaMenorPresion].getPresion()))

    def calcularTemperaturaPromedioHora(self, hora:int):
        promedio = None
        if 0<=hora<=23:
            total = 0
            for i in range(30):
                total += self.__lista[i][hora].getTemperatura()
            promedio = total / 30

        return promedio

    def mostrarTemperaturaPromedioTodasHoras(self):
        print("Temperaturas promedio mensual")
        print("Hora y Temperatura")
        for hora in range(24):
            temperatura = self.calcularTemperaturaPromedioHora(hora)
            print(hora, temperatura)

    def listarValoresUnDia(self):
        dia = int(input("Ingrese el dia: "))
        if 1<=dia<=30:
            print(("Valores del dia "dia)
            print("Hora Temperatura Humedad Presion"))
            for hora in range(24):
                print(hora, self.__lista[dia-1][hora].getTemperatura(), self.__lista[dia-1][hora].getHumedad(), self.__lista[dia-1][hora].getPresion()))
        else:
            print("El dia debe estar comprendido entre 1 y 30")
