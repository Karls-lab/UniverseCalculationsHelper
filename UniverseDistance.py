# A program that uses the inverse square law to calculate distance 

import math 

def parsecToLightYear(parsec):
    return parsec * 3.26

def parsecToMeter(parsec):
    return parsec * (3.09 * pow(10, 16))

def lightYearToMeter(lightYear):
    return lightYear * (9.46 * pow(10, 15))

def meterToNanoMeter(meter):
    return meter * (1 * pow(10, 9))

def meterToParsec(meter):
    return meter / (3.09 * pow(10, 16))

def convertDistanceToMeters(distance, unit):
    if unit == "ly":
        return lightYearToMeter(distance)
    if unit == "parsec":
        return parsecToMeter(distance)
    if unit == "nm":
        return meterToNanoMeter(distance)
    if unit == "m":
        return distance
    
def handelLuminosityPower(luminosity, power):
    return luminosity * pow(10, power)

def main():
    print("d) Distance \n")
    print("f) Flux W/m^2 \n")
    print("l) Luminosity W \n")
    choice = input("please make a choice: \n")

    if choice == "d":
        flux = float(input("Enter Flux: "))
        luminosity_num = float(input("Enter Luminosity: "))
        luminosity_power = int(input("Enter Luminosity Power: "))
        luminosity = handelLuminosityPower(luminosity_num, luminosity_power)
        distance = math.sqrt(luminosity / (4 * math.pi * flux))
        print("Distance in meters: ", distance)
        print("Distance in light years: ", parsecToLightYear(distance))
        print("Distance in parsecs: ", meterToParsec(distance))

    elif choice == "f":
        distance = float(input("Enter Distance: "))
        distance_units = input("Enter Distance Units: ")
        meters = convertDistanceToMeters(distance, distance_units)
        luminosity = float(input("Enter Luminosity: "))
        luminosity_power = int(input("Enter Luminosity Power: "))
        luminosity = luminosity * pow(10, luminosity_power)
        flux = luminosity / (4 * math.pi * pow(meters, 2))
        print("Flux: ", flux)

    elif choice == "l":
        distance = float(input("Enter Distance: "))
        distance_units = input("Enter Distance Units: ")
        meters = convertDistanceToMeters(distance, distance_units)
        flux = float(input("Enter Flux: "))
        luminosity = flux * (4 * math.pi * pow(meters, 2))
        print("Luminosity: ", luminosity)


if __name__ == "__main__":
    main()