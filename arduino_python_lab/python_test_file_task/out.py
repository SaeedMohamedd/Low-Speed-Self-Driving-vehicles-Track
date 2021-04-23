
s=0
flag=False 
i=0
read_file = open("python_test_file.txt","r+")
write_fle = open("output_text.txt","w")
for line in read_file: 
    words = line.split(",")
    words = line.strip()
    #print(words)
    for word in words:
        #print(word)
        if any("v" in f for f in word):
            if any("e"in s for s in word) :
                print(words)
                flag=True
                continue
        
        if flag ==True :
            if word.isspace or word.isalpha:
                continue
                #  print(word)
            elif word.isdigit:
                #print(word)
                x1=float(word)
                print(x1)
                s+= pow(x1,2)
                print(s)
                i+=1
                if i > 2:
                    words.append(f"speed = {s}")
                    write_fle.write(words)
                    flag=False


            
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

    
