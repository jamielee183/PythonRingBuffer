import numpy as np





class RingBuffer:

    def __init__(self, bufferLength):
        self.bufferLength = bufferLength
        self._data = np.zeros(self.bufferLength)
        self.pointer = 0
        self.getNotFull = lambda : self._data
        self.getBuff = lambda : np.append(self._data[self.pointer:], self._data[:self.pointer])
        self.get = lambda : np.flip(self.getBuff(),0)


    def append(self, sample):
        # add an element overwriting the oldest one.
        self._data[self.pointer] = sample
        self.pointer = (self.pointer+1) % self.bufferLength

    @property
    def data(self):
        return self._data

# sample usage
if __name__=='__main__':
    x=RingBuffer(5)
    print(x.data, x.get())
    x.append(1)
    print(x.data, x.get())
    x.append(2)
    print(x.data, x.get())
    x.append(3)
    print(x.data, x.get())
    x.append(4)
    print(x.data, x.get())
    x.append(5)
    print(x.data, x.get())
    x.append(6)
    print(x.data, x.get())
    x.append(7)
    x.append(8)
    print(x.data, x.get())
    x.append(9)
    x.append(10)
    x.append(11)
    print(x.data, x.get())
