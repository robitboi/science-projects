#The following program is used to take the user data based on information that may be useful in a lab for Biology or Chemistry
#Then the users data is displayed at the end
#To run the code, click the arrow (play) button in the top right. From there all the user needs to do is input the data when prompted
#The user must press enter to continue to the next question

#This is the dictionary that stores all the keys and values for the code
main_line = { 
    "dictA" : {
    "time": 0,
    "pH": float,
    "color": str,
    "smell": str,
    "temp": float 
    }
    ,
    "dictB" : {
    "time": 0,
    "pH": float,
    "color": str,
    "smell": str,
    "temp": float 
    }
    ,
    "dictC" : {
    "time": 0,
    "pH": float,
    "color": str,
    "smell": str,
    "temp": float 
    }
    ,


}

#This array makes it easier to call back the nested dictionaries later
dictionary_keys = ["dictA", "dictB", "dictC"]

#This loop goees through the number of nested dictionaries and asked for the users information
#I added a while loop here to make it easier for the code to loop or stop based on the users input
incriment = 0
while True:
    keys = dictionary_keys[incriment]
    set_time = int(input("\nWhat time are you checking the solution? (in minutes): "))
    main_line[keys]["time"] = set_time
    set_ph = float(input("What is the pH of the solution?: "))
    main_line[keys]["pH"] = set_ph
    set_color = input("What is the color of the solution?: ")
    main_line[keys]["color"] = set_color
    set_smell = input("What does the solution smell like?: ")
    main_line[keys]["smell"] = set_smell
    set_temp = float(input("What is the temp of the solution?: "))
    main_line[keys]["temp"] = set_temp
    
    move_on = input("\n Would you like to move on?(Yes/No): ")
    
    if move_on.lower() == "no":
        print("Thank you for using the science lab program!")
        break
    incriment = incriment + 1
    
for i in list(main_line.values()):
    print("  - " + i)