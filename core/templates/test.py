import requests
import json
from time import sleep, strftime
from plotly import graph_objects as go
from datetime import datetime


ohlc = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/ohlc?vs_currency=usd&days=1').json()
ohlc = json.loads(json.dumps(ohlc))

# print(ohlc[1][0])

#WORKS
for i in range(len(ohlc)):
    timestamp = str(ohlc[i][0])[0:10]
    ohlc[i][0] = str(datetime.fromtimestamp(int(timestamp)).strftime("%m/%d/%Y %H:%M:%S"))
    print(ohlc[i])




# fig = go.Figure(data=go.Ohlc(x=ohlc[0],
#                     open=ohlc[1],
#                     high=ohlc[2],
#                     low=ohlc[3],
#                     close=ohlc[5]))
# fig.update(layout_xaxis_rangeslider_visible=False)
# fig.show()

# -----------------------------------------

# API = 'https://api.coingecko.com/api/v3/exchanges/currency/tickers?coin_ids=dogecoin&include_exchange_logo=true'

# lst = ['binance','bitcoin_com','bitbns','bitfinex','cryptology','ftx','gdax','gemini','huobi','wazirx','kraken','']



# for dex in lst:
#     api = API.replace('currency', dex, 1)
#     Coin_Price_Of_Specific_Exchange = requests.get(api).json()
#     exg = json.loads(json.dumps(Coin_Price_Of_Specific_Exchange))
#     cnt = 0
    
    
#     for i in range(len(exg)):
#         try:
        
#             if exg['tickers'][cnt]['target'] == 'USDT' or exg['tickers'][cnt]['target'] == 'USD':
#                 print(exg['name'])
#                 print(exg['tickers'][cnt]['base'])
#                 print(exg['tickers'][cnt]['last'])

#             cnt += 1
#             sleep(0.3)
#         except Exception as e:
#             print(e)        
#             break
# print(exg)

# -----------------------------------------

# Display coin prices of different exchanges

# Coin_ExchangeBased = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin?market_data=false&community_data=false&developer_data=false&sparkline=false').json()
# coin = json.loads(json.dumps(Coin_ExchangeBased))

# cnt = 0
# print(len(coin))
# for i in range(len(coin)):
#     try:
#         print(coin['tickers'][cnt]['market']['name'])
#         cnt += 1
#         sleep(1)
#     except Exception as e:
#         print(e)   
#         break

# -----------------------------------------

# Coins = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=400&page=1&sparkline=false').json()
# coin = json.loads(json.dumps(Coins))

# cnt = 0
# print(len(coin))
# for i in range(len(coin)):
#     try:
#         print(coin[cnt]['id'], '  ', coin[cnt]['name'], '  ', coin[cnt]['current_price'], '  ', coin[cnt]['image'])
#         cnt += 1
#         sleep(1)
#     except Exception as e:
#         print(e)
        
#         break


# -----------------------------------------

# Binance = requests.get('https://api.coingecko.com/api/v3/exchanges/binance/tickers?coin_ids=bitcoin%2Cdogecoin%2Clitecoin%2Cfilecoin').json()
# Coinbase = requests.get('https://api.coingecko.com/api/v3/exchanges/gdax/tickers?coin_ids=bitcoin%2Cdogecoin%2Clitecoin%2Cfilecoin').json()
# Kraken = requests.get('https://api.coingecko.com/api/v3/exchanges/kraken/tickers?coin_ids=bitcoin%2Cdogecoin%2Clitecoin%2Cfilecoin').json()

# Exchanges = [Binance,Coinbase,Kraken]

# for exchange in Exchanges:
#     res = json.loads(json.dumps(exchange))
#     cnt2 = 0

#     while 1:
#         try:
#             if 'USD' == res.get('tickers')[cnt2]['target']:
#                 print(res.get('tickers')[1]['market']['name'])
#                 print(res.get('tickers')[cnt2]['base'])
#                 print(res.get('tickers')[cnt2]['last'])
#                 print(res.get('tickers')[cnt2]['coin_id'])
#                 print(' __ ')
#                 cnt2 += 1
#                 # sleep(1.5)
#             else:
#                 cnt2 += 1
#         except Exception as e:
          
#             break

# -----------------------------------------

# print response
# print(response)
# print json content
# print(response.json())

# for i in 
#     if res['tickers'][0]['target'] == "USDT":
#         print('exchange :',res['name'])
#         print('base :',res['tickers'][0]['base'])
#         print('price :',res['tickers'][0]['last'])

