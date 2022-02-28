
def max_even_seq(n):
    
    counter = 0
    current_counter = 0
    
    while (n//10 != 0) or (n != 0):
        
        if n%2 == 0:
            current_counter += 1
        else:   
            current_counter = 0
            
        if current_counter > counter:
            counter = current_counter
            
        n = n//10
    return counter

########
# Tester
########

def test():
    if max_even_seq(23300247524689) != 4:
        print("error in max_even_seq")
