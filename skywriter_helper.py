#!/usr/bin/env python
import sys
import json
import signal
import skywriter

airwheel_count = 5000

def to_node(type, message):
    # convert to json and print (node helper will read from stdout)
    try:
        print(json.dumps({type: message}))
    except Exception:
        pass
    # stdout has to be flushed manually to prevent delays in the node helper communication
    sys.stdout.flush()

to_node("status", 'Skywriter started...')

# @skywriter.airwheel()
# def airwheel(delta):
    # to_node("gesture", f"airwheel {delta}" )
    # global airwheel_count
    # airwheel_count += delta
    # if airwheel_count < 0:
        # airwheel_count = 0
    # if airwheel_count > 10000:
        # airwheel_count = 10000
        # to_node("gesture", f"airwheel {delta}" )
    # #print('Airwheel:', airwheel_count/100)
    

# @skywriter.garbage()    
# def garbage():
    # to_node("gesture", "garbage")

@skywriter.flick()
def flick(start,finish):
    if(start == "north" and finish == "south"):
        to_node("gesture", "down")
 
    elif(start == "south" and finish == "north"):
        to_node("gesture", "up")
  
    elif(start == "west" and finish == "east"):
        to_node("gesture", "next")
  
    #previous track
    elif(start == "east" and finish == "west"):
        to_node("gesture", "previous")

signal.pause()