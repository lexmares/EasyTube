
````markdown
# EasyTube Architecture

EasyTube is a terminal-based application that wraps `yt-dlp` to download songs, playlists and albums more easily.

## Current Goal

The current goal of EasyTube is to provide a simple interface for downloading audio from YouTube and YouTube Music, while keeping the download logic separated from the user interface.

## Main Principles

- Keep the download engine independent from the interface.
- Store user preferences in a JSON configuration file.
- Avoid hardcoding download options in the menu.
- Keep each module focused on one responsibility.
- Design the app so the current console menu can later be replaced by a richer TUI.

## Current Structure

```text
easytube/
├── main.py
├── settings.json
├── requirements.txt
├── README.md
├── docs/
│   └── ARCHITECTURE.md
└── app/
    ├── __init__.py
    ├── config.py
    ├── config_manager.py
    ├── downloader.py
    ├── menu.py
    └── utils.py
````

## Module Responsibilities

### `main.py`

Application entry point.

Responsibilities:

* Load the user configuration.
* Create the menu.
* Start the application loop.

### `app/config.py`

Defines the data structures used by the application.

Main class:

* `DownloadConfig`

Responsibilities:

* Store download preferences.
* Represent the current download configuration as a Python object.

### `app/config_manager.py`

Handles configuration persistence.

Responsibilities:

* Load configuration from `settings.json`.
* Save configuration to `settings.json`.
* Create a default configuration when no config file exists.

### `app/downloader.py`

Download engine.

Responsibilities:

* Check if `yt-dlp` is available.
* Convert `DownloadConfig` into a valid `yt-dlp` command.
* Execute the download command.
* Return whether the download succeeded.

### `app/menu.py`

Current console interface.

Responsibilities:

* Show menu options.
* Read user input.
* Call the download engine.
* Modify configuration through the config manager.

### `app/utils.py`

Reserved for general utility functions.

Currently unused or experimental.

## Current Flow

```text
main.py
  ↓
load_config()
  ↓
Menu(config)
  ↓
User selects an action
  ↓
download(url, config)
  ↓
build_command(config)
  ↓
yt-dlp
```

## Configuration Flow

```text
settings.json
  ↓
load_config()
  ↓
DownloadConfig
  ↓
Menu
  ↓
User changes setting
  ↓
save_config()
  ↓
settings.json
```

## Download Flow

```text
User selects song or playlist
  ↓
Menu sets playlist mode
  ↓
User enters URL
  ↓
download(url, config)
  ↓
build_command(config)
  ↓
subprocess.run()
  ↓
yt-dlp downloads content
```

## Future Structure

When EasyTube moves to a richer terminal interface, the UI should be separated from the core engine:

```text
easytube/
├── main.py
├── app/
│   ├── config.py
│   ├── config_manager.py
│   ├── downloader.py
│   └── utils.py
├── ui/
│   ├── app.py
│   ├── screens/
│   │   ├── home.py
│   │   ├── download.py
│   │   └── settings.py
│   └── widgets/
│       ├── menu.py
│       └── progress.py
└── docs/
    └── ARCHITECTURE.md
```

## Planned Improvements

### Interface

* Replace the basic console menu with a richer terminal UI.
* Add navigation with keyboard.
* Add clearer download screens.
* Add visual status messages.

### Download Experience

* Add better output organization.
* Add video download support.
* Add download queue support.
* Add better error handling.

### History

A simple `yt-dlp --download-archive` approach was considered, but postponed.

Reason:

* `yt-dlp` archive tracks video IDs only.
* It does not distinguish between formats such as `mp3`, `opus`, or `flac`.
* EasyTube may later need a custom history system that stores title, format, path, playlist, date and video ID.

### Distribution

* Add proper packaging.
* Allow running EasyTube with a command like:

```bash
easytube
```

* Add releases on GitHub.

````

Después:

```bash
git add docs/ARCHITECTURE.md
git commit -m "Add architecture document"
git push
````
