"""Rubiks cube implementation on python
Initial orientation
0 front: red
1 top: yellow
2 right:green
3 bottom: yellow
4 left: blue
5 back: orange



"""
front=[['r','r','r'],['r','r','r'],['r','r','r']]


top=[['y','y','y'],['y','y','y'],['y','y','y']]
right=[['g','g','g'],['g','g','g'],['g','g','g']]
bottom=[['w','w','w'],['w','w','w'],['w','w','w']]
left=[['b','b','b'],['b','b','b'],['b','b','b']]
back=[['o','o','o'],['o','o','o'],['o','o','o']]

cube=[front,top,right,bottom,left,back]
def facerotate(a):
    ftemp=[0,0,0]#temp list for face rotation
    for i in range(3):
        
        ftemp[i]=cube[a][0][i]
    for i in range(3):
        
        cube[a][0][i]=cube[a][2-i][0]
    for i in range(3):
        
        cube[a][i][0]=cube[a][2][i]
    for i in range(3):
        
        cube[a][2][i]=cube[a][2-i][2]
    for i in range(3):
        
        cube[a][i][2]=ftemp[i]
    #each face(front, top, bottom..)has updated values even though they have not been explicitly changed
def f():#clockwise front face turn
    global cube,front,top,right,bottom,left,back
    temp=[0,0,0]#temp list
    for i in range(3):
        
        temp[i]=top[2][i] 
    for i in range(3):
        
        top[2][i]=left[2-i][2]
    for i in range(3):
        
        left[i][2]=bottom[0][i]
    for i in range(3):
        
        bottom[0][i]=right[2-i][0]
    for i in range(3):
        
        right[i][0]=temp[i]

    facerotate(0)


def r():
    global cube,front,top,right,bottom,left,back
    temp=[0,0,0]#temp list
    for i in range(3):
        
        temp[i]=top[2-i][2] 
    for i in range(3):
        
        top[2-i][2]=front[2-i][2]
        
    for i in range(3):
        
        front[2-i][2]=bottom[2-i][2]
    for i in range(3):
        
        bottom[2-i][2]=back[i][0]
    for i in range(3):
        
        back[i][0]=temp[i]

    facerotate(2)

    

    


def l():
    global cube,front,top,right,bottom,left,back
    temp=[0,0,0]#temp list
    for i in range(3):
        
        temp[i]=top[i][0] 
    for i in range(3):
        
        top[i][0]=back[2-i][2]
        
    for i in range(3):
        
        back[2-i][2]=bottom[i][0]
    for i in range(3):
        
        bottom[i][0]=front[i][0]
    for i in range(3):
        
        front[i][0]=temp[i]

    facerotate(4)
def u():
    global cube,front,top,right,bottom,left,back
    temp=[0,0,0]#temp list
    for i in range(3):
        
        temp[i]=back[0][2-i] 
    for i in range(3):
        
        back[0][2-i]=left[0][2-i]
        
    for i in range(3):
        
        left[0][2-i]=front[0][2-i]
    for i in range(3):
        
        front[0][2-i]=right[0][2-i]
    for i in range(3):
        
        right[0][2-i]=temp[i]

    facerotate(1)
def d():
    global cube,front,top,right,bottom,left,back
    temp=[0,0,0]#temp list
    for i in range(3):
        
        temp[i]=front[2][i] 
    for i in range(3):
        
        front[2][i]=left[2][i]
        
    for i in range(3):
        
        left[2][i]=back[2][i]
    for i in range(3):
        
        back[2][i]=right[2][i]
    for i in range(3):
        
        right[2][i]=temp[i]

    facerotate(3)
def b():
    global cube,front,top,right,bottom,left,back
    temp=[0,0,0]#temp list
    for i in range(3):
        
        temp[i]=top[0][2-i] 
    for i in range(3):
        
        top[0][2-i]=right[2-i][2]
    for i in range(3):
        
        right[2-i][2]=bottom[2][i]
    for i in range(3):
        
        bottom[2][i]=left[i][0]
    for i in range(3):
        
        left[i][0]=temp[i]

    facerotate(5)
def askalgorithm():
    moves=list(input("ENTER ALGORITHM : "))

    for j in range(len(moves)):
        if moves[j]=="'":
            eval(moves[j-1]+"()")
            eval(moves[j-1]+"()")
        elif moves[j]==" ":
            pass
            
        else:
            eval(moves[j]+"()")
askalgorithm()

