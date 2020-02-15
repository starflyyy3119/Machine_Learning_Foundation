import numpy as np
import copy 
import random

def open_file(file_name):
        f = open(file_name, "r")
        lines = f.readlines()
        m = len(lines)

        X = np.ones((m, 5))
        Y = np.zeros((m,), dtype = int)

        for i in range(m):
            line = lines[i]
            line_temp1 = line.strip("\n")
            line_temp2 = line_temp1.split(" ")
            for j in range(3):
                X[i][j+1] = float(line_temp2[j])
            line_temp3 = line_temp2[3]
            line_temp4 = line_temp3.split("\t")
            X[i][4] = float(line_temp4[0])
            Y[i] = int(line_temp4[1])
        return X, Y

def sign(x):
    if (x > 0):
        return 1
    else :
        return -1

class Pocket:
    def error_train(self, w):
        sum = 0
        for i in range(self.sample_num):
            inner_product = np.dot(self.X_train[i, :], w)
            if (sign(inner_product) != self.Y_train[i]):
                sum = sum + 1
        ratio = sum / self.sample_num
        return ratio
    
    def assign_value(self, a, b):                                               # np.array 如果直接赋值的话： 如 self.best_w = self.w 是浅拷贝, 仅仅是引用
        for i in range(self.size_of_each_example):                        # self.best_w 指向了 self.w 所指的对象，当后面self.w 更新的时候，也会改变
            a[i] = b[i]                                                                # self.best_w
    def error_test(self, w):
        sum = 0
        for i in range(X_test.shape[0]):
            inner_product = np.dot(self.X_test[i, :], w)
            if (sign(inner_product) != self.Y_test[i]):
                sum = sum + 1
        ratio = sum / X_test.shape[0]
        return ratio
        
    def __init__(self, max_iter):
        
        # maximum iterations
        self.max_iter = max_iter
        
        # open the training set and test set
        self.X_train, self.Y_train = open_file("pocket_train.txt")
        self.X_test, self.Y_test = open_file("pocket_test.txt")
        
        # get the sample number and the size of each example
        self.sample_num = self.X_train.shape[0]
        self.size_of_each_example = self.X_train.shape[1]
        
        # initialize
        self.w = np.zeros((self.size_of_each_example,))
        self.best_w = np.zeros((self.size_of_each_example,))
        self.best_error_rate = self.error_train(self.best_w)
        
        # now iteration 
        t = 0
        while (t < self.max_iter):
            index = random.randint(0, self.sample_num-1)
            sample = self.X_train[index, :]
            true_value = self.Y_train[index]
            inner_product = np.dot(sample, self.w)
            if (sign(inner_product) != true_value):
                t = t + 1
                self.w = self.w + true_value * sample
                self.w_error = self.error_train(self.w)
                if (self.w_error <= self.best_error_rate):
                    self.assign_value(self.best_w, self.w)
                    self.best_error_rate = self.error_train(self.best_w)
                    print(self.best_error_rate)
        print("test_error = ",self.error_test(self.best_w))

        
if __name__ == '__main__':
    pocket = Pocket(100)