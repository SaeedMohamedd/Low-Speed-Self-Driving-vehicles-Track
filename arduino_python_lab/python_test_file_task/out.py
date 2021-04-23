

strr=" "
read_file = open("python_test_file.txt","r+")
write_fle = open("output_text.txt","+r")
for line in read_file: 
    words = line.split(",")
    #print(words)
    for i in range(len(words)):
        if words[i] == "velocity":
            #print(words[i+1])
            '''
            if words[i+1].isspace:
                print("in")
                continue
                print("out")
            '''
            #print(words[i+1])
            try:
                x1=float(words[i+1])
             #   print(f"x1 {x1}")
                x2=float(words[i+2])
            #    print(f"x2 {x2}")
                x3=float(words[i+3])
           #     print(f"x3 {x3}")
                s=pow((x1),2)+pow(x2,2)+pow(x3,2)
                #print(s) 
                strr=f"the speed = {s}\n"
                #speeds.insert(strr)
                #print(strr)

                #words.insert(int(s),i+3)
                #print(str_words)
            except :
                continue

    newdata=line+strr
    #print(newdata)
    write_fle.write(newdata)
#print(words)
#for line in read_file:
 #   read_file.write("")
#write_fle.write("\n")
#write_fle.write(strr)

'''
    for word in words:
        print(word)
        if word == "velocity":
            
            if flag == True :
                print("true")
                print(word)
                print(f"flag value is :{flag}")
                if word =="velocity":
                    continue
                x1=float(word)
                print(x1)
                s+= pow(x1,2)
                print(s)
                i+=1
                if i > 2:
                    words.append(f"speed = {s}")
                    write_fle.write(words)
                    flag=False
                    print("flag is False")
                    continue

            flag=True
            print("flag is true")
            break
'''


'''        
        if flag ==True :
            if word.isspace or word.isalpha:
                print(word)
                continue
                
            elif word.isdigit:
                print("get x1")
                x1=float(word)
                print(x1)
                s+= pow(x1,2)
                print(s)
                i+=1
                if i > 2:
                    words.append(f"speed = {s}")
                    write_fle.write(words)
                    flag=False

'''
            
           # i=0
           # while(i<3):     
           # wow.append(words)
            #strenges=str(words)
           # words=words.split("'"," ")
           # strenges=strenges.replace(" ]"," ")
           # strenges=strenges.strip("\n")
           # elements=words.split(",")
            #print(elements[16+i])
            #x1=elements[16+i]
           
               # x1.translate({ord('\n ]'): " "})
                
              #  x1=float(word)
               # i+=1
            #s+= np.sum(pow(x1,2))

    
