num=int(input())
if num>=0 and num%2==0:
    print("positive even")
elif num>=0 and num%3==0:
    print("odd Positive")
elif num<0 and num%2==0:
    print("negativ even")
else:
    print("odd negative")