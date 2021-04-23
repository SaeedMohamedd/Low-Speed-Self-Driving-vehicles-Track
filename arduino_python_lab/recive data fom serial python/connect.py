# Importing Libraries
import serial
import time

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
def read_data():
    data = arduino.readline()
    return data        
while True:
  #  num = input("Enter a number: ") # Taking input from user
  #  value = write_read(num)
    value = read_data()
    line=value.decode('utf-8')
    print(line) # printing the value

    '''
    # importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()
'''