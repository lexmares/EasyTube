from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Input, Button
from textual.containers import Container, Vertical, Horizontal

from app.downloader import download


class DownloadSongScreen(Screen):
    CSS = """
    Screen {
        align: center middle;
    }

    #panel {
        width: 70;
        height: auto;
        border: round white;
        padding: 1 2;
    }

    #title {
        text-align: center;
        text-style: bold;
        margin-bottom: 1;
    }

    Input {
        margin: 1 0;
    }

    Button {
        margin: 1;
    }

    #status {
        margin-top: 1;
        text-align: center;
    }
    """

    def __init__(self, config):
        super().__init__()
        self.config = config

    def compose(self) -> ComposeResult:
        yield Header()

        yield Container(
            Vertical(
                Static("🎵 Descargar canción", id="title"),
                Input(placeholder="Pega la URL de YouTube o YouTube Music", id="url_input"),
                Horizontal(
                    Button("Descargar", id="download", variant="primary"),
                    Button("Volver", id="back"),
                ),
                Static("", id="status"),
            ),
            id="panel",
        )

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.app.pop_screen()

        elif event.button.id == "download":
            url_input = self.query_one("#url_input", Input)
            status = self.query_one("#status", Static)

            url = url_input.value.strip()

            if not url:
                status.update("Pega una URL primero.")
                return

            self.config.audio_only = True
            self.config.playlist_mode = False

            status.update("Descargando canción...")

            result = download(url, self.config)
            status.update(result.message)