import requests

VERSION_NUMBER_URL = "https://raw.githubusercontent.com/AXOMEstudios/nq-cli/master/data/nq-version"
SOFTWARE           = "nq-cli"
HOW_TO             = "clone the repository at https://github.com/AXOMEstudios/nq-cli into nq-cli"
CURRENT            = "1.01"

def checkForUpdate():
  version = requests.get(VERSION_NUMBER_URL).text
  if version != CURRENT:
    return (True, CURRENT, version)
  else:
    return (False, CURRENT, version)

def generateMessage(current, new):
  return f'''Warning!
  You are using {SOFTWARE} version {current}, however a new version of {SOFTWARE} is now available: {new}.
  We recommend updating {SOFTWARE} for your convinience. To do this, {HOW_TO}.'''