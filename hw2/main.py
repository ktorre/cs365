#   Author : Kevin De La Torre
#   Purpose: Expand every line in assembly file and write to word file

from sys import argv
from docx import Document

def main():
    if ( len( argv ) > 2 ):
        pcFile = argv[ 1 ]
        irFile = argv[ 2 ]
        
        for ( pc in pcFile ):
            irLine = irFile
    else:
        print( "Usage: {0} <pc> <ir>".format( argv[ 0 ] ) )

def encoder( instruction ):



 __name__ == "__main__":
    main()
