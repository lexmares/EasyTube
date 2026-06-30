
# EasyTube

EasyTube es una herramienta de línea de comandos para descargar audio desde enlaces compatibles con `yt-dlp`.  
El proyecto está pensado como una interfaz sencilla para descargar canciones, playlists o álbumes, guardando una configuración local reutilizable.

> Proyecto en desarrollo. Actualmente la descarga de video todavía no está implementada.

## Características

- Descarga canciones en modo audio.
- Descarga playlists o álbumes.
- Permite elegir formato de audio:
  - `opus`
  - `mp3`
  - `m4a`
- Inserta miniatura cuando está disponible.
- Agrega metadatos al archivo descargado.
- Guarda configuración local en `settings.json`.
- Usa `yt-dlp` como motor principal de descarga.

## Requisitos

Antes de ejecutar EasyTube necesitas tener instalado:

- Python 3
- `yt-dlp`
- `ffmpeg`

`ffmpeg` es necesario para convertir audio, agregar metadatos y trabajar con miniaturas.

Puedes instalar `yt-dlp` con:

```bash
pip install yt-dlp
```

En Linux, también puedes instalar `ffmpeg` con el gestor de paquetes de tu distribución. Por ejemplo:

```bash
sudo apt install ffmpeg
```

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/lexmares/EasyTube.git
cd EasyTube
```

Opcionalmente, crea un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

Instala las dependencias necesarias:

```bash
pip install yt-dlp
```

## Uso

Ejecuta el programa desde la raíz del proyecto:

```bash
python main.py
```

Al iniciar, EasyTube mostrará un menú como este:

```text
1. Descargar canción
2. Descargar playlist/álbum
3. Descargar video
4. Configuración
5. Salir
```

### Descargar una canción

Selecciona la opción `1` e ingresa la URL de la canción.

### Descargar una playlist o álbum

Selecciona la opción `2` e ingresa la URL de la playlist o álbum.

### Cambiar configuración

Selecciona la opción `4` para ver la configuración actual y cambiar el formato de audio.

Actualmente se puede cambiar el formato entre:

- `opus`
- `mp3`
- `m4a`

## Configuración

EasyTube genera automáticamente un archivo llamado `settings.json` en la raíz del proyecto.

Este archivo guarda la configuración actual del programa, por ejemplo:

```json
{
    "audio_only": true,
    "audio_format": "opus",
    "audio_quality": 0,
    "embed_thumbnail": true,
    "add_metadata": true,
    "output_template": "~/Música/MusicEasy/%(playlist)s/%(playlist_index)02d - %(title)s.%(ext)s",
    "output_single": "~/Música/MusicEasy/Singles/%(title)s.%(ext)s",
    "output_playlist": "~/Música/MusicEasy/%(playlist)s/%(playlist_index)02d - %(title)s.%(ext)s",
    "playlist_mode": false
}
```

Si el archivo `settings.json` no existe, el programa lo crea automáticamente con valores por defecto.

## Estructura del proyecto

```text
EasyTube/
├── app/
│   ├── config.py
│   ├── config_manager.py
│   ├── downloader.py
│   ├── menu.py
│   └── utils.py
├── main.py
├── requirements.txt
└── README.md
```

### Archivos principales

- `main.py`: punto de entrada del programa.
- `app/menu.py`: contiene el menú interactivo de consola.
- `app/downloader.py`: construye y ejecuta los comandos de `yt-dlp`.
- `app/config.py`: define la configuración del programa con `DownloadConfig`.
- `app/config_manager.py`: carga y guarda la configuración en `settings.json`.

## Estado actual

Funcional:

- Descarga de canciones como audio.
- Descarga de playlists o álbumes.
- Configuración persistente en JSON.
- Cambio de formato de audio desde el menú.

Pendiente:

- Implementar descarga de video.
- Mejorar validaciones de entrada.
- Verificar automáticamente si `yt-dlp` y `ffmpeg` están instalados.
- Agregar más opciones de configuración desde el menú.
- Agregar manejo de errores más detallado.

## Nota de uso

EasyTube utiliza `yt-dlp`. Asegúrate de usar esta herramienta respetando los términos de servicio de cada plataforma y las leyes aplicables en tu país.

## Autor

Desarrollado por [lexmares](https://github.com/lexmares).
```
