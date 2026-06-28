from app.downloader import download
from app.config import DownloadConfig
from app.config_manager import save_config

class Menu:
    def __init__(self, config: DownloadConfig):
        self.running = True
        self.config = config


    def show(self):
        print("1. Descargar canción")
        print("2. Descargar playlist/álbum")
        print("3. Descargar video")
        print("4. Configuración")
        print("5. Salir")

    def show_config_menu(self):
        print("\n=== Configuración actual ===")
        print(f"Formato de audio: {self.config.audio_format}")
        print(f"Calidad de audio: {self.config.audio_quality}")
        print(f"Miniatura: {self.config.embed_thumbnail}")
        print(f"Metadatos: {self.config.add_metadata}")
        print(f"Salida: {self.config.output_template}")

        print("\n=== Configuración ===")
        print(f"1. Cambiar formato actual: {self.config.audio_format}")
        print("2. Volver")

        option = input("Elige una opción: ")

        if option == "1":
            self.change_audio_format()
        
    def change_audio_format(self):
        print("\nFormatos disponibles:")
        print("1. opus")
        print("2. mp3")
        print("3. flac")

        option = input("Elige formato: ")

        if option == "1":
            self.config.audio_format = "opus"
        elif option == "2":
            self.config.audio_format = "mp3"
        elif option == "3":
            self.config.audio_format = "flac"
        else:
            print("Opción inválida")
            return

        save_config(self.config)
        print(f"Formato cambiado a {self.config.audio_format}")


    def run(self):
        while self.running:
            self.show()
            option = input("Elige una opción: ")

            if option == "1":
                self.download_song()
            elif option == "2":
                self.download_playlist()
            elif option == "3":
                self.download_video()
            elif option == "4":
                self.show_config_menu()
            elif option == "5":
                self.running = False
            else:
                print("Opción inválida")
                

    def download_song(self):
        url = input("URL de la canción: ")

        self.config.playlist_mode = False

        if download(url, self.config):
            print("Canción descargada")
        else:
            print("Error al descargar canción")


    def download_playlist(self):
        url = input("URL de la playlist/álbum: ")

        self.config.playlist_mode = True

        if download(url, self.config):
            print("Playlist/álbum descargado")
        else:
            print("Error al descargar playlist/álbum")

    def download_video(self):
        print("Descarga de video todavía no implementada")