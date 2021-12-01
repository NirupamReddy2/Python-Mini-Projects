'''
This program assigns roll numbers on the basis of the name of the person, but in REVERSE ALPHABETICAL ORDER

Example:
Sample Input : "Nirupam Bhandar Reddy Mahindra University", choice : any key other than '1'
Sample Output : 
    University - 1
    Reddy - 2
    Nirupam - 3
    Mahindra - 4
    Bhandar - 5
'''

if __name__ == "__main__":
    Names = input("Gimme the names of all the members, each name seperated by a space: ")
    Lowercase_List = []
    count = 1

    Names_List = Names.split(" ")

    for name in Names_List:
        Lowercase_List.append(name.lower())
    
    Lowercase_List.sort()
    Lowercase_List.reverse()

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
    