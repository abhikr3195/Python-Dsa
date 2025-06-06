"""
Write a program to calculate bill. 
Ask the final amount from the user.
You have to give discount and print the final bill after discount.

50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 - 10% discount
1 - 9999 - No discount

Print the discount and the final amount to be paid.
Example 1
Enter bill amount = 80000
You got 30% discount
Your final bill is Rs. 56000
"""


bill_amount: float=float(input("Enter the bill amount:"))
if bill_amount >= 50000:
    discount_per=30
elif 40000 <= bill_amount <=49999:
    discount_per=25
elif 30000 <= bill_amount <= 39999:
    discount_per=20
elif 10000 <= bill_amount <= 29999:
    discount_per=10
else:
    discount_per=0

discount_amt= (discount_per/100)* bill_amount
final_amt= bill_amount-discount_amt
print(f"the discounted amount is {discount_amt}")
print(f"the final amount is {final_amt}")    
