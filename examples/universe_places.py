"""
This example shows how to get all places in a universe.
Does not require a cookie.
"""

import asyncio
from roblox import Client
client = Client()


async def main():
    places = await client.get_universe_places(5349377275)
    async for placeListing in places:
        print(placeListing.id)


asyncio.get_event_loop().run_until_complete(main())
