from prettytable import PrettyTable

# def calculate_annuity_payment_schedule(initial_payment, interest_rates, inflation_rates, num_periods, rounding_amount):
#     total_payments = []
#     for i in range(num_periods):
#         # Calculate present value of payment using inflation-adjusted interest rate
#         present_value = initial_payment / ((1 + inflation_rates[i]) ** (i+1))
        
#         # Calculate payment amount based on present value and number of periods
#         payment = present_value / ((1 - (1 + interest_rates[i]) ** -num_periods) / interest_rates[i])
#         total_payments.append(payment)
    
#     # Round the final payment to the nearest million
#     total_payments[-1] = round(total_payments[-1] / rounding_amount) * rounding_amount
    
#     return total_payments

# # Example usage
# initial_payment = 1000000
# interest_rates = [0.05] * 3 + [0.075] * 4 + [0.08] * 3
# inflation_rates = [0.02] * 10  # Example inflation rates (can vary)
# num_periods = 10
# rounding_amount = 1000000  # Round to the nearest million

# payment_schedule = calculate_annuity_payment_schedule(initial_payment, interest_rates, inflation_rates, num_periods, rounding_amount)

# # Create a PrettyTable
# table = PrettyTable()
# table.field_names = ["Year", "Payment"]

# # Populate the table with the payment schedule
# for year, payment in enumerate(payment_schedule, start=1):
#     table.add_row([year, "${:,.2f}".format(payment)])

# print(table)


def calculate_rounded_total_payment(first_year_payment, interest_rates, num_periods, rounding_amount):
    total_payment = 0
    table = PrettyTable()
    table.field_names = ["Year", "Annual Payment", "Interest Rate", "Accumulated Total"]
    
    for i in range(num_periods):
        # Calculate payment amount for each period using the interest rate
        payment = first_year_payment * ((1 + interest_rates[i]) ** i)
        total_payment += payment
        table.add_row([i + 1, "${:,.2f}".format(payment), "{:.2%}".format(interest_rates[i]), "${:,.2f}".format(total_payment)])
    
    # Round the total payment to the nearest million
    total_payment = round(total_payment / rounding_amount) * rounding_amount
    
    print(table)
    return total_payment

# Example usage
first_year_payment = 1000000
interest_rates = [0.05] * 3 + [0.075] * 4 + [0.08] * 3
num_periods = 10
rounding_amount = 1000000  # Round to the nearest million

rounded_total_payment = calculate_rounded_total_payment(first_year_payment, interest_rates, num_periods, rounding_amount)
print("\nRounded Total Payment: ${:,.2f}".format(rounded_total_payment))

