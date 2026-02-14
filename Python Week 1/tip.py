def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollar = d.replace("$", "")
    dollar_float = float(dollar)

    rounded_dollar = round(dollar_float, 1)

    return rounded_dollar


def percent_to_float(p):
   tip = p.replace('%', '')
   tip_float = float(tip)

   tip_value = tip_float/100.0

   rounded_tip = round(tip_value, 2)

   return rounded_tip


main()