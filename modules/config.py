import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "21591773"))
API_HASH = getenv("API_HASH", "7e59ca50130d93574ec3145e692430b8")
BOT_TOKEN = getenv("BOT_TOKEN", "7893194449:AAEbKOe2ay8FtzIkF7oapXtwV1ybj6Wrz2k")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AgFJdt0ApXYqZ8RDVv-yHrPKUCFzLUsaMO5H-UOp6iTRvs8djjmYao-aXBzA9ZF6WcUIXET-4WxVfK1hH-lTIbnH7VPb2_0a4tQNLs44bYbCX3-c89sFcut5e8859XEVN0OyI5h-FjNBMTtbAnxP7cb6JUjItjonxWtb6bdmGrAxpf16M68uwKoTKvrOjFPPPv_yoDgyahk13Vskq6Bd5D0Bnfl9sHBxmABVB3fzC8MAeHTjsrXRrbq14qr1bnQstUJuv7QKME-8Zs9iTkZWsN9aKawWmff239JS3Nb876pxZK4_xIf3bfNBrTbQiOzo5SzzdZkSHmMth5txV7iwkTm9AYvR_gAAAAG8GOfFAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7450716101").split()))
