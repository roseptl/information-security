
import json
from urllib.request import Request, urlopen
from urllib.error import URLError

API_URL = "http://127.0.0.1:8000/logs"


def save_to_file(text):
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(text + "\n")


def send_log():
    try:
        with open("log.txt", "r", encoding="utf-8") as file:
            data = file.read()

        request = Request(
            API_URL,
            data=json.dumps({"log": data}).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        with urlopen(request, timeout=5) as response:
            print("Server response:", response.read().decode("utf-8"))

    except (OSError, URLError) as error:
        print("Could not send log:", error)


print("Enter test text. Type STOP to finish.")

while True:
    text = input("> ")

    if text == "STOP":
        break

    save_to_file(text)

send_log()
