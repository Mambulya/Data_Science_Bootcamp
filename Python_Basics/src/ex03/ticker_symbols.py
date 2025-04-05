import sys

def get_stock(stock:str) -> str:
    COMPANIES = {
  'Apple': 'AAPL',
  'Microsoft': 'MSFT',
  'Netflix': 'NFLX',
  'Tesla': 'TSLA',
  'Nokia': 'NOK'
  }

    STOCKS = {
  'AAPL': 287.73,
  'MSFT': 173.79,
  'NFLX': 416.90,
  'TSLA': 724.88,
  'NOK': 3.37
  }

    new_stocks = {key.lower(): value for key, value in STOCKS.items()}
    new_companies = {key: value.lower() for key, value in COMPANIES.items()}

    if (stock in new_stocks.keys()):
        price = new_stocks[stock]
        comp = ""
        for k, v in new_companies.items():
            if v == stock:
                comp = k
        return "{} {}".format(comp, price)
    else:
        return "Unknown ticker"



if __name__ == "__main__":
    arguments = sys.argv
    if (len(arguments) == 2):
        stock = arguments[-1].lower()
        answer = get_stock(stock)
        print(answer)
    
