import sys
import termios
import atexit
from select import select

class keys_hit:
    def __init__(self):
         # Save the terminal settings
        self.fd = sys.stdin.fileno()
        self.new_term = termios.tcgetattr(self.fd)
        self.old_term = termios.tcgetattr(self.fd)
        self.__a=1
            # New terminal setting unbuffered
        self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)

            # Support normal-terminal reset at exit
        atexit.register(self.set_normal_term)
    def keyhit(self):
        dr,dw,de = select([sys.stdin],[],[],0)
        return dr != []
    def set_normal_term(self):
        ''' Resets to normal terminal.  On Windows this is a no-op.
        '''

        
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)

    
    def hitkey(self):
        return sys.stdin.read(1)