class contact:
    def __init__(self,person_name,number):
        self.name = person_name
        # Created list of numbers in order to hold multiple numbers for each person 
        self.numbers = []
        self.numbers.append(number)

def display_contacts(contact_list):
    print('Name   -   NUMBERS -')
    print('-------------------------------------------')
    for i in contact_list:
        print(f'{i.name}     -     {i.numbers}')

def search_specific_contact(list,key):
    temp_contact_list = []
    for i in list:
        if key in i.name:
            temp_contact_list.append(i)

    if not temp_contact_list:
        print("No contact matched....")
    else:
        print("Search results for given name are-,")
        
        count=0
        for j in temp_contact_list:
            print('   ',count+1,':',j.name)
            count = count + 1
        print('\n')
        
        index = int(input("Enter contact's Sr.No to get (s)he numbers :"))
        print(f'\n{temp_contact_list[index-1].name}:{temp_contact_list[index-1].numbers}')

if __name__=='__main__':
    contact_list = []
    flag = True
    print('\nWelcome to ContactKeeper-')
    while flag:
        n = int(input('''\nPress 1 to store contact\nPress 2 to print contacts\nPress 3 to search contact\nPress 4 to exit\nEnter input:'''))
                            
        if n==1:
            name = input("\nEnter Name : ")
            while(True):
                mnumber = input("Mobile Number : ")

                if(len(mnumber)==10):
                    try:
                        mnumber = int(mnumber)
                        break
                    except ValueError:
                        print("Invalid number entered")
                else:
                    print("Invalid number entered")
            
            name_already_exits=None
            for i in contact_list:
                if i.name==name:
                    name_already_exits=i
                else:
                    name_already_exits=None
           
            if name_already_exits:
                name_already_exits.numbers.append(mnumber)
            else:
                contact_list.append(contact(name,mnumber))
            
            #Reference - stackOverflow to print the contact_list in sorted order by names
            contact_list = sorted(contact_list, key=lambda item: item.name.casefold())

        elif n==2:
            print('\n')
            if(contact_list):
                display_contacts(contact_list)
            else:
                print("Contact contact_list is Empty")

        elif n==3:
            print('\n')
            key = input("Enter the letter or word to be searched:")
            search_specific_contact(contact_list,key)

        elif n==4:
            flag = False
        
        else:
            print('Invalid input entered..Try Again')