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


