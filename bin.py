num = int(input("Enter a binary number "))

digits = [int(d) for d in str(num)]


length = len(digits)

def func():
    dec = 0
    for i in digits:
        calc = digits*2**length
        dec += calc
        calc = 0
    print(dec)

func()