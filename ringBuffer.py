import numpy as np


class RingBuffer:

    def __init__(self, bufferLength):
        self.bufferLength = bufferLength
        self._data = np.zeros(self.bufferLength)
        self.pointer = 0
        self.fullFlag = False
        self.get = lambda : self.getFull() if  self.fullFlag else np.roll(self.getNotFull(),self.bufferLength-self.pointer)
        self.append = lambda x : self.appendFull(x) if self.fullFlag else self.appendNotFull(x)

        

    def appendNotFull(self, sample):
        # add an element at the pointer location in the buffer
        self._data[self.pointer] = sample
        self.pointer += 1
        
        if self.pointer == self.bufferLength:
            self.pointer = 0    
            self.fullFlag = True    

    def appendFull(self, sample):
        # add an element overwriting the oldest one.
        self._data[self.pointer] = sample
        self.pointer = (self.pointer+1) % self.bufferLength

    def getNotFull(self):
        return self._data

    def getFull(self):
        # correct the order of the _data
        return np.append(self._data[self.pointer:], self._data[:self.pointer])

    @property
    def data(self):
        return self._data


# sample usage
if __name__=='__main__':
    x=RingBuffer(5)
    print(x.data, x.get(), np.flip(x.get(),0))
    x.append(1)
    print(x.data, x.get(), np.flip(x.get(),0))
    x.append(2)
    print(x.data, x.get(), np.flip(x.get(),0))
    x.append(3)
    print(x.data, x.get(), np.flip(x.get(),0))
    x.append(4)
    print(x.data, x.get(), np.flip(x.get(),0))
    x.append(5)
    print(x.data, x.get(), np.flip(x.get(),0))
    x.append(6)
    print(x.data, x.get(), np.flip(x.get(),0))
    x.append(7)
    x.append(8)
    print(x.data, x.get(), np.flip(x.get(),0))
    x.append(9)
    x.append(10)
    x.append(11)
    print(x.data, x.get(), np.flip(x.get(),0))
