#########################################################
##coded by ankitmaheswari130@gmail.com                  #
##Ankit Maheshwari https://www.freelancer.in/u/mankit121#
#########################################################
import requests
from bs4 import BeautifulSoup as soup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json
print('sending post request')

with open("xing.json",'r') as f:
  da=json.load(f)


api_key='ga04gfgehkdLepr9YUAARZ4N4EYY0ufPHeKI8B5SaewsYN32dOe'

url='https://viuwi.com/v1/import/'+api_key


r=requests.post(url,json=da,verify=False)
print('post request sent with status code '+str(r.status_code))
