import json
import sys
from random import randint
from time import time

import aiohttp
from MissLyraRobot import aiohttpsession 
from aiohttp import ClientSession

from google_trans_new import google_translator
from Python_ARQ import ARQ
from search_engine_parser import GoogleSearch

from MissLyraRobot import BOT_ID, OWNER_ID, ARQ_API_URL, ARQ_API_KEY
from MissLyraRobot import pbot

ARQ_API = "WZQUBA-PFAZQJ-OMIINH-MIVHYM-ARQ"
ARQ_API_KEY = "WZQUBA-PFAZQJ-OMIINH-MIVHYM-ARQ"
SUDOERS = OWNER_ID
ARQ_API_URL = "https://grambuilders.tech"

# Aiohttp Client
print("[INFO]: INITIALZING AIOHTTP SESSION")
aiohttpsession = ClientSession()
# ARQ Client
print("[INFO]: INITIALIZING ARQ CLIENT")
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

app = pbot
import socket
