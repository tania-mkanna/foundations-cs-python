import re
##### 1.Count Digits ######

    
def countDigits(num,count=0):

    if (num//10==0):
       return count+1
    
    return countDigits(num//10,count+1)


#---------------------------------#

###### 2.Find Max #######

def findMax(listOfNum):

    if(len(listOfNum)==0):  ## if list is empty
        return 0

    if(len(listOfNum)==1):  ##base case
        return listOfNum[0]
    
    if(listOfNum[0]>listOfNum[1]):

        listOfNum[1]=listOfNum[0]
        return findMax(listOfNum[1:])
       

    elif(listOfNum[1]>=listOfNum[0]):
        
        return findMax(listOfNum[1:])
            
        
    return listOfNum[0]

#-----------------------------------# 

#### 3.Count Tags ######  

def CountTags(listOfTags,tag,count=0):
    if(len(listOfTags)==0):  ##base case
        return count
    
    if(tag==listOfTags[0][2:-1]):
        return CountTags(listOfTags[1:],tag,count+1)
    else:
        return CountTags(listOfTags[1:],tag,count+0)
    
   
#------------------------------------#


def main():

    

    while True:
        choice=int(input("1.Count Digits\n2.Find Max\n3.Count Tags\n4.Exit\nEnter a choice: "))

        if(choice==1):

            print("choice:1.Count Digits")
            num=int(input("Enter an integer: "))
            count_digits=countDigits(num)
            print("there are:",count_digits ,"digits")

        elif(choice==2):

            print("choice:2.Find Max")
            listOfNum=[]
            dimention=int(input("Enter the dimention of the list: "))
            for i in range(dimention):
                n=int(input("enter the elemts: "))
                listOfNum.append(n)

            find_max=findMax(listOfNum)
            print("max=",find_max)

        elif(choice==3):

            print("choice:3.Count Tags")
            tag=input("Enter a tag: ")

            ## Reading html file:  ('r' for reading the file)
            with open('assignment_03_Tania_Mkanna\index.html','r') as file:
                html_string=file.read()

            ### put all the closed tags in a list ( ".*?" it takes every thing between < and > )  
            listOfTags=re.findall('</.*?>',html_string)

            count_tags=CountTags(listOfTags,tag)
            print(tag,"occurs",count_tags,"times")

        elif(choice==4):
            print("the programs end")
            break    
        
        else:

            choice=input("invalid choice!\n1.Count Digits\n2.Find Max\n3.Count Tags\n4.Exit\nEnter a choice: ")

main()