# finaml_types.py

# Define a financial instrument using Algebraic Data Types
class FinancialInstrument:
    def __str__(self):
        return f"{self.__class__.__name__}({', '.join([f'{key}={value}' for key, value in self.__dict__.items()])})"

class Stock(FinancialInstrument):
    def __init__(self, ticker_symbol, current_price):
        self.ticker_symbol = ticker_symbol
        self.current_price = current_price

class Bond(FinancialInstrument):
    def __init__(self, ticker_symbol, face_value, coupon_rate):
        self.ticker_symbol = ticker_symbol
        self.face_value = face_value
        self.coupon_rate = coupon_rate

class Option(FinancialInstrument):
    def __init__(self, option_type, underlying_asset, strike_price, expiration_date):
        self.option_type = option_type
        self.underlying_asset = underlying_asset
        self.strike_price = strike_price
        self.expiration_date = expiration_date
