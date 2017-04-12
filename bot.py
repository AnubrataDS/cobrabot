import discord
from bs4 import BeautifulSoup
import urllib.request

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!party'):
        msg = 'Hell yeah , {0.author.mention} , we like to party ! '.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!kill'):
        req = urllib.request.Request('https://zkillboard.com/corporation/yourcorpId/kills/')
        with urllib.request.urlopen(req) as response:
            page = response.read()
        soup  = BeautifulSoup(page , "lxml")
        link = soup.find_all("tbody")[2] 
        victims = link.find_all("td" , class_="victim")
        finalBlows = link.find_all("td" , class_="finalBlow")
        kills = link.find_all("tr" , class_="killListRow")
        x = '```Markdown\n#The last 10 kills by COBRA INC. :-```\n\n'.format(message)
        await client.send_message(message.channel, x)
        for num in range(0,10):
            victimParse = victims[num].find_all("a")
            killerParse = finalBlows[num].find_all("a")
            victimName = victimParse[0].get_text();
            victimCorp = victimParse[1].get_text();
            killerName = killerParse[0].get_text();
            killerCorp = killerParse[1].get_text();
            y= str(num+1)+". Link : https://www.zkillboard.com/kill/"+kills[num]['killid']+"\n\n".format(message)
            await client.send_message(message.channel, y)

    if message.content.startswith('!loss'):
        req = urllib.request.Request('https://zkillboard.com/corporation/yourcorpId/losses/')
        with urllib.request.urlopen(req) as response:
            page = response.read()
        soup  = BeautifulSoup(page , "lxml")
        link = soup.find_all("tbody")[2] 
        victims = link.find_all("td" , class_="victim")
        finalBlows = link.find_all("td" , class_="finalBlow")
        kills = link.find_all("tr" , class_="killListRow")
        x = '```Markdown\n#The last 10 losses for COBRA INC. :-```\n\n'.format(message)
        await client.send_message(message.channel, x)
        for num in range(0,10):
            victimParse = victims[num].find_all("a")
            killerParse = finalBlows[num].find_all("a")
            victimName = victimParse[0].get_text();
            victimCorp = victimParse[1].get_text();
            killerName = killerParse[0].get_text();
            killerCorp = killerParse[1].get_text();
            y= str(num+1)+". Link : https://www.zkillboard.com/kill/"+kills[num]['killid']+"\n\n".format(message)
            await client.send_message(message.channel, y)
       
    
    if message.content.startswith('!overview'):
        req = urllib.request.Request('https://zkillboard.com/corporation/yourcorpId/')
        with urllib.request.urlopen(req) as response:
            page = response.read()
        soup  = BeautifulSoup(page , "lxml")
        link = soup.find_all("tbody")[2] 
        victims = link.find_all("td" , class_="victim")
        finalBlows = link.find_all("td" , class_="finalBlow")
        kills = link.find_all("tr" , class_="killListRow")
        x = '```Markdown\n#The last 10 kills/losses for COBRA INC. :-```\n\n'.format(message)
        await client.send_message(message.channel, x)
        for num in range(0,10):
            victimParse = victims[num].find_all("a")
            killerParse = finalBlows[num].find_all("a")
            victimName = victimParse[0].get_text();
            victimCorp = victimParse[1].get_text();
            killerName = killerParse[0].get_text();
            killerCorp = killerParse[1].get_text();
            y= str(num+1)+". Link : https://www.zkillboard.com/kill/"+kills[num]['killid']+"\n\n".format(message)
            await client.send_message(message.channel, y)
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('####your api key here####')
