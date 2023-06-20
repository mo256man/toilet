import asyncio
from bleak import discover

async def run():
    devices = await discover()
    for d in devices:
        #見つかった機器のmacアドレス、名前、距離を表示
        print(d.address,d.name,d.rssi)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
