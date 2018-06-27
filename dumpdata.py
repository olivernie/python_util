import struct

'''
dumpData(data) print data as following format:
   0:    01 02 03 04 05 06 07 08   09 0a 01 02 03 04 05 06
  10:    07 08 09 0a 01 02 03 04   05 06 07 08 09 0a 01 02
  20:    03 04 05 06 07 08 09 0a   01 02 03 04 05 06 07 08
  30:    09 0a 01 02 03 04 05 06   07 08 09 0a 01 02 03 04
  40:    05 06 07 08 09 0a 01 02   03 04 05 06 07 08 09 0a
  50:    01 02 03 04 05 06 07 08   09 0a 01 02 03 04 05 06
  60:    07 08 09 0a 01 02 03 04   05 06 07 08 09 0a 01 02
  70:    03 04 05 06 07 08 09 0a   01 02 03 04 05 06 07 08
  80:    09 0a 01 02 03 04 05 06   07 08 09 0a 01 02 03 04
  90:    05 06 07 08 09 0a 01 02   03 04 05 06 07 08 09 0a
  A0:    01 02 03 04 05 06 07 08   09 0a 01 02 03 04 05 06
  B0:    07 08 09 0a 01 02 03 04   05 06 07 08 09 0a 01 02
  C0:    03 04 05 06 07 08 09 0a   01 02 03 04 05 06 07 08
  D0:    09 0a 01 02 03 04 05 06   07 08 09 0a 01 02 03 04
  E0:    05 06 07 08 09 0a 01 02   03 04 05 06 07 08 09 0a
  F0:    01 02 03 04 05 06 07 08   09 0a 01 02 03 04 05 06
 100:    07 08 09 0a 01 02 03 04   05 06 07 08 09 0a 01 02
'''
def dumpData(data):
    # data is string or binary blob
    size = len(data)
    for i in range (0, size, 16):
        subData = data[i:i+16]
        #ch_list is tuple
        ch_num = len(subData)
        ch_list = struct.unpack('=' + 'B' * ch_num, subData)
        print '%4X:   ' % i,
        if (ch_num > 8): 
            print ('%02x ' * 8 + ' ' + ' %02x' * (ch_num-8)) % ch_list
        else:
            print '%02x ' * ch_num % ch_list
    print '\n'
