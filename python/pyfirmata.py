from pyfirmata import Arduino, util
board = Arduino('/dev/ttyACM6')
board.digital[13].write(1)
#board.digital[13].write(0)