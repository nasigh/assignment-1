print ('Enter The 3 Sides Of The Triangle')
Side_A=int(input())
Side_B=int(input())
Side_C=int(input())
if Side_A + Side_B > Side_C :
    if Side_A + Side_C > Side_B :
        if Side_B + Side_C > Side_A :
            print('Yes')          
else:
    print('No')