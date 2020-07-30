import kociemba
def sol(input1):
	input2=[[[]],[[]],[[]],[[]],[[]],[[]]]

	for i in range(6):
		if(input1[i][1][1]=='w'):
			input2[0]=input1[i]
			break

	for i in range(6):
		if(input1[i][1][1]=='r'):
			input2[1]=input1[i]
			break

	for i in range(6):
		if(input1[i][1][1]=='g'):
			input2[2]=input1[i]
			break

	for i in range(6):
		if(input1[i][1][1]=='y'):
			input2[3]=input1[i]
			break


	for i in range(6):
		if(input1[i][1][1]=='o'):
			input2[4]=input1[i]
			break




	for i in range(6):
		if(input1[i][1][1]=='b'):
			input2[5]=input1[i]
			break

	for i in range(6):
		for j in range(3):
			for k in range(3):
				if (input2[i][j][k]=='w'):
					input2[i][j][k]='U'
				elif (input2[i][j][k]=='y'):
					input2[i][j][k]='D'
				elif (input2[i][j][k]=='r'):
					input2[i][j][k]='R'
				elif (input2[i][j][k]=='o'):
					input2[i][j][k]='L'
				elif (input2[i][j][k]=='g'):
					input2[i][j][k]='F'
				elif(input2[i][j][k]=='b'):
					input2[i][j][k]='B'

	b=''
	for i in range(6):
		for j in range(3):
			for k in range(3):
				b+=input2[i][j][k]
	
        
	a = kociemba.solve(b)
	print(a)
	a = a.replace("U'","R L F2 B2 R' L' D' R L F2 B2 R' L'")
	a = a.replace("U2","R L F2 B2 R' L' D2 R L F2 B2 R' L'")
	a = a.replace("U","R L F2 B2 R' L' D R L F2 B2 R' L'")
	return a
cube=[[['y', 'b', 'y'], ['w', 'g', 'w'], ['o', 'o', 'o']], [['o', 'o', 'y'], ['r', 'r', 'o'], ['w', 'g', 'r']], [['r', 'r', 'r'], ['y', 'b', 'y'], ['w', 'g', 'w']], [['w', 'r', 'r'], ['r', 'o', 'o'], ['o', 'b', 'y']], [['g', 'g', 'g'], ['b', 'w', 'b'], ['b', 'w', 'b']], [['g', 'g', 'g'], ['y', 'y', 'y'], ['b', 'w', 'b']]]
a=sol(cube)

print(a)
