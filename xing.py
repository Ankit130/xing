#########################################################
##coded by ankitmaheswari130@gmail.com                  #
##Ankit Maheshwari https://www.freelancer.in/u/mankit121#
#########################################################
import requests
from bs4 import BeautifulSoup as soup
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
headers={
'Host': 'login.xing.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
'Accept': 'application/json',
'Accept-Language': 'en-GB,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://login.xing.com/?dest_url=https%3A%2F%2Fwww.xing.com%2Fhome',
'content-type': 'application/json; charset=utf-8',
'x-csrf-token': 'iwu7MDnYxVdARwjLC1mShzpSQt-acfQF',
'Origin': 'https://login.xing.com',
'Content-Length': '104',
'Connection': 'keep-alive',
'Cookie': 'visitor_id=c171c004-2757-4f34-8e66-b19ac99a394e; AMCV_0894FF2554F733210A4C98C6%40AdobeOrg=1585540135%7CMCIDTS%7C18472%7CMCMID%7C34431240474313072722481623697729984457%7CMCAAMLH-1596560138%7C12%7CMCAAMB-1596560138%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1595962538s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18460%7CvVersion%7C4.4.0; s_ecid=MCMID%7C34431240474313072722481623697729984457; userConsent=%7B%22version%22%3A%221%22%2C%22marketing%22%3Atrue%7D; browser_id=0275aa7c-3634-4bdb-abdb-c0aedf988a61; login_session=BAhJIjkyMzk2NTc0OC1FNnBMN2Y0N1AxWmhRaDhCLUc2dG5UWTV3WnZheXhaeW02MUJZTENleC1BBjoGRVQ%3D--fd861b7b1bd822dcc8e6f32ef678e2c68dcc26cc; ab.storage.userId.bd5d74db-085a-4722-a85a-7080dbaa6faa=%7B%22g%22%3A%2223965748%22%2C%22c%22%3A1594308929317%2C%22l%22%3A1594308929317%7D; ab.storage.sessionId.bd5d74db-085a-4722-a85a-7080dbaa6faa=%7B%22g%22%3A%22d84036de-51a0-f4cc-08ec-4c761d503fee%22%2C%22e%22%3A1594398431699%2C%22c%22%3A1594396441450%2C%22l%22%3A1594396631699%7D; ab.storage.deviceId.bd5d74db-085a-4722-a85a-7080dbaa6faa=%7B%22g%22%3A%22b6c4d960-38d0-bd3b-3ed4-01f866deeca3%22%2C%22c%22%3A1594308929326%2C%22l%22%3A1594308929326%7D; cto_bundle=IyHupV9JVXJYRzdFQ2pHNHRTcDZhamd1eVNITnVrSUF0U3RzZnNGdGV5R05KREs0b0MzSSUyRkJyOSUyRm0yWUo4bnhzUyUyRmVlTTNyUjZiVEFuU08xRExZZGZKeXNIcUFlQzkwdnAwVDRrNkFGZWdGeE5BamhmQ3UlMkIweDNZNlozcVZsSE84blVQaVpoaGFjMm9TamprZEtIM01XRDZwdyUzRCUzRA; language=en; c_=ab1e0b621f61f957ef8643e955508aec; xing_csrf_token=iwu7MDnYxVdARwjLC1mShzpSQt-acfQF; xing_csrf_checksum=lclwh_6J5glxEGtbrB5g-FB51wRbftfrvqCwJHSCV4A; prevPage=wbm%2FWelcome%2Flogin; AMCVS_0894FF2554F733210A4C98C6%40AdobeOrg=1; s_cc=true'}

headers1={
'Host': 'www.xing.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
'Accept': '*/*',
'Accept-Language': 'en',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://www.xing.com/network/contactlist?sc_o=contacts_network_contactlist_click',
'content-type': 'application/json',
'xing-hops-version': '12.8.1',
'X-CSRF-Token': 'LFb5YNkJ-ao6klwOC0TlxzMEl57dC9mY',
'Origin': 'https://www.xing.com',
'Connection': 'keep-alive',
'Cookie': 'visitor_id=c171c004-2757-4f34-8e66-b19ac99a394e; AMCV_0894FF2554F733210A4C98C6%40AdobeOrg=1585540135%7CMCIDTS%7C18472%7CMCMID%7C34431240474313072722481623697729984457%7CMCAAMLH-1596560138%7C12%7CMCAAMB-1596560138%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1595962538s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18460%7CvVersion%7C4.4.0; s_ecid=MCMID%7C34431240474313072722481623697729984457; userConsent=%7B%22version%22%3A%221%22%2C%22marketing%22%3Atrue%7D; was_logged_in_once=true; ab.storage.userId.bd5d74db-085a-4722-a85a-7080dbaa6faa=%7B%22g%22%3A%2223965748%22%2C%22c%22%3A1594308929317%2C%22l%22%3A1594308929317%7D; ab.storage.sessionId.bd5d74db-085a-4722-a85a-7080dbaa6faa=%7B%22g%22%3A%223e4b35b1-176b-580c-af01-9432944749ba%22%2C%22e%22%3A1595957316852%2C%22c%22%3A1595955514728%2C%22l%22%3A1595955516852%7D; ab.storage.deviceId.bd5d74db-085a-4722-a85a-7080dbaa6faa=%7B%22g%22%3A%22b6c4d960-38d0-bd3b-3ed4-01f866deeca3%22%2C%22c%22%3A1594308929326%2C%22l%22%3A1594308929326%7D; cto_bundle=H-lWMV9JVXJYRzdFQ2pHNHRTcDZhamd1eVNFQWkxdWpjemRNNnV2RXVuJTJGa0FGakdxVWpRUTlWTHpMcTglMkJYVHpCSmhGSHoySFpCVnpaVjVXalU2VWJRU3hDTlZ5akhuQXppS1k5d1RFaENEeGdaYktzcWw4VWtrT0l4TmtMZkRUNmd0VjdDbUJVZmJueG5vMzRJTXRwcFEwUVVBJTNEJTNE; language=en; xing_csrf_token=LFb5YNkJ-ao6klwOC0TlxzMEl57dC9mY; xing_csrf_checksum=tsHa1393wBzmhE0HwiEJarvDAQ07HY1KYkjfNDSVOdA; c_=ab1e0b621f61f957ef8643e955508aec; prevPage=wbm%2FContacts%2Fnetwork; AMCVS_0894FF2554F733210A4C98C6%40AdobeOrg=1; s_cc=true; s=PSjg6AJA8_LJwmhJnC4HzQ; login=MjM5NjU3NDgjMjM5NjU3NDgtRF8wQk9WYkxoV0pqR2RGR0ptZEFqYnBhbDRH%0ATkZPNVc4NWdVR2ZHNFlYOA%3D%3D--63d75bef8d1d8fbfb106c2ff7138d7ac23c283f3'}

headers2={
'Host': 'www.xing.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
'Accept': '*/*',
'Accept-Language': 'en',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://www.xing.com/profile/Peter_AMohr?sc_o=contacts_contactlist_profile_click',
'content-type': 'application/json',
'XING-ONE-PREVIEW': 'true',
'xing-hops-version': '12.9.1',
'X-CSRF-Token': 'sA78WAco9n4dM9lyBRejng5mlLnrcFMe',
'Origin': 'https://www.xing.com',
'Connection': 'keep-alive',
'Cookie': 'visitor_id=c171c004-2757-4f34-8e66-b19ac99a394e; AMCV_0894FF2554F733210A4C98C6%40AdobeOrg=1585540135%7CMCIDTS%7C18472%7CMCMID%7C34431240474313072722481623697729984457%7CMCAAMLH-1596629440%7C12%7CMCAAMB-1596629440%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1596031841s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18460%7CvVersion%7C4.4.0; s_ecid=MCMID%7C34431240474313072722481623697729984457; userConsent=%7B%22version%22%3A%221%22%2C%22marketing%22%3Atrue%7D; was_logged_in_once=true; ab.storage.userId.bd5d74db-085a-4722-a85a-7080dbaa6faa=%7B%22g%22%3A%2223965748%22%2C%22c%22%3A1594308929317%2C%22l%22%3A1594308929317%7D; ab.storage.sessionId.bd5d74db-085a-4722-a85a-7080dbaa6faa=%7B%22g%22%3A%223e4b35b1-176b-580c-af01-9432944749ba%22%2C%22e%22%3A1595958140865%2C%22c%22%3A1595955514728%2C%22l%22%3A1595956340865%7D; ab.storage.deviceId.bd5d74db-085a-4722-a85a-7080dbaa6faa=%7B%22g%22%3A%22b6c4d960-38d0-bd3b-3ed4-01f866deeca3%22%2C%22c%22%3A1594308929326%2C%22l%22%3A1594308929326%7D; cto_bundle=dizAR19JVXJYRzdFQ2pHNHRTcDZhamd1eVNQUzlWZzVWQW1uYk1xeDNSSk51Q2dEblZDUm9xUFQlMkJZQVNtZWt4ak5PdVBIQmIyY1JEWCUyQkZER0s4MHJGbm1YJTJCNjVPOFZCdmZzJTJGaVdncDlmZGNuS0RFZE9iZW9yM2MxcllISnZwbWQ5NG5BbFV3UzlDMDE2dnVPdjBqN2haczdEUSUzRCUzRA; language=en; c_=ab1e0b621f61f957ef8643e955508aec; login=MjM5NjU3NDgjMjM5NjU3NDgtRF8wQk9WYkxoV0pqR2RGR0ptZEFqYnBhbDRH%0ATkZPNVc4NWdVR2ZHNFlYOA%3D%3D--63d75bef8d1d8fbfb106c2ff7138d7ac23c283f3; xing_csrf_token=sA78WAco9n4dM9lyBRejng5mlLnrcFMe; xing_csrf_checksum=0Ov49zConsW2cAZxPQR7NmfBMix1-a2zo8ra6zroX78; prevPage=wbm%2FContacts%2Fcontactlist; AMCVS_0894FF2554F733210A4C98C6%40AdobeOrg=1; s_cc=true'}

s=requests.Session()
url='https://login.xing.com/login/api/login'
json={"password":"PWSandeep","perm":"1","dest_url":"https://www.xing.com/home","username":"pierre@viuwi.com"}
r=s.post(url,json=json,headers=headers,verify=False)
rows=[]
num=1
import time
while 1:
  url='https://www.xing.com/xing-one/api'
  json={"operationName":"contactsNetwork","variables":{"limit":100,"offset":(num-1)*100,"orderBy":"LAST_NAME"},"query":"query contactsNetwork($offset: Int, $limit: Int, $orderBy: ContactsListOrderBy, $filters: ContactsFilters) {\n  viewer {\n    contactsNetwork(offset: $offset, limit: $limit, orderBy: $orderBy, filters: $filters) {\n      total\n      collection {\n        id\n        contactCreatedAt\n        normalizedInitialOfFirstName\n        normalizedInitialOfLastName\n        memo\n        tagList {\n          id\n          name\n          __typename\n        }\n        xingId {\n          firstName\n          lastName\n          ...UserInfoWithOccupation\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment UserInfoWithOccupation on XingId {\n  ...UserInfo\n  profileOccupation {\n    occupationOrg\n    occupationTitle\n    __typename\n  }\n  __typename\n}\n\nfragment UserInfo on XingId {\n  userFlags {\n    displayFlag\n    __typename\n  }\n  displayName\n  gender\n  pageName\n  profileImage(size: SQUARE_64) {\n    url\n    __typename\n  }\n  __typename\n}\n"}
  r=s.post(url,json=json,headers=headers1,verify=False)
  d=r.json()
  objs=d['data']['viewer']['contactsNetwork']['collection']
  print(num,len(objs))
  if(len(objs)==0):
    break
  for obj in objs:
    time.sleep(1)
    fname=obj['xingId']['firstName']
    lname=obj['xingId']['lastName']
    gender=obj['xingId']['gender']
    tags=obj['tagList']
    tag=[]
    for t in tags:
      tag.append(t['name'])
    tag=','.join(tag)
    pgname=obj['xingId']['pageName']
    pid=obj['id']
    print(pgname)
    ur='https://www.xing.com/xing-one/api'
    jdata={"operationName":"getXingId","variables":{"profileId":pgname,"actionsFilter":["ADD_CONTACT","ADVERTISE_PROFILE","BLOCK_USER","CONFIRM_CONTACT","EDIT_XING_ID","FOLLOW","INVITE_GROUP","OPEN_INSIDER_COLLECTION","OPEN_SETTINGS","OPEN_XTM","PRINT","REPORT_PROFILE","SEND_MESSAGE","SHARE","SHOW_CONTACT_DETAILS","UNBLOCK_USER","UNFOLLOW"]},"query":"query getXingId($profileId: SlugOrID!, $actionsFilter: [AvailableAction!]) {\n  profileModules(id: $profileId) {\n    __typename\n    xingIdModule(actionsFilter: $actionsFilter) {\n      xingId {\n        status {\n          localizationValue\n          __typename\n        }\n        __typename\n      }\n      __typename\n      ...xingIdContactDetails\n      ...xingIdModuleCta\n    }\n  }\n}\n\nfragment xingIdContactDetails on XingIdModule {\n  contactDetails {\n    business {\n      address {\n        city\n        country {\n          countryCode\n          name: localizationValue\n          __typename\n        }\n        province {\n          id\n          canonicalName\n          name: localizationValue\n          __typename\n        }\n        street\n        zip\n        __typename\n      }\n      email\n      fax {\n        phoneNumber\n        __typename\n      }\n      mobile {\n        phoneNumber\n        __typename\n      }\n      phone {\n        phoneNumber\n        __typename\n      }\n      __typename\n    }\n    private {\n      address {\n        city\n        country {\n          countryCode\n          name: localizationValue\n          __typename\n        }\n        province {\n          id\n          canonicalName\n          name: localizationValue\n          __typename\n        }\n        street\n        zip\n        __typename\n      }\n      email\n      fax {\n        phoneNumber\n        __typename\n      }\n      mobile {\n        phoneNumber\n        __typename\n      }\n      phone {\n        phoneNumber\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment xingIdModuleCta on XingIdModule {\n  actions {\n    __typename\n    label\n  }\n  __typename\n}\n"}
    r1=s.post(ur,json=jdata,headers=headers2,verify=False)
    d1=r1.json()
    k=d1['data']['profileModules']['xingIdModule']['contactDetails']
    k=k['business']
    try:
      city=k['address']['city']
    except:
      city=''
    try:
      country=k['address']['country']['name']
    except:
      country=''
    try:
      prov=k['address']['province']['name']
    except:
      prov=''
    try:
      street=k['address']['street']
    except:
      street=''
    try:
      zip=k['address']['zip']
    except:
      zip=''
    try:
      email=k['email']
    except:
      email=''
    try:
      fax=k['fax']['phoneNumber']
    except:
      fax=''
    try:
      mobile=k['mobile']['phoneNumber']
    except:
      mobile=''
    try:
      phone=k['phone']['phoneNumber']
    except:
      phone=''
    urll='https://www.xing.com/profile/'+pgname+'/portfolio'
    #print(city,country,prov,street,zip,email,fax,mobile,phone)
    row=[fname,lname,gender,tag,city,country,prov,street,zip,email,fax,mobile,phone,urll]  
    rows.append(row)
  print(num,len(rows))
  num=num+1
  time.sleep(10)


js={"data":[]}

for row in rows:
  div={
        "uuid": row[13],
        "email": row[9],
        "gender": row[2],
        "firstname": row[0],
        "lastname": row[1],
        "tag":row[3],
        "phone": row[12],
        "mobile": row[11],
        "fax": row[10],
        "street": row[7],
        "postcode": row[8],
        "city": row[4],
        "region": row[6],
        "country": row[5]
         }
  js["data"].append(div)

import json
with open("xing.json", "w") as outfile:  
    json.dump(js, outfile)

    
print('scraping finished')
print('to send data to server use python send.py')

#########################################################
##coded by ankitmaheswari130@gmail.com                  #
##Ankit Maheshwari https://www.freelancer.in/u/mankit121#
#########################################################
import requests
from bs4 import BeautifulSoup as soup
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
print('sending post request')

with open("xing.json",'r') as f:
  da=json.load(f)


api_key='ga04gfgehkdLepr9YUAARZ4N4EYY0ufPHeKI8B5SaewsYN32dOe'

url='https://viuwi.com/v1/import/'+api_key


r=requests.post(url,json=js['data'],verify=False)
print('post request sent with status code '+str(r.staus_code))
