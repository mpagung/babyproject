import argparse
import csv
import datetime
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

print('Reading MCP3008 values, press Ctrl-C to quit...')

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

with open(args.filename,'w') as csvfile:
    spamwriter=csv.writer(csvfile, delimiter=',',
                          quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['time','channel_a','channel_b','channel_c','channel_d','channel_e'])

    while True:
        t1=datetime.datetime.now()
        ch=[0]*5
        for i in range(5):
            ch[i]=mcp.read_adc(i);
        spamwriter.writerow([str(t1),ch[0],ch[1],ch[2],ch[3],ch[4]])
        print('{0:>4} {1:4} {2:4} {3:4} {4:4} {5:5}'.format(str(t1),ch[0],ch[1],ch[2],ch[3],ch[4]))
        time.sleep(0.1)


                
    
                    
