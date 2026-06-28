from dataclasses import dataclass

@dataclass
class DownloadConfig:
    audio_only: bool = True
    audio_format: str = "opus"
    audio_quality: int = 0
    embed_thumbnail: bool = True
    add_metadata: bool = True
    output_template: str = "~/Música/MusicEasy/%(playlist)s/%(playlist_index)02d - %(title)s.%(ext)s"
    output_single: str = "~/Música/MusicEasy/Singles/%(title)s.%(ext)s"
    output_playlist: str = "~/Música/MusicEasy/%(playlist)s/%(playlist_index)02d - %(title)s.%(ext)s"
    playlist_mode: bool = False