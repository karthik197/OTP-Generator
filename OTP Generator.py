import math,random

digit="1234567890"
OTP=""
for i in range(5):
    OTP+=digit[math.floor(random.random()*10)]
print(OTP)