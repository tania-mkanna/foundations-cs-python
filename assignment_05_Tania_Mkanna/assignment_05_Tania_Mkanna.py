


class CourseEnrollmentSystem:

    def __init__(self,list_of_students,course_catalog ):
        
        self.list_of_students= list_of_students
        self.course_catalog= course_catalog

    ####################################  ADD COURSE  ##################################

    def addCourse(self,course):
        if course.code in self.course_catalog:
            print("the course is already added")
            return
        self.course_catalog[course.code]={"name" : course.course_name,"number of credits":course.num_of_credits,"type of course":course.course_type}

    ###################    ENROLLED STUDENT IN COURSE   ##################################     
    def studentEnrollment(self,student,course):
        
        
        if course.code in self.course_catalog:
            student.enroll(course)
           
        else:
            print("the course is not available") 
            return

    #################################################################################

    ###################    drop course for student   ################################## 
    def dropCourse(self,student,course):
        
                
        if course.code in student.enrolled_courses:
                
            student.drop(course)
        else:    
            print("the course is not enrolled") 
            return
   
                    
               
    ############################################################################## 

    ###################   List Student Courses   #################################
    def displayCourses(self,student):
        print("The enrolled courses  : ")
        for course_id in student.enrolled_courses:
            print(f"{course_id}:{self.course_catalog[course_id]}")
    ###############################################################################


    ###################   Save Course Catalog  ################################## 
    def saveCourseCatalog(self,output_file):
        self.course_catalog=str(self.course_catalog).replace("'",'"').replace("True","true").replace("False","false").replace("None","null")
        with open (output_file,"w") as file:
            file.write(self.course_catalog)
    ############################################################################

    ###################       Load Course Catalog    ###########################
    def loadCourseCatalog(self,input_file):
        with open (input_file,"r") as file:
            file=file.read()

        file = file.replace("true","True").replace("false","False").replace('"',"'").replace("null","None")
        self.course_catalog=file   

    ############################################################################
    
        


   
class Course:
    def __init__(self,code,course_name,num_of_credits,course_type):
        self.code=code
        self.course_name=course_name
        self.num_of_credits=num_of_credits
        self.course_type=course_type


class Student:
    def __init__(self,id,name):
        self.id = id
        self.name=name
        self.enrolled_courses={}

    def enroll(self, course):
        #check if course already enrolled
        if course.code in self.enrolled_courses:
            print("the student already enroll this course")
            return
        else:
            self.enrolled_courses[course.code]=course    



    def drop(self, course):
        if course.code in self.enrolled_courses:
            
            del self.enrolled_courses[course.code]
        else:
            print("the course is not found")
            return
             
        

    # def __str__(self) :
           
    #     return f"{self.enrolled_courses}"


def main():
    
    is_student=False
    course_type_dict={1:"core course",2:"elective course"}
    s1=Student("01","tania")
    s2=Student("02","tania")
    s3=Student("03","nagham")

    list_of_students=[s1,s2,s3]
    course_catalog={}
    course_enrollment_system=CourseEnrollmentSystem(list_of_students,course_catalog)
    while True:
        choice=int(input("1. Add Course\n2.Enroll Student in Course\n3. Drop Course for Student\n4. List Student Courses\n5. Save Course Catalog\n6. Load Course Catalog\n7. Exit: Exit the program\nenter a choice:"))
        if choice==1:

            course_code=input("enter the code of the course: ")
            course_name=input("enter the name of the course: ")
            number_of_credits=int(input("enter the number of credits: "))
            course_type=int(input("enter 1.core course\nenter 2.elective course\n"))
            
            course=Course(course_code,course_name,number_of_credits,course_type_dict[course_type])

            course_enrollment_system.addCourse(course)
            
            print("------------------------------")
        
        elif choice==2:
            
            student_id=input("enter the id of the student:")
            

            for i in list_of_students:
                if i.id ==student_id:
                    is_student=True
                    student=i
                    break

            if is_student==False:
                print("the student is not found")
                continue

            course_code=input("enter the code of the course:")

            course_name=course_enrollment_system.course_catalog[course_code]["name"]
            number_of_credits=course_enrollment_system.course_catalog[course_code]["number of credits"]
            course_type=course_enrollment_system.course_catalog[course_code]["type of course"]
            course=Course(course_code,course_name,number_of_credits,course_type)

            course_enrollment_system.studentEnrollment(student,course)

            print("------------------------------")
           
        elif choice==3:

            course_code=input("enter the code of the course: ")

            student_id=input("enter the id of the student: ")

            for i in list_of_students:
                if i.id ==student_id:
                    student=i
                    break
        

            course_name=course_enrollment_system.course_catalog[course_code]["name"]
            number_of_credits=course_enrollment_system.course_catalog[course_code]["number of credits"]
            course_type=course_enrollment_system.course_catalog[course_code]["type of course"]
            course=Course(course_code,course_name,number_of_credits,course_type)

            course_enrollment_system.dropCourse(student,course)

            print("------------------------------")

        elif choice==4:

            student_is_found=False
            student_id=input("enter the id of the student: ")

            for i in list_of_students:
                if i.id ==student_id:
                    student_is_found=True
                    student=i
                    break
            
            if(student_is_found==True):
                course_enrollment_system.displayCourses(student)
            else:
                print("student is not found")

            print("------------------------------")  

        elif choice==5:
            file_name=input("enter the name of file to save the course catalog: ")
            course_enrollment_system.saveCourseCatalog(file_name)
            print("------------------------------")

        elif choice==6:
            file_name=input("enter the name of file: ")
            course_enrollment_system.loadCourseCatalog(file_name)
            print("------------------------------")

        elif choice==7:
            print("you exit the program")
            break
        
        else:
            print("this chice is not available!!\nplease enter again:\n")
   
main()