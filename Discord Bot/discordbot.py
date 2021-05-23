import discord
import MarioBot

TOKEN = 'ODM1Nzc2ODA4Nzk1MzczNTc5.YIUXzw.NGyFYPBqcUk47HMFMEglDUSpTpk'

client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} is alive".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.channel.name == 'mario-channel':

        response = MarioBot.Mario(message.content)

        if str(type(response)) == str(type(" ")):
            await message.channel.send(response)

        elif str(type(response)) == str(type(["list",])):

            if len(response) != 0:
                await message.channel.send("The available Blood Donors are:")
                msg = ""
                for i in response:
                    if len(i) != 0:
                        msg = msg + i + '\n'
                    else:
                        await message.channel.send(msg)
                        msg = ""
                await message.channel.send("I hope the patient gets recovered soon!\nDo you need any other help?")

            else:
                await message.channel.send("Sorry, No Blood Donors found!")


client.run(TOKEN)