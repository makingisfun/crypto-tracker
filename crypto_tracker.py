#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Cryptocurrency tracker
# Based on the API from coinmarketcap.com (https://api.coinmarketcap.com)
# Date: 07.07.2018
# code hosted on https://github.com/makingisfun42/crypto-tracker
# project website: https://makingisfun42.github.io/crypto-tracker

# Import packages
import json
import urllib2
import time

sleeptime = 15 # defines, how long the script waits to refresh the price data (in seconds)

# Create & Open logfile
logfile = open("cryptologger.txt", "a")

# function to write information to the logfile
def writeToFile(time, bitcoinprice):
    logfile = open("cryptologger.txt", "a") # open the logfile to append information
    # Print information in console    
    print 'Time: ', time
    print 'Current Price (USD):'
    print 'Bitcoin: ', bitcoinprice
    print '---------------'
    # Write information to logfile
    logfile.write(time + " , " + bitcoinprice + "\n")
    logfile.close() # close logfile

# API / Source for the data
bitcoin = "https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=USD"

# Get current data
bitcoindata = json.load(urllib2.urlopen(bitcoin))

# Extract prices
bitcoinprice1 = bitcoindata[0]['price_usd']
bitcoinprice2 = bitcoinprice1
# Get current time
timeNow = time.strftime("%d %b %Y %H:%M:%S")
# Write information to logfile
writeToFile(timeNow, bitcoinprice1)

# loop
while True:
    if bitcoinprice1 == bitcoinprice2: # if the price didn't change compared to the last refresh, do nothing
        time.sleep(sleeptime)
        bitcoindata = json.load(urllib2.urlopen(bitcoin))
        bitcoinprice2 = bitcoindata[0]['price_usd']
    else: # if it did change, write the new information into the logfile and print it to the console
        bitcoinprice1 = bitcoinprice2
        bitcoindata = json.load(urllib2.urlopen(bitcoin))
        bitcoinprice2 = bitcoindata[0]['price_usd']
        timeNow = time.strftime("%d %b %Y %H:%M:%S")
        writeToFile(timeNow, bitcoinprice1)
