import kociemba

input1=[
[['Y','Y','Y'],['Y','Y','Y'],['Y','Y','Y']],
[['R','R','R'],['G','G','G'],['G','G','G']],
[['W','W','W'],['W','W','W'],['W','W','W']],
[['O','O','O'],['B','B','B'],['B','B','B']],
[['B','B','B'],['R','R','R'],['R','R','R']],
[['G','G','G'],['O','O','O'],['O','O','O']]]


def sol(input1):
	input2=[[[]],[[]],[[]],[[]],[[]],[[]]]

	for i in range(6):
		if(input1[i][1][1]=='Y'):
			input2[0]=input1[i]
			break

	for i in range(6):
		if(input1[i][1][1]=='O'):
			input2[1]=input1[i]
			break

	for i in range(6):
		if(input1[i][1][1]=='G'):
			input2[2]=input1[i]
			break

	for i in range(6):
		if(input1[i][1][1]=='W'):
			input2[3]=input1[i]
			break


	for i in range(6):
		if(input1[i][1][1]=='R'):
			input2[4]=input1[i]
			break




	for i in range(6):
		if(input1[i][1][1]=='B'):
			input2[5]=input1[i]
			break

	for i in range(6):
		for j in range(3):
			for k in range(3):
				if (input2[i][j][k]=='Y'):
					input2[i][j][k]='U'
				elif (input2[i][j][k]=='W'):
					input2[i][j][k]='D'
				elif (input2[i][j][k]=='O'):
					input2[i][j][k]='R'
				elif (input2[i][j][k]=='R'):
					input2[i][j][k]='L'
				elif (input2[i][j][k]=='G'):
					input2[i][j][k]='F'
				elif(input2[i][j][k]=='B'):
					input2[i][j][k]='B'

	b=''
	for i in range(6):
		for j in range(3):
			for k in range(3):
				b+=input2[i][j][k]

	a = kociemba.solve(b)
	a = a.replace("U","R L F2 B2 R' L' D R L F2 B2 R' L'")
	a = a.replace("U'","R L F2 B2 R' L' D' R L F2 B2 R' L'")
	a = a.replace("U2","R L F2 B2 R' L' D2 R L F2 B2 R' L'")
	return a
def cleansolution(solution):
    cleanedsolution=""
    prev=solution[0]
    for current in solution[1:]:
        if current=="'":
            cleanedsolution+=prev.lower()
        elif current=="2":
            cleanedsolution+=prev
            cleanedsolution+=prev
        else:
            cleanedsolution+=prev
        prev=current
    cleanedsolution = cleanedsolution.replace("'", "")
    cleanedsolution = cleanedsolution.replace("2", "")
    cleanedsolution = cleanedsolution.replace(" ", "")
    
    return cleanedsolution
print(cleansolution(sol(input1)))
