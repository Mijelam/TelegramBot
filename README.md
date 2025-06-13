# TelegramBot
A handy Telegram bot that tells you the weather and lets you download YouTube videos as MP3s.

## Features
- `/weather <city>` → Get the current weather in the specified city.  
- `/youtube <link>` → Download the audio from a YouTube video as an MP3.

## Requirements
- Python 3.12.4 (you can try older versions, it should work fine)
- You need to install the `requests` dependency
- You need to download [FFmpeg] (required by yt-dlp for audio conversion)  
  - Go to https://www.gyan.dev/ffmpeg/builds/  
  - In the **Release builds** section, click on `ffmpeg-release-essentials.zip` to download  
  - Then unzip it somewhere on your machine
- Telegram bot token
- Chat ID
- OpenWeatherMap API key

## Setup
- Clone this repo
- Go to Telegram and search for [@BotFather](https://t.me/BotFather) to create a bot. He will give you a token — copy and paste it into the `TOKEN` variable.
- Use your token here: `https://api.telegram.org/bot<TOKEN>/getUpdates`
- Send a message to your bot, then use the link above to find your Chat ID. Copy and paste it into the `CHAT_ID` variable.
- Go to [openweathermap.org](https://openweathermap.org/), create an account and get your API key
- Copy and paste your API key into the `OWM_API_KEY` variable
- Edit the `download_and_send_mp3` function — specifically this line:  
  `"--ffmpeg-location", r"THE_PATH_TO_YOUR_FFMPEG_EXE_FOLDER_HERE"`  
  Replace it with the actual path to your `ffmpeg.exe`. For example:  
  `"--ffmpeg-location", r"C:\Path\To\ffmpeg\bin"`
- And that’s it — you’re ready to go
