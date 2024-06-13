# This was a Joby Aviation practice question (for a flight sensor engineer intern position) that I absolutely bricked
# The Idea is, fed an input class, calculate a moving average on a numpy array

from collections import deque
import numpy as np

# from my memory, this is the basic setup of the input class
class Input:
    def __init__(self):
        self.stream = np.array([-1, 10, 23, 45, 6 ,7 -25, 3, 1, 5, 17])
        self.idx = 0
    
    def get(self):
        if self.idx < len(self.stream):
            output = self.stream[self.idx]
            self.idx += 1
            return output
        else:
            return None

class Window:
    def __init__(self, window):
        self.window = window
        self.buffer = deque([])
        self.sum = 0

    
    def avg1(self, val):
        self.buffer.append(val)
        self.sum += val

        if (len(self.buffer) < self.window):
            return(self.sum/self.window)
        else: 
            avg = self.sum/self.window
            self.sum -= self.buffer.popleft()
            return(avg)

def main():
    stream = Input()
    avg_window = Window(3)

    while True:
            val = stream.get()
            if val is None:
                break  # End of stream
            avg = avg_window.avg1(val)
            print(f"Moving average: {avg}")

if __name__ == '__main__':
    main()



        

            
        

        
