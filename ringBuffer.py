import numpy as np


class RingBuffer:

    def __init__(self, bufferLength):
        self.bufferLength = bufferLength
        self._data = np.zeros(self.bufferLength)
        self.pointer = 0
        self.fullFlag = False
        
        self.getNotFull = lambda : self._data
        self.getFull = lambda : np.append(self._data[self.pointer:], self._data[:self.pointer])
        self.getBuff = lambda : self.getFull() if  self.fullFlag else np.roll(self.getNotFull(),self.bufferLength-self.pointer)

        self.get = lambda : np.flip(self.getBuff(),0)
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
