from Classes import Sudoku

#ask coordinate
def xy():
    x = int(input("Put x coordinate:"))
    y = int(input("Put y coordinate:"))
    return x,y
        
#testing area
s = Sudoku()
s.timed()
while True:
    print("[1]Input Number")
    print("[2]Display Sudoku")
    print("[3]Erase Number")
    print("[4]Check Answer")
    print("[5]Make Test Sudoku")
    print("[6]Clear Sudoku")
    print("[7]Clear Answer")

    #ask for input
    user = input("Select:")
    #convert to string without making error
    try:
        user = int(user)
    except:
        break

    #check input for available method (wrong/empty will exit)
    match user:
        case 1: #Input
            x,y = xy()
            ans = int(input("Input answer:"))
            try:
                s.insert(x,y,ans)
                print("Inserted")
            except:
                print("Error")
        case 2: #Display
            print(s)
        case 3: #Delete
            x,y = xy()
            try:
                s.delete(x,y)
                print("Deleted")
            except:
                print("Error")
        case 4: #Check answer
            if s.correct():
                print("You Win")
                break
            else:
                print("Wrong")
        case 5: #make sudoku
            s.make_sudoku_copy()
            s.empty_random()
        case 6: #Clear Sudoku
            s.clear()
        case 7: #Clear Answer
            s.clear_answer()
        case 8:
            s.make_sudoku()
        case _: #exit
            break
s.timed()
print(s.display_time())