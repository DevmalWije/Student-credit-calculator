 # I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20210220/w1912859
# Date:17/03/2022

#Creating variables
marks=''

progress=[]
progress_trailer=[]
no_progess=[]
exclude=[]
final_credits=[]
master_list=[]

credit_range=(0,20,40,60,80,100,120)
cred_total=0

pass_cred=0
defer_cred=0
fail_cred=0
total_candidates=0
max_val=0
menue_option=0

#Prompting for menue option to execute respective part of code
while True:
    try:
        menue_option=int(input("Press: 1 for Student version\nPress: 2 to execute Staff version Part-1\nPress: 3 to execute Staff version part 2\nPress: 4 to execute Staff version part 3\nPress: 5 to execute Staff version part 4\nEnter option: "))
        if menue_option>5 or menue_option<1:
            print("Invalid option")
            print()
            continue
        break
    except ValueError:
        print("Integer required")
        print()

        
def progress_predict():
    global total_candidates,pass_cred,fail_cred,defer_cred,marks
    "Reading and validating credit inputs"
    
    while True:
        try:
            marks=''
            print()
            pass_cred=int(input("Please enter your credits at pass: "))
        except ValueError:
            print("Integer required")
        else:
            if pass_cred not in credit_range:
                print("Out of range")
            else:
                marks=marks+(str(pass_cred))
                try:
                    defer_cred=int(input("Please enter your credits at defer: "))
                except ValueError:
                    print("Integer required")
                else:
                    if defer_cred not in credit_range:
                        print("Out of range")
                    else:
                        marks=marks+","+str(defer_cred)
                        try :
                            fail_cred=int(input("Please enter your credits at fail: "))
                        except ValueError:
                            print("Integer required")
                        else:
                            if fail_cred not in credit_range:
                                print("Out of range")
                            else:
                                cred_total=(pass_cred+defer_cred+fail_cred)
                                if cred_total !=120:
                                    print("Total incorrect")
                                    continue
                                else:
                                    marks=marks+","+str(fail_cred)
                                    total_candidates=total_candidates+1
                                    break

def mark_cal(pass_cred,fail_cred,defer_cred):
    "Deciding progression outcome"
    
    if pass_cred==120:
        master_list.append("Progress - "+marks )
        progress.append("*")
        print("Progress")
        print()
        
    elif pass_cred==100:
        master_list.append("Progress (module trailer) - "+marks)
        progress_trailer.append("*")
        print("Progress (module trailer) ")
        print()
        
    elif fail_cred>=80:
        master_list.append("Exclude -"+marks)
        exclude.append("*")
        print("Exclude")
        print()
        
    else:
        master_list.append("Module retriever - "+marks)
        no_progess.append("*")
        print("Module retriever")
        print()
        
def histogram():
    "Printing histogram"
    print("---------------------------------------------------------------")
    print("Horizontal Histogram")
    print("Progress",len(progress),"  :",*progress) 
    print("Trailer ",len(progress_trailer),"     :",*progress_trailer)
    print("Retriever",len(no_progess),":",*no_progess)
    print("Excluded",len(exclude)," :",*exclude)
    print()
    print(total_candidates,"Outcomes in total")
    print("---------------------------------------------------------------")
    print()
    
def vertical_histogram():
    "Printing vetical histogram"
    final_credits=[progress, progress_trailer, no_progess, exclude]
    max_val=max(len(progress),len(progress_trailer),len(no_progess),len(exclude))
    print('Progress',len(progress),'|Trailing',len(progress_trailer),'|Retriever',len(no_progess),'|Excluded',len(exclude))
    
    for i in range (max_val):
        for x in range (len(final_credits)):
            try:
                print("          ",final_credits[x][i],"\t",end='')
            except IndexError:
                print("\t",end='')
        print()
    print(total_candidates,"Outcomes in total")
    print()
        
def list_print(master_list):
    "Printing outcomes using list"
    print()
    for x in range(len(master_list)):
        print(master_list[x])
        
def print_file():
    "Printing outcomes to text file"
    with open("outcomes.txt","w")as open_file:
        for i in range (len(master_list)):
            open_file.writelines("{}\n".format(master_list[i]))

def read_file():
    "Reading outcomes from text file"
    with open("outcomes.txt","r")as to_read:
        for x in to_read:
            print(x,end="")
        
                
#Executing functions in loop according to menue option
if menue_option==1:
    progress_predict()
    mark_cal(pass_cred,fail_cred,defer_cred)
    
elif menue_option==2:
    re_try="Y"
    while re_try=="Y":
        progress_predict()
        mark_cal(pass_cred,fail_cred,defer_cred)
        re_try=input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:").upper()
        print()
    if re_try=="Q":
        print()
        histogram()
        
elif menue_option==3:
    re_try="Y"
    while re_try=="Y":
        progress_predict()
        mark_cal(pass_cred,fail_cred,defer_cred)
        re_try=input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:").upper()
        print()
    if re_try=="Q":
        print()
        histogram()
        vertical_histogram()
        
elif menue_option==4:
    re_try="Y"
    while re_try=="Y":
        progress_predict()
        mark_cal(pass_cred,fail_cred,defer_cred)
        re_try=input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:").upper()
        print()
    if re_try=="Q":
        histogram()
        vertical_histogram()
        list_print(master_list)
        
elif menue_option==5:
    re_try="Y"
    while re_try=="Y":
        progress_predict()
        mark_cal(pass_cred,fail_cred,defer_cred)
        re_try=input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:").upper()
        print()
    if re_try=="Q":
        histogram()
        vertical_histogram()
        print_file()
        read_file()
        

