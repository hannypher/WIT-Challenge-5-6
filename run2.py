from flask import Flask
from url import GetUrls
APP = Flask(__name__)
APP.env = 'development'
APP.testing = True
GetUrls.fetch_urls(APP)

if  __name__ =='__main__':
    APP.run(debug=True)