def main():
    print("This program converts from US dollars to euros.")
    print("The current exchange rate is 1 USD = 0.85 EUR.")

    dollars = float(input("Enter the amount in US dollars: "))
    euros = dollars * 0.85
    print("That will be", euros, "euros.")

main()