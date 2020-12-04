import signal
import time


# please run this code on repl.it

def signal_handler(signum, frame):
    print("You have pressed ctrl c which stop the program")
    exit(0)


# if __name__ == '__main__':
print("in 5 second, press ctrl c to initiate SIGINT command or do nothing ")
signal.signal(signal.SIGINT, signal_handler)
time.sleep(5)
print("program exit after it reached 5 second")