import hikari
import os
from dotenv import load_dotenv

load_dotenv()
#print(os.environ.get('DC-TOKEN'))

bot = hikari.GatewayBot(token=os.environ.get('DC-TOKEN'))
bot.run()