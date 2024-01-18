#with enumerate function
DNA_input = str(input("Enter the sequence \n").upper())
sequence = ["A", "C", "G", "T"]
counter = 0

for position, letter in enumerate(DNA_input):
    if not letter in sequence:
        print(letter + " is an invalid base at position " + str(position + 1))
    else:
        #print(str(position + 1), letter)
        counter += 1

if counter == len(DNA_input):
    print("Valid DNA sequence")
else:
    print("Invalid DNA sequence")

'''

# without enumerate function
sequence = ['A', 'G', 'T', 'C']
DNA_input = str(input("Enter a DNA seq:\n").upper())
index=0
counter =0
for letter in DNA_input:
    if letter in sequence:
        counter +=1
    else:
        print(letter + " at " + str(index) + " is an incorrect base")
    index +=1

if counter == len(DNA_input):
    print("Valid input")
else:
    print("Invalid input!")
'''