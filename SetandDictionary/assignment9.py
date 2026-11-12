"""9)create a phone book using dictionary,ask the user to enter a name and display the associated number of that name

     ex => 

     john:9758689518
     jack:8756884984

"""
phoneDictionary ={}
for i in range(5):
    name = input("Enter the name ")
    number = int(input("Enter the number "))
    phoneDictionary.update({name:number})
print(phoneDictionary)