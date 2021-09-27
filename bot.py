
from typing import Counter, Pattern
from telethon import TelegramClient, events
import telethon.sync
import logging
import collections

from telethon.events.newmessage import NewMessage

API_ID = 6057309
API_HASH = "e309ebccc3c9c88f7cce34adec0fdbcc"

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


client = TelegramClient('anon', API_ID, API_HASH)


@client.on(events.NewMessage)
async def answer_to_message(event):
    if '@BlushingGorilla' in event.text:
        if "Oski" in event.text:
            await event.reply("DAILY REMINDER ZE NIEJAKI WOJ MA PONAD ĆWIERĆ TYSIĄCA PAR NA TINDERZE (TO TAK JAKBY CAŁE CG GO CHCIALO!!!)")
        elif "oski" in event.text:
            await event.reply("DAILY REMINDER ZE NIEJAKI WOJ MA PONAD ĆWIERĆ TYSIĄCA PAR NA TINDERZE (TO TAK JAKBY CAŁE CG GO CHCIALO!!!)")
    if 'kolya' in event.text:
        if "Oski" in event.text:
            await event.reply("DAILY REMINDER ZE NIEJAKI WOJ MA PONAD ĆWIERĆ TYSIĄCA PAR NA TINDERZE (TO TAK JAKBY CAŁE CG GO CHCIALO!!!)")
        elif "oski" in event.text:
            await event.reply("DAILY REMINDER ZE NIEJAKI WOJ MA PONAD ĆWIERĆ TYSIĄCA PAR NA TINDERZE (TO TAK JAKBY CAŁE CG GO CHCIALO!!!)")
    if 'Kolya' in event.text:
        if "Oski" in event.text:
            await event.reply("DAILY REMINDER ZE NIEJAKI WOJ MA PONAD ĆWIERĆ TYSIĄCA PAR NA TINDERZE (TO TAK JAKBY CAŁE CG GO CHCIALO!!!)")
        elif "oski" in event.text:
            await event.reply("DAILY REMINDER ZE NIEJAKI WOJ MA PONAD ĆWIERĆ TYSIĄCA PAR NA TINDERZE (TO TAK JAKBY CAŁE CG GO CHCIALO!!!)")
    if 'Zeczero' in event.text:
        if "Oski" in event.text:
            await event.reply("DAILY REMINDER ZE NIEJAKI WOJ MA PONAD ĆWIERĆ TYSIĄCA PAR NA TINDERZE (TO TAK JAKBY CAŁE CG GO CHCIALO!!!)")
        elif "oski" in event.text:
            await event.reply("DAILY REMINDER ZE NIEJAKI WOJ MA PONAD ĆWIERĆ TYSIĄCA PAR NA TINDERZE (TO TAK JAKBY CAŁE CG GO CHCIALO!!!)")
    if 'zeczero' in event.text:
        if "Oski" in event.text:
            await event.reply("DAILY REMINDER ZE NIEJAKI WOJ MA PONAD ĆWIERĆ TYSIĄCA PAR NA TINDERZE (TO TAK JAKBY CAŁE CG GO CHCIALO!!!)")
        elif "oski" in event.text:
            await event.reply("DAILY REMINDER ZE NIEJAKI WOJ MA PONAD ĆWIERĆ TYSIĄCA PAR NA TINDERZE (TO TAK JAKBY CAŁE CG GO CHCIALO!!!)")


@client.on(events.NewMessage)
async def calculate_ranking(event):
    top = Counter()
    phone = Counter()
    if "!ranking" in event.raw_text:
        chat_id = event.chat_id
        async for message in client.iter_messages(chat_id, reverse=True):
           # author = message.sender.username
            if message.sender.username == None:
                phone[message.sender.phone] += 1
            else:
                top[message.sender.username] += 1
        for value, count in top.most_common():
            await client.send_message(
                chat_id,
                f"{value}:{count}")


client.start()
client.run_until_disconnected()
