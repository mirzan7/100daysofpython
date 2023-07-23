row1 = ['+','+','+']
row2 = ['+','+','+']
row3 = ['+','+','+']
map = [row1,row2,row3]
hide = input("Enter where you want to hide the treasure  :")
colum = int(hide[0])
row = int(hide[1])
map[colum-1][row-1] = "X"
print(map)