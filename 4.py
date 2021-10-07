print (' Enter Your Weight ')
Weight = float(input())
print(' Enter Your Height ')
Height = float(input())
BMI= Weight / (Height * Height)
print(' BMI Is ',BMI)
if BMI < 18.5:
    print(' UnderWeight ')
elif BMI >= 18.5 and BMI <= 24.9:
    print(' Normal ')
elif BMI>24.9 and BMI <=29.9:
    print(' OverWeight ')
elif BMI>29.9 and BMI <=34.9:
    print(' Obese ')
elif BMI>34.9 :
    print(' Extremely Obese ')