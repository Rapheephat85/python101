num_emps = int(input('How many employes records do you want to creats?'))
with open ('employees01.txt','w')as emp_file:
    for count in range(1,num_emps +1):
        print('Enter data for employess#',count,sep='')
        name = input('Name: ')  
        id_num = input('ID: ')
        dept = input('Dept: ')

        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')
        print()     
print('Employee records written to eemployees01.txt. ')