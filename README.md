# FinAML Documentation

FinAML (Financial Analytical Markup Language) is a cutting-edge programming language tailored for financial analysis and modeling. This documentation provides an overview of key features, syntax, and usage of FinAML, drawing inspiration from the functional programming paradigm of OCaml.

## Key Features

1. **Functional Paradigm**
   FinAML embraces a functional programming paradigm, providing immutability and first-class functions for enhanced code clarity and maintainability.

2. **Static Typing and Inference**
   Similar to OCaml, FinAML employs static typing and type inference to ensure robustness, catching errors at compile-time and promoting code reliability.

3. **Expressive Syntax**
   FinAML features a clean and expressive syntax, minimizing boilerplate code and promoting concise expression of complex financial algorithms. The language aims to enhance productivity without compromising readability.

4. **Algebraic Data Types (ADTs)**
   ADTs are a cornerstone of FinAML, enabling developers to model complex financial structures accurately, enhancing code organization and facilitating comprehensive representation of financial instruments.

5. **Pattern Matching**
   Pattern matching, inspired by OCaml, is integral to FinAML, allowing developers to concisely handle various scenarios in financial data manipulation and analysis.

6. **Native Support for Financial Operations**
   FinAML comes with built-in libraries tailored for financial calculations, time-series analysis, and risk modeling, reducing the need for external dependencies.

## Example Code

```ocaml
type option_type = Call | Put

type option = {
  option_type: option_type;
  underlying_asset: string;
  strike_price: float;
  expiration_date: string;
  volatility: float;
}

(* Function to calculate the present value of a financial instrument *)
let present_value = function
  | Stock (_, price) -> price
  | Bond (_, face_value, coupon_rate) -> face_value /. (1. +. coupon_rate)
  | Option (_, _, _, _) -> 0. (* Placeholder for options *)

(* Function to calculate the Black-Scholes option pricing model *)
let black_scholes_option_pricing option current_price risk_free_rate time_to_maturity =
  let d1 = (log (current_price /. option.strike_price) +. (risk_free_rate +. (option.volatility ** 2.) /. 2.) *. time_to_maturity) /.
           (option.volatility *. sqrt time_to_maturity) in
  let d2 = d1 -. option.volatility *. sqrt time_to_maturity in

  match option.option_type with
  | Call ->
    current_price *. Stats.norm_cdf d1 -. option.strike_price *. exp (-. risk_free_rate *. time_to_maturity) *. Stats.norm_cdf d2
  | Put ->
    option.strike_price *. exp (-. risk_free_rate *. time_to_maturity) *. Stats.norm_cdf (-. d2) -. current_price *. Stats.norm_cdf (-. d1)
;;

(* Function to calculate the future value of a financial instrument *)
let future_value financial_instrument time_period growth_rate =
  match financial_instrument with
  | Stock (_, current_price) -> current_price *. (1. +. growth_rate) ** time_period
  | Bond (_, face_value, coupon_rate) -> face_value *. (1. +. coupon_rate) ** time_period
  | Option (_, _, _, _) -> 0. (* Placeholder for options *)

(* Function to simulate a portfolio with multiple financial instruments *)
let simulate_portfolio portfolio discount_rate growth_rate =
  List.fold_left (fun acc inst -> acc +. present_value inst /. (1. +. discount_rate) +. future_value inst 5. growth_rate) 0. portfolio
;;

(* Function to calculate the net present value (NPV) of a cash flow *)
let calculate_npv cash_flow discount_rate =
  List.fold_left (fun acc (i, cash) -> acc +. cash /. (1. +. discount_rate) ** float i) 0. (List.mapi (fun i cash -> (i, cash)) cash_flow)
;;

(* Function to perform sensitivity analysis on NPV *)
let sensitivity_analysis cash_flow discount_rate_range =
  List.map (fun rate -> rate, calculate_npv cash_flow rate) discount_rate_range
;;

(* Additional features *)
let average_portfolio_return portfolio =
  let simulate_single_portfolio () = simulate_portfolio portfolio 0.1 0.05 in
  Stats.mean (Array.init 10000 (fun _ -> simulate_single_portfolio ()))
;;

let portfolio_std_dev portfolio =
  let simulate_single_portfolio () = simulate_portfolio portfolio 0.1 0.05 in
  Stats.stddev (Array.init 10000 (fun _ -> simulate_single_portfolio ()))
;;

let option_price_bs option current_price =
  black_scholes_option_pricing option current_price 0.03 1.0
;;

let calculate_var portfolio confidence_level =
  let simulate_single_portfolio () = simulate_portfolio portfolio 0.1 0.05 in
  Stats.percentile (Array.init 10000 (fun _ -> simulate_single_portfolio ())) (1. -. confidence_level)
;;

let calculate_es portfolio confidence_level =
  let simulate_single_portfolio () = simulate_portfolio portfolio 0.1 0.05 in
  let portfolio_values = Array.init 10000 (fun _ -> simulate_single_portfolio ()) in
  Stats.mean (Array.filter (fun value -> value < calculate_var portfolio confidence_level) portfolio_values)
;;

(* Financial modeling example *)
let main () =
  let stock = Stock("AAPL", 150.0) in
  let bond = Bond("XYZ", 1000.0, 0.05) in
  let option = Option(Call, "AAPL", 160.0, "2023-12-31", 0.2) in
  let portfolio = [stock; bond; option] in

  let pv_stock = present_value stock in
  let pv_bond = present_value bond in

  Printf.printf "Present Value of Stock: $%.2f\n" pv_stock;
  Printf.printf "Present Value of Bond: $%.2f\n" pv_bond;

  let average_return = average_portfolio_return portfolio in
  Printf.printf "Average Portfolio Return: $%.2f\n" average_return;

  let std_dev = portfolio_std_dev portfolio in
  Printf.printf "Portfolio Standard Deviation: $%.2f\n" std_dev;

  let option_price = option_price_bs option stock.current_price in
  Printf.printf "Black-Scholes Option Price: $%.2f\n" option_price;

  let var_result = calculate_var portfolio 0.95 in
  Printf.printf "Value at Risk (VaR) at 95%% confidence level: $%.2f\n" var_result;

  let es_result = calculate_es portfolio 0.95 in
  Printf.printf "Expected Shortfall (ES) at 95%% confidence level: $%.2f\n" es_result
;;

(* Run the financial modeling example *)
let () = main ()

