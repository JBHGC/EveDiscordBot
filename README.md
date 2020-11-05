# EveDiscordBot
This Bot was something coded last month to try out some new ideas. This was uploaded already completed because I forgot about my Github.

Currently "**EveBot**" as I call it, is as the name implies, a **Discord Bot**, using the **Discord.py** API Wrapper. Me not knowing that there are 2 versions; wrote the outdated version and then "rewrote" the code with the *rewrite* version.

As it stands this was more of a project to get to mess with some libraries/make something that I couldn't find myself.

I personally run **EveBot** on an AWS instance, but something that I'm messing with is running this code on a Raspberry Pi locally so I can make "faster" adjustments and also mess around with a Raspberry Pi to use it as a mini 24/7 server.
**COMPLETED!!**

# Commands:
All of the following commands are currently supported by EveBot, and are used as follows:

## The !Quote System:
### !quote:
Typing this command alone will grab a random quote from the **quotes.json** file in the same folder.
If you add a number after, `EX: !quote ##` the command will instead grab the specific quote that goes by that number.

### !addquote:
Typing this command with a quote after, `EX: !addquote I thought it'd work - Phillip` the command will add the quote: `I thought it'd work - Phillip` to the **quotes.json** file as the earliest available integer above 0.

### !delquote:
Typing this commands with a number(of the quote) will delete the quote.

## The !Roll System:
### !roll:
Typing this command with a die(D4, D6, D8, D10, D12, D20, D90, D100) will "roll" the die.
The D100 will be rolled as a D90 and a D10.
