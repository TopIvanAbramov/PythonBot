import requests

def btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    r = requests.get(url).json()
    return str(r['ticker']['avg']) + ' $'

def eth():
    url = 'https://yobit.net/api/2/eth_usd/ticker'
    r = requests.get(url).json()
    return str(r['ticker']['avg']) + ' $'

def trx():
    url = 'https://yobit.net/api/2/trx_usd/ticker'
    r = requests.get(url).json()
    return str(r['ticker']['avg']) + ' $'
