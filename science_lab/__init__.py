main_line = { 
    "dictA" : {
    "time": int,
    "pH": float,
    "color": str,
    "smell": str,
    "temp": float 
    }
    ,
    "dictB" : {
    "time": int,
    "pH": float,
    "color": str,
    "smell": str,
    "temp": float 
    }
    ,
    "dictC" : {
    "time": int,
    "pH": float,
    "color": str,
    "smell": str,
    "temp": float 
    }

}

dictionary_keys = ["dictA", "dictB", "dictC"]

for i in range(len(dictionary_keys)):
    keys = dictionary_keys[i]
    set_time = int(input("What time are you checking the solution? (in minutes): "))
    main_line[keys]["time"] = set_time
    set_ph = float(input("What is the pH of the solution?: "))
    main_line[keys]["pH"] = set_ph
    set_color = input("What is the color of the solution?: ")
    main_line[keys]["color"] = set_color
    set_smell = input("What does the solution smell like?: ")
    main_line[keys]["smell"] = set_smell
    set_temp = float(input("What is the temp of the solution?: "))
    main_line[keys]["temp"] = set_temp

    
print("\nDictionary = \n", main_line)






