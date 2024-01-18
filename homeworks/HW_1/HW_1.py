# while it should read: "Bowl of petunias 42 Sperm whale 2005"

line1 = ["petunia", ["whale", ["2", "s"]], "arthurBowldentSperm", [4, ["20", 0, "5",["of"]]]]
word1 = line1[2][6:10]
word2 = line1[3][1][3][0]
word3 = line1[0]+line1[1][1][1]
word4 = str(line1[3][0]) + line1[1][1][0]
word5 = line1[2][14:19]
word6 = line1[1][0]
word7 = line1[3][1][0] + str(line1[3][1][1]) + line1[3][1][2]
print(word1, word2, word3, word4, word5, word6, word7)

"""
# dead codes
def sentence_fixer():
    scrambled_line = list(x for x in input("Enter the line please!\n").strip().split("''"))
    #scrambled_line = input_line.strip().split()
    fix1 = scrambled_line[2][6:10]
    fix2 = scrambled_line[3][1][3][0]
    fix3 = scrambled_line[0] + scrambled_line[1][1][1]
    fix4 = str(scrambled_line[3][0]) + scrambled_line[1][1][0]
    fix5 = scrambled_line[2][14:19]
    fix6 = scrambled_line[1][0]
    fix7 = scrambled_line[3][1][0] + str(scrambled_line[3][1][1]) + scrambled_line[3][1][2]
    print(fix1, fix2, fix3, fix4, fix5, fix6, fix7)

sentence_fixer()

"""

"""
input_line = str(input("Enter the line please!\n"))
#scrambled_line = list(map(str,input_line.strip().split()))
print(input_line.index("Bowl"))
print(input_line.index("of"))
print(input_line.index("petunia"))
print(input_line.index("s"))
print(input_line.index("4"))
print(input_line.index("2"))

print(input_line[42:46], input_line[78:80], (input_line[2:9]+input_line[29]), (input_line[59]+input_line[24]),
      )

#for name in scrambled_line:

"""