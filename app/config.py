from dataclasses import dataclass

@dataclass
class DownloadConfig:
    audio_only: bool = True

    audio_format: str = "opus"
    audio_quality: int = 0

    video_quality: str = "1080"
    video_format: str = "mp4"

    embed_thumbnail: bool = True
    add_metadata: bool = True

    output_single: str = "~/Música/EasyTube/Singles/%(title)s.%(ext)s"
    output_playlist: str = "~/Música/EasyTube/%(playlist)s/%(playlist_index)02d - %(title)s.%(ext)s"
    output_video: str = "~/Vídeos/EasyTube/%(title)s.%(ext)s"
    
    playlist_mode: bool = False
