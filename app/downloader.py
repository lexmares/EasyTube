import subprocess
from app.config import DownloadConfig

def check_ytdlp():
    resultado = subprocess.run(["yt-dlp", "--version"], capture_output = True,text = True)

    return resultado.returncode == 0
    

def download(url: str, config: DownloadConfig):
    
    final_command = build_command(config) + [url]

    resultado = subprocess.run(final_command)
    
    return resultado.returncode == 0
        

def build_command(config: DownloadConfig):
    command = ["yt-dlp"]

    if config.audio_only:
        command.append("-x")
        command.extend(["--audio-format", config.audio_format])
        command.extend(["--audio-quality", str(config.audio_quality)])

    if config.embed_thumbnail:
        command.append("--embed-thumbnail")

    if config.add_metadata:
        command.append("--add-metadata")

    if config.playlist_mode:
        command.extend(["-o", config.output_playlist])
    else:
        command.extend(["-o", config.output_single])

    return command


    