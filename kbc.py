#exercise 03 of 100daysofpython
print(">>>>>>>>>>  Welcome To KBC")
questions=[
    ["Who is the Prime Minister of India ?","Narendra Modi","Rahul Gandhi","Arvind Kejriwal","Manmohan singh","a"],
    ["Who creates Python Language ?","Charls babbage","Guido van russom","harry","tim burners lee","a"],
    ["In which year covid-19 ocuurs ?","2021","2019","2020","2024","c"],
    ["Who is the founder of Microsoft ?","Bill gates","Steve jobs","Mark zuckerberg","Dolly Chai Wala","a"]
]
levels=[10000,20000,30000,40000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print("\nQuestion for rs",levels[i])
    print(question[0])
    print(f"a. {question[1]}          b. {question[2]} ")
    print(f"c. {question[3]}          d. {question[4]} ")
    reply=(input("\nEnter your choice otherwise quit : "))
    if (reply=="quit"):
        print("You Quit")
        money=levels[i-1]
        break
    if(reply==question[-1]):
        print("\nCorrect Answer you won rs",levels[i])
        if(i==2):
            money=30000
        elif(i==3):
            money=40000
    else:
        print("Wrong Answer")
        break
print("You are going with rs",money)
