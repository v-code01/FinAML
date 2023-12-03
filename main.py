# FinAML Implementation in Python

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

# Function to calculate the present value of a financial instrument
def present_value(financial_instrument):
    if isinstance(financial_instrument, Stock):
        return financial_instrument.current_price
    elif isinstance(financial_instrument, Bond):
        return financial_instrument.face_value / (1 + financial_instrument.coupon_rate)
    elif isinstance(financial_instrument, Option):
        return 0  # Placeholder, as options require more complex pricing models

# Function to calculate the future value of a financial instrument
def future_value(financial_instrument, time_period):
    if isinstance(financial_instrument, Stock):
        return financial_instrument.current_price * (1 + 0.05) ** time_period
    elif isinstance(financial_instrument, Bond):
        return financial_instrument.face_value * (1 + financial_instrument.coupon_rate) ** time_period
    elif isinstance(financial_instrument, Option):
        return 0  # Placeholder, as options require more complex pricing models

# Function to simulate a portfolio with multiple financial instruments
def simulate_portfolio(portfolio):
    return sum(present_value(inst) for inst in portfolio)

# Function to calculate the net present value (NPV) of a cash flow
def calculate_npv(cash_flow, discount_rate):
    return sum(cash / (1 + discount_rate) ** i for i, cash in enumerate(cash_flow))

# Function to perform sensitivity analysis on NPV
def sensitivity_analysis(cash_flow, discount_rate_range):
    return {rate: calculate_npv(cash_flow, rate) for rate in discount_rate_range}

# Financial modeling example
def main():
    stock = Stock("AAPL", 150.0)
    bond = Bond("XYZ", 1000.0, 0.05)
    option = Option("Call", "AAPL", 160.0, "2023-12-31")
    portfolio = [stock, bond, option]

    pv_stock = present_value(stock)
    pv_bond = present_value(bond)
    fv_stock = future_value(stock, 5)
    fv_bond = future_value(bond, 5)
    total_value = simulate_portfolio(portfolio)

    cash_flow = [-100, 20, 30, 40, 50]  # Initial investment followed by cash inflows
    discount_rate_range = [0.05, 0.08, 0.1, 0.12, 0.15]

    npv_result = calculate_npv(cash_flow, 0.1)
    sensitivity_result = sensitivity_analysis(cash_flow, discount_rate_range)

    print(f"Financial Modeling Example:")
    print(f" - {stock}")
    print(f" - {bond}")
    print(f" - {option}")
    print(f"Present Value of Stock: ${pv_stock:.2f}")
    print(f"Present Value of Bond: ${pv_bond:.2f}")
    print(f"Future Value of Stock (5 years): ${fv_stock:.2f}")
    print(f"Future Value of Bond (5 years): ${fv_bond:.2f}")
    print(f"Total Value of Portfolio: ${total_value:.2f}")
    print(f"Net Present Value (NPV) at 10% discount rate: ${npv_result:.2f}")
    print(f"Sensitivity Analysis on NPV:")
    for rate, npv in sensitivity_result.items():
        print(f" - Discount Rate {rate * 100}%: ${npv:.2f}")

# Run the financial modeling example
if __name__ == "__main__":
    main()
