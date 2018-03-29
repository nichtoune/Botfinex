# -*- coding: utf8 -*-

import urllib2
contents = urllib2.urlopen("https://api.bitfinex.com/v1/trades/BTCUSD?limit_trades=5").read()
print contents


'''création du timestamp h-24'''
now = time.time()
tsnow = time.localtime(now)
timerstart = time.mktime(tsnow)-86400
print timerstart
