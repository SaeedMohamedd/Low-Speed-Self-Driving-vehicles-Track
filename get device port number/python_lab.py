def get_port_number(device_name,read_file_name,out_file_name):
    wow=[]
    read_file = open(read_file_name,"r")
    search_result=open(out_file_name,"w")
    for line in read_file:
        line = line.strip()
        line = line.strip(":")
        line = line.strip("=")
        line = line.replace("/"," ")   
        words = line.split(" ")
        
        for word in words:
            search_result.write(word)
        if any(device_name in s for s in words):
            wow.append(words)
            strenges=str(wow)
            print(strenges)
            elements=strenges.split(" ")
            print(f"{device_name} is connect to port {elements[5]}")
            search_result.write(f"{device_name} is connect to port {elements[5]}")   
            break
    else:
        print("not found")


# Run the function take three parameter device name, input file name, output file name
get_port_number("ttyACM0","mega.txt","search_result.txt")







### code without function
### and some tries
'''
wow=[]
read_file = open("mega.txt","r")
search_result=open("search_result.txt","w")
for line in read_file:
    line = line.strip()
    line = line.strip(":")
    line = line.strip("=")
    line = line.replace("/"," ")   
    words = line.split(" ")
    
    for word in words:
        search_result.write(word)
    if any("ttyACM0" in s for s in words):
        wow.append(words)
        strenges=str(wow)
        print(strenges)
        elements=strenges.split(" ")
        print(f"ttyACM0 is connect to port {elements[5]}")
        search_result.write(f"ttyACM0 is connect to port {elements[5]}")   
        break
    else:
        print("not found")




read_file.close()
search_result.close()
'''


'''    
    for word in words:
        if word.find("ttyACM0"):
        #    print(word.index)
        #   print("true")


'''


''' 
i=0
while (i<len(words)):
    if words[i] =="ttyACM0":
        print("here")
        print(words[i])
        exit() 
    i+=1
 '''               

       
