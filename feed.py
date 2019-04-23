import RPi.GPIO as GPIO, time
from picamera import PiCamera
from time import sleep
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(16, 500)
camera = PiCamera()

def SpinMotor(direction, num_steps):
    GPIO.output(18, direction)
    while num_steps > 0:
        p.start(1)
        time.sleep(0.01)
        num_steps -= 1
    p.stop()
    
    return True

def Morning():
    hour = time.localtime().tm_hour
    if hour == 16:
        SpinMotor(True, 175)
        time.sleep(3)
        SpinMotor(True, 87.5)
        time.sleep(3)
        SpinMotor(False, 87.5)
        time.sleep(3)
        SpinMotor(False, 92.5)
        time.sleep(3)
        camera.start_preview()
        sleep(2)
        camera.capture('/home/pi/Desktop/image.jpg')
        camera.stop_preview()
        sleep(3)
        message = "The cats have been fed!"
        image = open('/home/pi/Desktop/image.jpg', 'rb')
        response = twitter.upload_media(media=image)
        media_id = [response['media_id']]
        twitter.update_status(status=message, media_ids=media_id)
        
def Afternoon():
    hour = time.localtime().tm_hour
    if hour == 17:
        SpinMotor(True, 175)
        time.sleep(3)
        SpinMotor(True, 87.5)
        time.sleep(3)
        SpinMotor(False, 87.5)
        time.sleep(3)
        SpinMotor(False, 92.5)
        camera.start_preview()
        sleep(2)
        camera.capture('/home/pi/Desktop/image.jpg')
        camera.stop_preview()
        sleep(3)
        message = "The cats have been fed!"
        image = open('/home/pi/Desktop/image.jpg', 'rb')
        response = twitter.upload_media(media=image)
        media_id = [response['media_id']]
        twitter.update_status(status=message, media_ids=media_id)
        
def Night():
    hour = time.localtime().tm_hour
    if hour == 18:
        SpinMotor(True, 175)
        time.sleep(3)
        SpinMotor(True, 87.5)
        time.sleep(3)
        SpinMotor(False, 87.5)
        time.sleep(3)
        SpinMotor(False, 92.5)
        camera.start_preview()
        sleep(2)
        camera.capture('/home/pi/Desktop/image.jpg')
        camera.stop_preview()
        sleep(3)
        message = "The cats have been fed!"
        image = open('/home/pi/Desktop/image.jpg', 'rb')
        response = twitter.upload_media(media=image)
        media_id = [response['media_id']]
        twitter.update_status(status=message, media_ids=media_id)
        

Morning()
#GPIO.cleanup()
Afternoon()
#GPIO.cleanup()
Night()
GPIO.cleanup()
