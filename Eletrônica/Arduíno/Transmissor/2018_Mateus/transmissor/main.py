import serial
from time import sleep

#port = serial.Serial('/dev/ttyUSB0',115200)
#port = serial.Serial('/dev/ttyACM0',115200)
port = serial.Serial('COM5',115200)



'''vetorDeDados = [ord('B'),ord('D'),116,116,116,116,118,118,ord('P'), ord('\n')]
print(vetorDeDados)'''

'''for k in range(0,200):
    vetorDeDados = [ord('B'),ord('D'),(k)+50,(-k)+250,180,180,(k)+50,(-k)+250,ord('P'), ord('\n')]
    port.write(vetorDeDados)
    sleep(0.1.
    print(vetorDeDados)'''

'''for k in range(0,200):
    vetorDeDados = [ord('B'),ord('D'),(k)+50,(-k)+250,(k)+50,(-k)+250,(k)+50,(-k)+250,ord('P'), ord('\n')]
    port.write(vetorDeDados)
    sleep(0.1)
    print(vetorDeDados)'''

'''vetorDeDados = [ord('B'),ord('D'),50,250,180,180,100,100,ord('P'), ord('\n')]
port.write(vetorDeDados)
print(vetorDeDados)'''

for k in range(0,2000000000000):
    vetorDeDados = [ord('B'),ord('D'),50+k,50+k,50+k,250-k,250-k,250-k,ord('P'), ord('\n')]
    if k > 200:
        vetorDeDados = [ord('B'),ord('D'),50,50,100,200,250,250,ord('P'), ord('\n')]
    port.write(vetorDeDados)
    #read = port.readline()
    sleep(0.1)
    print(vetorDeDados)
    #print(read)

'''tm = 10
for k in range(0,1000):

    vetorDeDados = [ord('B'),ord('D'),131,131,116,116,118,118,ord('P'), ord('\n')]
    if k > tm*10:
        vetorDeDados = [ord('B'),ord('D'),120,120,116,116,118,118,ord('P'), ord('\n')]
    if k >tm*20:
        vetorDeDados = [ord('B'),ord('D'),131,131,116,116,118,118,ord('P'), ord('\n')]
    if k > tm*30:
        vetorDeDados = [ord('B'),ord('D'),120,120,116,116,118,118,ord('P'), ord('\n')]
    if k >tm*40:
        vetorDeDados = [ord('B'),ord('D'),131,131,116,116,118,118,ord('P'), ord('\n')]
    if k > tm*50:
        vetorDeDados = [ord('B'),ord('D'),120,120,116,116,118,118,ord('P'), ord('\n')]
    if k >tm*60:
        vetorDeDados = [ord('B'),ord('D'),131,131,116,116,118,118,ord('P'), ord('\n')]
    if k > tm*70:
        vetorDeDados = [ord('B'),ord('D'),120,120,116,116,118,118,ord('P'), ord('\n')]
    if k >tm*80:
        vetorDeDados = [ord('B'),ord('D'),131,131,116,116,118,118,ord('P'), ord('\n')]
    if k > tm*90:
        vetorDeDados = [ord('B'),ord('D'),120,120,116,116,118,118,ord('P'), ord('\n')]
    
    port.write(vetorDeDados)
    sleep(0.015)
    print(vetorDeDados)'''

'''while 1:
    vetorDeDados = [ord('B'),ord('D'),220,220,220,220,50,250,ord('P'), ord('\n')]
    port.write(vetorDeDados)
    sleep(0.1)
    print(vetorDeDados)'''

'''for k in range(50, 250):
    vetorDeDados = [ord('B'),ord('D'),150,150,250,150,150,150,ord('P'), ord('\n')]
    port.write(vetorDeDados)
    sleep(0.1)
    print(vetorDeDados)'''

'''for k in range(0, 100):
    vetorDeDados = [ord('B'),ord('D'),180,180,210,210,250,250,ord('P'), ord('\n')]
    port.write(vetorDeDados)
    sleep(0.1)
    print(vetorDeDados)'''

'''for l in range(0, 3):
    for k in range(0, 10):
        vetorDeDados = [ord('B'),ord('D'),250,250,180,180,100,100,ord('P'), ord('\n')]
        port.write(vetorDeDados)
        sleep(0.1)
        print(vetorDeDados)

    for k in range(0, 10):
        vetorDeDados = [ord('B'),ord('D'),50,50,120,120,200,200,ord('P'), ord('\n')]
        port.write(vetorDeDados)
        sleep(0.1)
        print(vetorDeDados)'''

'''char vetorEmChar[BUFFER_SIZE]={'B','D',vel[0],vel[1],116,116,118,118,'P', '\n'};



sleep(2)
k = 0
a = len(s)
print (s)
print (a)
# string = bytes()
while k+25 <= a:
    ser.write(s[k:k+25])
    k += 25
    #string += ser.read(25)

    print(ser.read(25))

    #sleep(0.1)
ser.write(s[k:a])
print(ser.read(a-k))
#string += ser. read(a-k)'''

# fh = open("Faceaux.jpg","wb")
# fh.write(base64.b64decode(string))
# fh.close()
#print(ser.read(a-k))
# while 1:
#     print(ser.read(204))
