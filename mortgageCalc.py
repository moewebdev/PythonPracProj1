import math
def main():
    print("--- MORTGAGE CALCULATOR ---")
    while True:
        loan_amount = float(input("Loan Amount: ")) 
        loan_term = int(input("Loan Term (years): "))
        interest_rate = float(input("Interest Rate: ")) 
    
        p = loan_amount #principal 
        r = ((interest_rate / 100 ) / 12) #monthly interest rate 
        n = loan_term * 12 #number of payments 

        #Monthly Payment (PMT) = P * (r * (1+r)^n) / ((1+r)^n - 1)
        monthly_payment = p * (r * pow((1 + r), n)) / (pow((1 + r), n) - 1)

        print(f"Monthly Payment: ${math.ceil(monthly_payment)}")
        
        print("Calculate another Mortgage?")
        prompt = input("Y or N ").lower()
        if prompt == "y":
            continue
        else:
            break

main()