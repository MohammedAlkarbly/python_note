p=input("enter tha path of work\n:->>\t")#ask user for a path to save foles
while True :#the main loop
    txt="""enter w to write a new note
enter s to show a file
enter x to exit
***********************************************\n"""#the program controll key
    print(txt)#the program help
    ope=input(":->>\t")#what do you wont to do
    if ope == 'w':#write a new note
        note=input("enter your note here:\n")
        name=note[0:10]
        file=open(p+name+".txt","w+")
        file.write(note)
        print(p+name+".txt")
        file.close()
    elif ope=='s':# show an old file
        name=input("enter file name here:\n")
        file=open(p+name,"r+")
        file.seek(0)
        t=file.read()
        
        file.close()
        print(t+"\n************************************\n")
    elif ope=='x':
        break # exit
    else :
        print ("invalid input")
