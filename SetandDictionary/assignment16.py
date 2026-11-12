"""18)
for a class representation post,3 students are the candidates,your teacher has code named 'a','b' and 'c' 
each student of the class has to vote to select the cr from them , the voting data is available in the form of follwing dictionary ,which stores which roll number voted for them 

votes = {1:'a',2:'a',3:'c',4:'a',5:'c',6:'b',7:'b',8:'b',9:'a',10:'c',11:'a',12:'b',13:'b',14:'c',15:'b'}

write a program to calcultae total vote for each of the candidates and declare the winner"""

votes = {1:'a',2:'a',3:'c',4:'a',5:'c',6:'b',7:'b',8:'b',9:'a',10:'c',11:'a',12:'b',13:'b',14:'c',15:'b'}
avote =0
bvote =0
cvote =0
for i in votes:
    if votes[i]=="a":
        avote+=1
    elif votes[i]=="b":
        bvote+=1
    else:
        cvote+=1
if avote > bvote and avote > cvote:
    print("A is the CR of Class")
elif bvote>avote and bvote> cvote:
    print("B is the CR of class")
else:
    print("C is the CR of the class")