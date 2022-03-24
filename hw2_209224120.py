# Skeleton file for HW2 - Spring 2022 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.
# you can add new functions if needed.

# Change the name of the file to include your ID number (hw2_ID.py).
import random # loads python's random module in order to use random.random() in question 2

##############
# QUESTION 1 #
##############
#  Q1a
def divisors(n):
        
    return [ i for i in range(1,n+1//2) if n%i==0 ]

#  Q1b
def perfect_numbers(n):
    
    perfect_numbers_list = []
    i = 1
    
    while len(perfect_numbers_list) < n:
        
        if sum(divisors(i)) == i:
            perfect_numbers_list.append(i)
        i += 1
    return perfect_numbers_list

#  Q1c
def abundant_density(n):
    
    abundant_numbers = 0
    
    for i in range(1,n+1):
        if sum(divisors(i)) > i:
            abundant_numbers += 1
            
    return abundant_numbers/n

#  Q1e
def semi_perfect_4(n):

    count = 0
    left = n
    
    if sum(divisors(n)) >= n:
        for i in divisors(n)[::-1]:
            if left - i >= 0:
                count += 1
                left -= i
    return left == 0 and count == 4

##############
# QUESTION 2 #
##############
# Q2a
def coin():
    
    return random.random() < 0.5


# Q2b
def roll_dice(d):
    return int( random.random() * d ) + 1


# Q2c
def roulette(bet_size, parity):
    
    roll = roll_dice(37) - 1
    if roll == 0:
        return 0
    elif (roll % 2 == 0 and parity == "even") or (roll % 2 == 1 and parity == "odd"):
        return bet_size * 2
    else:
        return 0


# Q2d
def roulette_repeat(bet_size, n):

    profit = 0
        
    for i in range(n):
        
        if coin():
            parity = "even"
        else:
            parity = "odd"
            
        profit += roulette(bet_size, parity) - bet_size
        
    return profit
    
# Q2e
def shuffle_list(lst):

    card_deck = lst
    cards_number = len(card_deck)
    
    for i in range(cards_number):
        current_index = roll_dice(cards_number) - 1
        current_card = card_deck[current_index]
        card_deck.pop(current_index)
        card_deck.append(current_card)
    return card_deck   
    

##############
# QUESTION 3 #
##############
# Q3a
def inc(binary):
    binary_list = [x for x in binary[::-1]]
    for i in range(len(binary_list)):
        if binary_list[i] == "0":
            binary_list[i] = "1"
            break
        elif binary_list[i] == "1" and len(binary_list) - (i + 1) > 0:
            binary_list[i] = "0"
        else:
            binary_list[i] = "0"
            binary_list.append("1")
            
    return ''.join(binary_list[::-1])

# Q3b
def pad_rev_lists(bin1, bin2):
    pass  # replace with your code


def add(bin1, bin2):
    if len(bin1) >= len(bin2):
        binary = bin1
        add = bin2
    else:
        binary = bin2
        add = bin1
    binary_list = [x for x in binary[::-1]]
    add_list = [x for x in add[::-1]]

    ans = []
    carry = "0"

    for i in range(len(add_list)):
        if add_list[i] == "0" and binary_list[i] == "0" and carry == "0":
            ans.append("0")
        elif add_list[i] == "0" and binary_list[i] == "0" and carry == "1":
            ans.append("1")
            carry = "0"
        elif add_list[i] == "1" and binary_list[i] == "0" and carry == "0":
            ans.append("1")
        elif add_list[i] == "0" and binary_list[i] == "1" and carry == "0":
            ans.append("1")
        elif add_list[i] == "0" and binary_list[i] == "1" and carry == "1":
            ans.append("0")
        elif add_list[i] == "1" and binary_list[i] == "0" and carry == "1":
            ans.append("0")
        elif add_list[i] == "1" and binary_list[i] == "1" and carry == "0":
            ans.append("0")
            carry = "1"
        elif add_list[i] == "1" and binary_list[i] == "1" and carry == "1":
            ans.append("1")
            
    for i in range(len(add_list),len(binary_list)):
        if carry == "1" and binary_list[i] == "1":
            ans.append("0")
        elif carry == "1" and binary_list[i] == "0":
            ans.append("1")
            carry = "0"
        elif carry == "0" and binary_list[i] == "0":
            ans.append("0")
        elif carry == "0" and binary_list[i] == "1":
            ans.append("1")
            
    if carry == "1":
        ans.append("1")
                    
    return ''.join(ans[::-1])


# Q3c
def pow_two(binary, power):
    return binary + "0" * power


# Q3d
def div_two(binary, power):
    
    result = binary[:-power]
    
    if result == "":
        return "0"
    else:
        return result

# Q3e
def leq(bin1, bin2):
    return bin1 <= bin2


# Q3f
def to_decimal(binary):
    result = 0
    for i in range(len(binary)):
        print(result)
        if binary[-(i+1)] == "1":
            result += 2**i
    return result

##############
# QUESTION 4 #
##############
# Q4a
def lychrel_loops(n):

    count = 0
    while str(n) != str(n)[ : :-1]:
        n_reverse = int(str(n)[ : :-1])
        n = n + n_reverse
        count += 1
    return count

# Q4b
def is_lychrel_suspect(n, t):

    count = 0
    for i in range(t):
        n_reverse = int(str(n)[ : :-1])
        n = n + n_reverse
        count += 1
    return str(n) != str(n)[ : :-1]

# Q4c
def lychrel_sort(numbers, t):

    is_lychrel_suspect_dict = {}
    is_not_lychrel_suspect_dict = {}

    for number in numbers:
        is_suspect = True
        count = 0
        n = number
        while is_suspect and count < t:
            n_reverse = int(str(n)[ : :-1])
            n = n + n_reverse
            is_suspect = str(n) != str(n)[ : :-1]
            count += 1
            
        if is_suspect :
            is_lychrel_suspect_dict[number] = count
        else:
            is_not_lychrel_suspect_dict[number] = count

    is_lychrel_suspect_dict_sorted = dict(sorted(is_lychrel_suspect_dict.items(), key=lambda item: item[1]))
    is_not_lychrel_suspect_dict_sorted = dict(sorted(is_not_lychrel_suspect_dict.items(), key=lambda item: item[1]))
    
    is_lychrel_suspect_dict_sorted_keys = list(is_lychrel_suspect_dict_sorted)
    is_not_lychrel_suspect_dict_sorted_keys = list(is_not_lychrel_suspect_dict_sorted)

    return is_not_lychrel_suspect_dict_sorted_keys + is_lychrel_suspect_dict_sorted_keys

##############
# QUESTION 5 #
##############
# Q5a
def calculate_grades_v1(grades):
    
    calculated_grades_list = []
    for student_grades in grades:
        
        home_assignment_average = sum(student_grades[1]) / len(student_grades[1])

        if home_assignment_average > student_grades[0]:
            calculated_grades_list.append(0.9 * student_grades[0] + 0.1 * home_assignment_average)
        else:
            calculated_grades_list.append(student_grades[0])
            
    return(calculated_grades_list)

# Q5b
def calculate_grades_v2(grades, w, f):
    
    calculated_grades_list = []
    factor = f
    
    for student_grades in grades:

        student_test_grade = student_grades[0]
        student_test_grade_factor = factor(student_test_grade) 

        home_assignment_average = sum(student_grades[1]) / len(student_grades[1])

        final_grade = student_test_grade_factor * w + home_assignment_average * (1 - w)

        calculated_grades_list.append(final_grade)
                
    return calculated_grades_list
        
# Q5c_i
def calculate_grades_v3(grades, w):

    calculated_grades_list = []
    
    for student_grades in grades:

        student_test_grade = student_grades[0] 
        home_assignment_average = ( sum(student_grades[1]) - min(student_grades[1]) ) / 2
        final_grade = student_test_grade * w + home_assignment_average * (1 - w)

        calculated_grades_list.append(final_grade)

    return calculated_grades_list
# Q5c_ii
def calculate_w(grades, target_average):
    
    number_of_student = len(grades)

    test_grades_sum = 0
    home_assignment_grades_sum = 0
    
    for student_grades in grades:

        test_grades_sum += student_grades[0]
        home_assignment_grades_sum += ( sum(student_grades[1]) - min(student_grades[1]) ) / 2

    weight = ( ( target_average * number_of_student) - home_assignment_grades_sum ) / ( test_grades_sum - home_assignment_grades_sum )
    return weight

##########
# Tester #
##########

def test():
    if divisors(6) != [1, 2, 3] or divisors(7) != [1]:
        print("Error in Q1a")

    if perfect_numbers(2) != [6, 28]:
        print("Error in Q1b")

    if abundant_density(20) != 0.15:
        print("Error in Q1c")

    if not semi_perfect_4(20) or semi_perfect_4(28):
        print("Error in Q1e")

    for i in range(10):
        if coin() not in {True, False}:
            print("Error in Q2a")
            break

    for i in range(10):
        if roll_dice(6) not in {1, 2, 3, 4, 5, 6}:
            print("Error in Q2b")
            break

    for i in range(10):
        if (roulette(100, "even") not in {0, 200}) or (roulette(100, "odd") not in {0, 200}):
            print("Error in Q2c")
            break

    shuffled_list = shuffle_list([1, 2, 3, 4])
    for i in range(1, 5):
        if i not in shuffled_list:
            print("Error in Q2e")
            break

    if inc("0") != "1" or \
            inc("1") != "10" or \
            inc("101") != "110" or \
            inc("111") != "1000" or \
            inc(inc("111")) != "1001":
        print("Error in Q3a")

    if add("0", "1") != "1" or \
            add("1", "1") != "10" or \
            add("110", "11") != "1001" or \
            add("111", "111") != "1110":
        print("Error in Q3b")

    if pow_two("10", 2) != "1000" or \
            pow_two("111", 3) != "111000" or \
            pow_two("101", 1) != "1010":
        print("Error in Q3c")

    if div_two("10", 1) != "1" or \
            div_two("101", 1) != "10" or \
            div_two("1010", 2) != "10" or \
            div_two("101010", 3) != "101":
        print("Error in Q3d")

    if not leq("1010", "1010") or \
            leq("1010", "0") or \
            leq("1011", "1010"):
        print("Error in Q3e")

    if lychrel_loops(28) != 2 or lychrel_loops(110) != 1:
        print("Error in Q4a")

    if (not is_lychrel_suspect(28, 1)) or is_lychrel_suspect(28, 2) or is_lychrel_suspect(28, 3):
        print("Error in Q4b")

    if lychrel_sort([165, 164, 28, 110, 196], 8) != [110, 28, 165, 164, 196]:
        print("Error in Q4c")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    if calculate_grades_v1(grades) != [95, 90.4]:
        print("Error in Q5a")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    w = 0.7
    f = lambda x: min(100, x + 3)
    if calculate_grades_v2(grades, w, f) != [95.6, 93.3]:
        print("Error in Q5b")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    w = 0.7
    if calculate_grades_v3(grades, w) != [94.25, 91.8]:
        print("Error in Q5c_i")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    target_average = 93.025  # This is the average of [94.25, 91.8]
    if abs(calculate_w(grades, target_average) - 0.7) > 0.000001:
        print("Error in Q5c_ii")
test()
