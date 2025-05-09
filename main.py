import os
import yt_dlp
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty, BooleanProperty
)
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import builder
from android.storage import primary_external_storage_path


"""class WidgetsExample(GridLayout):
    counter = 0
    my_text = StringProperty("0")
    widget_state= StringProperty("OFF")
    state= BooleanProperty(False)
    text_input_str = StringProperty("Write")
    #volumen = StringProperty("")

    def presionado(self):
        if(self.state == True):
            print("Presionado")
            self.counter += 1
            self.my_text = str(self.counter)


    def on_toggle(self, widget):
         print("Estoy: " + widget.state)
         if widget.state == "normal":
              widget.text = "OFF"
              self.state = False
              
         else:
              widget.text= "ON"
              self.state = True
    def on_switch_active(self, switch):
         print("Switch is: " + str(switch.active))
    
    def on_slider_value(self, slider):
         print("Slider: " + str((int(slider.value))))
         #self.volumen = str(int(slider.value))  
    def text_validate(self, input):
         self.text_input_str = input.text
         
                  
         
        
class AnchorLayoutExample(AnchorLayout):
     pass 
class BoxLayoutExample(BoxLayout):
    pass
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B") 
        b3 = Button(text="C")
        #agregar buton a layout
        self.add_widget(b1)
        self.add_widget(b2)  
        self.add_widget(b3)"""
class Aplicacion(GridLayout):

    ydl_opts= {}
    URLS = "" 
    nombre_del_artista = StringProperty("")
    nombre_del_album = StringProperty("")
    directorio = r""
    info = ""
    directorio_full= r""
    #directorio_completo = r""
    

    pass

    def descargar_audio(self):
        self.ydl_opts = {
        'ignoreerrors': True,
        'format': 'm4a/bestaudio/best', 'paths': {"home": self.directorio},
        }
        return self.ydl_opts
    
    def descargar_boton(self):
        
        #Se usa el directorio y si no existe, crea el directorio
       # os.getcwd() para pc
        self.directorio= os.path.join(primary_external_storage_path(), "Music")
        if not os.path.exists(self.directorio):
            os.makedirs(self.directorio)
        
        self.descargar_audio()
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download(self.URLS) 
            


        
class Descargador(App):
    def build(self):
        return Aplicacion()
if __name__ == '__main__':
    Descargador().run()


