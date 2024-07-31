import random
import string

def EC2_instance_name_script(Department,Number_of_instance):
    Instance_Name = []
    for i in range(Number_of_instance):
        Random_Character = ''.join(random.choices(string.ascii_letters, k=3))
        Random_Number = ''.join(random.choices(string.digits, k=3))
        Random_EC2_Instance_Name = Department + '-' + Random_Character + Random_Number
        Instance_Name.append(Random_EC2_Instance_Name)
    return Instance_Name
    
Department_Name = input('Enter your Department name: ').lower()
Department_list = [ 'Marketing', 'Accounting', 'FinOps']
Department_list_case_variation = [Dept.lower()for Dept in Department_list]
if Department_Name in Department_list_case_variation:
     print('Random EC2 name Generator script can be used by your Department ')
     No_of_EC2_Instances = int(input('Please enter how many EC2 instances you want: '))
     print('List of EC2 instance names:')
     Final_Result= EC2_instance_name_script(Department_Name,No_of_EC2_Instances)
     for item in Final_Result:
         print(item)

else:
    print("You can't use the EC2 name Generator")