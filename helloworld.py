import mwclient
import requests
from requests_oauthlib import OAuth2

site = mwclient.Site("myfirsttestwiki.fandom.com", path="/")

# This is so We dont have to put ayones password in a plaintext file.
# WORKAROUND
site.force_login = False

page = site.pages["New page name"]
page.edit("Hello World! (Relma wuz here)")
