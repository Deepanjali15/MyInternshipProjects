#Conversion of Length Units:
def length_conv(s_unit, t_unit, ivalue):
    #formula for meter to ft:
    m_to_ft=3.28084

    #Error handling:
    if s_unit.lower() not in ["m", "ft"] or t_unit.lower() not in ["m", "ft"]:
        raise ValueError("Unsupported units. Please use 'm' or 'ft'.")
    #Meter to Feet
    if s_unit=="m":
        ovalue= ivalue*m_to_ft
    #Feet to Meter
    else:
        ovalue= m_to_ft/ivalue

    # Output
    return ovalue

#Conversion of Temperature Units:
def temp_conv(s_unit, t_unit, ivalue):

    #Error handling:
    if s_unit.lower() not in ["c", "f"] or t_unit.lower() not in ["c", "f"]:
        raise ValueError("Unsupported units. Please use 'c' or 'f'.")
    #Celsius to Fahrenheit
    if s_unit=="c":
        ovalue= (ivalue* (9/5))+32
    #Fahrenheit to Celsius
    else:
        ovalue= (ivalue -32)*(5/9)

    # Output
    return ovalue

#Conversion of Weight Units:
def weight_conv(s_unit, t_unit, ivalue):
    #formula for kg to pound:
    kg_to_pound= 2.20462

    #Error handling:
    if s_unit.lower() not in ["kg", "pound"] or t_unit.lower() not in ["kg", "pound"]:
        raise ValueError("Unsupported units. Please use 'kg' or 'pound'.")
    #Kilogram to pounds
    if s_unit=="kg":
        ovalue= ivalue*kg_to_pound
    #Pounds to Kilogram
    else:
        ovalue= kg_to_pound/ivalue

    # Output
    return ovalue

#Main Program
print("UNIT CONVERTOR\n")
print("1.Length unit conversion")
print("2.Temperature unit conversion")
print("3.Weight unit conversion")
choice=int(input("Enter your choice(1-3): "))
if choice==1:
    s_unit=input("enter the source unit(m/ft): ")
    t_unit=input("enter the target unit(ft/m): ")
    ivalue=float(input("Enter the value in source unit: "))
    #function calling
    req_value=length_conv(s_unit, t_unit, ivalue)
    print("{:.3f} {} = {:.3f} {} ".format(ivalue, s_unit, req_value, t_unit))
if choice==2:
    s_unit=input("enter the source unit(C/F): ")
    t_unit=input("enter the target unit(F/C): ")
    ivalue=float(input("Enter the value in source unit: "))
    #function calling
    req_value=temp_conv(s_unit, t_unit, ivalue)
    print("{:.3f} {} = {:.3f} {} ".format(ivalue, s_unit, req_value, t_unit))
if choice==3:
    s_unit=input("enter the source unit(kg/pound): ")
    t_unit=input("enter the target unit(pound/kg): ")
    ivalue=float(input("Enter the value in source unit: "))
    #function calling
    req_value=weight_conv(s_unit, t_unit, ivalue)
    print("{:.3f} {} = {:.3f} {} ".format(ivalue, s_unit, req_value, t_unit))
