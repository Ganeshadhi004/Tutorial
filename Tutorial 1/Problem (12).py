num = [int(input(f"Enter number {i+1}: ")) for i in range(4)]
p = [a for a in num if a > 0]
n = [a for a in num if a < 0]
print(f"Sum of positive nos: {sum(p)}" )
print(f"Sum of negative nos: {sum(n)}")
print(f" Average (positive) : {sum(p)/len(p) if p else 0}") 
print(f" Average (negative) : {sum(n)/len(n) if n else 0}") 
