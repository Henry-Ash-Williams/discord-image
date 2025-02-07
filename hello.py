import json
import os
import urllib
import urllib.parse
import uuid

import requests
from tqdm import tqdm

PATH = "/Users/henrywilliams/Documents/discord-data/messages"

if __name__ == "__main__":
    dirs = os.listdir(PATH)

    paths = []

    for dir in dirs:
        if dir == "index.json":
            continue

        file_path = os.path.join(PATH, dir, "messages.json")
        paths.append(file_path)

    data = []
    for fp in paths:
        data.append(json.load(open(fp, "r")))
    attachments = []
    for thread in data:
        for message in thread:
            attachments.append(message["Attachments"])

    attachments = [attachment for attachment in attachments if attachment != ""]

    for i, attachment in enumerate(tqdm(attachments)):
        url = urllib.parse.urlparse(attachment)
        filename = str(uuid.uuid4()) + f".{url.path.split('/')[-1].split('.')[-1]}"
        res = requests.get(attachment)
        if res.status_code != 200:
            continue

        with open(os.path.join("./images/", filename), "wb") as fp:
            fp.write(res.content)
