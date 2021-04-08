Wght = float(input("Enter Weight: "))
Hght = float(input("Enter Height: "))

BMI = (Wght * Wght)/Hght

if BMI < 18.5:
    print("Under")
elif 18.5 <= BMI <= 24.9:
    print("Normal")
elif 25 <= BMI <= 29.9:
    print("Over")
elif 30 <= BMI <= 34.9:
    print("Fat ")
elif BMI >= 35:
    print("Very Fat")
