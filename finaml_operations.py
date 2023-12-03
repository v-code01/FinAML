# finaml_operations.py
from finaml_types import Stock, Bond, Option

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
