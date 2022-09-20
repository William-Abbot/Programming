#mini project 1
#William Abbot 

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from math import sqrt
import numpy as np
from sklearn.model_selection import train_test_split
import re

color = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

#iris data
iris = open('iris.scale.txt')
counter = 0
label = 0
featureList = []
iris_data = np.zeros((150, 4))
buffer = ''
iris_labels = np.zeros(150)

for j in range(150):
    featureList = []
    counter = 0
    label = 0
    buffer = ''
    string = iris.readline()
    for i in range(len(string)):
        if string[i] != ' ':
            buffer+=string[i]
        else:
            counter += 1
            if counter == 1:
                label = int(buffer)
            else:
                featureList.append(float(buffer[2:]))
            buffer = ''
    if len(featureList) < 4:
        featureList.insert(1, 0.0)
    iris_data[j] = featureList
    iris_labels[j] = label

    

#a4a data
a4a_train = open('a4a.txt')
a4a_test = open('a4a.t.txt')
a4a_train_data = np.zeros((500, 14))
a4a_test_data = np.zeros((500, 14))
buffer1 = ''
buffer2 = ''
a4a_test_labels = np.zeros(500)
a4a_train_labels = np.zeros(500)
regex = re.compile(r'(\d+)(:)(\d)')

for j in range(500):
    featureList1 = []
    featureList2 = []
    counter1 = 0
    counter2 = 0
    test_label = 0
    train_label = 0
    buffer1 = ''
    buffer2 = ''
    string1 = a4a_train.readline()
    string2 = a4a_test.readline()
    for i in range(len(string1)):
        if string1[i] != ' ':
            buffer1+=string1[i]
        else:
            counter1 += 1
            if counter1 == 1:
                train_label = float(buffer1)
            else:
                mo = regex.search(buffer1)
                featureList1.append(float(mo.group(1)))
            buffer1 = ''
    for i in range(len(string2)):
        if string2[i] != ' ':
            buffer2+=string2[i]
        else:
            counter2 += 1
            if counter2 == 1:
                test_label = float(buffer2)
            else:
                mo = regex.search(buffer2)
                featureList2.append(float(mo.group(1)))
            buffer2 = ''
    #pad with zeros
    if len(featureList1) < 14:
        for i in range(14-len(featureList1)):
            featureList1.append(0)
    if len(featureList2) < 14:
        for i in range(14-len(featureList2)):
            featureList2.append(0)
    
    a4a_train_data[j] = featureList1
    a4a_test_data[j] = featureList2
    a4a_train_labels[j] = train_label
    a4a_test_labels[j] = test_label



#distance methods
def euclidean_distance(x, y):
    return sqrt(np.sum((x-y)**2))

def manhattan_distance(x, y):
    return sum(abs(a-b) for a, b in zip(x, y))


#for finding nearest neighbor
def most_frequent(List): 
    return max(set(List), key = List.count)


#knn
class KNN:

    def __init__(self, k=3, distanceMethod=0):
        self.k = k
        self.distanceMethod = distanceMethod

    def train(self, X, y):
        self.X = X
        self.labels = y
    
    def set_distance_method(self, method):
        self.distanceMethod = method
    
    def predict(self, X):
        p_labels = list()
        for x in X:
            k_neighbors = self.get_neighbors(x)
            p_labels.append(most_frequent(k_neighbors))
        return p_labels
    
    def get_neighbors(self, x):
        if self.distanceMethod == 0:
            distances = [euclidean_distance(x, x2) for x2 in self.X]
        else:
            distances = [manhattan_distance(x, x2) for x2 in self.X]
        k_idx = np.argsort(distances)[:self.k]
        return([self.labels[i] for i in k_idx])



#perceptron
class perceptron:

    def __init__(self, lr=0.1, N=100):
        self.lr = lr
        self.N = N
        self.w = None
        self.bias = None
        self.missclassified = list()
        self.a = self.activate_boundary
    
    def train(self, D, f):
        self.w = np.zeros(D.shape[1])
        self.bias = 0
        for i in range(self.N):
            error_buffer = 0
            for x, y in zip(D, f):
                update = self.lr*(y - self.predict(x))
                self.bias += update
                self.w += update * x
                error_buffer += int(update != 0.0)
            
            self.missclassified.append(error_buffer)
        
        
    def predict(self, X):
        a_param = np.dot(X, self.w) + self.bias
        return self.a(a_param)
    
    def activate_boundary(self, x):
        return np.where(x<=0.0, -1, 1)


def error(y, y_hat):
    error = np.sum(y == y_hat) / len(y_hat)
    return error



X_train_iris, X_hat_iris, y_train_iris, y_hat_iris = train_test_split(iris_data, iris_labels, test_size=0.3, random_state=4872011)



knn0 = KNN(k=10, distanceMethod=0)
knn0.train(X_train_iris, y_train_iris)
prediction = knn0.predict(X_hat_iris)

knn1 = KNN(k=10, distanceMethod=1)
knn1.train(X_train_iris, y_train_iris)
prediction1 = knn1.predict(X_hat_iris)

knn2 = KNN(k=10, distanceMethod=0)
knn2.train(a4a_train_data, a4a_train_labels)
prediction2 = knn2.predict(a4a_test_data)

knn3 = KNN(k=10, distanceMethod=1)
knn3.train(a4a_train_data, a4a_train_labels)
prediction3 = knn3.predict(a4a_test_data)


print("euclidean KNN classification accuracy (iris): ", error(y_hat_iris, prediction))
print("manhattan KNN classification accuracy (iris): ", error(y_hat_iris, prediction1))
print("euclidean KNN classification accuracy (a4a): ", error(a4a_test_labels, prediction2))
print("manhattan KNN classification accuracy (a4a): ", error(a4a_test_labels, prediction3))
print(" ")



iris_per = perceptron(lr=0.1, N=1000)
iris_per.train(X_train_iris, y_train_iris)
per_prediction_iris = iris_per.predict(X_hat_iris)

a4a_per = perceptron(lr=0.1, N=1000)
a4a_per.train(a4a_train_data, a4a_train_labels)
per_prediction_a4a = a4a_per.predict(a4a_test_data)

print("Perceptron classification accuracy (iris): ", error(y_hat_iris, per_prediction_iris))
print("Perceptron classification accuracy (a4a): ", error(a4a_test_labels, per_prediction_a4a))



plt.figure()
plt.scatter(iris_data[:, 1], iris_data[:, 3], c=iris_labels, cmap=color, edgecolor='k', s=20)
plt.xlabel('2')
plt.title('iris KNN feature graph')
plt.ylabel('4')
plt.show()



