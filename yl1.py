print("Converting EEK into Euro")
EEK = float(input("Please enter amount of money you would like to convert into euro: "))

euro = round(EEK/15.6466,2) #This for caluclation
print("You will receive {0} Euros for your holiday.".format(euro))