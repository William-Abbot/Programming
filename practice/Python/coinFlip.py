import random
#import matplotlib.pyplot as plt


def flipCoin():
    return random.choice([0,1])



if __name__ == '__main__':

    X = list([0]*(int(input('Enter number of times you want to flip a coin: '))))

    '''
    xAxis = range(0,len(X), int(len(X)/10))
    '''

    sum = 0

    for i in range(len(X)):
        y = flipCoin()
        if y == 1: #if coinflip() returns 1, then replace the next 0 in X with a 1
            X[sum] = 1 
            sum += 1

    total_zeros = len(X) - sum
    
    '''
    if sum >= 100:
        plt.plot(X)
        plt.show()
    '''
    
    print(str((sum/len(X))*100)+'% of coin flips are heads')
    print(str((total_zeros/len(X))*100)+'% of coin flips are tails')
    