#!/usr/bin/python3

# n_arclogger
# by n_arc


# Import Required Libraries
from time import strftime, localtime
import asyncio
import discord
import re
import datetime

# Declare Global Client
c = discord.Client()

# Server Owner User Token
token = "randomlettersandnumbers.willbe.mixedwithperiods"

# Loading Credits
@c.event
async def on_ready():
    print("\nLoading n_arclogger...\n")

# Asynchroniously Stream Chats
@c.event
async def on_message(message):
    # convert Message to Embed
    print("[", datetime.datetime.now().strftime("%y-%m-%d-%H-%M"),  "]", message.embeds[0].description, ": ", message.embeds[0].title)
c.run(token, bot=False)