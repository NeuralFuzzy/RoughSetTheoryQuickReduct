from random import seed
from random import randrange
from random import random
from csv import reader
from math import exp
from sklearn.metrics import confusion_matrix
import numpy as np
import math
from itertools import combinations

def load_csv(filename):
        dataset = list()
        with open(filename, 'r') as file:
                csv_reader = reader(file)
                for row in csv_reader:
                        if not row:
                                continue
                        dataset.append(row)
        return dataset
 
# Convert string column to float
def str_column_to_float(dataset, column):
        for row in dataset:
                try:
                        row[column] = float(row[column].strip())
                except ValueError:
                        print("Error with row",column,":",row[column])
                        pass
 
# Convert string column to integer
def str_column_to_int(dataset, column):        
        for row in dataset:
                row[column] = int(row[column])


def dependency(dataset,num):
        total=0
        dependency=0
        for j in range(3):        
                fold=list()
                for i in range(len(dataset)):                        
                        data=dataset[i]
                        #print(i)
                        if data[-1]==j:
                                fold.append(dataset[i])
                #print("Fold {}".format(fold))
                count=len(fold)
                #print("count {}".format(count))
                for k in range(len(fold)):
                        list1=fold[k]                
                        for l in range(len(dataset)):
                                #print("len{}".format(len(fold)))
                                list2=dataset[l]
                                if list1[:num]==list2[:num] and list1[-1]!=list2[-1]:                                        
                                        count = count-1
                                        #print("Count inside {}".format(count))
                                        break
                total=total+count
                #print("total {}",format(total))
        dependency=total/len(dataset)
        #print("{}".format(dependency))
        return dependency

def generate_new_dataset(row,l):
        #print(row)       
        X = np.empty((8, 0))
        #print(X)
        for i in range(len(row)):
                col=row[i]
                x=[row_new[col] for row_new in dataset]
                x=np.array([x])
                #print(np.transpose(x))
                #print(x)
                x=x.T
                X=np.append(X, x, axis=1)
        x=[row[-1] for row in dataset]
        X=np.append(X, [[x[0]],[x[1]],[x[2]],[x[3]],[x[4]],[x[5]],[x[6]],[x[7]]], axis=1)
        X=np.array(X).tolist()
        #print("X {}".format(X))
        return X
        
      
filename = 'TestData.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])-1):
        str_column_to_float(dataset, i)
# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)
#print(dataset)
#this is fuzzify input based on class belongin granulation
dp=dependency(dataset,4)

n=4
initial_val=[0,1,2,3]
comb=combinations([0,1,2,3],3)

co=[i for i in combinations([0,1,2,3],3)]
c=len(co)

while n>1 :
        for row in  comb:
                
                data_X=generate_new_dataset(row,len(row))
                #print(data_X)
                dp_data_X=dependency(data_X,len(row))
                
                if dp > dp_data_X:
                        c=c-1                        
                        continue                
                else:
                        n=n-1
                        prev_row=row
                        
                        break
        if c == 0:
                break
        comb=combinations(row,n)
        comb_temp=[i for i in combinations(row,n)]
        c=len(comb_temp)
        
                
print("final reduct {}".format(prev_row))
        


        
        

        
