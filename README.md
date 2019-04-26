# Cryptocurrency tracker


## Requirements
### Used libraries (if not already installed, install them first)
- json
- urllib2
- time
## How to use the code
- Make sure you have Python installed (version 2.7) & meet all the requirements
- Download crypto_tracker.py
- Run "python crypto_tracker.py" from your command line
## How the code works
- The coinmarketcap API is sourced for the current price
- the price is saved in a logfile together with the current time and writes it to the terminal
- the code pauses until the price changes
- the logfile can then be plotted and analyzed e.g. using Matlab, Excel, ...

## How to customize the code
- change bitcoin = "https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=USD" or add another value by replacing "bitcoin" with the value you want to track (e.g. to "https://api.coinmarketcap.com/v1/ticker/litecoin/?convert=USD" to track Litecoin)
- change currency: replace "?convert=USD" e.g. to "?convert=EUR" ;-)