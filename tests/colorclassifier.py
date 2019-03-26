"""HSV VALUES

WILL VARY SLIGHTLY WITH RUBIKS CUBE,CAMERA AND LIGHTING CONDITIONS

Red:    H 165-180
        S 200-255
        V 0-255
Orange: H 0-9
        S 200-255
        V 0-255
White:  H 100-130
        S 0-100
        V 0-255
Yellow: H 10-35
        S 100-255
        V 0-255
Blue:   H 110-120
        S 200-255
        V 0-255
Green   H 60-109
        S 200-255
        V 0-255

As you may notice white and blue have intersecting blue values but vary in their saturation values

If lighting is not proper orange may be interpreted as red or vice versa

"""

#hsv ranges in list form [[min_h,min_s,min_v],[max_h,max_s,max_v]]
red_hsv=[[150,150,0],[190,255,120]]
orange_hsv=[[0,150,121],[15,215,200]]
white_hsv=[[100,0,0],[130,199,255]]
yellow_hsv=[[40,100,0],[70,255,255]]
blue_hsv=[[110,200,0],[149,255,255]]
green_hsv=[[70,200,0],[109,255,255]]


cube=[]





import cv2
import numpy as np
cap=cv2.VideoCapture(0)
_,frame=cap.read()
height,width,_=frame.shape


square_size_factor=0.4#fraction of height of image that square occupies
square_x1=int((width-((square_size_factor)*height))/2)#coordinate calculation for square corners
square_x2=int((width+((square_size_factor)*height))/2)


square_y1=int(((1-square_size_factor)/2)*height)
square_y2=int(((1+square_size_factor)/2)*height)

cube_dimension=square_y2-square_y1#height and width of cube in pixels
def classify(colors):
    import numpy as np
    N = 6*9
    
    def remove_indices(arr, ind):
        arr2 = [ele for ele in arr if ele[1] not in ind]
        return arr2

    colors = np.array(colors)
    
    colour_index = {'white': [], 'green': [], 'blue': [],
                'red':[], 'yellow':[], 'orange':[]}
    
    hue = list(zip(colors[:, 0].tolist(), range(N)))
    sat = list(zip(colors[:, 1].tolist(), range(N)))
    val = list(zip(colors[:, 2].tolist(), range(N)))

    hue.sort()
    sat.sort()
    val.sort()

    #whites
    sat.reverse()

    for i in range(int(N/6)):
        color = sat[i]
        colour_index['white'].append(color[1])

    hue = remove_indices(hue, colour_index['white'])
    sat = remove_indices(sat, colour_index['white'])
    val = remove_indices(val, colour_index['white'])

    #red
    dist_index = np.argsort(np.abs(colors[:,0]))

    for i in range(int(N/6)):
        colour_index['red'].append(dist_index[i])

    hue = remove_indices(hue, colour_index['red'])
    sat = remove_indices(sat, colour_index['red'])
    val = remove_indices(val, colour_index['red'])

    del dist_index

    #orange
    hue.sort()

    for i in range(int(N/6)):
        colour_index['orange'].append(hue[i][1])

    hue = remove_indices(hue, colour_index['orange'])
    sat = remove_indices(sat, colour_index['orange'])
    val = remove_indices(val, colour_index['orange'])

    #yellow
    hue.sort()

    for i in range(int(N/6)):
        colour_index['yellow'].append(hue[i][1])

    hue = remove_indices(hue, colour_index['yellow'])
    sat = remove_indices(sat, colour_index['yellow'])
    val = remove_indices(val, colour_index['yellow'])

    #green
    hue.sort()

    for i in range(int(N/6)):
        colour_index['green'].append(hue[i][1])

    hue = remove_indices(hue, colour_index['green'])
    sat = remove_indices(sat, colour_index['green'])
    val = remove_indices(val, colour_index['green'])

    #blue
    hue.sort()

    for i in range(int(N/6)):
        colour_index['blue'].append(hue[i][1])

    hue = remove_indices(hue, colour_index['blue'])
    sat = remove_indices(sat, colour_index['blue'])
    val = remove_indices(val, colour_index['blue'])

    output_colors = [0]*N

    for col in colour_index:
        l = colour_index[col]
        for i in l:
            output_colors[i] = col[0].upper()
    
    return output_colors


def find_color(h,s,v):#finds color given h,s,v values(average)
    if red_hsv[0][0]<=h<=red_hsv[1][0] and red_hsv[0][2]<=v<=red_hsv[1][2]:
        return "r"
    elif (orange_hsv[0][0]<=h<=orange_hsv[1][0] or 170<=h<=180) and orange_hsv[0][2]<=v<=orange_hsv[1][2]:
        return "o"
    elif yellow_hsv[0][0]<=h<=yellow_hsv[1][0]:
        return "y"
    elif green_hsv[0][0]<=h<=green_hsv[1][0]:
        return "g"
    elif white_hsv[0][0]<=h<=white_hsv[1][0] and white_hsv[0][1]<=s<=white_hsv[1][1]:
        return "w"
    elif blue_hsv[0][0]<=h<=white_hsv[1][0] and blue_hsv[0][1]<=s<=blue_hsv[1][1]:
        return "b"    
    else:
        print("h ",h," s ",s," v ",v,"colour not recognised")


def find_face_colors(face_hsv):#finds color of each tile and forms a 2d array of the face
    face_colors=[]
    for row in face_hsv:
        row_colors=[]
        for tile in row:
            
            row_colors.append(find_color(tile[0],tile[1],tile[2]))
        face_colors.append(row_colors)
    return face_colors



def find_avg_hsv(img):#given the cropped image of cube face finds the hsv values of each cybie(or tile) and forms a 3d array of hsv values
        
    tile_dimension=int(cube_dimension/3)#as cube face has 9(3x3) tiles
    tile_factor=0.3#factor of area where colour will be found(tile roi)
    tile_roi_start=int(((1-tile_factor)/2)*tile_dimension)#pixels to start of bounding rectangle of tile roi
    tile_roi_end=int((tile_dimension*tile_factor)+tile_roi_start)#pixels to end of bounding rectangle of tile roi
    
    tile_roi=[]#list which will hold roi (in image form) of all individual tiles
    for j in range(3):
        row=[]
        for i in range(3):
            row.append(img[(j*tile_dimension)+tile_roi_start:(j*tile_dimension)+tile_roi_end,(i*tile_dimension)+tile_roi_start:(i*tile_dimension)+tile_roi_end])#roi finding math
            cv2.rectangle(img, ((i*tile_dimension)+tile_roi_start,(j*tile_dimension)+tile_roi_start), ((i*tile_dimension)+tile_roi_end,(j*tile_dimension)+tile_roi_end), (255,0,0), 1)#draws rectangle on each tile roi
        tile_roi.append(row)
    cv2.imshow("check",img)
    hsv_avg=[]#list which will hold avg hsv value of each tile
    #bgr_avg=[]
    #h_all=set()
    #s_all=set()
    #v_all=set()
    for row_iterable in tile_roi:
        row=[]
        bgr_row=[]
        for col_iterable in row_iterable:
            b_avg,g_avg,r_avg,_=np.uint8(cv2.mean(col_iterable))#averages bgr value in roi
            color=cv2.cvtColor(np.uint8([[[b_avg,g_avg,r_avg]]]),cv2.COLOR_BGR2HSV)#converts bgr value to corresponding hsv
            h_avg= color[0][0][0]
            s_avg= color[0][0][1]
            v_avg= color[0][0][2]

            #h_all.add(h_avg)
            #s_all.add(s_avg)
            #v_all.add(v_avg)

            #bgr_row.append([b_avg,g_avg,r_avg])
            row.append([h_avg,s_avg,v_avg])
        hsv_avg.append(row)
    return hsv_avg
        #bgr_avg.append(bgr_row)
    #print(hsv_avg)
    
    #print(bgr_avg)
    #print("h",min(h_all),max(h_all))
    #print("s",min(s_all),max(s_all))
    #print("v",min(v_all),max(v_all))
    

    

while True:
    _,frame=cap.read()
    
    cv2.rectangle(frame, (square_x1, square_y1), (square_x2, square_y2), (255,0,0), 2)#cube should be placed within this square



    cv2.imshow("original",frame)
    k=cv2.waitKey(1) & 0xff
    if k==27:#ESC is pressed
        break
    elif k==32:#SPACE is pressed
        print("Image Captured")
        
        
        cube_roi=frame[square_y1:square_y2,square_x1:square_x2]#image of cube only
        
        cube.append((find_avg_hsv(cube_roi)))
        
        print(find_face_colors(find_avg_hsv(cube_roi)))#calls all the functions
    elif k==ord('s'):
        newcube=[]
        for i in cube:
            for j in i:
                for k in j:
                    newcube.append(k)

        print(classify(newcube))




cap.release()
cv2.destroyAllWindows()
