hrs=int(input("Enter a Hrs= "))
min=int(input("Enter a Min= "))

hrs_angle= (hrs % 12)* 30 + min * 0.5
minute_angle= min * 6

angel = abs(hrs_angle - minute_angle)

if angel > 180:
    angle= 360 -angel

print("smaller angle= ",angel,'degrees')

