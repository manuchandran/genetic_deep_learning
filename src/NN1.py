import numpy as np
from nn_utils import sigmoid

learning_rate = 0.001


class NN1:
    def __init__(self, dataset, epochs, w=None, print_step=None):
        self.train_x, self.test_x, self.train_y, self.test_y = dataset
        self.l1_error = 0
        self.neurons = self.train_x.shape[1]
        self.Xavier = np.sqrt(1.0 / 2 * self.neurons)

        if w is None:
            self.w0 = 2 * np.random.random((self.neurons, 1)) - 1
        else:
            self.w0 = w[0]
        for j in xrange(1, epochs + 1):
            l1 = sigmoid(np.dot(self.train_x, self.w0))
            self.l1_error = self.train_y - l1

            if (print_step is not None) and (
                    (j % print_step == 0) or j == epochs):
                accuracy = self.calc_accuracy()
                print(
                    "{},{},{}".format(
                        j,
                        np.mean(
                            np.abs(
                                self.l1_error)),
                        accuracy))

            adjustment = self.l1_error * sigmoid(l1, deriv=True)
            self.w0 += self.train_x.T.dot(adjustment) * learning_rate

    def get_weights(self):
        return [self.w0]

    def get_error(self):
        return np.mean(np.abs(self.l1_error))

    def calc_accuracy(self):
        prime_y = sigmoid(np.dot(self.test_x, self.w0))
        y_error = self.test_y - prime_y
        return 1 - np.mean(np.abs(y_error)), np.std(y_error)
