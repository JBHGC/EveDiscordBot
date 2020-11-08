import discord
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions
import random
import json
import requests
import os

client = discord.Client()
bot = commands.Bot(command_prefix="!")

## Dice because I'm lazy, and think this will work better for randomization, also trying out Dictionaries as an option
ALL_DICE = {
"d20":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
"d12":[1,2,3,4,5,6,7,8,9,10,11,12],
"d10":[1,2,3,4,5,6,7,8,9,10],
"d8":[1,2,3,4,5,6,7,8],
"d6":[1,2,3,4,5,6],
"d4":[1,2,3,4],
"d100":[10,20,30,40,50,60,70,80,90,100]
}

##FUNCTIONS FOR RANDOM THINGS:
def overwrite_quote_file( save ):
    """ Insert dict, and it will save over the json file. """
    with open("quotes.json", 'w') as storage:
        json.dump(save, storage)

    storage.close()

def loading_variables():
    all_quote_keys = []                         #Array that holds the "Table of Contents"

    with open("quotes.json") as jsn:            #Just loading the json file into a VAR: quotes
        quotes = json.load(jsn)
    
    if quotes:
       return all_quote_keys, quotes
    else:
        for each in quotes.keys():                  #Throwing the plain numbers into the ARR: all_quote_keys("Table of Contents")
            all_quote_keys.append(each)
    
        jsn.close()

        return all_quote_keys, quotes

def keys_to_int(numbers:list):
    int_list = []
    for each in numbers:
        int_list.append(int(each))
    
    return int_list

def earliest_avail_num(numbers:list):
    """ Grabs the earliest number from 1-(highest int in the list), if that number is 1, then it will return 1, if all the numbers are used, it will return (highest int in the list) + 1 """
    first_num:int

    for each in range(1, (max(numbers) + 2)):
        if each in numbers:
            continue
        else:
            first_num = each
            break

    available_num = f"{first_num}"
    return available_num

###EVENTS:
@client.event
async def on_ready():
    print('{0.user} Reporting In!'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        await message.channel.send("Hi! I have 4 quote commands at the moment:\n`!quote`\n> (available to everyone!) use with a number following this command to pick a specific one, or just leave it empty to get a random quote!\n`!addquote`\n> (admins/mods only) throw a quote after to have it added to the list of quotes!(no need to add a number, that's done automatically!)\n`!delquote`\n> (admins/mods only) throw a quote number to delete that quote.\n`!editquote`\n> (admins/mods only) throw a quote number, and follow with what you want to replace it with.")
        await message.channel.send("Coming Soon: `!roll`\n> (available to everyone!) pick a common die to roll after(ex:D4/D6/D8/D10/D12/D20/D100) and the I will return a random number for that amount. Worth noting: The D100 will roll a D90{00/10/20/30/40/50/60/70/80/90} and a D10{0/1/2/3/4/5/6/7/8/9}. If the D90 rolls a 00, it will overide the D10 that would be rolled with it, and give")
        
###COMMANDS:
@bot.command()
async def quote(ctx, *, message_content=""):
    all_quote_keys, quotes = loading_variables()

    if message_content != "":
        requested_quote = int( message_content.split(" ", 1)[0] )

        if str(requested_quote) not in all_quote_keys:
            await ctx.send("That quote doesn't exist... yet!")
            return

        await ctx.send(f'Quote #{requested_quote}: "{quotes[f"{requested_quote}"]}"')
    else:
        num = random.choice(all_quote_keys)

        await ctx.send(f'Quote #{num}: "{quotes[num]}"')

@bot.command()
@commands.has_any_role('ADMIN', 'MOD')
async def addquote(ctx, *, message_content=""):
    all_quote_keys, quotes = loading_variables()

    if message_content != "":
        new_quote = message_content

        if all_quote_keys:
            used_key_nums = keys_to_int(all_quote_keys)
            new_quote_num = earliest_avail_num(used_key_nums)
        else:
            new_quote_num = "1"

        insert = {str(new_quote_num): str(new_quote)}

        quotes.update( insert )
        overwrite_quote_file( quotes )

        await ctx.send(f'added quote #{new_quote_num}: "{new_quote}"')

    else:
        await ctx.send("Did in fact, add nothing!")

@bot.command()
@commands.has_any_role('ADMIN', 'MOD')
async def delquote(ctx, *, message_content=""):
    all_quote_keys, quotes = loading_variables()

    if message_content != "":
        requested_quote = int( message_content.split(" ", 1)[0] )

        if str(requested_quote) not in all_quote_keys:
            await ctx.send("Uhh... Sure it's gone...")
            return

        del quotes[requested_quote]

        await ctx.send(f'Deleted Quote #{requested_quote}: "{quotes[f"{requested_quote}"]}"')
    else:
        await ctx.send("Successfully deleted nothing!")

@bot.command()
@commands.has_any_role('ADMIN', 'MOD')
async def editquote(ctx, *, message_content=""):
    all_quote_keys, quotes = loading_variables()

    if message_content != "":
        requested_quote = int( message_content.split(" ", 1)[0] )
        replacement = str( message_content.split(" ", 1)[1] )

        if str(requested_quote) not in all_quote_keys:
            await ctx.send("Uhh... edit what exactly?")
            return
        
        del quotes[requested_quote]

        await ctx.send(f'Replaced Quote #{requested_quote}: "{quotes[f"{requested_quote}"]}", with: {replacement}')
    else:
        await ctx.send("EDITED THE HELLA OUTTA THAT EMPTY SPACE!")

@bot.command()
@commands.has_any_role('ADMIN', 'MOD')
async def roll(ctx, *, message_content=""):
    if message_content != "":
        roll = message_content.split(" ")
        if "" in roll:  #This covers for when someone trys/accidentally places a space somewhere and python's '.split' decides to add something in the list.
            roll.remove("")
        die = roll[0].lower()
        
        if die in ALL_DICE:
            output = random.choice(ALL_DICE[f'{die}'])

            if die == 'd100' & output != 100:
                sec10 = int(random.choice(ALL_DICE['d10'])-1)
                output += sec10

            await ctx.send( f'You rolled {output}' )
        else:
            await ctx.send("That's not a die I support.")
    else:
        await ctx.send("Rolled Nothing!")
        
bot.run('INSERT ENVIROMENT VARIABLE FOR OAUTH KEY HERE')
client.run('INSERT ENVIROMENT VARIABLE FOR OAUTH KEY HERE')