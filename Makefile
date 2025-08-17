# Default target


all: install help

install:
	cp src/main.sh ~/.local/bin/player-m3u8
	cp src/main.py ~/.local/bin/playlist.py
	chmod +x ~/.local/bin/player-m3u8
	@echo "player-m3u8	   -> Run the frontend"

help:
	@echo "make install        -> Install frontend"
	@echo "make run            -> Run the music player's frontend"
