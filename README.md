# player-playlist

**A frontend that brings `.m3u8` playlist magic to player.** Now you can play whole playlists with *album → title/artist* styling, clean progress bars, and all the adorable terminal charm I've shaped!

---

## What It Does

* Parses `.m3u8` playlist files (UTF-8-safe, BOM stripped, handles CRLF and LF)
* Skips comments and blank lines, so the first track always plays perfectly
* Resolves relative file paths relative to the playlist's directory
* Plays each track **one by one** using your existing `player.py` or equivalent
* Stops cleanly on your command—like the cutest bouncer ever!

---

## Installation

```bash
git clone https://github.com/vbloom-x3/player-playlist.git
cd player-playlist
make install
```

That installs two handy scripts:

* `~/.local/bin/player-m3u8` – quick bash frontend to use playlists
* `~/.local/bin/playlist.py` – versatile Python playlist player

Make sure `~/.local/bin` is in your PATH!

### Requirements for Installation

* player : [ visit ](https://github.com/vbloom-x3/player)

---

## Usage

### Play a playlist simply:

```bash
player-m3u8 "/path/to/your/playlist.m3u8"
```

You'll see something like:

```
▶ Now playing: Album – Title — Artist
```

---

## Why It’s So Useful!

| Feature               | Sweet Benefit                                        |
| --------------------- | ---------------------------------------------------- |
| BOM + CRLF handling   | Supports Windows and Unix playlists equally          |
| Relative path support | No more broken links in M3U8                         |
| Clean error skipping  | It tells you if a track can't be found—cute honesty! |
| Modular design        | Keeps your **player.py** separate and focused        |

---
