
# Health management system

def gettime():
    import datetime
    return datetime.datetime.now()


name = int(input("Enter a 1 for Harry\nEnter 2 for Rohan\nEnter 3 for Hammid\n"))
if name==1:
    print("You Selected harry")
    LR = int(input("What you have to do\n1 for Lock\n2 for retrive\n"))
    if LR==1:
        print("You selected Lock option")
        EF = int(input("What you've to lock\n1 for Exercise\n2 for Food\n"))
        if EF==1:
            print("You Selected Exercise")
            t1 = open("Harry Exercise.txt" , ("a"))
            exercise1= input("Enter which exercise you completed now\n")
            datee1 = input("Enter todays date in the format of DD-MM-YYYY\n")
            timee1 = input("Enter the time\n")
            t1.write(datee1)

            t1.write(" ")
            t1.write(timee1)
            t1.write("-")
            t1.write(exercise1)
            t1.write("   ")
            t1.close()
            print("Registered Successfully")
            #Harry's exercise Succesfully

        if EF==2:
            print("You selected Food")
            t2 = open("Harry Food.txt" , ("a"))
            food1 = input("Enter which Food item you ate\n")
            datee2 = input("Enter todays date in the format of DD-MM-YYYY\n")
            timee2 = input("Enter the time\n")
            t2.write(datee2)
            t2.write(" ")
            t2.write(timee2)
            t2.write("-")
            t2.write(food1)
            t2.write("   ")
            t2.close()
            print("Registered Successfully")
            #Harry's food registered succesfully

    if LR==2:
        print("You selected retrive")
        EF1 = int(input("What you've to lock\n1 for Exercise\n2 for Food\n"))
        if EF1==1:
            print("You selected Exercise option")
            print("This is your result:\n\t")
            t3 = open("Harry Exercise.txt")
            content1 = t3.read()
            print(content1)
            #Harry Exercise retrive Successfully

        if EF1==2:
            print("You selected Food option")
            print("This is your result:\n\t")
            t4 = open("Harry Food.txt")
            content2 = t4.read()
            print(content2)
            # Harry Food retrive Successfully


if name==2:
    print("You selected Rohan")
    LR = int(input("What you have to do\n1 for Lock\n2 for retrive\n"))
    if LR == 1:
        print("You selected Lock option")
        EF = int(input("What you've to lock\n1 for Exercise\n2 for Food\n"))
        if EF == 1:
            print("You Selected Exercise")
            t1 = open("Rohan Exercise.txt", ("a"))
            exercise1 = input("Enter which exercise you completed now\n")
            datee1 = input("Enter todays date in the format of DD-MM-YYYY\n")
            timee1 = input("Enter the time\n")
            t1.write(datee1)
            t1.write(" ")
            t1.write(timee1)
            t1.write("-")
            t1.write(exercise1)
            t1.write("   ")
            t1.close()
            print("Registered Successfully")
            # Rohan exercise Succesfully

        if EF == 2:
            print("You selected Food")
            t2 = open("Rohan Food.txt", ("a"))
            food1 = input("Enter which Food item you ate\n")
            datee2 = input("Enter todays date in the format of DD-MM-YYYY\n")
            timee2 = input("Enter the time\n")
            t2.write(datee2)
            t2.write(" ")
            t2.write(timee2)
            t2.write("-")
            t2.write(food1)
            t2.write("   ")
            t2.close()
            print("Registered Successfully")
            # Rohan food registered succesfully

    if LR==2:
        print("You selected retrive")
        EF1 = int(input("What you've to lock\n1 for Exercise\n2 for Food\n"))
        if EF1==1:
            print("You selected Exercise option")
            print("This is your result:\n\t")
            t3 = open("Rohan Exercise.txt")
            content1 = t3.read()
            print(content1)
            # Rohan Exercise retrive Successfully

        if EF1==2:
            print("You selected Food option")
            print("This is your result:\n\t")
            t4 = open("Harry Food.txt")
            content2 = t4.read()
            print(content2)
            # Rohan Food retrive Successfully

if name==3:
    print("You selected Hammid")
    LR = int(input("What you have to do\n1 for Lock\n2 for retrive\n"))
    if LR == 1:
        print("You selected Lock option")
        EF = int(input("What you've to lock\n1 for Exercise\n2 for Food\n"))
        if EF == 1:
            print("You Selected Exercise")
            t1 = open("Hammid Exercise.txt", ("a"))
            exercise1 = input("Enter which exercise you completed now\n")
            datee1 = input("Enter todays date in the format of DD-MM-YYYY\n")
            timee1 = input("Enter the time\n")
            t1.write(datee1)
            t1.write(" ")
            t1.write(timee1)
            t1.write("-")
            t1.write(exercise1)
            t1.write("   ")
            t1.close()
            print("Registered Successfully")
            # Hammid exercise Succesfully

        if EF == 2:
            print("You selected Food")
            t2 = open("Hammid Food.txt", ("a"))
            food1 = input("Enter which Food item you ate\n")
            datee2 = input("Enter todays date in the format of DD-MM-YYYY\n")
            timee2 = input("Enter the time\n")
            t2.write(datee2)
            t2.write(" ")
            t2.write(timee2)
            t2.write("-")
            t2.write(food1)
            t2.write("   ")
            t2.close()
            print("Registered Successfully")
            # Hammid food registered succesfully

    if LR==2:
        print("You selected retrive")
        EF1 = int(input("What you've to lock\n1 for Exercise\n2 for Food\n"))
        if EF1==1:
            print("You selected Exercise option")
            print("This is your result:\n\t")
            t3 = open("Hammid Exercise.txt")
            content1 = t3.read()
            print(content1)
            # Rohan Exercise retrive Successfully

        if EF1==2:
            print("You selected Food option")
            print("This is your result:\n\t")
            t4 = open("Hammid Food.txt")
            content2 = t4.read()
            print(content2)
            # Rohan Food retrive Successfully






