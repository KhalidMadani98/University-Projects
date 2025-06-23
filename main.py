January,February,March,April,May,June,July,August,September,October,November,December = 1,2,3,4,5,6,7,8,9,10,11,12
M = int(input("Enter the month:"))
if M==1 or M==2 or M==3:
    print("first quarter")
elif M==4 or M==5 or M==6:
    print("Second quarter")
elif M==7 or M==8 or M==9:
    print("Third quarter")
elif M==10 or M==11 or M==12:
    print("fourth quarter")
elif M < 1 or M > 12:
    print("Error")