import requests
import json
import boto3
import os
import random

# Put the Pepe image URL's you wish to deploy here
SUPER_RARE_PEPE_FILE_URI = [
        "https://i.maga.host/2YHckUB.gif",
        "https://i.maga.host/6qY2f7d.png",
        "https://i.maga.host/js5gDv7.png"
]

def dispense_pepe():
	webhook = os.environ.get("DISCORD_WEBHOOK_URL")
	webhook = webhook.strip()
	if webhook == None:
		raise IOError("DISCORD_WEBHOOK_URL should not be empty, exiting.")
	elif "YOUR_WEBHOOK_URL_GOES_HERE" in webhook:
		print ("No value detected for DISCORD_WEBHOOK_URL, exiting")
		exit(1)
	elif "https://discord.com/api/webhooks" in webhook:
		print ("Using webhook: " + webhook)
	else:
		print ("Invalid Webhook Provided, exiting...")

	thepepe = {
		"content" : "!!~!! A SUPER RARE PEPE HAS APPEARED !!~!! " + random.choice(SUPER_RARE_PEPE_FILE_URI)
	}

	return requests.post(webhook, data=json.dumps(thepepe), headers={"Content-Type": "application/json"})

if __name__ == "__main__":
	dispense_pepe()

