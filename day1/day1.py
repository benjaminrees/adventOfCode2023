test_list =  ["1abc2",
"pqr3stu8vwx",
"a1b2c3d4e5f",
"treb7uchet"]

stringNumbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

stringDict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def getNumbers(number_list):
    res = 0
    for string in number_list:
        print(string)
        for letter in string:
            if letter.isnumeric():
                a = letter
                break

        for i in range(len(string) - 1, -1, -1):
            if string[i].isnumeric():
                b = string[i]
                break

        number = int(a + b)
        res += number

    return res

def getNumbers2(number_list):
    res = 0
    for string in number_list:

        ### FINDING THE FIRST NUMBER ###
        for i in range(0, len(string), 1):
            # find index of first individual number
            if string[i].isnumeric():
                a_index = i
                a = string[i]
                break

        # find index of first string number
        str_index = 0
        # for each number string
        for str_number in stringNumbers:
            # check if string is in big string
            # -1 if not found
            str_index = string.find(str_number)
            if str_index != -1:
                if str_index < a_index:
                    a = stringDict[str_number]
                    print(a)
                    a_index = str_index

        ## FINDING THE SECOND NUMBER ###
        for j in range(len(string) - 1, -1, -1):
            if string[j].isnumeric():
                b = string[j]
                b_index = j
                break

        str_index = 0
        for str_number in stringNumbers:
            # check if string is in big string
            # -1 if not found
            str_index = string.rfind(str_number)
            if str_index != -1:
                if str_index > b_index:
                    b = stringDict[str_number]
                    b_index = str_index


        number = (str(a) + str(b))
        res += int(number)

    return res

print(getNumbers2(content))

# iterate through loop and pick the first one that is valid
# check string for number. if not a number, check for letter. easier to return the first one
# then you have to do it backwards, or find the last one

# iterate and pick first numeral, then try again and find the first string. use the one with the lowest index
# do the same thing going backwards. easy to use "find" for string