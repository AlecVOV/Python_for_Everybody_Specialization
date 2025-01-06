hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
h, rate = float(hrs), float(rate)
if h <= 40: 
    print(h * rate)
else:
    ot = h - 40
    print(40 * rate + ot * 1.5 * rate)