# EveDiscordBot
This Bot was something coded last month to try out some new ideas. Uploaded completed because I forgot about Github.

Currently "**EveBot**" as I call it, is as the name implies, a **Discord Bot**, using the **Discord.py** API Wrapper. Me not knowing that there are 2 versions wrote the outdated version and then "rewrote" the code with the *rewrite* version.

## Commands:
All of the following commands are currently supported by EveBot, and are used as follows:

# The !Quote System:
### !quote:
Typing this command alone will grab a random quote from the **quotes.json** file in the same folder.
If you add a number after, `EX: !quote ##` the command will instead grab the specific quote that goes by that number.

### !addquote:
Typing this command with a quote after, `EX: !addquote I thought it'd work - Phillip` the command will add the quote: `I thought it'd work - Phillip` to the **quotes.json** file as the earliest available integer above 0.

### !delquote:
Typing this commands with a number(of the quote) will delete the quote.

# The !Roll system:
###!roll:
Typing this command with a die(D4, D6, D8, D10, D12, D20, D90, D100) will "roll" the die.
The D100 will be rolled as a D90 and a D10.

README STILL UNDER CONSTRUCTION!!!
