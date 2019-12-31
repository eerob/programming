from aiy.board import Board, Led
import subprocess
import signal, os

def main():
    print('LED is ON while button is pressed (Ctrl-C for exit).')
    with Board() as board:
        while True:
            board.button.wait_for_press()
            print('ON')
           # proc1 = subprocess.Popen(['while [1];', 'do', 'aplay', '/home/pi/fire.wav', 'done'], s$
            #proc1 = subprocess.Popen("(while :; do aplay %s ; done)" % '/home/pi/fire.wav', start_$
            proc1 = subprocess.Popen("(while :; do aplay %s ; done)" % '/home/pi/fire.wav', stdout=$
            board.led.state = Led.ON
            board.button.wait_for_press()

            os.killpg(os.getpgid(proc1.pid), signal.SIGTERM)

#proc1.kill()
            #board.button.wait_for_release()
            print('OFF')
            board.led.state = Led.OFF


if __name__ == '__main__':
    main()
