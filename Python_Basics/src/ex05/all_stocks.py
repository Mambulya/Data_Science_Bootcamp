import sys
def find_exp(exp_arg):
    result = ""
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
    # ticker -> company
    # company -> price

    new_stocks = {key.lower(): value for key, value in STOCKS.items()}
    new_companies = {key.lower(): value.lower() for key, value in COMPANIES.items()}
    
    if exp_arg in new_stocks.keys():
        res = "{} is a ticker symbol for {}".format(exp_arg.capitalize(), new_stocks[exp_arg])
    elif exp_arg in new_companies.keys():
        res = "{} stock price is {}".format(exp_arg.capitalize(), new_stocks[new_companies[exp_arg]])
    else:
        res = "{} is an unknown company or an unknown ticker symbol".format(exp_arg.capitalize())

    return res


if __name__ == "__main__":
    if (len(sys.argv) == 2):
        expressions = sys.argv[1:]
        if (len(expressions) == 1):
            expressions[0] = expressions[0].replace(' ', '')

            if (",," not in expressions[0]):
                expressions = expressions[0].split(',')

                for exp in expressions:
                    exp = exp.lower()
                    print(find_exp(exp))

