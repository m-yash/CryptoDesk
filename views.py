from django.shortcuts import render, redirect

import requests
import json

from datetime import datetime

# Create your views here.

def index(request):
    Coins = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=350&page=1&sparkline=false').json()
    coin = json.loads(json.dumps(Coins))

    return render(request,'index.html', {'coin':coin})

def feeds(request,id):
    ohlc = requests.get('https://api.coingecko.com/api/v3/coins/'+id+'/ohlc?vs_currency=usd&days=1').json()
    ohlc = json.loads(json.dumps(ohlc))

    # for i in range(len(ohlc)):
    #     timestamp = str(ohlc[i][0])[0:10]
    #     ohlc[i][0] = str(datetime.fromtimestamp(int(timestamp)).strftime("%m/%d/%Y %H:%M:%S"))

    

    print(id, type(id)) 
    
    API = 'https://api.coingecko.com/api/v3/exchanges/Exhange/tickers?coin_ids=coin&include_exchange_logo=true'
    lst = ['binance','bitcoin_com','bitmax','bitbns','bitfinex','bittrex','cex','coindcx','cryptology','coincheck','bitflyer','bithumb','ftx','gdax','gemini','gate','huobi','kucoin','kraken','wazirx']
    
    
    exg = []

    for dex in lst:
        try:
            api = API.replace('Exhange', dex).replace('tickers?coin_ids=coin&include_exchange_logo=true','tickers?coin_ids='+id+'&include_exchange_logo=true',1)
            exg.append(api)
            # Coin_Price_Of_Specific_Exchange = requests.get(api).json()
            # exg.append(json.loads(json.dumps(Coin_Price_Of_Specific_Exchange)))
        except Exception as e:
            print(e)

    exg = json.dumps(exg)
    
    # cnt = 0
    # for i in range(len(exg)):
        
    #     try:
    #         print(exg[cnt]['name'])
    #         print(exg[cnt]['tickers'][cnt]['base'])
    #         print(exg[cnt]['tickers'][cnt]['target'])
    #         print(exg[cnt]['tickers'][cnt]['last'])
    #     except Exception as e:
    #         print(e)

    #     cnt += 1
          
    

 
    return render(request,'feed.html',{'exg': exg, 'ohlc': ohlc})