# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# ♥

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

letter_t = int( lower_case_name1.count("t") ) + int( lower_case_name2.count("t") )
letter_r = int( lower_case_name1.count("r") ) + int( lower_case_name2.count("r") )
letter_u = int( lower_case_name1.count("u") ) + int( lower_case_name2.count("u") )
letter_e = int( lower_case_name1.count("e") ) + int( lower_case_name2.count("e") )

total_true = letter_t + letter_r + letter_u + letter_e

letter_l = int( lower_case_name1.count("l") ) + int( lower_case_name2.count("l") )
letter_o = int( lower_case_name1.count("o") ) + int( lower_case_name2.count("o") )
letter_v = int( lower_case_name1.count("v") ) + int( lower_case_name2.count("v") )
letter_e = int( lower_case_name1.count("e") ) + int( lower_case_name2.count("e") )

total_love = letter_l + letter_o + letter_v + letter_e

love_score_word = str(total_true) + str(total_love)
love_score_num = int(love_score_word)

if love_score_num <= 10 or 90 <= love_score_num:
    print(f"Your score is {love_score_word}, you go together like coke and mentos.")
elif 40 <= love_score_num and love_score_num <= 50:
    print(f"Your score is {love_score_word}, you are alright together.")
else:
    print(f"Your score is {love_score_word}.")
