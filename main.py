import os
import discord
from dotenv import load_dotenv
import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime
import requests
import json
import http.client


#new comment
#another comment

load_dotenv()
#load_dotenv('---.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
AUTH = os.getenv('AUTHORIZATION')
#DISCORDCHANNEL = os.getenv('DISCORD_CHANNEL')

def myInfo():
    conn = http.client.HTTPSConnection("api.zoom.us")

    headers = {
        'authorization': "Bearer " + AUTH,
        'content-type': "application/json"
        }

    conn.request("GET", "https://api.zoom.us/v2/users/me", headers=headers)

    res = conn.getresponse()
    data = res.read()
    
    y = data.decode("utf-8")
    new = json.loads(y)
    #print(type(y))
    #print(y)
    result = [new['personal_meeting_url'], new['first_name'], new['last_name'], new['created_at']]
    return result


def createMeeting():
    conn = http.client.HTTPSConnection("api.zoom.us")

    payload = "{\"topic\":\"string\",\"type\":\"integer\",\"start_time\":\"string [date-time]\",\"duration\":\"integer\",\"schedule_for\":\"string\",\"timezone\":\"string\",\"password\":\"string\",\"agenda\":\"string\",\"recurrence\":{\"type\":\"integer\",\"repeat_interval\":\"integer\",\"weekly_days\":\"string\",\"monthly_day\":\"integer\",\"monthly_week\":\"integer\",\"monthly_week_day\":\"integer\",\"end_times\":\"integer\",\"end_date_time\":\"string [date-time]\"},\"settings\":{\"host_video\":\"boolean\",\"participant_video\":\"boolean\",\"cn_meeting\":\"boolean\",\"in_meeting\":\"boolean\",\"join_before_host\":\"boolean\",\"mute_upon_entry\":\"boolean\",\"watermark\":\"boolean\",\"use_pmi\":\"boolean\",\"approval_type\":\"integer\",\"registration_type\":\"integer\",\"audio\":\"string\",\"auto_recording\":\"string\",\"enforce_login\":\"boolean\",\"enforce_login_domains\":\"string\",\"alternative_hosts\":\"string\",\"global_dial_in_countries\":[\"string\"],\"registrants_email_notification\":\"boolean\"}}"
    #payload = "{\"topic\":\"string\",\"type\":\"integer\",\"start_time\":\"string [date-time]\",\"duration\":\"integer\",\"schedule_for\":\"string\",\"timezone\":\"string\",\"password\":\"string\",\"agenda\":\"string\",\"recurrence\":{\"type\":\"integer\",\"repeat_interval\":\"integer\",\"weekly_days\":\"string\",\"monthly_day\":\"integer\",\"monthly_week\":\"integer\",\"monthly_week_day\":\"integer\",\"end_times\":\"integer\",\"end_date_time\":\"string [date-time]\"},\"settings\":{\"host_video\":\"boolean\",\"participant_video\":\"boolean\",\"cn_meeting\":\"boolean\",\"in_meeting\":\"boolean\",\"join_before_host\":\"boolean\",\"mute_upon_entry\":\"boolean\",\"watermark\":\"boolean\",\"use_pmi\":\"boolean\",\"approval_type\":\"integer\",\"registration_type\":\"integer\",\"audio\":\"string\",\"auto_recording\":\"string\",\"enforce_login\":\"boolean\",\"enforce_login_domains\":\"string\",\"alternative_hosts\":\"string\",\"global_dial_in_countries\":,\"registrants_email_notification\":\"boolean\"}}"

    headers = {
        'authorization': "Bearer " + AUTH,
        'content-type': "application/json"
        }

    conn.request("POST", "/v2/users/me/", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

#createMeeting()
myInfo()

#discord getting info
client = discord.Client()
#channel = client.get_channel(DISCORDCHANNEL)
id = client.get_guild(GUILD)
#print(channel)
#print(id)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    # print(
    #     f'{client.user} is connected to the following guild:\n'
    #     f'{guild.name}(id: {guild.id})\n'
    # )

# @client.event
# async def on_message(message):
#     if message.content.find("!hello") != -1:
#         await message.channel.send("Hi")
#     elif message.content == ("!stop"):
#         await client.close()

collection = myInfo()
print(collection)
print(type(collection))

@client.event
async def on_message(message):
    if message.content.find("!new") != -1:
        await message.channel.send("Hello " + collection[1] + " " + collection[2] + ", here is your zoom link created at " + collection[3] + "!")
        time.sleep(2)
        await message.channel.send(collection[0])
        

client.run(TOKEN)