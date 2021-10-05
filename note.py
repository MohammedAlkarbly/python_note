from datetime import *
p=input("enter tha path of work\n:->>\t")#ask user for a path to save foles
while True :#the main loop
    txt="""enter c to creat a new note
enter s to show a file
enter e to edit a file
enter x to exit
***********************************************\n"""#the program controll key
    print(txt)#the program help
    ope=input(":->>\t")#what do you wont to do
    if ope == 'c':#creat a new note
        note=input("enter your note here:\n")
        name=str(datetime.now().date())# the name of the file is the date of day
        file=open(p+name+".txt","w+")
        file.write(note)
        file.close()
    elif ope=='s':# show an old file
        name=input("enter file name here:\n")
        file=open(p+name,"r+")
        file.seek(0)
        t=file.read()
        
        file.close()
        print(t+"\n************************************\n")
    elif ope=='e':# edite an old file
        name=input("enter file name here:\n")
        file=open(p+name,"r+")
        file.seek(0)
        t=file.read()
        file.close()
        print(t+"\n************************************\n")# print the old text 
        file=open(p+name,"w")
        note=input("enter the new note text")
        file.write(note)# writ a new note text
        file.close()
    elif ope=='x':
        break # exit
    else :
        print ("invalid input")
