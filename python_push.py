import json
import requests
import time
import pprint

# url = "https://script.google.com/macros/s/AKfycbwnzaNnVT1wYH7StAFkqWehJCPceK6DLbOaB9YrvCPWkq7yDwRIv803Fub8ijGeiKAniQ/exec"
url = "https://script.google.com/macros/s/AKfycbzkdJs-8NSnWrGwXAPGrhlPb4y-3b18coYq9j9-DmE24-JqWb2lpYXu5zBCzica--XA/exec"
headers = {"Content-Type": "application/json"}

# JSON形式でデータを用意してdataに格納
data = {
	"device": "from Python",
    }

# json.dumpでデータをJSON形式として扱う
r = requests.post(url, data=json.dumps(data), headers=headers)

print(f"response: {r}")
pprint.pprint(data)
