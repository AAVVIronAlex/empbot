from emp import bot
import random
import string
import asyncio

new = 'random text'

# start session

async def main():
    global new
    messages = await client.get_messages('channel sample')
    new = messages[0].text

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print(new)  # message text