import event, timer_event
import sl_metro, suicide

#make callback function

def call1(val1, val2):
    print "[Call1] args=", val1, ",", val2 , "2sec"


def call2():
    print "[Call2] 4SEC"  , "4sec"
    timer.end()
    suicide.run()


#add the function as event
event.add("/call1" , call1)
event.add("/call2" , call2)

#Create Metro
metro = sl_metro.Metro(0.5)

#create timer with event name and args
timer = timer_event.Timer_event(2.0, "/call1" , 137, 13.8)
timer2 = timer_event.Timer_event(4.0, "/call2") #a event without argments is also ok.


#start waiting the involing the event
print "Set timer event named call1 after 2sec and call2 after 4sec."
try:
    while True:
        if metro.update():
            print "Waiting timer ..."

except KeyboardInterrupt :
    timer.end()
    print "Finished. "

