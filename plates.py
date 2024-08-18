def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)
    if length > 6 or length < 2:
        return False
    first_two = s[:2]
    return_digit= False
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0' or not s[i:].isdigit():
                return False
            return_digit= True
            break
    if s[i].isalpha():
            return_digit= True

    if not first_two.isalpha():
        return False
    for letter in s:
        if not letter.isalnum():
            return False
    return return_digit

if __name__ == "__main__":
    main()
