import warnings
import mwclient
import requests
from credentials import usr, pas

site = mwclient.Site("myfirsttestwiki.fandom.com", path="/")

if not (usr and (not usr.isspace())) or not (pas and (not pas.isspace())):
    warnings.warn("Put your fandom username and password in credentials.py (don't worry, its in the gitignore).")
    exit()
try:
    site.login(usr, pas)
except:
    #Edit anonymously instead
    site.force_login = False


page = site.pages["New page name"]
page.edit("Hello World! (...)")