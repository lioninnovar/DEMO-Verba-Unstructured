import os
import json
import requests

from wasabi import msg
from dotenv import load_dotenv

load_dotenv()

msg.divider("Starting PDF Conversion to Text")

file_names = ["./data/combining_taste.pdf", "./data/taste_and_smell.pdf"]

url = "https://api.unstructured.io/general/v0/general"

api_key = os.environ.get("UNSTRUCTURED_API_KEY", "")

if api_key != "":
    msg.good("Unstructured API Key available")
    headers = {
        "accept": "application/json",
        "unstructured-api-key": api_key,
    }

    data = {
        "strategy": "auto",
    }

    for file_path in file_names:
        msg.info(f"Converting {file_path}")
        file_data = {"files": open(file_path, "rb")}

        response = requests.post(url, headers=headers, data=data, files=file_data)

        file_data["files"].close()

        json_response = response.json()

        full_content = ""

        for chunk in json_response:
            if "text" in chunk:
                text = chunk["text"]
                full_content += text + " "

        root, _ = os.path.splitext(file_path)

        new_file_path = root + ".txt"

        with open(f"{new_file_path}", "w") as writer:
            writer.writelines(full_content)

        msg.good(f"Successfully saved to {new_file_path}")

else:
    msg.fail("No Unstructured API Key available. Please add your key to your .env file")
