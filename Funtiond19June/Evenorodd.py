def even_odd (num):
    if num%2==0:
        print("Number is Even")
    else:
        print("Number is odd")

even_odd(5)


check_even_odd = lambda num: "even" if num%2 ==0 else "odd"
print(check_even_odd)