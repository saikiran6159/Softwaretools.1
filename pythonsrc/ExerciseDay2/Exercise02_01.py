# import numpy package
import numpy as np

# function for calculate the mean and deviation of a matrix
def cal(matrix):
    Total_mean = np.mean(matrix)  # cal mean of the array
    Total_std = np.std(matrix)    # cal the standard deviation of the array

    column_mean = np.mean(matrix,axis=0)   # cal the mean of the individual column of the array
    column_std =  np.std(matrix,axis=0)    # cal the standard deviation of the individual coloumn
    return Total_mean,Total_std,column_mean,column_std

matrix = np.random.uniform(0,4,size=(200,3))    # define the matrix(200*3)
Total_mean,Total_std,column_mean,column_std = cal(matrix)     # function  calling

# printing all required answers
print(' the mean of the array is : ' , Total_mean)
print(' the standard deviation of the array :' , Total_std)
print(' the  mean of the individual columns :' , column_mean)
print(' the standard deviation of the individual columns : ', column_std)

