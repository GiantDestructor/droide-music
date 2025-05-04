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
import requests
from mutagen.mp4 import MP4, MP4Cover
from mutagen.m4a import M4A, M4ACover
#from android.storage import primary_external_storage_path
import os

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
       # primary_external_storage_path()
        self.directorio= os.path.join(os.getcwd(), "Music")
        if not os.path.exists(self.directorio):
            os.makedirs(self.directorio)
        

        """try:
            audio = MP4(self.directorio)
        except PermissionError: ("cagaste")"""
        
        self.descargar_audio()
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            self.info = ydl.extract_info(self.URLS, download=True)
            self.directorio_full= os.path.join(self.directorio, ydl.prepare_filename(self.info).replace(".webm", ".m4a").replace(".m4a.m4a", ".m4a"))
            self.agregar_metadatos()

    def agregar_metadatos(self):
        audio = MP4(self.directorio_full)
        audio.tags["\xa9ART"] = self.nombre_del_artista  # Artista
        audio.tags["\xa9alb"] = self.nombre_del_album  # Álbum

        
        portada_url = self.info.get("thumbnail", None)
        if portada_url:
            imagen = requests.get(portada_url).content
            audio["covr"] = [MP4Cover(imagen, imageformat=MP4Cover.FORMAT_JPEG)]
        
        audio.save()

        
class Descargador(App):
    def build(self):
        return Aplicacion()
if __name__ == '__main__':
    Descargador().run()

"""def descargar_audio(directorio):
        nombre_del_artista = ""
        nombre_del_album = ""
        albumSN = input("¿Quiere descargar un album? \n (s/n)")
        if (albumSN == "s"):
            nombre_del_album= input("---> Nombre del Album ")
            nombre_del_artista= input("---> Nombre del Artista ")
        else: pass
        ydl_opts = {
        'ignoreerrors': True,
        'format': 'm4a/bestaudio/best', 'paths': {"home": directorio},
        'postprocessors': 
        [{  
            'key': 'FFmpegExtractAudio',
         'preferredcodec': 'mp3'
        },
        
        {
            'key': 'FFmpegMetadata',
        
        },
        {
            'key': 'EmbedThumbnail'
        }
        ],
        'postprocessor_args': [  
            '-metadata', f'artist={nombre_del_artista}',
            '-metadata', f'album={nombre_del_album}',
        ],
        
        "writethumbnail" : True
        
    }
        return ydl_opts"""
def descargar_video_sinFfmpeg(directorio):

    ydl_opts = {
    'ignoreerrors': {True},
    'format': 'mp4/best',
    'paths': {"home": directorio}
         }
    
    return ydl_opts

def conFf(directorio):
    ydl_opts= {
        'ignoreerrors': True,
        'format': 'bv*[vcodec^=avc1][height<=1080]+m4a/best', #una forma de descargar solo la versión de 1080 o mejor pero no en Av01 o Av1 y descargar el mejor audio y convertirlo en wav y luego los juntamos.
        'merge_output_format' : 'mp4',
        'paths' : {"home" : directorio},
         'postprocessors':
           [                
            {                
                'key': 'FFmpegVideoConvertor',  #asegurar video en mp4
                'preferedformat': 'mp4'
            }
            
            ],
            
    
    }
    return ydl_opts
    
def bienvenida():
    print(r'  _____  ______  _____  _____          _____   _____          _____   ____  _____  ')
    print(r' |  __ \|  ____|/ ____|/ ____|   /\   |  __ \ / ____|   /\   |  __ \ / __ \|  __ \ ')
    print(r' | |  | | |__  | (___ | |       /  \  | |__) | |  __   /  \  | |  | | |  | | |__) |')
    print(r' | |  | |  __|  \___ \| |      / /\ \ |  _  /| | |_ | / /\ \ | |  | | |  | |  _  / ')
    print(r' | |__| | |____ ____) | |____ / ____ \| | \ \| |__| |/ ____ \| |__| | |__| | | \ \ ')
    print(r' |_____/|______|_____/ \_____/_/    \_\_|  \_\\_____/_/    \_\_____/ \____/|_|  \_/')
    print(r'                                                                                   ')

"""programa = True;
bienvenida()
directorio = input(r"Directorio: ")
while programa == True:
    
    
    # 1
    URLS = input("--> URL ") 
    opcion = input("--> ¿Video o Audio? \n (v/a) ")

    if(opcion == "a"):
        ydl_opts = descargar_audio(directorio)
    # que pasa cuando queremos video
    elif (opcion =="v"):
        ffm = input("Si quiere descargar videos de alta calidad, requiere tener descargado Ffmpeg ¿Lo tiene?\n s/n")
        if(ffm == "s"):
         #si
            ydl_opts = conFf(directorio)
        else:
            ydl_opts = descargar_video_sinFfmpeg(directorio)

    # Que pasa cuando queremos audio
    

   
    
         
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS) 
        print("Continuar? s/n")
        continuar = input("")
        if continuar == "s":
            pass
        else:
            programa = False"""
