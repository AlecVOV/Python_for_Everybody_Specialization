def computepay(hours, rate):
    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours * rate
    return total_pay
    

# Prompt the user for input
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate per Hour: "))

# Compute the pay
pay = computepay(hours, rate)

# Print the result
print(f"Pay {pay}")