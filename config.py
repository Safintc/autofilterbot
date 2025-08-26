
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8237474547:AAGku8w1thZ_yGT5jJrt2RW_h1_G1AO6R_M")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "21116415"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "8e23c9d97d71d525741e33f6b3584f45")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQFCNf8AcDnhigMZt643WfY7AyghykoeTug7yZiUK6o6HPAbxBjN5CrB1lJy5OYs6nzhvYnJLtKqhI9JgorINnGnGX1KIjlQGugPLnVTOa-uZpfbe9_HVP1fgHJKfrmsafZCjjUdO9xYIlHNyFyM62KbNtTQ-b-Uis5bHWH289jcmiynpy-FngQubWuuHs4nM4UThcpcfKJoreT0bB05jecX3nzRvf2Dtd9KdyGNrRKSnDvaPejWJWAiZxuwb74cAaar9z6Z5jNQGftaVW4xFrNApKDSaWMtl7hG_J0ROLWJhsjB14quwnptiHyqDKW0fW83d63iZHmrZryNPBkxLdknTAyJWAAAAABQP9SDAA")

# Database URL from https://cloud.mongodb.com/
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://safin:x0EwcqRWeyafnQIo@cluster0.1qpfh4t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Your database name from mongoDB
DATABASE_NAME = os.environ.get("DATABASE_NAME", "safin")

# ID of users that can use the bot commands
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "-1003073675420").split())

# Should bot search for document files in channels
DOC_SEARCH = os.environ.get("DOC_SEARCH", "yes").lower()

# Should bot search for video files in channels
VID_SEARCH = os.environ.get("VID_SEARCH", "no").lower()

# Should bot search for music files in channels
MUSIC_SEARCH = os.environ.get("MUSIC_SEARCH", "no").lower()




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
