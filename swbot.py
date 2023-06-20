import asyncio
from bleak import discover
from bleak import BleakClient
import time

#switchbotのMacアドレス.[Discover.py]で調べる必要がある
#address = "E7:F2:08:89:D0:AD"
address = "DB:8A:12:6D:B1:8D"
#switchbotのUUID.SwitchBotのgithubから発掘した
cUUID = "cba20d00-224d-11e6-9fb8-0002a5d5c51b"
rUUID = "cba20002-224d-11e6-9fb8-0002a5d5c51b"
tUUID = "cba20003-224d-11e6-9fb8-0002a5d5c51b"


async def run(address, loop):
    async with BleakClient(address, loop=loop) as client:
        #同期ミスを防止するため一時停止。
        time.sleep(5)

        #以下で接続テスト。[Connected: False]と表示されると接続に失敗している
        x = await client.is_connected()
        print("Connected: {0}".format(x))
        #現在のswitchbotの状態を確認
        #y = await client.read_gatt_char(rUUID)
        #print("status is")
        #print(y)
        print("接続に成功しました。コマンドを入力してください。\nコマンド → press,on,off,exit")
        while True:
            #入力受け取り。コマンド毎に送信する命令を変更する。exitなら終了する
            print("command?")
            command = input()
            if command == "press":
                write_byte = bytearray(b'\x57\x01\x00')
            elif command == "on":
                write_byte = bytearray(b'\x57\x01\x01')
            elif command == "off":
                write_byte = bytearray(b'\x57\x01\x02')
            elif command == "exit":
                #[exit]と入力した場合、1秒後に終了
                await asyncio.sleep(1.0, loop=loop)
                break
            else:
                print("コマンドを入力してください。\nコマンド → press,on,off,exit")
                continue

            #switchbotに命令を送信
            await client.write_gatt_char(tUUID, write_byte)
            #現在のswitchbotの状態を確認
            y = await client.read_gatt_char(rUUID)
            print("status is")
            print(y)
            #同期ミスが起こるので一時停止
            time.sleep(2)


#bleakによるswitchbotとの通信開始
loop = asyncio.get_event_loop()
loop.run_until_complete(run(address, loop))
