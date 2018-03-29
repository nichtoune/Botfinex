# -*- coding: utf8 -*-

import urllib2
import time

'''création du timestamp h-24'''
now = time.time()
tsnow = time.localtime(now)
timerstart = time.mktime(tsnow)-86400
print timerstart


''' requête des 50 trades à partir du timestart'''

tradeUrl = "https://api.bitfinex.com/v1/trades/BTCUSD?limit_trades=50&timestamp="

contents = urllib2.urlopen(tradeUrl+str(timerstart)).read()
print contents


