import numpy as np

class RingBuffer:

    def __init__(self, bufferLength):
        self.bufferLength = bufferLength
        self._data = np.zeros(self.bufferLength)
        self.pointer = 0

    def append(self, sample):
        # add an element overwriting the oldest one.
        self._data[self.pointer] = sample
        self.pointer = np.mod((self.pointer+1), self.bufferLength)

    @property
    def data(self):
        return self._data
    
    @property
    def getFlippedBuffer(slef):
        return np.concatenate((self._data[self.pointer:], self._data[:self.pointer]))
    
    @property
    def getBuffer(self):
        return np.flipud(self.getFlippedBuffer)
    
    def clear(self):
        self._data = np.zeros(self.bufferLength)
        self.pointer = 0
        

# sample usage
if __name__=='__main__':
    x=RingBuffer(5)
    print(x.data, x.getBuffer)
    x.append(1)
    print(x.data, x.getBuffer)
    x.append(2)
    print(x.data, x.getBuffer)
    x.append(3)
    print(x.data, x.getBuffer)
    x.append(4)
    print(x.data, x.getBuffer)
    x.append(5)
    print(x.data, x.getBuffer)
    x.append(6)
    print(x.data, x.getBuffer)
    x.append(7)
    x.append(8)
    print(x.data, x.getBuffer)
    x.append(9)
    x.append(10)
    x.append(11)
    print(x.data, x.getBuffer)
