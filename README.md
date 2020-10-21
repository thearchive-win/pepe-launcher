# PEPE CANNON
This PEPE CANNON deploys RARE PEPE to your discord server via webhooks. 

To run this properly, follow the instructions listed on DockerHub [here](https://hub.docker.com/repository/docker/cryptobiff/pepe-launcher/general)

## Requirements
You must meet the following requirements for this ancient tool to be useful to your memeing efforts: 
* Docker Installed & Running
* DockerHub Account 
* Requires the end user too be based.  Special snowflakes will experience strange errors when running this tool. 

## Pepe Discord Bombardment Cannon
Set up a Webhook URL for the discord channel you want to deploy the pepe bombardment cannon to by following the instructions below: 
* Go to **Server Settings** --> **Integrations** --> **Webhooks** --> **Create New Webhook**
* Select the name for the webhook bot user to display
* Add an avatar if desired to your webhook PEPE User
* Select the destination channel for your pepe cannon
* Copy the "Webhook URL" after you have configured it and paste it below where it says **`PASTE_YOUR_DISCORD_WEBHOOK_URL_HERE`** and the rare pepe will be deployed after you run the docker command shown below.

```
 docker run -e DISCORD_WEBHOOK_URL="PASTE_YOUR_DISCORD_WEBHOOK_URL_HERE" cryptobiff/pepe-launcher

```