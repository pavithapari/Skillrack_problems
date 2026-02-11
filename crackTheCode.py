"""Given a code with dotted line where each pair of the dotted line's length represents the position of letter in the given 5X5 matrix.One position will contain two alphabets separated by / in that position we
have to take the first alphabet"""


dotted=input().split()
pairs=[list(map(len,dotted[i-2:i]) for i in range(2,len(dotted)+1,2)]
mat=[]
for i in range(5):
  mat.append(input().split())
for i,j in pairs:
  if(len(mat[i-1][j-1])==2):
    print(mat[i-1][j-1],end="")
  else:
    print(mat[i-1][j-1],end="")
