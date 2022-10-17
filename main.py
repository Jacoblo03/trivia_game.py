quiz = { "question1": {"question" :"What is the capitol of the United states?" ,
"answer" : "Washington DC"},

"question2" :  {"question" :"How many inches are in 1 foot?" ,
"answer" : "12"},

"question3" :  {"question" :"How many bones are in the human body?" ,
"answer" : "206"},

"question4" :  {"question" :"What is the world's longest river called?" ,
"answer" : "Amazon"},

"question5" :  {"question" :"Which American president appears on the one dollar bill?" ,
"answer" : "George Washington"},

"question6" :  {"question" :"What is the largest ocean on earth?" ,
"answer" : "Pacific"},

"question7" :  {"question" :"How many colors are there in a rainbow?" ,
"answer" : "7"},

"question8" : {"question" :"How many days are there in a year?" ,
"answer" : "365"},

"question9" : {"question" :"How many continents are there?" ,
"answer" : "7"},
} 

score = 0 

for key, value in quiz.items():
    print(value['question'])
    answer = input('Answer: ')

    if answer.lower() == value["answer"].lower():
        print("Correct!")
        score = score + 1 
        print("Your score is: " + str(score))
        print()

    else:
        print('Wrong Answer!')
        print ("the answer is: " + value['answer'])
        print("Your score is: " + str(score))
        print()
        