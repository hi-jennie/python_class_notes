def main():
   dollars = float(dollars_to_float(input("How  much was the meal?")))
   percent = float(percent_to_float(input("what percentage would you like to tip?")))
   tip = round(dollars,2) * round(percent,2)
   print(f"Leave ${tip:.2f}")

def dollars_to_float(n):
       z = n.replace("$","")
       return z

def percent_to_float(m):
       x = int(m.replace("%",""))
       y = x / 100
       return y

main()
