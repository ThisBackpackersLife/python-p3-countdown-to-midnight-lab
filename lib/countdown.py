# your code goes here!
# import ipdb
import time

def countdown( number ):
    while number > 0:
        print( f'{ number } SECOND(S)!' )
        number -= 1

    print( "HAPPY NEW YEAR!" )

def countdown_with_sleep( number ):
    while number > 0:
        print( f'{ number } SECOND(S)!' )
        number -= 1
    time.sleep( 1 )

    print( "HAPPY NEW YEAR!" )


# ipdb.set_trace()