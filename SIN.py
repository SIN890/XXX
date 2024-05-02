import time
import requests
import random
import string
import json,re
import time
import hashlib
import uuid,os
from faker import Faker
def SIN():
	def windows():
	    aV=str(random.choice(range(10,20)))
	    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
	    bV=str(random.choice(range(1,36)))
	    bx=str(random.choice(range(34,38)))
	    bz=f"5{bx}.{bV}"
	    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
	    cV=str(random.choice(range(1,36)))
	    cx=str(random.choice(range(34,38)))
	    cz=f"5{cx}.{cV}"
	    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
	    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
	    return random.choice([A,B,C,D])
	def generate_random_string(length):
	    letters_and_digits = string.ascii_letters + string.digits
	    return ''.join(random.choice(letters_and_digits) for i in range(length))
	def get_mail_domains():
	    url = "https://api.mail.tm/domains"
	    try:
	        response = requests.get(url)
	        if response.status_code == 200:
	            return response.json()['hydra:member']
	        else:
	            print(f'[×] E-mail Error : {response.text}')
	            return None
	    except Exception as e:
	        print(f'[×] Error : {e}')
	        return None
	def create_mail_tm_account():
	    fake = Faker()
	    mail_domains = get_mail_domains()
	    if mail_domains:
	        domain = random.choice(mail_domains)['domain']
	        username = generate_random_string(10)
	        password = fake.password()
	        birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
	        first_name = fake.first_name()
	        last_name = fake.last_name()
	        url = "https://api.mail.tm/accounts"
	        headers = {"Content-Type": "application/json"}
	        data = {"address": f"{username}@{domain}", "password":password}       
	        try:
	            response = requests.post(url, headers=headers, json=data)
	            if response.status_code == 201:
	                print(f'\x1b[1;94m*Wait ')
	                return f"{username}@{domain}", password, first_name, last_name, birthday
	            else:
	                print(f'[×] Email Error : {response.text}')
	                return None, None, None, None, None
	        except Exception as e:
	            print(f'[×] Error : {e}')
	            return None, None, None, None, None
	def register_facebook_account(email, password, first_name, last_name, birthday):
	    api_key = '882a8490361da98702bf97a021ddc14d'
	    secret = '62f8ce9f74b12f84c123cc23437a4a32'
	    gender = random.choice(['M', 'F'])
	    req = {'api_key': api_key,'attempt_login': True,'birthday': birthday.strftime('%Y-%m-%d'),'client_country_code': 'EN','fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod','fb_api_req_friendly_name': 'registerAccount','firstname': first_name,'format': 'json','gender': gender,'lastname': last_name,'email': email,'locale': 'en_US','method': 'user.register','password': password,'reg_instance': generate_random_string(32),'return_multiple_errors': True}
	    sorted_req = sorted(req.items(), key=lambda x: x[0])
	    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
	    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
	    req['sig'] = ensig
	    api_url = 'https://b-api.facebook.com/method/user.register'
	    reg = _call(api_url, req)
	    id=reg['new_user_id']
	    token=reg['session_info']['access_token']
	    r= requests.Session()
	    head = {'Host':'b-graph.facebook.com','X-Fb-Connection-Quality':'EXCELLENT','Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; RMX3740 Build/QP1A.190711.020) [FBAN/FB4A;FBAV/417.0.0.33.65;FBPN/com.facebook.katana;FBLC/in_ID;FBBV/480086274;FBCR/Corporation Tbk;FBMF/realme;FBBD/realme;FBDV/RMX3740;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.0,width=540,height=960};FB_FW/1;FBRV/483172840;]','X-Tigon-Is-Retry':'false','X-Fb-Friendly-Name':'authenticate','X-Fb-Connection-Bandwidth':str(random.randrange(70000000,80000000)),'Zero-Rated':'0','X-Fb-Net-Hni':str(random.randrange(50000,60000)),'X-Fb-Sim-Hni':str(random.randrange(50000,60000)),'X-Fb-Request-Analytics-Tags':'{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}','Content-Type':'application/x-www-form-urlencoded','X-Fb-Connection-Type':'WIFI','X-Fb-Device-Group':str(random.randrange(4700,5000)),'Priority':'u=3,i','Accept-Encoding':'gzip, deflate','X-Fb-Http-Engine':'Liger','X-Fb-Client-Ip':'true','X-Fb-Server-Cluster':'true','Content-Length':str(random.randrange(1500,2000))}
	    data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':email,'password':'#PWD_FB4A:0:{}:{}'.format(str(time.time())[:10],password),'generate_analytics_claim':'1','community_id':'','linked_guest_account_userid':'','cpl':True,'try_num':'1','family_device_id':str(uuid.uuid4()),'secure_family_device_id':str(uuid.uuid4()),'credentials_type':'password','account_switcher_uids':[],'fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3','fb4a_shared_phone_cpl_group':'enable_v3_at_risk','enroll_misauth':False,'generate_session_cookies':'1','error_detail_type':'button_with_disabled','source':'login','machine_id':str(''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(24)])),'jazoest':str(random.randrange(22000,23000)),'meta_inf_fbmeta':'V2_UNTAGGED','advertiser_id':str(uuid.uuid4()),'encrypted_msisdn':'','currently_logged_in_userid':'0','locale':'id_ID','client_country_code':'ID','fb_api_req_friendly_name':'authenticate','fb_api_caller_class':'Fb4aAuthHandler','api_key':'882a8490361da98702bf97a021ddc14d','sig':str(hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:32]),'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
	    pos=r.post('https://b-graph.facebook.com/auth/login', data=data, headers=head).json()
	    if  ('session_key' in str(pos)) and ('access_token' in str(pos)):
	    	tokene  = pos['access_token']
	    	cookie = ''.join(['{}={};'.format(i['name'],i['value']) for i in pos['session_cookies']])	    	
	    	
	    	open(".cok.txt", "a").write(cookie)
	    	open(".token.txt", "a").write(token)
	    	
	    print(f'''
•••••••••An account has been created••••
EMAIL : {email}
PASWORD : {password}
Birthday: {birthday}
First_name: {first_name}
Last_name: {last_name}
Token : {tokene}
COOKIES :  {cookie}
DV : @B_S_A_I''')
	def _call(url, params, post=True):
	    headers = {'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'}
	    if post:
	        response = requests.post(url, data=params, headers=headers)
	    else:
	        response = requests.get(url, params=params, headers=headers)
	    return response.json()
	for i in range(int((1))):
	 email, password, first_name, last_name, birthday = create_mail_tm_account()
	 if email and password and first_name and last_name and birthday:
	  register_facebook_account(email, password, first_name, last_name, birthday)
SIN()
