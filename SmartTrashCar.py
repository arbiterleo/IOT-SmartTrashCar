import RPi.GPIO as gpio
import time
from flask import Flask, render_template, Response, request
from collections import deque

N1 = 31
N2 = 33
N3 = 35
N4 = 37

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(N1, gpio.OUT)
gpio.setup(N2, gpio.OUT)
gpio.setup(N3, gpio.OUT)
gpio.setup(N4, gpio.OUT)
pwm1 = gpio.PWM(N2, 100)
pwm2 = gpio.PWM(N3, 100)


app = Flask(__name__)

stack = []


@app.route('/')

def controll():
    return render_template('controll.html')

def index():
    return render_template('index.html')


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(N1, gpio.OUT)
    gpio.setup(N2, gpio.OUT)
    gpio.setup(N3, gpio.OUT)
    gpio.setup(N4, gpio.OUT)

@app.route('/call', methods=['GET', 'POST'])
def call():

    temp = deque(stack)
    while(temp):
        act = temp.popleft()

        if(act == 1):
            forward()

        elif(act == 2):
            back()

        elif(act == 3):
            left()

        elif(act == 4):
            right()

@app.route('/return', methods=['GET', 'POST'])
def callback():

    temp = stack
    while(temp):
        act = temp.pop()

        if(act == 1):
            forward()

        elif(act == 2):
            back()

        elif(act == 3):
            left()

        elif(act == 4):
            right()


@app.route('/forward', methods=['GET', 'POST'])
def forward():

    stack.append(1)
    
    init()

    gpio.output(N1, False)
    gpio.output(N2, True)
    gpio.output(N3, True)
    gpio.output(N4, False)
    time.sleep(0.5)

    stop()
    autoBack(0.5)
    return render_template('index.html')


@app.route('/back', methods=['GET', 'POST'])
def back():

    stack.append(2)
    gpio.cleanup()
    init()
    gpio.output(N1, True)
    gpio.output(N2, False)
    gpio.output(N3, False)
    gpio.output(N4, True)
    return render_template('index.html')


@app.route("/left", methods=['GET', 'POST'])
def left():

    stack.append(3)

    gpio.cleanup()
    init()
    gpio.output(N1, False)
    gpio.output(N2, True)
    gpio.output(N3, False)
    gpio.output(N4, True)
    return render_template('index.html')


@app.route("/right", methods=['GET', 'POST'])
def right():

    stack.append(4)
    
    gpio.cleanup()
    init()
    gpio.output(N1, True)
    pwm1.stop()
    pwm2.start(0)
    pwm2.ChangeDutyCycle(90)
    gpio.output(N4, False)
    return render_template('index.html')


@app.route("/stop", methods=['GET', 'POST'])
def stop():

    init()
    gpio.output(N1, False)
    gpio.output(N4, False)
    gpio.cleanup()
    pwm1.stop()
    pwm2.stop()
    return render_template('index.html')


def autoBack(t):
    gpio.cleanup()
    init()
    gpio.output(N1, True)
    gpio.output(N2, False)
    gpio.output(N3, False)
    gpio.output(N4, True)
    time.sleep(t)
    gpio.cleanup()

def speed():
    value = request.form['speed']
    speed = int(value)*10
    pwm1.ChangeDutyCycle(speed)
    pwm2.ChangeDutyCycle(speed)
    print("value", value)
    return render_template('index.html')


@app.route('/controlSpeed', methods=['POST'])
def controlSpeed():
    value = request.form['speed']
    speed = int(value)*10

    init()

    while(distance() > 25):
        gpio.output(N1, False)
        pwm1.start(0)
        pwm1.ChangeDutyCycle(speed)
        pwm2.start(0)
        pwm2.ChangeDutyCycle(speed)
        gpio.output(N4, False)
        time.sleep(0.5)

    stop()
    autoBack(0.5)
    return render_template('index.html')


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
