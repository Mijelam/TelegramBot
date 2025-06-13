import requests
import time
import json
import subprocess
import os

# Replace with your own Telegram bot token and chat ID
TOKEN = 'YOUR  TOKEN FROM TELEGRAM HERE'
CHAT_ID = 'THE ID FROM YOUR CHAT  HERE'
OWM_API_KEY = "YOUR KEY FROM  THE  WEATHER  API HERE"

# Function to send a text message
def send_message(text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {
        'chat_id': CHAT_ID,
        'text': text
    }
    response = requests.post(url, params=params)

# Function to send an audio file
def send_audio(audio_mp3):
    url = f'https://api.telegram.org/bot{TOKEN}/sendAudio'
    params = {
        'chat_id': CHAT_ID
    }
    with open(audio_mp3, 'rb') as audio_file:
        files = {
            'audio': audio_file
        }
        response = requests.post(url, params=params, files=files)

# Function to get weather info for a given city
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM_API_KEY}&units=metric&lang=en"
    response = requests.get(url)
    print(f"Message received: {response}")
    if response.status_code != 200:
        return "Could not retrieve weather data. Did you spell the city correctly?"
    
    data = response.json()
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    name_city = data["name"]
    name_country = data["sys"]["country"]
    return f"The weather in {name_city}, {name_country} is {temperature}°C with {description}."

# To avoid processing the same message multiple times
last_update_id = 0

# Function to check incoming messages and respond accordingly
def review_messages():
    global last_update_id 
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset={last_update_id + 1}"
    response = requests.get(url).json()
    print(json.dumps(response, indent=2, ensure_ascii=False))
    print("Checking messages...")
    for messages in response["result"]:
        
        text = messages["message"]["text"]
        
        if text.startswith("/weather"):
            a_split = text.split(maxsplit=1)
            if len(a_split) > 1:
                chosen_city = a_split[1]
                getting_weather = get_weather(chosen_city)
                send_message(getting_weather)
                print("Reply sent to user.")
            else:
                send_message("Please provide a valid city. Example: /weather Berlin")
        
        elif text.startswith("/youtube"):
            a_split = text.split(maxsplit=1)
            if len(a_split) > 1:
                youtube_url = a_split[1]
                send_message("Downloading audio, please wait...")
                result = download_and_send_mp3(youtube_url)  
                send_message(result)
            else:
                send_message("Please send the video link. Example: /youtube https://...")

        last_update_id = messages["update_id"]

# Function to download a YouTube video as MP3 and send it
def download_and_send_mp3(youtube_url):
    try:
        output_file = "%(title)s.%(ext)s"

        subprocess.run([
            "yt-dlp",
            "--ffmpeg-location", r"THE_PATH_TO_YOUR_FFMPEG_EXE_FOLDER_HERE",
            "-x", "--audio-format", "mp3",
            "-o", output_file,
            youtube_url
        ], check=True)

        # Look for and send the mp3 file
        for file in os.listdir():
            if file.endswith(".mp3"):
                send_audio(file)
                os.remove(file)
                return f"Audio '{file}' sent successfully."

        return "MP3 file not found."

    except Exception as e:
        return f"Error while downloading audio: {e}"

# Loop to continuously check for new messages
while True:
    review_messages()
    time.sleep(15)





