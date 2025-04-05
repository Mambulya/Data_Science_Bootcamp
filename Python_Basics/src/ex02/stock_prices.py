import sys

def get_stock(comp:str) -> str:
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

    new_companies = {key.lower(): value for key, value in COMPANIES.items()}

    if (comp in new_companies.keys()):
        return STOCKS[new_companies[comp]]
    else:
        return "Unknown company"



if __name__ == "__main__":
    arguments = sys.argv
    if (len(arguments) == 2):
        company = arguments[-1].lower()
        print(get_stock(company))
    
