import numpy as np
import math

def sigmoid(x):
    return 1/(1 + math.exp(-x))

class acorn():
    def __init__(self, A_inputs_number, B_inputs_number, n_outputs, hidden1, hidden2, hidden3, n_modularity,random=None ):
        self.n_neuron = n_neuron
        self.A_inputs = A_inputs
        self.B_inputs = B_inputs
        self.hidden1 = np.zeros([hidden1,1])
        self.hidden2 = np.zeros([hidden2,1])
        self.hidden3 = np.zeros([hidden3,1])
        self.n_outputs = n_outputs
        self.n_modularity = n_modularity

        # the given random_state might be either an actual RandomState object,
        # a seed or None (in which case we use numpy's builtin RandomState)
        if isinstance(random, np.random.RandomState):
            self.random_state_ = random
        elif random:
            try:
                self.random_state_ = np.random.RandomState(random_state)
            except TypeError as e:
                raise Exception("Invalid seed: " + str(e))
        else:
            self.random_state_ = np.random.mtrand._rand

        #make bias per each neuron per layer
        self.bias_1 = np.random_state_.rand([hidden1,1]) *2-1
        self.bias_2 = np.random_state_.rand([hidden2,1]) *2-1
        self.bias_3 = np.random_state_.rand([hidden3,1]) *2-1
        
        #make weight
        self.weight1 = np.random_state_.rand(self.A_inputs+self.B_inputs, self.hidden1) *2-1
        self.weight2 = np.random_state_.rand(self.hidden1, self.hidden2) *2-1
        self.weight3 = np.random_state_.rand(self.hidden2, self.hidden3) *2-1
        self.weight4 = np.random_state_.rand(self.hidden3, self.n_outputs) *2-1


    def _updata(self, weight):


    def modularity(self):

    def train(self):

    def test(self):

    def generartion(self):
        a = np.random.choice(["True","False"],p=[0.2,0.8])
        b = np.random.choice(["True","False"],p=[0.2,0.8])
        c = np.random.choice(["True","False"],p=[2/connection/100,1-])
        d = np.random.choice(["True","False"],p=[0.2,])
        e = np.random.choice(["True","False"],p=[0.2,])

        if a == "True":
            add_connection()
        if b == "True":
            remove_connection()
        if c == "True":
            change_weight()
        if d == "True":
            change_neuron_tyape()
        if e == "True":
            move_connection()
    def add_connection(self):

    def remove_connection(self):

        ele = np.random.randint(128)
        if ele < 80:
            a = int(ele/10))
            b = ele%10
            self.weight1[a][b] = 0
        elif ele < 120:
            ele = ele-80
            a = int(ele/14))
            b = ele%4
            self.weight1[a][b]=0

        elif ele < 128:
            ele = ele-120
            a = int(ele/2))
            b = ele%2
            self.weight3[a][b]=0

        self.weight1[np.random.mtrand.rand(*self.weight1.shape)<0.1] = 0
        self.weight2[np.random.mtrand.rand(*self.weight2.shape)<0.1] = 0
        self.weight3[np.random.mtrand.rand(*self.weight3.shape)<0.1] = 0

    def change_weight(self):

    def change_neuron_tyape(self):
    
    def move_connection(self):
