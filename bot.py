import telebot
import os
import time
from loguru import logger

count = 0
bots = [token_list]  # Enter the bot token list
all_files = os.listdir("path")  # Enter the directory with .jpg files
time_out = 3.2
print(all_files)


def add_photo(token_bot, file):
    # The method posts the photo to the channel and removes it from the directory

    bot = telebot.TeleBot(f"{token_bot}")
    bot.send_photo("@channel",  # Enter the username of the @channel
                   photo=open(f"path{file}", "rb"))  # Enter a directory with .jpg files
    print(file)
    #os.remove(f"path{file}")  # Enter a directory with .jpg files
    time.sleep(time_out)  # Sleep time is taken on the basis that each bot
    # will add no more than 20 posts per minute (Telegramm limitation)


if __name__ == "__main__":

    for files in all_files:
        try:
            if count == len(bots):
                count = 0
                add_photo(bots[count], files)
            else:
                add_photo(bots[count], files)
                count += 1
        except Exception as e:
            logger.error(e)
            logger.add('log_path',  # Enter the directory where the log file will be located
                       format="{time} {message}",
                       level='ERROR')
