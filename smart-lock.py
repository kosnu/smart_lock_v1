import RPi.GPIO as GPIO
import time
import nfc


def startup(targets):
    print("> waiting for new NFC tags...")
    return targets


def connected(tag):
    print("> connected!")
    if tag.ndef:
        for i in range(1):
            servo.ChangeDutyCycle(2.5)
            time.sleep(0.5)

            servo.ChangeDutyCycle(12)
            time.sleep(0.5)
    return True


def released(tag):
    print("> released!")


if __name__ == '__main__':
    clf = nfc.ContactlessFrontend('usb')
    GPIO.setmode(GPIO.BCM)

    gp_out = 4
    GPIO.setup(gp_out, GPIO.OUT)

    servo = GPIO.PWM(gp_out, 50)
    servo.start(0)

    if clf:
        while clf.connect(rdwr={
            'on-startup': startup,
            'on-connect': connected,
            'on-release': released,
        }):
            pass

    servo.stop()
    GPIO.cleanup()
