from random import randint as random_number_generator

leader_board_dict = {}
correct_answers = []
user_answers = []
lets_play = True


def number_input():
    try:
        global user_start_number 
        global user_end_number
        user_start_number = int(input("Please enter your start number: "))  #user inputs
        user_end_number = int(input("Please enter your end number: "))
        if user_end_number < user_start_number:
            print("Invaid input the second number must be less than the first, try again!")
            number_input()
    except ValueError:    # prevents entry of a float
        print("Please enter integers only, try again!" )
        number_input()

leader_board_dict = {}

def leader_board_sort(leader_board_dict):
    temp = []
    for key, val in leader_board_dict.items(): 
        temp.append([key] + [val]) 
    # We go through the list as many times as there are elements
    for i in range(len(temp)):
        # We want the last pair of adjacent elements to be (n-2, n-1) where n = length
        for j in range(len(temp) - 1):
            if temp[j][1] < temp[j+1][1]:
                # Swap
                temp[j][1], temp[j+1][1] = temp[j+1][1], temp[j][1]
    return temp


def leader_board(total_score): #allows user to input their score on leader board with custom name
    leader_board_dict.update({input("please enter your attempt name: "): total_score})
    print("This list is sorted from best to worse! Where are you?")
    print(leader_board_sort(leader_board_dict))
    
    
def empty_answer_lists(): #resets lists and variables so they can be used repeatdly for each call
    global correct_answers
    global user_answers 
    global game_score
    correct_answers = []
    user_answers = []
    game_score = 0


def sort_score_array(list_of_scores):
    score_array = list_of_scores
     # We go through the list as many times as there are elements
    for i in range(len(score_array)):
        # We want the last pair of adjacent elements to be (n-2, n-1) where n = length
        for j in range(len(score_array) - 1):
            if score_array[j] < score_array[j+1]:
                # Swap
                score_array[j], score_array[j+1] = score_array[j+1], score_array[j]
    return score_array

def play_3_games(): #tringgered if the user plans to play three games
        global practice_type
        global game_score
        global score_array
        total_score = 0
        score_array = []
        
        if game_score == None: #thhese control flow statements total up each round and prevent errors due to ans == Null
            game_score = 0
            total_score += game_score 
            score_array.append(game_score)  
        else:
            total_score += game_score 
            score_array.append(game_score)
        practice_type = input("what would you like to practice now? ") #ask for practice type
        empty_answer_lists()
        game_2 = play() #Calls for a new ame to be played which depends on the value of practice type as to what type of game
        if game_2 == None:
            game_2 = 0
            total_score += game_2 
            score_array.append(game_2)  
        else:
            total_score += game_2 
            score_array.append(game_2)
        practice_type = input("what would you like to practice now? ")
        empty_answer_lists()
        game_3 = play()
        if game_3 == None:
            game_3 = 0
            total_score += game_3 
            score_array.append(game_3)  
        else:
            total_score += game_3 
            score_array.append(game_3)
        score_array = sort_score_array(score_array) #sorts scores from best to worse and prints it from code below
        print("You best score was " + str(score_array[0]) + " then " + str(score_array[1]) + " and lastly " + str(score_array[2]) + " was your worst." )
        leader_board(total_score) #adss total of the three attemps to leader board dict


def user_score(correct_answer, user_answers): #called by division_func to total users score 
    score = 0
    for i in range (5):
        if correct_answer[i] == user_answers[i]:
            print("You got " + str(i+1) + " question right")
            score = score + 1
        else:
            print("You got " + str(i) + " question wrong")
    global game_score
    game_score = score #keeps track of score so it can be totaled for leaderboard in play_3_games()
    print("You got " + str(score) + " of the questions right!") #prints the total score for te round
    

def division_func(start_number, end_number): #recursive fucntion which calls its self 5 time to provide 5 questions to the user
    if len(user_answers) >= 5: #recursive break case
        user_score(correct_answers, user_answers)
    else:
        temp1 = random_number_generator(start_number,end_number) #random number enerator functions
        temp2 = random_number_generator(start_number,end_number)
        try:
            user_answers.append(float(input("what is the answer to " + str(temp1) + " / " + str(temp2) + " to 3 s.f. ? ")))
            correct_answers.append(round(float((temp1/temp2)), 3))
            division_func((start_number + random_number_generator(0,5)), (end_number + random_number_generator(0,5))) #recursive case
        except: #error handling
            print("try again invalid input")
            division_func(start_number, end_number)
    
    

def multiplication_func(start_number, end_number):
    if len(user_answers) >= 5:
        user_score(correct_answers, user_answers)
    else:
        temp1 = random_number_generator(start_number,end_number)
        temp2 = random_number_generator(start_number,end_number)
        try:
            user_answers.append(float(input("what is the answer to " + str(temp1) + " * " + str(temp2) + " to 3 s.f. ? ")))
            correct_answers.append(round(float((temp1*temp2)), 3))
            multiplication_func((start_number + 5), (end_number + 5))
        except:
            print("try again invalid input")
            multiplication_func(start_number, end_number)

def play(): #main menu function
    global practice_type 
    global game_score
    if practice_type == "Division" or practice_type == "division" or practice_type == "/":
        print("We will now practice division ;)")
        empty_answer_lists() #Emptys answer lists so we can use same arrays to count each game
        number_input() #Asks user for number inputs viva calling the fuction
        division_func(user_start_number, user_end_number) #Inputs the gobal inout varibales taken on last line into te divison function
        return game_score #return score
        
    #operates same as divison
    elif practice_type == "Multiplication" or practice_type == "multiplication" or practice_type == "*": #operates same as divison 
        print("We will now do multiplication ;)")
        empty_answer_lists()
        number_input()
        multiplication_func(user_start_number, user_end_number)
        return game_score
    elif practice_type == "scoreboard" or practice_type == "Scoreboard" or practice_type == "s" or practice_type == "S":
        print(leader_board_sort(leader_board_dict))
    #error handleing
    else:
        print("Enter a valid game mode! ")
        practice_type = input("what would you like to practice today? ")
        play()

def play_again():
    global lets_play
    global practice_type
    user_play_again = input("Would you like to play again? y/n ")
    if user_play_again == "y" or user_play_again == "yes" or user_play_again == "Y" or user_play_again == "Yes":
        lets_play = True
    else:
        practice_type = input("Type S to see current score board: ") # allows user to see score board
        if practice_type == "scoreboard" or practice_type == "Scoreboard" or practice_type == "s" or practice_type == "S":
            play()
            play_again()
        else: 
            lets_play = False
            

while lets_play == True: #main loop for game
    lets_play = False #prevents infinte game loop
    practice_type = input("what would you like to practice today? ") #user inputs game type to be used in play()
    
    play() # calls play fuction to start game 
    #gives optiton for user to play 3 games 
    play_for_leaderboard = input("You have finished would you like to play 2 more times and enter the leader board? y/n ")
    if play_for_leaderboard == "y" or play_for_leaderboard == "yes" or play_for_leaderboard == "Y" or play_for_leaderboard == "Yes":
        play_3_games()
    #Asks user to play again
    play_again()
        