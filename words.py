#prints:
# HELO
# HEY
# GOODBYE
# YO
# YES

def print_upper_words2(arr):
    for words in arr:
        upper_case = words.upper()
        print(upper_case)


#----------------------------
#print_upper_words(["ello", "ey", "goodbye", "yo", "yes"])
#prints:  
# ELO
# EY

def print_upper_words3(arr):
    for words in arr:
        if words.startswith('E') or words.startswith('e'):
            print(words)

#----------------------------
#print_upper_words(["ello", "ey", "goodbye", "yo", "yes"])
#prints:  
           

def print_upper_words4(arr, set):
    for letter in set:
        for words in arr:
            if words.startswith(letter) or words.startswith(letter.upper()):
                print(words)



print_upper_words2(["hello", "hey", "goodbye", "yo", "yes"])
                #    must_start_with={"h", "y"})

print_upper_words3(["ello", "ey", "goodbye", "yo", "yes"])
                #    must_start_with={"h", "y"})

print_upper_words4(["hello", "hey", "goodbye", "yo", "yes"], ["h", "y"])

                   
