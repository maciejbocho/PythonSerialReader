import serial

port = "COM8"

DataBuffer=[]

def UART_ReadingData():
    try:    
        ser = serial.Serial(port, 115200, timeout=1)
    except: 
        print("Communcation is not esthabilished. Check connection or parameters")
        return



    while serial.Seri:
        data= ser.readline()
        if len(data)>0:
            data_sensor = data.decode('utf8')
            DataBuffer.append(data_sensor)
        

UART_ReadingData()
