n1 = int(input("enter n1: "))
n2 = int(input("enter n2: "))

tn1 = n1
tn2 = n2

while n1 % n2 != 0:
    r = n1 % n2
    n1 = n2
    n2 = r
gcd = n2
print("GCD:", n2)

lcm = (tn1 * tn2) / gcd
print("LCM: ", lcm)