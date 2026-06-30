import subprocess
from app.config import DownloadConfig
from dataclasses import dataclass

@dataclass
class DownloadResult:
    success: bool
    message: str
    command: list[str]

def check_ytdlp():
    resultado = subprocess.run(["yt-dlp", "--version"], capture_output = True,text = True)

    return resultado.returncode == 0
    
def parse_error(stderr: str) -> str:
    if "module mutagen was not found" in stderr:
        return "Falta instalar mutagen. Ejecuta: pip install mutagen"

    if "ffmpeg" in stderr.lower() and "not found" in stderr.lower():
        return "Falta instalar FFmpeg."

    if "requested format is not available" in stderr.lower():
        return "El formato solicitado no está disponible para este video."

    return "Ocurrió un error durante la descarga."


def download(url: str, config: DownloadConfig) -> DownloadResult:
    final_command = build_command(config) + [url]

    resultado = subprocess.run(
        final_command,
        capture_output=True,
        text=True
    )

    if resultado.returncode == 0:
        return DownloadResult(
            success=True,
            message="Descarga completada ✅",
            command=final_command
        )

    return DownloadResult(
        success=False,
        message=parse_error(resultado.stderr),
        command=final_command
    )        

def build_command(config: DownloadConfig):
    command = ["yt-dlp"]

    if config.audio_only:
        command.append("-x")
        command.extend(["--audio-format", config.audio_format])
        command.extend(["--audio-quality", str(config.audio_quality)])

        if config.embed_thumbnail:
            command.append("--embed-thumbnail")

        if config.playlist_mode:
            command.extend(["-o", config.output_playlist])
        else:
            command.extend(["-o", config.output_single])

    else:
        command.extend([
            "-f",
            f"bv*[height<={config.video_quality}]+ba/b[height<={config.video_quality}]"
        ])
        command.extend(["--merge-output-format", config.video_format])
        command.extend(["-o", config.output_video])

    if config.add_metadata:
        command.append("--add-metadata")

    return command
    
