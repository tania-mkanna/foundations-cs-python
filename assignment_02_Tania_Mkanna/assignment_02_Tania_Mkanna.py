######### Assignment 2 #########

##Exercise:1


def isFectorial(n):
    fectorial=1
    for i in range(1,n+1):
        fectorial=fectorial*i
    if(fectorial==1):
        print(1)
    else:    
        print(fectorial,end="")
        print("(",end="")
        for i in range(1,n+1):
            if(n>1):
                print(i,"* ",end="")
        print("\b\b)")  ### "\b"to delete the last *         
        



n=int(input("enter a positive integer: "))
while(n<0):
    n=int(input("Invalid!Enter a positive integer:")) 
isFectorial(n)

################

#Exercise:2

function
def findDivisors(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i,",",end="")

def main():
    n=int(input("Enter an integer: ")) 
    print("[",end="")
    findDivisors(n)
    print("\b]") 
main()       




#Exercise:3 

def reverseString(sentence):
    for i in range(len(sentence)-1,-1,-1):
        print(sentence[i],end="")


def main():
    sentence=input("Enter a sentence: ")
    reverseString(sentence)
main()    

###############


#Exercise:4  


def findEvenNumbers(my_list):
    even_list=[]
    for i in range(0,len(my_list)):
        if(my_list[i]%2==0):
            even_list.append(my_list[i])
    return even_list       

def main():
    my_list=[]
    dimention=int(input("enter the dimention: "))

    for i in range(0,dimention):
        num=int(input("enter the nums: "))
        my_list.append(num)

    even_list=findEvenNumbers(my_list)
    print(even_list)
main()  

####################

#Exercise:5

def strongPassword(code):
    strong_password=True
    charecters_count=uppercase_count=lowercase_count=digit_count=special_character_count=0
    special_character=["#","?","!","$"]
    for i in range(0,len(code)):
        if(code[i].isupper()):
            uppercase_count+=1
               
        elif(code[i].islower()):
            lowercase_count+=1
        elif(code[i].isdigit()):
            digit_count+=1
      
        for j in range(0,len(special_character)):
            if(code[i]==special_character[j]):
                special_character_count+=1
        charecters_count+=1   
    if(charecters_count>=8):
        if(uppercase_count!=0 and lowercase_count!=0 and digit_count!=0 and special_character_count!=0) :
             strong_password=True
        else:
            strong_password=False     
    else:
        strong_password=False 

    return strong_password            
                    

def main():
    code=input("enter you password: ")
    strong=strongPassword(code)
    if(strong==True):
        print("strong password")
    else:
        print("Week password")    

main()


##Exercise:6

def checkIPv4Adderss(IPaddress):
    validIP=True
    start=0
    split_address=[]
    for i in range(0,len(IPaddress)):
        
        if(IPaddress[i] ==  "."):
            split_address.append(IPaddress[start:i])
            start=i+1
    split_address.append(IPaddress[start:])

    if(len(split_address)!=4):
        validIP=False

    else:
        validIP=True
        for i in range(0,len(split_address)):
            if(split_address[i][0]=="0" and len(split_address[i])>1):
                validIP=False
                break
            else: 
                validIP=True
                for i in range(0,len(split_address)):
                    if(int(split_address[i])<0 or int(split_address[i])>255):
                        validIP=False
                    else:True   

    return validIP

def main():
    IPv4_address=input("enter the IPv4 address: ")
    valid_IPv4=checkIPv4Adderss(IPv4_address)
    if(valid_IPv4==True):
        print("valid IPv4 address")
    else:
        print("invalid IPv4 address")       
                
main()               

    

    




    

    
    
              
