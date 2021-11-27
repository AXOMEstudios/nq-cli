import requests

VERSION_NUMBER_URL = "https://raw.githubusercontent.com/AXOMEstudios/nq-cli/master/data/qn-version"
SOFTWARE           = "nq-cli"
HOW_TO             = "clone the repository at https://github.com/AXOMEstudios/nq-cli into nq-cli"

def checkForUpdate():
  version = requests.get(VERSION_NUMBER_URL).text
  with open("version") as f:
    current = f.read()
    f.close()
  if version != current:
    return (True, current, version)
  else:
    return (False, current, version)

def generateMessage(current, new):
  return f'''Warning!
  You are using {SOFTWARE} version {current}, however a new version of {SOFTWARE} is now available: {new}.
  We recommend updating {SOFTWARE} for your convinience. To do this, {HOW_TO}.'''