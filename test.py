import struct
import time



def save_data():
    ts  = int(time.time())
    fname = "data/%d.csv" % ts
    f = open(fname, 'w')
    return f

s = "a5"

i = int(s, 16)
print i
print 0xa5 == 0xa5
data = "123455"

ts  = int(time.time())
fp = save_data()
fp.write("dsadsa \n")
fp.write("aaaaaaaaaa \n")
fp.close()