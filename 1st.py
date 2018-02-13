#Length in centimeter and convert it into meter & kilometer
centimeter = int(input("Enter length in centimeter: "))
print("Entered length is: ", str(centimeter)+ " cm")

meter = centimeter/100
kilometer = centimeter/100000

print("Converted length in meter: ", str(meter)+ " m")
print("Converted length in kilometer: ", str(kilometer)+ " km")
