import discord 
from discord.ext import commands
import os
import asyncio

import requests
import random
os.system(f'cls & mode 80,15 & title AbuserClient Login')

token = input(f'Token: ')



os.system('cls')



intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", case_insensitive=False, intents=intents)
client.remove_command("help")

class AbuserNuker:
    def __init__(self):
        self.member_count = 0
        
        
    async def Scrape(self):
        guild = input(f'Guild Id: ')
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        members = guildOBJ.members
        try:
            os.remove("data/token.txt")
            os.remove("data/guild.txt")
            os.remove("Scrape/members.txt")
           
        
        except:
           pass
        
        with open("data/token.txt", 'a') as t:
            t.write(token)
            
            t.close()
            
        with open("data/guild.txt", 'a') as g:
            g.write(guild)
            
            g.close()
            
        with open("Scrape/members.txt", 'a') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                self.member_count += 1
            
            print(self.member_count)
            m.close()
            
    async def Menu(self):
        print("DO NOT CLOSE THIS WINDOW")
        choice = input("Scrape[Y/n] : ")
        if choice == "Y" or choice == "y":
            await self.Scrape()
            await asyncio.sleep(2)
            await self.Menu()
            
        elif choice == "N" or choice == "n":
            os._exit(0)
    
    @client.event
    async def on_ready():
        await AbuserNuker().Menu()
    
    def startup(self):
        try:
            client.run(token)
            
        except:
            print(f'Invalid Token')
            input()
            os._exit(0)
            
if __name__ == "__main__":
    AbuserNuker().startup()
        