import mwclient
from BotPassword import password

site = mwclient.Site("myfirsttestwiki.fandom.com", path="/")

site.login("Gryhyphen@Botdude", password)

page = site.pages["New page name"]
page.edit("Hello World!")
