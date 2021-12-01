'''
This program assigns roll numbers on first-come-first served basis

Example:
Sample Input : "Nirupam Bhandar Reddy Mahindra University", choice : any key other than '1'
Sample Output : 
    Nirupam - 1
    Bhandar - 2
    Reddy - 3
    Mahindra - 4
    University - 5
'''

if __name__ == "__main__":
    Names = input("Gimme the names of all the members, each name seperated by a space: ")
    Lowercase_List = []
    Names_List = Names.split(" ")

    count = 1


    for name in Names_List:
        Lowercase_List.append(name.lower())

    choice = input("Do you wish to start the numbering from 0(zero), if yes, enter '1', else enter any key: ")

    if choice == '1':
        count = 0
        for name in Lowercase_List:
            print(name, end=" - ")
            print(count)
            count = count + 1

    else:
        for name in Lowercase_List:
            print(name, end=" - ")
            print(count)
            count = count + 1