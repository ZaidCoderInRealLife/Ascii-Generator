while(True):
    text=input("Enter letters = ")
    found=0
    for i in range(0, len(text),1):
        if(text[i]!='X' and text[i]!='o'):
            found=1
    if(found==1):
        continue
    else:
        for i in range(0,len(text),1):             #loop 1
            if(text[i]=='X'):
                print("XX      XX",end='')
            elif(text[i]=='o'):
                print("      ",end='')
            print("        ",end='')
        print("")
        for i in range(0,len(text),1):                #loop 2
            if(text[i]=='X'):
                print("  XX  XX  ",end='')
            elif (text[i] == 'o'):
                print(" oooo ", end='')
            print("        ",end='')
        print("")
        for i in range(0,len(text),1):            #loop 3
            if(text[i]=='X'):
                print("    XX    ",end='')
            elif(text[i]=='o'):
                print("oo  oo",end='')
            print("        ",end='')
        print("")
        for i in range(0,len(text),1):               #loop 4
            if (text[i] == 'X'):
                print("  XX  XX  ", end='')
            elif (text[i] == 'o'):
                print("oo  oo", end='')
            print("        ",end='')
        print("")
        for i in range(0,len(text),1):        #loop 5
            if(text[i]=='X'):
                print("XX      XX",end='')
            elif (text[i] == 'o'):
                print(" oooo ", end='')
            print("        ",end='')
        break




















