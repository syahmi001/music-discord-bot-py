# Discord Music bot
Prominent music discord bots have been banned from searching song in Youtube. Thus, many developers decided to host their own music discord bot.
Below are the commands:

/help - displays all the available commands
/p <keywords> - finds the song on youtube and plays it in your current channel. Will resume playing the current song if it was paused
/q - displays the current music queue\
/skip - skips the current song being played\
/clear - Stops the music and clears the queue\
/leave - Disconnected the bot from the voice channel\
/pause - pauses the current song being played or resumes if already paused\
/resume - resumes playing the current song

# Running with docker
To run with docker simply run the command `docker run -e TOKEN=<your_token_here> -d <your_dockerhub_name>/music_bot:latest`


# Installation
To run the discord bot all you need is python 3.4 or above.\
Then run `pip install -r requirements.txt` to install all of the python dependencies.\
Please note that you will also need to have [ffmpeg](https://ffmpeg.org/download.html) installed and make sure that the path to the bin folder is in your environment variables. 

# Token
You can either decide to put the token value in `config.py` file or in `.env` file.
