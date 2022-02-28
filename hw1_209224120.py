#Skeleton file for HW1 - Spring 2022 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.
#you can add new functions if needed.

#Change the name of the file to include your ID number (hw1_ID.py).

#Question 4a
def replace(text, alphabet, new_alphabet):
    
    new_text = ""

    for i in range(len(text)):
        index = alphabet.find(text[i])
        if index != -1:
            new_text += new_alphabet[index]
        else:
            new_text += text[i]
    return new_text

#Question 4b
def is_pal(text):

    no_space_text = text.replace(" ", "")
    no_space_text_length = len(no_space_text)
    
    for i in range(no_space_text_length//2):
        if no_space_text[i] == no_space_text[-(i+1)]:
            continue
        else:
            return False
        
    return True


#Question 4c
def num_different_letters(text):
    chars = "abcdefghijklmnopqrstuvwxyz"
    chars_group = ""
    for char in text:
        if char in chars and char not in chars_group:
            chars_group += char
    return len(chars_group)

#Question 4d
def most_frequent(text):

    dictionary = {}

    for i in range(len(text)):   
        if text[i] in dictionary.keys():
            dictionary[text[i]] += 1
        else:
            dictionary[text[i]] = 1


    return max(dictionary, key = dictionary.get)
#Question 4e
def kth_order(text, k):
    
    dictionary = {}

    for i in range(len(text)):   
        if text[i] in dictionary.keys():
            dictionary[text[i]] += 1
        else:
            dictionary[text[i]] = 1

    dictionary = sorted(dictionary.items(), reverse=True, key=lambda x: x[1])
    
    return dictionary[k-1][0]
        

#Question 5
def calc(expression):

    expression = [ char for char in expression.split("'") if char != ""]
    current_expression = expression[0]
    
    for i in range(len(expression)):
        if expression[i] == "*":
            current_expression *= int(expression[i+1])
        elif expression[i] == "+":
            current_expression += expression[i+1]
        elif expression[i] == "-":
            current_expression = current_expression.replace(expression[i+1],"")

    return current_expression

########
# Tester
########

def test():
    #testing Q4
    if replace("hello world", "abcde fghijkl", "1234567890xyz") != "95zzo6worz4":
        print("error in replace - 1")
    if replace("abcd123", "1", "x") != "abcdx23":
        print("error in replace - 2")

    if not is_pal("go dog"):
        print("error in is_pal - 1")
    if is_pal("anda"):
        print("error in is_pal - 2")
        
    if num_different_letters("aa bb cccc dd ee fghijklmnopqrstuvwxyz") != 26:
        print("error in num_different_letters - 1")
    if num_different_letters("aaa98765432100000000") != 1:
        print("error in num_different_letters - 2")

    if most_frequent("abcdee") != "e":
        print("error in most_frequent - 1")
    if most_frequent("x11x22x33x") != "x":
        print("error in most_frequent - 2")

    if kth_order("aaaabbbccd", 3) != "c":
        print("error in kth_order - 1")
    if kth_order("abcdabcaba", 1) != "a":
        print("error in kth_order - 2")

    #testing Q5
    if calc("'123321'*'2'") != "123321123321":
        print("error in calc - 1")
    if calc("'Hi there '*'3'+'you2'") != "Hi there Hi there Hi there you2":
        print("error in calc - 2")
    if calc("'hi+fi'*'2'*'2'") != "hi+fihi+fihi+fihi+fi":
        print("error in calc - 3")
    if calc("'a'*'2'+'b'*'2'") != "aabaab":
        print("error in calc - 4")
    if calc("'a'*'2'+'b'*'2'-'b'") != "aaaa":
        print("error in calc - 5")
    if calc("'a'*'2'+'b'*'2'-'c'") != "aabaab":
        print("error in calc - 6")
