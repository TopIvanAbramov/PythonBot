import requests
import json
import yobit

token =  "623282742:AAFLDCLBWHp3Mssn2CKYUbci_RiqkaSNjvE"
URL = 'https://api.telegram.org/bot' + token + '/'
global last_update_id
last_update_id = 0

def get_updates():
    url = URL + 'getupdates'
    #print(url)
    r = requests.get(url)
    return r.json()

def get_message():
    data = get_updates()
    current_update_id = data['result'][-1]['update_id']
    global last_update_id
    if last_update_id != current_update_id:
        chat_id = data['result'][-1]['message']['chat']['id']
        m_text = data['result'][-1]['message']['text']
        message = {'chat_id' : chat_id, 'text' : m_text}
        last_update_id = current_update_id
        return message
    return None

def send_message(chat_id, text = 'Wait a second ...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    d = get_updates()
    answer = get_message()
    if answer != None:
        chat_id = answer['chat_id']
        text = answer['text']
        if 'btc' in text or '/btc' in text or 'bitcoin' in text or 'биткойн' in text:
            message = yobit.btc()
            send_message(chat_id, message)

        if 'eth' in text or '/eth' in text or 'ethereum' in text or 'биткойн' in text:
            message = yobit.eth()
            send_message(chat_id, message)

        if 'trx' in text or 'ripple' in text or 'рипл' in text:
            message = yobit.trx()
            send_message(chat_id, message)



if __name__ == '__main__':
    while True:
        main()
