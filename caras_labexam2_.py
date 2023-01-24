listt=[]
odd=[]
even=[]

while True:
    try:
        choice=str.capitalize(input('Do you want to proceed?'))

        match choice:
            case 'Y':
            

                print('***** ODD AND EVEN NUMBERS *****')

                name=str(input('Name: '))
                id=int(input('ID: '))
                code=int(input('Code: '))
                break

            case 'N':
           
                exit()


    except ValueError:    
     print('Error in Data')
     continue


n=int(input('Enter number you want to store: \n'))

for x in range(0,n):
    ele=int(input('Enter Value: '))
    listt.append(ele)

print(listt)


for i in listt:
    if(i % 2 == 0):
        even.append(i)

    else:
        odd.append(i)


odd.sort
even.sort
print(f'User: {name} , {id}, {code}')
print('Odd: ',odd)
print('Even: ',even)
