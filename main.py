
# Anil

def getDate():
    import datetime
    return datetime.datetime.now()
def client(choice):
    """ this function gives you the information about your clint's exercise and diet plan"""
    option= {"1" :"Harry_", "2" : "Rohan_", "3" : "hammad_"}
    option2={"e" : "exercise", "d": "diet"}
    ch = input("e: Exercise \n"
                   "d:  Diet ")
    import os
    address = "C:\python37\pychram_project\Health_management_system\\" + option[choice]+option2[ch]
    print(address)
    exists = os.path.isfile(address)
    if exists:
        print("Record Found")
        with open(address, "r+") as f:
            print(getDate(), end=":   ")
            var=f.readlines()
            for x in var:
                print(x)
            add1= input("\nDo you want to add anything?  "
                        "1:  yes\n"
                        "0:  no  ")
            while(add1=='1'):
                with open(address, "r+") as f:
                    var2=input("\nWhat do you want to add?  ")
                    f.write("\n" + str(getDate())+"    ")
                    f.write(var2)
                    var = f.readlines()
                    for x in var:
                        print(x)
                    add1 = input("\nDo you want to add anything?  "
                                 "1:  yes\n"
                                 "0:  no  ")

            if add1=='0':
                with open(address, "r+") as f:
                    print(getDate(), end=":   ")
                    var = f.readlines()
                    for x in var:
                        print(x)
                print("Run Again if you want to add")
            else:
                print("Wrong Choice ")

    else:
        with open(address, "w+") as f:
            var2 = input("\nWhat do you want to add?  ")
            f.write("\n" + str(getDate()) + "    ")
            f.write(var2)
            var = f.readlines()
            for x in var:
                print(x)
            print("Record Successfully Created ")
choice= input("type number for respective Patient:"
            "1: Harry\n"
            "2: Rohan\n"
            "3: Hammad:   ")
client(choice)
exit()