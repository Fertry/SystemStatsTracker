###############################

import platform
import cpuinfo
import psutil

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# Función getInfo que obtenga los datos del sistema:
def getInfo():

    procesador = platform.processor()
    marca = cpuinfo.get_cpu_info()["brand"]
    cpu = psutil.cpu_percent(interval=1)
    ram =  "Sólo en linux" #psutil.virtual_memory()["percent"]
    temp = "Sólo en linux" #psutil.cpu_temperature(celsius=True)

    data = {"CPU": str(procesador), "MARCA": str(marca), "CARGA": str(cpu), "RAM": str(ram), "TEMP": str(temp)}

    return data

# Clase Interfaz (de tipo BoxLayaout) que muestre los datos:
class Interfaz(BoxLayout):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.label = Label()
        self.add_widget(self.label)
        self._update()
        self._scheduler = Clock.schedule_interval(self._update, 30)

    def _update(self, dt=None):

        datos = getInfo()
        self.label.text = (

            f'# {datos["CPU"]}\n# {datos["MARCA"]}\nCPU: {datos["CARGA"]}\n'
            f'RAM: {datos["RAM"]}\nTEMPERATURA: {datos["TEMP"]}\n'

            )

# Clase MyApp que instancia Interfaz:
class MyApp(App):

    def build(self):

        return Interfaz()

if __name__ == '__main__':

    # LLamamos a la clase MyApp que hace display de Interfaz:
    MyApp().run()
