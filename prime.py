list = list(range(10,99))

prime = []

for i in list:
     c = 0
     for j in range(1,i):
        if i % j == 0:
           c = c+1
     if c == 1:
         prime.append(i)

print(f"Prime numbers are: {prime}")