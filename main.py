import json
import requests
import configparser
import sys, os
import datetime as dt
from datetime import timedelta

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

configfilename = os.path.abspath(os.path.dirname(sys.argv[0])) + '\properties.ini'
config = configparser.ConfigParser()

config.read(configfilename)
hostname = config['DEFAULT']['hostname']
login = config['DEFAULT']['login']
password = config['DEFAULT']['password']
str_date = config['DEFAULT']['date']

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\' + config['DEFAULT']['folder']
    if not os.path.exists(path):
        os.mkdir(path)

    auth_data = "{\"action\":\"login\",\"data\":{\"login\":\"" + login + "\",\"password\":\"" + password + "\"}}"

    req = requests.Session()
    responce = req.post(hostname + '/action/login', data=auth_data)
    c = req.cookies
    h = req.headers
