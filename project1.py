import csv
def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.write(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "age", "contact number", "E-Mail id"])
        writer.writerow(info_list)
if __name__=='__main__':
    condition = True
    student_num = 1
    while (condition):
        student_info = input("enter student information for student #{} in the following format(name age contact_number E-Mail_id: ".format(student_num))
        student_info_list = student_info.split(' ')
        print("\nentered split up information is -\nName: {}\nage: {}\ncontact_number: {}\nE-Mail id: {}"
          .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
        choice_check = input("is the entered information correct?(yes/ no): ")
        if choice_check == "yes":
            write_into_csv(student_info_list)
            condition_check = input("enter (yes/no) if you want to enter information for another student: ")
            if condition_check == "yes":
                condition = true
                student_num = student_num + 1
            elif condition_check == "no":
                condition == false
        elif choice_check == "no":
            print("\nplease re-enter the values!")
        
