import random

Food = {
    "What is the main ingredient in guacamole?":"Avocado",
    "Which fruit has its seeds on the outside?" : "Strawberry",
    "Samosa is originally from which country?" : "India",
    "What spice gives curry its yellow color?" : "Turmeric",
    "Sushi is a traditional food from which country?" : "Japan",
    "Which nut is used to make marzipan?" : "Almond",
    "What is tofu made from?" : "Soybeans",
    "Which cheese is traditionally used in pizza?" : "Mozzarella",
    "What is the world’s most consumed beverage after water?" : "Tea",
    "Which fruit is known as the 'king of fruits'?" : "Durian"
}

Tollywood = {
    "Who played Baahubali in the movie?": "Prabhas",
    "Who is known as the 'Mega Star' of Tollywood?": "Chiranjeevi",
    "Which movie won the National Award for Best Feature Film in Telugu in 2016?": "Pelli Choopulu",
    "Who directed the movie 'Arjun Reddy'?": "Sandeep Reddy Vanga",
    "Which actor is called 'Power Star'?": "Pawan Kalyan",
    "Who played the female lead in 'Magadheera'?": "Kajal Aggarwal",
    "Which Tollywood movie is about reincarnation and revenge?": "Magadheera",
    "Who is the music director of 'Rangasthalam'?": "Devi Sri Prasad",
    "Which movie featured a 100-minute long climax action scene?": "Eega",
    "Which film’s tagline was 'Mind It!'?": "Gabbar Singh"
}

Cricket = {
    "Who is known as the 'God of Cricket'?": "Sachin Tendulkar",
    "Which country won the first-ever Cricket World Cup?": "West Indies",
    "What is the maximum number of runs a batsman can score in a single ball?": "6",
    "Who has the fastest century in ODI cricket?": "AB de Villiers",
    "Which bowler is nicknamed the 'Prince of Swing'?": "James Anderson",
    "Which country hosted the 2019 Cricket World Cup?": "England & Wales",
    "Who holds the record for most wickets in Test cricket?": "Muttiah Muralitharan",
    "Which cricketer is called 'Captain Cool'?": "MS Dhoni",
    "What is a 'duck' in cricket?": "Scoring 0 runs",
    "Who hit the winning six in the 2011 World Cup final?": "MS Dhoni"
}

GeneralKnowledge = {
    "What is the largest planet in our solar system?": "Jupiter",
    "Who invented the telephone?": "Alexander Graham Bell",
    "What is the capital of Australia?": "Canberra",
    "How many continents are there?": "7",
    "Which is the fastest land animal?": "Cheetah",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the smallest prime number?": "2",
    "Which element has the chemical symbol 'O'?": "Oxygen",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the tallest mountain in the world?": "Mount Everest"
}

print("Hello! welcome to trivia adventure\n")
username = input("Please Enter your name: ")
print("Heyyyy ",username,"thats a nice name")

userInput = 0

while(userInput != 5):
    score = 0
    
    print("\nPlease select a field you are interested to give quiz!")
    print("press '1' for Food")
    print("press '2' for Tollywood Movies")
    print("press '3' for Cricket")
    print("press '4' for General knowledge")
    print("press '5' to Exit")
    userInput = int(input("Enter your choice: "))

    if userInput == 1:
        print("You have choosed Food")
        questions = random.sample(list(Food.keys()), 8)

        for q in questions:
            print(q)
            ans = input("Enter your answer: ")
            if ans.strip().lower() == Food[q].lower():
                score += 1
                print("Your answer is correct!")
            else:
                print("Sorry thats incorrect! ,Correct answer is", Food[q])

        print("Your score:", score)
        print("if you want to play again press 'yes' or you want exit press 'no'")
        uchoice = input("Enter your choice: ")
        if uchoice.lower() == "yes":
            continue
        else:
            print("Thanks for playing! bye bye")
            break

    if userInput == 2:
        print("You have choosed Tollywood Movie")
        questions = random.sample(list(Tollywood.keys()), 8)

        for q in questions:
            print(q)
            ans = input("Enter your answer: ")
            if ans.strip().lower() == Tollywood[q].lower():
                score += 1
                print("Your answer is correct!")
            else:
                print("Sorry thats incorrect! ,Correct answer is", Tollywood[q])

        print("Your score:", score)
        print("if you want to play again press 'yes' or you want exit press 'no'")
        uchoice = input("Enter your choice: ")
        if uchoice.lower() == "yes":
            continue
        else:
            print("Thanks for playing! bye bye")
            break

    if userInput == 3:
        print("You have choosed Cricket")
        questions = random.sample(list(Cricket.keys()), 8)

        for q in questions:
            print(q)
            ans = input("Enter your answer: ")
            if ans.strip().lower() == Cricket[q].lower():
                score += 1
                print("Your answer is correct!")
            else:
                print("Sorry thats incorrect! ,Correct answer is", Cricket[q])

        print("Your score:", score)
        print("if you want to play again press 'yes' or you want exit press 'no'")
        uchoice = input("Enter your choice: ")
        if uchoice.lower() == "yes":
            continue
        else:
            print("Thanks for playing! bye bye")
            break

    if userInput == 4:
        print("You have choosed General Knowledge")
        questions = random.sample(list(GeneralKnowledge.keys()), 8)

        for q in questions:
            print(q)
            ans = input("Enter your answer: ")
            if ans.strip().lower() == GeneralKnowledge[q].lower():
                score += 1
                print("Your answer is correct!")
            else:
                print("Sorry thats incorrect! ,Correct answer is", GeneralKnowledge[q])

        print("Your score:", score)
        print("if you want to play again press 'yes' or you want exit press 'no'")
        uchoice = input("Enter your choice: ")
        if uchoice.lower() == "yes":
            continue
        else:
            print("Thanks for playing! bye bye")
            break
