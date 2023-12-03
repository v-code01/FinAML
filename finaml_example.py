# finaml_example.py
from finaml_types import Stock, Bond, Option
from finaml_operations import present_value, future_value, simulate_portfolio, calculate_npv, sensitivity_analysis

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
