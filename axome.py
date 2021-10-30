import os, random

templates = {
  "auth": ("auth.py", '''from requests import post

cache = {}

# Before pushing to production: enter the URL you specified in the URL of the Signin-Button or link here!

# https://auth.axome.de/signin?url=SOMETHING
# Needed part of this url:         ^^^^^^^^^

URL = ""

if not URL:
  raise Exception("It looks like you forgot to specify the URL used at the button or link for signin in the client file. Visit auth.py and enter the proper URL.")

def login(token):
  if token in cache.keys(): return cache[token]
  x = post("https://auth.axome.repl.co/check",{"usr": token}).text.split(";")
  if x[1] != URL:
    raise Exception("The token of the user comes from another platform. To prevent malicious access to the users account on this platform, probably performed by the other platform, the login has been terminated. This error might happen when you did not correctly configure the URL constant at the top of the client file. To fix this issue, enter this URL in the constant: "+x[1])
    return ""
  if len(x[0]) > 20:
    raise Exception("The AXOME server rejected the given token or did not find it.")
  cache[token] = x[0]
  return x[0]

def logout(token):
  x = cache[token]
  del cache[token]
  return x
  
def getUser(token):
  if token in cache.keys(): return cache[token]
  x = post("https://auth.axome.repl.co/check",{"usr": token}).text.split(";")[0]
  if len(x) > 20:
    raise Exception("The AXOME server rejected the given token or did not find it.")
  cache[token] = x
  return x'''),
  "antixsrf": ("antixsrf.py", '''import random
import string

data = {}
chars = string.ascii_letters + string.digits

def generateToken():
  res = ""
  for i in range(16):
    res += random.choice(chars)
  return res

def createEndpoint(user, action):
  if not action in data.keys():
    data[action] = {}
  data[action][user] = generateToken()

  return data[action][user]

def validateEndpoint(token, user, action):
  if not action in data.keys():
    return False
  if token != data[action][user]:
    del data[action][user]
    return False
  del data[action][user]
  return True'''),
  "sitemap": ("sitemap.py", '''def generateSiteMap(articles, users, extra=[]):
  global res
  res = ""
  def addUrl(url):
    global res
    res += "<url><loc>"+str(url)+"</loc></url>"

  start = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{{data}}</urlset>'

  for i in articles:
    addUrl("https://peritum.axome.de/article/"+str(i["_id"]))

  for i in users:
    addUrl("https://peritum.axome.de/profile/"+str(i["name"]))

  for i in extra:
    addUrl("https://peritum.axome.de/"+str(i))

  return start.replace("{{data}}", res)''')
}

def _add(f, c, m="w"):
    with open(f, m) as f:
        f.write(c)
        f.close()

def add(n, d="."):
  file = templates[n]
  print("Please do not violate the AXOME Terms of service: https://policies.axome.repl.co/terms.html")
  print("Adding "+file[0]+"...")
  os.chdir(d if d != "." else ".")
  filename = file[0]
  while os.path.isfile(filename):
    filename = str(random.randint(1,999))+"-"+file[0]
  _add(filename, file[1])

def build(d):
    print("No build for this template available.")

def create(d):
    print("This template is for adding axomeapis to your project. Please use the add command instead.")

def run(d):
    print("No run for this template available.")