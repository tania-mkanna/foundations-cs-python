######### Assignment 4 #########

#### Exercise:1 ####

## choice 1: Sum Tuples 

def sumTuples(tup1,tup2):

    my_list=[]
    if(len(tup1)==len(tup2)):
        for i in range(len(tup1)): ##len(tup)==len(tup2)
            sum_tuples=tup1[i]+tup2[i]
            my_list.append(sum_tuples)

        return tuple(my_list)        
    else:
        return -1        

    

##############################
       


# choice 2: Export JASON

def exportJSON(dictionary,file_name): 

    #dictionary by default put the string in '' and a the string in json file must be in "" 
    new_dictionary=(str(dictionary)).replace("'",'"').replace("True","true").replace("False","false").replace("None","null")
        

    with open(file_name,"w") as json_file:
        json_file.write(str(new_dictionary))
    
       
##########################################

## choice 3: Import JASON
def importJSON(JSON_file):
    list_of_dict=[]
    open_brace=[]

    with open(JSON_file,"r") as file:
        file=file.read()


    file = file.replace("true","True").replace("false","False").replace('"',"'").replace("null","None")

    for i in range(len(file)):
        
        if (file[i]=="{"):

            open_brace.append(i)

        elif(file[i]=="}"):    
            last_open_brace=open_brace.pop() 
            objects=eval(file[last_open_brace:i+1]) ###eval() : convert string to dict
            list_of_dict.append(objects)

    
    # while("{" in read_file):

    #     start_dict=read_file.find("{")
    #     end_dict=read_file.find("}")
    #     dictionaries=eval(read_file[start_dict:end_dict+1])  ###eval() : convert string to dict
    #     list_of_dict.append(dictionaries)
    #     read_file=read_file[end_dict+2:]
    
    return list_of_dict



#################################################
# display menu
def displayMenu():

   
    while True:
        choice=int(input("1. Sum Tuples\n2. Export JSON\n3. Import JSON\n4. Exit\nEnter a choice: ")) 

        if(choice==1):
            list1=[]
            list2=[]
            dimention=int(input("enter the dimention :"))

            for i in range(dimention):
                num=int(input("Enter the elemnets of tup1: "))
                list1.append(num)

            tup1=tuple(list1)

            print("-----------------------------")

            for i in range(dimention):
                num=int(input("enter the elements of tup2: "))
                list2.append(num)

            tup2=tuple(list2)

            sum_tuples=sumTuples(tup1,tup2)
            print(f"tup1={tup1},tup2={tup2},sum={sum_tuples}")
            print("\n--------------------------------\n")

        elif(choice==2):
            file_name=input("enter a file name: ")
            dictionary={}
            n=int(input("enter the number of items : "))

            for i in range(n):

                key=eval(input(f"enter key[{i}]: ")) ## eval() allows the user to enter any valid type they want    
                value=eval(input(f"enter the value of {key}: ")) 
                dictionary[key]=value  

            exportJSON(dictionary,file_name)
            print("\n--------------------------------\n")

        elif(choice==3):
            file=input("enter the name of file: ")
            list_of_dict=importJSON(file)
            print("list_of_dict=",list_of_dict)
            print("\n--------------------------------\n")

        elif(choice==4):
            print("the program ends")
            break

        else:
            print("Invalid choice !!")
            print("\n--------------------------------\n")
 



displayMenu()

#####################################################
            
#### Exercise:2 ####

# a.O(N^3)
#b.O(N^3)
# c.O(N!)
# d.O(NlogN)
# e.O(N)
# f.O(N^2)
# g.O(NlogN^2)
# h.O(N!)
