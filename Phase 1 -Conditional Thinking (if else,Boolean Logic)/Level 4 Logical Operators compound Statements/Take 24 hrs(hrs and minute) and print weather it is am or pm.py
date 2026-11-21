hrs = int(input("Enter hours (0-23): "))
minute = int(input("Enter minutes (0-59): "))

if hrs < 0 or hrs > 23 or minute < 0 or minute > 59:
    print("Invalid time")
elif hrs < 12:
    print(hrs, ":", minute, "- AM")
else:
    print(hrs, ":", minute, "- PM")