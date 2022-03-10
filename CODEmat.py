row = int(input("enter number of rows: "))
col = int(input("enter number of columns: "))
Mat = []
for i in range (0,col):
    Mat.append([])
for i in range (0,row):
    for j in range(0,col):
        Mat[i].append(j)

#asking for integers in matrix
for i in range (0,row):
    print('Enter integer for row-',i+1)
    for j in range (0,col):
        print('column-',j+1)
        Mat[i][j] = int(input())
Mat_org = Mat
print(Mat_org)

#taking determinant
det = Mat[0][0] * Mat[1][1] - Mat[0][1] * Mat[1][0]
print('The Determinant is: ',det)

#switching sides after taking determinant
Mat[0][1]=(Mat[0][1]*(-1))
Mat[1][0]=(Mat[1][0]*(-1))
x = Mat[0][0]
Mat[0][0] = Mat[1][1]
Mat[1][1] = x
print('The Adjoint is:',Mat)

#multiplying matrix with 1/determinant
Inv = [[Mat[0][0]/det, Mat[0][1]/det],
                [Mat[1][0]/det, Mat[1][1]/det]]

print("_Inverse_")
for a in range(len(Inv)):
    for b in Inv:
        print(b[a], end ='  ')
    print()

#multiply Mat with Inverse
identity = [[Inv[0][0]*Mat_org[0][0] + Inv[0][1]*Mat_org[1][0], Inv[0][0]*Mat_org[0][1] + Inv[0][1]*Mat_org[1][1]],
                    [Inv[1][0]*Mat_org[0][0] + Inv[1][1]*Mat_org[1][1], Inv[1][0]*Mat_org[0][1] + Inv[1][1]*Mat_org[1][1]]]
print("Identity Matrix after multiplying matrix with inverse: ",identity)
