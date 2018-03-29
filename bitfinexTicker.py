import urllib.request
contents = urllib.urlopen("https://api.bitfinex.com/v1/pubticker/BTCUSD").read()
print contents