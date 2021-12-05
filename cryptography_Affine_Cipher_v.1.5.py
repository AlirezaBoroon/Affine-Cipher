def coprime_inspector_fun (a): #the main reason and motivation for making this function is to have a bigger list of symbols on the keyboard.
    a_divisors= []
    for i in range (2, a+1):
        if a%i== 0:
            a_divisors.append(i)
    _101_divisors= [101]
    for i in range (0, len(_101_divisors)):
        for j in range (0, len(a_divisors)):
            if a_divisors[j]== _101_divisors[i]:
                return 0
    return 1
def t2c_converting_fun(strL, a, b):
    # Here we  have introduced the space between letters, so it's a letter itself in encrypted cipher text.
    alphabet= [" ", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "–", "-", "_", "=", "+", "[", "]", "{", "}", "\\", "|", ";", ":", "‘", "'", "\"", "“", ",", ".", "/", "<", ">", "?", "£", "¢", "€", "¥", "∞", "§", "¶", "™", "©", "®", "º", "≠", "≈", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Calphabet= ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    alphabetindexes= ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]
    strL2indexes= []
    #for unknown characters we make a list for them to introduce to the user to not type them again in the future:
    unknownchar= []
    for i in range (0, len(strL)):
        flag= 0
        for j in range (0, len(alphabet)):
            if alphabet[j]== strL[i]:
                flag= 1
                strL2indexes.append(j)
        if flag==0:
            unknownchar.append(strL[i])
    if len(strL)!= len(strL2indexes):
        print("Error, you typed unknown character(s), that is (they are) as follows:")
        print(unknownchar)
        return 0
    converted_numeric_list= []
    for i in range (0, len(strL2indexes)):
        n= (a*strL2indexes[i])+b
        while n> 100:
            n= n- 101
        converted_numeric_list.append(n)
    converted_letter_list= []
    for i in range (0, len(converted_numeric_list)):
        converted_letter_list.append(alphabet[converted_numeric_list[i]])
    return converted_letter_list
def c2t_converting_fun(strL, a, b):
    alphabet= [" ", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "–", "-", "_", "=", "+", "[", "]", "{", "}", "\\", "|", ";", ":", "‘", "'", "\"", "“", ",", ".", "/", "<", ">", "?", "£", "¢", "€", "¥", "∞", "§", "¶", "™", "©", "®", "º", "≠", "≈", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Calphabet= ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    alphabetindexes= ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]
    strL2indexes= []
    for i in range (0, len(strL)):
        for j in range (0, len(alphabet)):
            if alphabet[j]== strL[i]:
                strL2indexes.append(j)
    converted_numeric_list= []
    for i in range (0, len(strL)):
        while True:
            n= (strL2indexes[i]- b)/ a #in python the counting starts from zero and the zero should be among the counter numbers, but in dividation process, zero is sensitive, so we should have a special empty space for that!.
            if n>= 1 or n== 0.0:
                break
            else:
                strL2indexes[i]+= 101
        if n!= 0.0:
            while n/ int(n)!= 1.0 :
                strL2indexes[i]+= 101
                n= (strL2indexes[i]- b)/ a
        converted_numeric_list.append(int(n))
    converted_letter_list= []
    for i in range (0, len(converted_numeric_list)):
        converted_letter_list.append(alphabet[converted_numeric_list[i]])
    return converted_letter_list
def main1_enc ():
    print("Welcome to the encryption part:")
    print("The encryption in Affine cipher algorithm is subsitution cipher, so we need number 'a' for having a Coefficient for every letter and also number 'b' for shifting.")
    print("The operation is: EncryptedLetter= a. i_(x)+ b")
    print("So Please enter your string first, for encryption process:")
    string= input()
    strL= list(string)
    print("Now please enter the number : a (The number 'a' should be coprime with number 101") # coprime with number 101 means that the number a shouldn't be only 101, 'cause number 101 is a prime number.
    while True:
        a= int(input())
        if coprime_inspector_fun(a)== 0:
            print("The number 'a' should be coprime with number 101, try re-enter the number")
        else:
            break
    print("Now please enter the number : b")
    b= int(input())
    Affine_ciphered_list= t2c_converting_fun(strL, a, b)
    if Affine_ciphered_list== 0:
        print("And your entered text is:")
        textt= ""
        for i in range (0, len(strL)):
            textt+= strL[i]
        print(textt)
        return
    else:
        ciphered_string= ""
        for i in range (0, len(Affine_ciphered_list)):
            ciphered_string+= Affine_ciphered_list[i]
        print("The encrypted text is:", ciphered_string)
        return
    return
def main2_dec ():
    print("Welcome to the decryption part:")
    print("The decryption in Affine cipher algorithm is subsitution cipher, so we need number 'a' for having a Coefficient for every letter and also number 'b' for shifting.")
    print("The operation is: DecryptedLetter= (i_(x)- b)/ a")
    print("So Please enter your encrypted string first, for decryption process:")
    string= input()
    strL= list(string)
    print("Now please enter the number : a")
    while True:
        a= int(input())
        if coprime_inspector_fun(a)== 0:
            print("The number 'a' should be coprime with number 101, try re-enter the correct number!!")
        else:
            break
    print("Now please enter the number : b")
    b= int(input())
    decrypted_list= c2t_converting_fun(strL, a, b)
    decrypted_string= ""
    for i in range (0, len(decrypted_list)):
        decrypted_string+= decrypted_list[i]
    print("The decrypted text is:", decrypted_string)
    return
# start0:
print("Hello, This application is used for Substitution cipher, called Affine cipher.")
while True:
    print("Please enter what you want. Encryption (1) / Decryption (2) / *end of program* (0)")
    c= int(input())
    if c== 1:
        main1_enc()
    elif c== 2:
        main2_dec()
    elif c== 0:
        break
print("Good bye, see you next time.")
