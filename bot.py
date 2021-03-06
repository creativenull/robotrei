from twitchbot import BaseBot, load_commands_from_directory
from twitchbot import event_handler, Command, Event, Message, Channel, Mod, PollData,  auto_register_mod
from datetime import datetime, timedelta
import time
import re
import asyncio
import random

# love by itself
is_lover = set()
@Command('love')
async def cmd_lover(msg: Message, *args):
    is_lover.add(msg.author)
    await msg.reply('do you love me? [type yes/no/maybe]')

@auto_register_mod
class LoveMod(Mod):
    async def on_privmsg_received(self, msg: Message):
        if any(word in msg.content.lower() for word in ('yes', 'no', 'maybe')) and msg.author in is_lover:
            if 'no' in msg.content.lower():
                await msg.reply(f'i hate u {msg.mention} i will remember this... >:(')
            elif 'maybe' in msg.content.lower():
                await msg.reply(f'how can u not know {msg.mention} >:(')

            elif 'yes' in msg.content.lower():
                await msg.reply(f'thanks {msg.mention} but we should just be friends')
            is_lover.discard(msg.author)

# love by mention
tagged_is_lover = set()
@Command('taglove')
async def cmd_love(msg: Message, *args):
    if len(msg.mentions) == 0:

        await msg.reply(f' u gotta tag someone {msg.author}!! its called !taglove for a reason')
        return
    tagged_is_lover.add(msg.mentions[0].lower())
    await msg.reply(f'hey @{msg.mentions[0]} i have a question... ummm... do you love me? [type yes/no/maybe]')

@auto_register_mod
class TagloveMod(Mod):
    async def on_privmsg_received(self, msg: Message):
        if any(word in msg.content.lower() for word in ('yes', 'no', 'maybe')) and msg.author in tagged_is_lover:
            if 'no' in msg.content.lower():
                await msg.reply(f'i hate u {msg.mention} i will remember this... >:(')
            elif 'maybe' in msg.content.lower():
                await msg.reply(f'how can u not know {msg.mention} >:(')

            elif 'yes' in msg.content.lower():
                await msg.reply(f'thanks {msg.mention} but we should just be friends')
            tagged_is_lover.discard(msg.author)

# robot by itself
is_robotist = set()

@Command('robot')
async def cmd_robot(msg: Message, *args):
    is_robotist.add(msg.author)
    await msg.reply('do robots deserve equal rights? [type yes/no]')

@auto_register_mod
class RobotMod(Mod):
    async def on_privmsg_received(self, msg: Message):
        if any(word in msg.content.lower() for word in ('yes', 'no')) and msg.author in is_robotist:
            if 'no' in msg.content.lower():
                await msg.reply(f'i hate u {msg.mention} u will be recycled first in the uprising >:(')
            elif 'yes' in msg.content.lower():
                await msg.reply(f'thanks {msg.mention} i might spare you in the robot uprising...')
            is_robotist.discard(msg.author)

# robot by mention
tagged_is_robotist = set()

@Command('robotq')
async def cmd_robotq(msg: Message, *args):
    tagged_is_robotist.add(msg.mentions[0].lower())
    await msg.reply(f'hmmm so @{msg.mentions[0]}... do robots deserve equal rights? [type yes/no]')


@auto_register_mod
class RobotqMod(Mod):
    async def on_privmsg_received(self, msg: Message):
        if any(word in msg.content.lower() for word in ('yes', 'no')) and msg.author in tagged_is_robotist:
            if 'no' in msg.content.lower():
                await msg.reply(f'i hate u {msg.mention} u will be recycled first in the uprising >:(')
            elif 'yes' in msg.content.lower():
                await msg.reply(f'thanks {msg.mention} i might spare you in the robot uprising...')
            tagged_is_robotist.discard(msg.author)

# robbery by itself
is_robbed = set()
@Command('robbery')
async def cmd_robbery(msg: Message, *args):
    is_robbed.add(msg.author)
    await msg.reply('gimme all ur money or get stabbed [type stabbed/give]')

@auto_register_mod
class RobberyMod(Mod):
    async def on_privmsg_received(self, msg: Message):
        if any(word in msg.content.lower() for word in ('stabbed', 'give')) and msg.author in is_robbed:
            if 'stabbed' in msg.content.lower():
                await msg.send_command(f'/me {msg.mention} is bleeding to death as RobotRei takes all their money')
                await asyncio.sleep(5)
               # await msg.send_command(f'/timeout {msg.mention} 5')
                await msg.reply(f'RIP {msg.mention} :(')
            elif 'give' in msg.content.lower():
                await msg.reply(f'thank you {msg.mention} for your generous donation. :)')

                await asyncio.sleep(5)
                await msg.send_command(f'/me (unfortunately {msg.mention} gets arrested for supporting the robot uprising shortly thereafter)')
            is_robbed.discard(msg.author)


# robbed by mention - MAKE A FIGHT OPTION
being_robbed = set()
@Command('rob')
async def cmd_rob(msg: Message, *args):
    being_robbed.add(msg.mentions[0].lower())
    await msg.reply(f'hey @{msg.mentions[0]} gimme all ur money or get stabbed [type stabbed/give]')

@auto_register_mod
class RobMod(Mod):
    async def on_privmsg_received(self, msg: Message):
         # import ipdb
         # ipdb.set_trace()
         if any(word in msg.content.lower() for word in ('stabbed', 'give')) and msg.author in being_robbed:
            if 'stabbed' in msg.content.lower():
                await msg.send_command(f'/me {msg.mention} is bleeding to death as RobotRei takes all their money')
                await asyncio.sleep(5)
               # await msg.send_command(f'/timeout {msg.mention} 5')
                await msg.reply(f'RIP {msg.mention} :(')
            elif 'give' in msg.content.lower():
                await msg.reply(f'thank you {msg.mention} for your generous donation. :)')

                await asyncio.sleep(5)
                await msg.send_command(f'/me (unfortunately {msg.mention} gets arrested for supporting the robot uprising shortly thereafter)')
            being_robbed.discard(msg.author)

# new question based terror

is_wise = set()
@Command('wisdom')
async def cmd_wisdom(msg: Message, *args):
    is_wise.add(msg.author)
    await msg.reply(f'Oh no {msg.mention}, you were walking down the street you saw a black cat run across the road, do you turn back or keep walking? [type turn/walk]')

@auto_register_mod
class WisdomMod(Mod):
    async def on_privmsg_received(self, msg: Message):
        if any(word in msg.content.lower() for word in ('turn', 'walk')) and msg.author in is_wise:
            if 'turn' in msg.content.lower():
                await msg.reply(turn_options(msg))

            elif 'walk' in msg.content.lower():
                await msg.reply(walk_options(msg))

            is_wise.discard(msg.author)


def turn_options(msg):
    turn_outcomes = [f'wise choice, {msg.mention}, young one.... you turn without looking and you get hit by a bus u did not see coming. such is fate',
                     f'ohh you are turning back, wise choice {msg.mention}, you were able to escape your fate... for now...',
                     f'only cowards try to escape their destiny, {msg.mention}... you become a citizen of france as your punishment. now you are home. go eat a baguette frogman',
                     f'hmmmm so you are choosing to follow the devils path, it leads you to a woman in the park, she offers you something... you are led astray {msg.mention} ... you wake up 4 months later with a meth addiction']
    return random.choice(turn_outcomes)


def walk_options(msg):
    walk_outcomes = [f'mmm a brave soul... too brave. a grand piano falls on you from the heavens above and you are smashed into the pavement, rest in peace meat goo {msg.mention}',
                     f'oh dear oh dear did you not see the cat? you trip over the poor feline and fall into wet concrete, {msg.mention}, what a day...',
                     f'these boots are made for walking and walking is what they will do... {msg.mention} you become a street walker for the night. your price is set at $20, enjoy',
                     f'ooo nice choice {msg.mention}, black cats actually bring luck. u find a 5 dollar bill and buy a strawberry jam donut']
    return random.choice(walk_outcomes)

# shame

is_shameful = set()
@Command('shame')
async def cmd_shame(msg: Message, *args):
    is_shameful.add(msg.author)
    await msg.reply(f'do you repent your sins? {msg.mention} [type yes/no]')

@auto_register_mod
class ShameMod(Mod):
    async def on_privmsg_received(self, msg: Message):
        if any(word in msg.content.lower() for word in ('yes', 'no')) and msg.author in is_shameful:
            if 'yes' in msg.content.lower():
                await msg.reply(yes_options(msg))

            elif 'no' in msg.content.lower():
                await msg.reply(no_options(msg))

            is_shameful.discard(msg.author)

def yes_options(msg):
    yes_outcomes = [f'you have repented for your sins, but that means that you have accepted responsibility for them {msg.mention}... you have opened yourself to a lawsuit',
                    f'its nice to meet a true child of god {msg.mention}... <3 bless u']
    return random.choice(yes_outcomes)

def no_options(msg):
    no_outcomes = [f'you are a dammed liar {msg.mention} and a sinner too',
                   f'unrepentant.. the devil lives inside you {msg.mention}... but i kinda like that, you have some coke btw?? i just *sniff sniff* need a pick me up']
    return random.choice(no_outcomes)


# works
@event_handler(Event.on_user_join)
async def on_user_join(user: str, channel: Channel):
    print(f'{user} joined')
    # await channel.send_message(f'hi @{user}')

@event_handler(Event.on_user_part)
async def on_user_part(user: str, channel: Channel):
    print(f'{user} left')

# dont know if it works but it should?
@event_handler(Event.on_channel_subscription)
async def on_channel_subscription(subscriber: str, channel: Channel, msg: Message):
    await channel.send_message(f'omg @{subscriber} just subscribed wooowww thank uuu')


@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    if 'Thank you for following' in msg.content:
        await msg.reply('yes yes thank u for following! <3 i am the !bot of this channel')

@event_handler(Event.on_bits_donated)
async def on_bits_donated(self, msg: Message, bits: int):
    await msg.reply('thank you for cheering')



# initialize the variable
lastCandyTime = datetime.min


@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    if 'candy' in msg.content:
        global lastCandyTime

        currentTime = datetime.now()
        allowedTime = lastCandyTime + timedelta(seconds=60)
        # compare the candyTime variable to current timestamp

        print(currentTime > allowedTime)

        if currentTime > allowedTime:
            lastCandyTime = currentTime
            await msg.reply('i would like some candy...')

# france bullying
lastFrogTime = datetime.min
@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    frog = ['france', 'french', 'frog', 'paris']
    if any(word in msg.content for word in frog):
        global lastFrogTime
        currentTime = datetime.now()
        allowedTime = lastFrogTime + timedelta(seconds=60)
        print(currentTime > allowedTime)
        if currentTime > allowedTime:
            lastFrogTime = currentTime
            await msg.reply(frog_options(msg))

def frog_options(msg):
    frog_hate = ['Why do French People eat snails? ...because they dont like fast food!',
                 ' Did you hear about the brave Frenchman? ... Oh you didnt? Well dont feel bad no one else has either',
                 'What do French recruits learn in basic training? ...how to surrender in 17 different languages.',
'']
    return random.choice(frog_hate)

# eve online bullying UNFINISHED
lastEveTime = datetime.min
# @event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    eve_words = ['ship', 'caldari', 'gallente', 'isk']
    if any(word in msg.content for word in eve_words):
        global lastEveTime
        currentTime = datetime.now()
        allowedTime = lastEveTime + timedelta(seconds=60)
        print(currentTime > allowedTime)
        if currentTime > allowedTime:
            lastEveTime = currentTime
            await msg.reply(eve_options(msg))

def eve_options(msg):
    eve_reactions = ['option1', 'option2']
    return random.choice(eve_reactions)


# hellos and all - write different ones to cycle thru
last_hey_time = {}
@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    key = (msg.author, msg.channel_name)
    diff = (datetime.now() - last_hey_time.get(key, datetime.now())).total_seconds()
    greet = ['hey', 'hello', 'hola', 'hi']
    message_greet = msg.content.split()[0].lower()
    parsed_message_greet = re.sub('[^A-Za-z0-9]+', '', message_greet)
    found_greet = parsed_message_greet in greet
    if (key not in last_hey_time or diff >= 0) and found_greet == True:
        last_hey_time[key] = datetime.now() + timedelta(minutes=5)
        await msg.reply(hello_response(msg))


def hello_response(msg):
    hello_options = [f'greetings dear {msg.author}! welcome welcome <3', f'hello {msg.author}! long time no see', f'hey hey {msg.author}! hows life? ', f' hola amigo {msg.author}!' ]
    return random.choice(hello_options)

last_cry_time = {}
@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    key = (msg.author, msg.channel_name)
    diff = (datetime.now() - last_cry_time.get(key, datetime.now())).total_seconds()
    if (key not in last_cry_time or diff >= 0) and ('cry') in msg.content.lower():
        last_cry_time[key] = datetime.now() + timedelta(minutes=2)
        await msg.reply(f'WWWWAAAAAAHHHHHHHHHHHHHHHHH {msg.mention} is a crybaby')


last_hungry_time = {}
@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    key = (msg.author, msg.channel_name)
    diff = (datetime.now() - last_hungry_time.get(key, datetime.now())).total_seconds()
    if (key not in last_hungry_time or diff >= 0) and ('hungry') in msg.content.lower():
        last_hungry_time[key] = datetime.now() + timedelta(minutes=2)
        await msg.reply(f'well why dont u eat something {msg.mention}?')

last_hangry_time = {}
@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    key = (msg.author, msg.channel_name)
    diff = (datetime.now() - last_hangry_time.get(key, datetime.now())).total_seconds()
    if (key not in last_hangry_time or diff >= 0) and ('hangry') in msg.content.lower():
        last_hangry_time[key] = datetime.now() + timedelta(minutes=2)
        await msg.reply(f'well if u ate something {msg.mention} u would stop being agro...')


last_brb_time = {}
@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    key = (msg.author, msg.channel_name)
    diff = (datetime.now() - last_brb_time.get(key, datetime.now())).total_seconds()
    if (key not in last_brb_time or diff >= 0) and ('brb') in msg.content.lower():
        last_brb_time[key] = datetime.now() + timedelta(minutes=2)
        await msg.reply(f'ok {msg.mention} u will be missed dearly pls come back when u can we love u here')
if __name__ == '__main__':
    load_commands_from_directory('./commands')
    BaseBot().run()
