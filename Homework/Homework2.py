#part 1
attemps = 0
while attemps < 3:
    try:
        age =  int(input('Age: '))
    except ValueError:
        print("Invalid valid. Try again")
        attemps +=1
        continue
    if age >= 18:
        print("You are a grown up!")
    else:
        print("You are a child!")

    break

if attemps == 3:
    print("Maximum attemps exceeded. Please try again later!")





