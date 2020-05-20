import mwclient
import requests
from credentials import usr, pas

site = mwclient.Site("myfirsttestwiki.fandom.com", path="/")

if !(usr and (not usr.isspace())) and !(pas and (not pas.isspace())):
site.force_login = False

page = site.pages["New page name"]
page.edit("Hello World! (Relma wuz here)")
