def repeatedDigits():
    try:
        firstYear = int(input("Please input the first year inclusive: "))
        lastYear = int(input("Please input the last year inclusive: "))
    except ValueError:
        return("Please enter valid years.")


    if (firstYear < 0) or (lastYear < 0):
        return("Please enter valid years.")

    if firstYear > lastYear:
        return("Please ensure your first year is before your last year.")
    

    listOfYears = []
    year = firstYear

    repeatedDigitsYears = []

    while year <= lastYear:
        listOfYears.append(year)
        year += 1

    for number in listOfYears:
        listOfDigits = [int(i) for i in str(number)]
        
        length = len(listOfDigits)

        counter = 0
        while counter < length:
            num = listOfDigits[counter]
            if listOfDigits.count(num) > 1:
                repeatedDigitsYears.append(num)
                counter = length
            else:
                counter += 1
        
    numberOfYears = len(repeatedDigitsYears)

    return(f'There are {numberOfYears} years with repeated digits.')

print(repeatedDigits())
