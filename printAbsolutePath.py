"""Problem:
The program must accept a string S representing a file system as the input. The program must print the absolute path to each file in the given file system. If there is no file, then the program must print -1 as the output. The string S contains the names of the directories, sub-directories and files, where \n and \t are used to indicate the difference between the directories and sub-directories.

Boundary Conditions:
8 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The line(s), each contains the absolute path to the file or the first line contains -1.

Example Input/Output 1:
Input:
MyDir\n\tPhotos\n\t\tmyphoto.jpeg\n\t\tMiniProject\n\tDocuments\n\t\tIDProof\n\t\t\tMyAadhaar.pdf

Output:
MyDir\Photos\myphoto.jpeg
MyDir\Documents\IDProof\MyAadhaar.pdf

Example Input/Output 2:
Input:
Hector\n\tAndroid\n\tJava\n\t\tNetBeans\n\t\tEclipse\n\tCodeBlocks\n\tSampleProject\n\tGeany

Output:
-1"""
import re
lines = s.split("\\n")
stack = []
paths = []

for line in lines:
  depth = line.count("\\t")
  name = line.replace("\\t", "")
  while len(stack) > depth:
    stack.pop()
    stack.append(name)
    if re.search(r"\.[A-Za-z0-9]+$", name):
      paths.append("\\".join(stack))
if paths:
  for p in paths:
    print(p)
  else:
    print(-1)

