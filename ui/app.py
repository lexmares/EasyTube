from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Container, Vertical
from app.config_manager import load_config
from ui.screens.download_song import DownloadSongScreen

class EasyTubeApp(App):
    CSS = """
    Screen {
        align: center middle;
    }

    #main-panel {
        width: 60;
        height: auto;
        border: round white;
        padding: 1 2;
    }

    #title {
        text-align: center;
        text-style: bold;
        margin-bottom: 1;
    }

    #subtitle {
        text-align: center;
        color: gray;
        margin-bottom: 2;
    }

    Button {
        width: 100%;
        margin: 1 0;
    }

    #status {
        margin-top: 2;
        text-align: center;
        color: gray;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        yield Container(
            Vertical(
                Static("🎵 EasyTube", id="title"),
                Static("Download music and videos with yt-dlp", id="subtitle"),
                Button("Descargar canción", id="download_song"),
                Button("Descargar playlist/álbum", id="download_playlist"),
                Button("Descargar video", id="download_video"),
                Button("Configuración", id="settings"),
                Button("Salir", id="exit"),
                Static("Audio format: OPUS | Video: 1080p MP4", id="status"),
            ),
            id="main-panel",
        )

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "download_song":
            self.push_screen(DownloadSongScreen(self.config))
        elif event.button.id == "exit":
            self.exit()


    def __init__(self):
        super().__init__()
        self.config = load_config()