# PWM - pulse width modulation
import RPi.GPIO as GPIO
import time
import pygame
import math
from datetime import datetime


#   initializing

#time.sleep(30)
GPIO.setmode(GPIO.BOARD)
#GPIO.cleanup()
  
green1=12 ; blue1=15 ; yellow1 = 7 ; red1 = 16; yellow2 = 29; red2 = 31; green2=11; blue2 = 32
LED = [green1,blue1,yellow1,red1,yellow2, red2, green2, blue2]
freqLed = 200
max = 80
timeSleep = 0.5
deltaGrad = 40musicFileShort = "Knight-Rider-Theme-Song.mp3"
musicFile1 = "LS_Carol.mp3"
musicFile2 = "F1_forget.mp3"
musicFile3 = "F2_into_unknown.mp3"
musicFile4 = "Queen_ShowMustGO.mp3"
musicFile5 = "TSO_Sarajevo.mp3"
musicFileTest = "LS_Carol_all.mp3"

DCr1 = 0
DCr2 = 0
DCg1 = 0
DCg2 = 0
DCb1 = 30
DCb2 = 0
DCy1 = 0
DCy2 = 0

for i in LED:
    GPIO.setup(i, GPIO.OUT, initial=0)

greenfrq1 = GPIO.PWM(green1, freqLed)
greenfrq1.start(DCg1)
greenfrq2 = GPIO.PWM(green2, freqLed)
greenfrq2.start(DCg2)
redfrq1 = GPIO.PWM(red1, freqLed)
redfrq1.start(DCr1)
redfrq2 = GPIO.PWM(red2, freqLed)
redfrq2.start(DCr2)
bluefrq1 = GPIO.PWM(blue1, freqLed)
bluefrq1.start(DCb1)
bluefrq2 = GPIO.PWM(blue2, freqLed)
bluefrq2.start(DCb2)
yellowfrq1 = GPIO.PWM(yellow1, freqLed)
yellowfrq1.start(DCy1)
yellowfrq2 = GPIO.PWM(yellow2, freqLed)
yellowfrq2.start(DCy2)

pwms = [redfrq1, redfrq2, greenfrq1, greenfrq2, bluefrq1, bluefrq2, yellowfrq1, yellowfrq2]
pwmsFreqs = [DCr1, DCr2, DCg1, DCg2, DCb1, DCb2, DCy1, DCy2]

def setFreq(c1, val, maxVal):
    pwmsFreqs[c1] = val
    if pwmsFreqs[c1] > maxVal:
        pwmsFreqs[c1] = maxVal
    if pwmsFreqs[c1] > 100:
        pwmsFreqs[c1] = 100
    if pwmsFreqs[c1] < 0:
        pwmsFreqs[c1] = 0
    pwms[c1].ChangeDutyCycle(pwmsFreqs[c1])


#lighting up the led 
def lightUP( colorFRQ, sleeptim, steps, maxVal ):
    for c in range(0, maxVal, steps):
        colorFRQ.ChangeDutyCycle(c)
        time.sleep(sleeptim)
        
#lighting up the led 
def lightUPnum( c1, sleeptim, steps, maxVal ):
    for c in range(0, maxVal+steps, steps):
        setFreq(c1, c, maxVal)
        time.sleep(sleeptim)

#lighting off the led 
def lightOFF( colorFRQ, sleeptim, steps, maxVal ):
    for c in range(maxVal, -1, -steps):
        colorFRQ.ChangeDutyCycle(c)
        time.sleep(sleeptim)

#lighting off the led 
def lightOFFnum( c1, sleeptim, steps, maxVal ):
    for c in range(maxVal, -steps, -steps):
        setFreq(c1, c, maxVal)
        time.sleep(sleeptim)

#lighting up the led 
def lightUP2( colorFRQ, colorFRQ2, sleeptim, steps, maxVal ):
    for c in range(0, maxVal, steps):
        colorFRQ.ChangeDutyCycle(c)
        colorFRQ2.ChangeDutyCycle(c)
        time.sleep(sleeptim)

#lighting up the led 
def lightUP2num( c1, c2, sleeptim, steps, maxVal ):
    for c in range(0, maxVal+steps, steps):
        setFreq(c1, c, maxVal)
        setFreq(c2, c, maxVal)
        time.sleep(sleeptim)
        
#lighting up the led 
def lightUP4num( c1, c2, c3, c4, sleeptim, steps, maxVal ):
    for c in range(0, maxVal+steps, steps):
        setFreq(c1, c, maxVal)
        setFreq(c2, c, maxVal)
        setFreq(c3, c, maxVal)
        setFreq(c4, c, maxVal)
        time.sleep(sleeptim)

#lighting off the led 
def lightOFF2( colorFRQ, colorFRQ2, sleeptim, steps, maxVal ):
    for c in range(maxVal, -1, -steps):
        colorFRQ.ChangeDutyCycle(c)
        colorFRQ2.ChangeDutyCycle(c)
        time.sleep(sleeptim)

#lighting off the led 
def lightOFF2num( c1, c2, sleeptim, steps, maxVal ):
    for c in range(maxVal, -steps, -steps):
        setFreq(c1, c, maxVal)
        setFreq(c2, c, maxVal)
        time.sleep(sleeptim)
        
#lighting off the led 
def lightOFF4num( c1, c2, c3, c4, sleeptim, steps, maxVal ):
    for c in range(maxVal, -steps, -steps):
        setFreq(c1, c, maxVal)
        setFreq(c2, c, maxVal)
        setFreq(c3, c, maxVal)
        setFreq(c4, c, maxVal)
        time.sleep(sleeptim)


#lighting up the led 
def lightUP2Delay( c1, c2, sleeptim, steps, maxVal ):
    max1Step = maxVal//2
    for c in range(0, max1Step, steps):
        pwmsFreqs[c1] = c
        pwms[c1].ChangeDutyCycle(c)
        #setFreq(c1, c, maxVal)
        time.sleep(sleeptim)
    
    print("done c1")
    tmpfreq = pwmsFreqs[c1]
    for c in range(0, maxVal+steps, steps):
        pwmsFreqs[c1] = tmpfreq + c
        if pwmsFreqs[c1] > maxVal:
            pwmsFreqs[c1] = maxVal
        pwms[c1].ChangeDutyCycle(pwmsFreqs[c1])
        
        pwmsFreqs[c2] = c
        pwms[c2].ChangeDutyCycle(c)
        time.sleep(sleeptim)
        
    print("done light up")
    print("c1=", pwmsFreqs[c1], "c2", pwmsFreqs[c2])
    
#lighting up the led 
def lightOFF2Delay( c1, c2, sleeptim, steps, maxVal ):
    max1Step = maxVal//2
    for c in range(maxVal, max1Step, -steps):
        pwmsFreqs[c1] = c
        pwms[c1].ChangeDutyCycle(pwmsFreqs[c1])
        time.sleep(sleeptim)
    
    print("done c1")
    tmpfreq = pwmsFreqs[c1]
    for c in range(0, maxVal+steps, steps):
        pwmsFreqs[c1] = tmpfreq - c
        if pwmsFreqs[c1] < 0:
            pwmsFreqs[c1] = 0
        pwms[c1].ChangeDutyCycle(pwmsFreqs[c1])
        
        pwmsFreqs[c2] = 100 - c
        pwms[c2].ChangeDutyCycle(pwmsFreqs[c2])
        time.sleep(sleeptim)
        
    print("done light up")
    print("c1=", pwmsFreqs[c1], "c2", pwmsFreqs[c2])

def clearALLfrq():
    for c in range(0, 8, 1):
        pwmsFreqs[c] = 0
        pwms[c].ChangeDutyCycle(0)
       
#lighting off the led 
def lightOFFall(sleeptim):
    tmpFreqs = pwmsFreqs
    
    for c in range(1, 100, 1):
        sum = 0
        for nx in range(0, 7+1, 1):
            sum = sum + pwmsFreqs[nx]
        if sum <= 0:
            break
        
        for n in range(0, 7+1, 1):
            setFreq(n, tmpFreqs[n] - c, 100)
            
        time.sleep(sleeptim)

#lighting up the led 
def lightUPall(sleeptim):
    tmpFreqs = pwmsFreqs
    
    for c in range(1, 100, 1):
        if c >= 80:
            break
        for n in range(0, 7+1, 1):
            setFreq(n, tmpFreqs[n] + c, 100)
        time.sleep(sleeptim)
        
#function sin(x)
def sinDC( x ):
    #print("x=", x)
    #print("sin x=", math.sin(math.radians(x)))
    f = math.ceil(math.sin(math.radians(x))*100)
    #f = math.ceil(100-math.fabs(math.sin(math.radians(x))*100))
    if f < 0:
        f=0
    #print("f=", f)
    return f

#test1
def test1():
    for c in range(-180, 181, 1):
        bluefrq1.ChangeDutyCycle(sinDC(c))
        bluefrq2.ChangeDutyCycle(sinDC(c+deltaGrad))
        redfrq1.ChangeDutyCycle(sinDC(c+deltaGrad*2))
        redfrq2.ChangeDutyCycle(sinDC(c+deltaGrad*3))
        greenfrq1.ChangeDutyCycle(sinDC(c+deltaGrad*8))
        greenfrq2.ChangeDutyCycle(sinDC(c+deltaGrad*5))
        yellowfrq1.ChangeDutyCycle(sinDC(c+deltaGrad*6))
        yellowfrq2.ChangeDutyCycle(sinDC(c+deltaGrad*7))
        time.sleep(0.10)
        
        
    for c in range(180, -181, -1):
        bluefrq1.ChangeDutyCycle(sinDC(c))
        bluefrq2.ChangeDutyCycle(sinDC(c+deltaGrad))
        redfrq1.ChangeDutyCycle(sinDC(c+deltaGrad*2))
        redfrq2.ChangeDutyCycle(sinDC(c+deltaGrad*3))
        greenfrq1.ChangeDutyCycle(sinDC(c+deltaGrad*8))
        greenfrq2.ChangeDutyCycle(sinDC(c+deltaGrad*5))
        yellowfrq1.ChangeDutyCycle(sinDC(c+deltaGrad*6))
        yellowfrq2.ChangeDutyCycle(sinDC(c+deltaGrad*7))
        time.sleep(0.10)


def test2():
    lightUP2( bluefrq1, bluefrq2, 0.10, 5, 100)
    lightUP2( redfrq1, redfrq2, 0.10, 5, 80)
    lightUP2( greenfrq1, greenfrq2, 0.10, 1, 20)
    lightUP2( yellowfrq1, yellowfrq2, 0.10, 5, 100)
        
    time.sleep(1)
        
    lightOFF2( bluefrq1, bluefrq2, 0.10, 5, 100)
    lightOFF2( redfrq1, redfrq2, 0.10, 5, 80)
    lightOFF2( greenfrq1, greenfrq2, 0.10, 2, 20)
    lightOFF2( yellowfrq1, yellowfrq2, 0.10, 5, 100)
        
    time.sleep(0.1)

#flash
def flashDown():
    clearALLfrq()
    #-90-41
    for c in range(-90, 186, 7):
        pwms[1].ChangeDutyCycle(sinDC(c))
        pwms[3].ChangeDutyCycle(sinDC(c+deltaGrad))
        pwms[5].ChangeDutyCycle(sinDC(c+deltaGrad*2))
        pwms[7].ChangeDutyCycle(sinDC(c+deltaGrad*3))
        time.sleep(0.009)
    
    #-90-11
    for c in range(180, -91, -7):
        pwms[1].ChangeDutyCycle(sinDC(c))
        pwms[3].ChangeDutyCycle(sinDC(c+deltaGrad))
        pwms[5].ChangeDutyCycle(sinDC(c+deltaGrad*2))
        pwms[7].ChangeDutyCycle(sinDC(c+deltaGrad*3))
        time.sleep(0.009)
        
    clearALLfrq()

#test1
def test1():
    for c in range(-180, 181, 1):
        bluefrq1.ChangeDutyCycle(sinDC(c))
        bluefrq2.ChangeDutyCycle(sinDC(c+deltaGrad))
        redfrq1.ChangeDutyCycle(sinDC(c+deltaGrad*2))
        redfrq2.ChangeDutyCycle(sinDC(c+deltaGrad*3))
        greenfrq1.ChangeDutyCycle(sinDC(c+deltaGrad*8))
        greenfrq2.ChangeDutyCycle(sinDC(c+deltaGrad*5))
        yellowfrq1.ChangeDutyCycle(sinDC(c+deltaGrad*6))
        yellowfrq2.ChangeDutyCycle(sinDC(c+deltaGrad*7))
        time.sleep(0.10)
        
        
    for c in range(180, -181, -1):
        bluefrq1.ChangeDutyCycle(sinDC(c))
        bluefrq2.ChangeDutyCycle(sinDC(c+deltaGrad))
        redfrq1.ChangeDutyCycle(sinDC(c+deltaGrad*2))
        redfrq2.ChangeDutyCycle(sinDC(c+deltaGrad*3))
        greenfrq1.ChangeDutyCycle(sinDC(c+deltaGrad*8))
        greenfrq2.ChangeDutyCycle(sinDC(c+deltaGrad*5))
        yellowfrq1.ChangeDutyCycle(sinDC(c+deltaGrad*6))
        yellowfrq2.ChangeDutyCycle(sinDC(c+deltaGrad*7))
        time.sleep(0.10)


def test2():
    lightUP2( bluefrq1, bluefrq2, 0.10, 5, 100)
    lightUP2( redfrq1, redfrq2, 0.10, 5, 80)
    lightUP2( greenfrq1, greenfrq2, 0.10, 1, 20)
    lightUP2( yellowfrq1, yellowfrq2, 0.10, 5, 100)
        
    time.sleep(1)
        
    lightOFF2( bluefrq1, bluefrq2, 0.10, 5, 100)
    lightOFF2( redfrq1, redfrq2, 0.10, 5, 80)
    lightOFF2( greenfrq1, greenfrq2, 0.10, 2, 20)
    lightOFF2( yellowfrq1, yellowfrq2, 0.10, 5, 100)
        
    time.sleep(0.1)

#flash
def flashDown():
    clearALLfrq()
    #-90-41
    for c in range(-90, 186, 7):
        pwms[1].ChangeDutyCycle(sinDC(c))
        pwms[3].ChangeDutyCycle(sinDC(c+deltaGrad))
        pwms[5].ChangeDutyCycle(sinDC(c+deltaGrad*2))
        pwms[7].ChangeDutyCycle(sinDC(c+deltaGrad*3))
        time.sleep(0.009)
    
    #-90-11
    for c in range(180, -91, -7):
        pwms[1].ChangeDutyCycle(sinDC(c))
        pwms[3].ChangeDutyCycle(sinDC(c+deltaGrad))
        pwms[5].ChangeDutyCycle(sinDC(c+deltaGrad*2))
        pwms[7].ChangeDutyCycle(sinDC(c+deltaGrad*3))
        time.sleep(0.009)
        
    clearALLfrq()

#0 part
def testNY0(mode):
    flashDown()
    
    if mode == 1:
        time.sleep(0.4)
        lightUP2num(5, 4, 0.02, 6, 80)
        lightOFF2num(5, 4, 0.02, 6, 80)
        clearALLfrq()
        time.sleep(0.4)
    else:
        time.sleep(1.2)
    
    #time.sleep(0)
    flashDown()
    
    time.sleep(0.2)
    
    if mode == 2:
        lightUP2num(5, 4, 0.02, 8, 80)
        lightUP2num(3, 2, 0.02, 8, 80)
        
        lightOFFall(0.4)
    else:
        #lightUPnum(3, 0.02, 6, 80)
        lightUP2num(3, 2, 0.02, 8, 80)
        clearALLfrq()
        #lightUPnum(1, 0.02, 6, 80)
        lightUP2num(1, 0, 0.02, 8, 80)
        clearALLfrq()
        #lightUPnum(7, 0.02, 6, 80)
        lightUP2num(7, 6, 0.02, 8, 80)
        clearALLfrq()
        #lightUPnum(5, 0.02, 6, 80)
        lightUP2num(5, 4, 0.02, 8, 80)
        clearALLfrq()
    
    time.sleep(0.4)
    
def testNY2():
    stime = 0.2
    #time.sleep(0.2)
    lightUPnum(4, 0.02, 4, 80)
    lightUPnum(5, 0.02, 4, 80)
    
    time.sleep(stime)
    lightOFFnum(4, 0.02, 4, 80)
    lightOFFnum(5, 0.02, 4, 80)
    
    time.sleep(stime)
    lightUPnum(2, 0.02, 4, 80)
    lightUPnum(3, 0.02, 4, 80)
    
    time.sleep(stime)
    lightOFFnum(2, 0.02, 4, 80)
    lightOFFnum(3, 0.02, 4, 80)
    
    time.sleep(stime)
    lightUPnum(6, 0.02, 4, 80)
    lightUPnum(7, 0.02, 4, 80)
    
    time.sleep(stime)
    lightOFFnum(6, 0.02, 4, 80)
    lightOFFnum(7, 0.02, 4, 80)
    
    time.sleep(stime)
    lightUPnum(0, 0.02, 4, 80)
    lightUPnum(1, 0.02, 4, 80)
    
    time.sleep(stime)
    lightOFFnum(0, 0.02, 4, 80)
    lightOFFnum(1, 0.02, 4, 80)
    
def testNY21():
    time.sleep(0.2)
    lightUP2Delay( 4, 5, 0.021, 4, 100)
    time.sleep(0.2)
    lightOFF2Delay( 5, 4, 0.021, 4, 100)
    
    time.sleep(0.2)
    lightUP2Delay( 4, 5, 0.021, 4, 100)
    time.sleep(0.2)
    lightOFF2Delay( 5, 4, 0.021, 4, 100)
    
    time.sleep(0.2)
    lightUP2Delay( 4, 5, 0.021, 4, 100)
    time.sleep(0.2)
    lightOFF2Delay( 5, 4, 0.021, 4, 100)
    
    time.sleep(0.2)
    lightUP2Delay( 4, 5, 0.021, 4, 100)
    time.sleep(0.2)
    lightOFF2Delay( 5, 4, 0.021, 4, 100)
    
def testNY3():
    stime = 0.22
    #time.sleep(0.2)
    lightUPnum(4, 0.02, 4, 80)
    lightUPnum(5, 0.02, 4, 80)
    
    time.sleep(stime)
    lightUPnum(2, 0.02, 4, 80)
    lightUPnum(3, 0.02, 4, 80)
    
    time.sleep(stime)
    lightOFFnum(4, 0.02, 4, 80)
    lightOFFnum(5, 0.02, 4, 80)
    
    time.sleep(stime)
    lightOFFnum(2, 0.02, 4, 80)
    lightOFFnum(3, 0.02, 4, 80)
    
    time.sleep(stime)
    lightUPnum(6, 0.02, 4, 80)
    lightUPnum(7, 0.02, 4, 80)
    
    time.sleep(stime)
    lightUPnum(0, 0.02, 4, 80)
    lightUPnum(1, 0.02, 4, 80)
    
    time.sleep(stime)
    lightOFFnum(6, 0.02, 4, 80)
    lightOFFnum(7, 0.02, 4, 80)
    
    time.sleep(stime)
    lightOFFnum(0, 0.02, 4, 80)
    lightOFFnum(1, 0.02, 4, 80)
    
def testNY4():
    
    #time.sleep(1)
    #musicplay()
    #time.sleep(1)
    tsleep = 0.15
    dt0 = datetime.now()
    
    time.sleep(tsleep)
    lightUP2Delay( 4, 5, 0.021, 4, 100)
    dt01 = datetime.now()
    
    time.sleep(tsleep)
    lightUP2Delay( 1, 0, 0.027, 4, 80)
    dt02 = datetime.now()
    
    time.sleep(tsleep)
    lightUP2Delay( 2, 3, 0.027, 2, 40)
    dt03 = datetime.now()
    
    time.sleep(tsleep)
    lightUP2Delay( 7, 6, 0.027, 4, 80)
    dt1 = datetime.now()
    
    td = dt01 - dt0
    td_sec = td.total_seconds()
    print('The difference is approx. 1 - %s seconds' % td_sec)
    
    td = dt02 - dt01
    td_sec = td.total_seconds()
    print('The difference is approx. 2 - %s seconds' % td_sec)
    
    td = dt03 - dt02
    td_sec = td.total_seconds()
    print('The difference is approx. 3 - %s seconds' % td_sec)
    
    td = dt1 - dt03
    td_sec = td.total_seconds()
    print('The difference is approx. 4 - %s seconds' % td_sec)
    
    td = dt1 - dt0
    td_sec = td.total_seconds()
    print('The difference is approx. ALL %s seconds' % td_sec)
    
    time.sleep(0.05)
    lightOFFall(0.05)
    #lightUPall(0.015)

def testNY5(specEnd):
    lightUPall(0.0005)
    
    tsleep = 1.0
    
    #green blue
    #time.sleep(tsleep)
    #lightOFF4num( 5, 4, 3, 2, 0.005, 4, 100)
    #lightUP4num( 4, 5, 2, 3, 0.001, 4, 100)
    
    #red yellow
    time.sleep(1.0)
    lightOFF4num( 1, 0, 7, 6, 0.005, 4, 100)
    lightUP4num( 1, 0, 7, 6, 0.001, 4, 100)
    dt03 = datetime.now()
    
    #green blue
    time.sleep(0.7)
    lightOFF4num( 5, 4, 3, 2, 0.005, 4, 100)
    lightUP4num( 4, 5, 2, 3, 0.001, 4, 100)
    #green blue
    time.sleep(0.16)
    lightOFF4num( 5, 4, 3, 2, 0.005, 4, 100)
    lightUP4num( 4, 5, 2, 3, 0.001, 4, 100)
    #green blue
    time.sleep(0.16)
    lightOFF4num( 5, 4, 3, 2, 0.005, 4, 100)
    lightUP4num( 4, 5, 2, 3, 0.001, 4, 100)
    #green blue
    time.sleep(0.1)
    lightOFF4num( 5, 4, 3, 2, 0.005, 4, 100)
    lightUP4num( 4, 5, 2, 3, 0.001, 4, 100)
    
    #red yellow
    time.sleep(0.1)
    lightOFF4num( 1, 0, 7, 6, 0.005, 4, 100)
    lightUP4num( 1, 0, 7, 6, 0.001, 4, 100)
    
    if specEnd == 1:
        time.sleep(0.3)
        lightOFFall(0.0033)
        lightUPall(0.0033)
        time.sleep(0.1)
        lightOFFall(0.0012)
        lightUPall(0.0001)
        lightOFFall(0.0012)
        lightUPall(0.001)
        lightOFFall(0.001)
        lightUPall(0.0012)
        lightOFFall(0.001)
    elif specEnd == 0:
        lightOFFall(0.065)
    else:
        lightOFFall(0.0)



def testNY51(mode):
    testNY5(0)
    time.sleep(0.1)
    testNY5(0)
    time.sleep(0.1)
    testNY5(0)
    
    if mode == 1:
        time.sleep(0.0)
        testNY5(1)
        time.sleep(0.0)
        testNY5(1)
    else:
        time.sleep(0.1)
        testNY5(1)
        
    
def musicplay():
    #print("init pygame")
    pygame.init()
    pygame.mixer.init()
    #print("mixer load")
    pygame.mixer.music.load(musicFileTest)
    pygame.mixer.music.stop()
    #print("pygame play")
    pygame.mixer.music.play()
    #print("...")
    
    #while pygame.mixer.music.get_busy() == True:
    #    continue
    
    #pygame.mixer.music.load(musicFileShort)
    #print("pygame play")
    #pygame.mixer.music.play()
    
    #time.sleep(10)

    #pygame.mixer.music.load(musicFile1)
    #pygame.mixer.music.fadeout(1000)
    
    #print("music stop")
    
    #pygame.mixer.music.load(musicFile1)
    #pygame.mixer.music.unpause()
    
    #print("music play")
    
    #time.sleep(2)
    
    #pygame.mixer.music.load(musicFile1)
    #pygame.mixer.music.stop()
    
def realNY():
    musicplay()
    time.sleep(0.95)
    testNY0(0)
    testNY0(0)
    #time.sleep(0.2)
    testNY0(1)
    testNY0(1)
    testNY2()
    time.sleep(0.1)
    testNY3()
    time.sleep(0.4)
    testNY3()
    time.sleep(0.2)
    testNY4()
    testNY51(0)
    
    testNY0(1)
    testNY0(1)
    testNY0(1)
    testNY0(1)
    testNY2()
    testNY2()
    time.sleep(0.4)
    testNY3()
    time.sleep(0.4)
    testNY3()
    time.sleep(0.2)
    testNY4()
    testNY51(0)
    testNY51(1)
    time.sleep(0.06)
    testNY0(2)
    
def realtime():
    while 1:
        test1()
    
def testim():
    i=2
    
    while True:
        mod = i % 2
        if mod == 0:
            if i > 3:
                pygame.mixer.music.stop()
            musicplay()
            time.sleep(0.5)
        testNY0()
        i=i+1
    

print ("Ctrl+C exits the program")
time.sleep(1)
bluefrq1.ChangeDutyCycle(15)
time.sleep(1)
bluefrq1.ChangeDutyCycle(0)

try:
    #testim()
    #test1()
    
    realNY()
    #testNY51(0)
    #testNY51(1)
    #time.sleep(0.06)
    #testNY0(2)
    
    #musicplay()
    
    #while True:
    #realtime()
        
    

except KeyboardInterrupt:
    print("Exit pressed Ctrl+C")        
except (AttributeError, TypeError) as e:
    print("Error occurred:", e)
    #print("Other Exception")            

finally:
    greenfrq1.stop()
    greenfrq2.stop()
    yellowfrq1.stop()
    yellowfrq2.stop()
    redfrq1.stop()
    redfrq2.stop()
    bluefrq1.stop()
    bluefrq2.stop()
    GPIO.cleanup()
    #pygame.mixer.music.stop()
    #pygame.quit()
    #pygame.mixer.music.unload()
    print("End of program")