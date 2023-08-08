from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import serial   
import csv


def home(request):
    if request.method == 'POST':

        csv_file = open('data1.csv', 'w', newline='')
        csv_writer = csv.writer(csv_file)
        header = ['Ax1', 'Ay1', 'Az1', 'Gx1', 'Gy1', 'Gz1', 'Ax2', 'Ay2', 'Az2', 'Gx2', 'Gy2', 'Gz2', 'Ax3', 'Ay3', 'Az3', 'Gx3', 'Gy3', 'Gz3']
        csv_writer.writerow(header)

        time = np.arange(0, 10)
        accel_x1=[]
        accel_y1=[]
        accel_z1=[]
        accel_x2=[]
        accel_y2=[]
        accel_z2=[]
        accel_x3=[]
        accel_y3=[]
        accel_z3=[]
        gyro_x1=[]
        gyro_x2=[]
        gyro_x3=[]
        gyro_y1=[]
        gyro_y2=[]
        gyro_y3=[]
        gyro_z1=[]
        gyro_z2=[]
        gyro_z3=[]
        ser = serial.Serial("COM8",115200)
        n=0
        while(n!=10):
            line = ser.readline().decode().strip()
            if line:
                values = line.split(',')
                if len(values) == 18:
                    accel_x1.append(values[0])
                    accel_y1.append(values[1])
                    accel_z1.append(values[2])
                    gyro_x1.append(values[3])
                    gyro_y1.append(values[4])
                    gyro_z1.append(values[5])
                    accel_x2.append(values[6])
                    accel_y2.append(values[7])
                    accel_z2.append(values[8])
                    gyro_x2.append(values[9])
                    gyro_y2.append(values[10])
                    gyro_z2.append(values[11])
                    accel_x3.append(values[12])
                    accel_y3.append(values[13])
                    accel_z3.append(values[14])
                    gyro_x3.append(values[15])
                    gyro_y3.append(values[16])
                    gyro_z3.append(values[17])
                    csv_writer.writerow([accel_x1[n], accel_y1[n], accel_z1[n], gyro_x1[n], gyro_y1[n], gyro_z1[n], accel_x2[n], accel_y2[n],accel_z2[n],
                                        gyro_x2[n], gyro_y2[n], gyro_z2[n], accel_x3[n], accel_y3[n], accel_z3[n], gyro_x3[n], gyro_y3[n], gyro_z3[n]])
                    n+=1
        csv_file.close()
        ser.close()
        fig, ax = plt.subplots()
        ax.plot(time, accel_x1)
        ax.set_xlabel('Time')
        ax.set_ylabel('Accelerometer of Sensor - 1 (X)')
        ax.grid(True)
       
        buffer = BytesIO()
        fig.savefig(buffer, format='png')
        plot1= buffer.getvalue()
        plot1= base64.b64encode(plot1).decode('utf-8').replace('\n', '')

        fig, ax = plt.subplots()
        ax.plot(time, accel_y1)
        ax.set_xlabel('Time')
        ax.set_ylabel('Accelerometer of Sensor - 1 (Y)')
        ax.grid(True)

        buffer.seek(0)  # Reset buffer position to the beginning
        fig.savefig(buffer, format='png')
        plot2 = buffer.getvalue()
        plot2 = base64.b64encode(plot2).decode('utf-8').replace('\n', '')
        
        
        fig, ax = plt.subplots()
        ax.plot(time, accel_z1)
        ax.set_xlabel('Time')
        ax.set_ylabel('Accelerometer of Sensor - 1 (Z)')
        ax.grid(True)

        buffer.seek(0)  # Reset buffer position to the beginning
        fig.savefig(buffer, format='png')
        plot3 = buffer.getvalue()
        plot3 = base64.b64encode(plot3).decode('utf-8').replace('\n', '')
       
        fig, ax = plt.subplots()
        ax.plot(time, accel_x2)
        ax.set_xlabel('Time')
        ax.set_ylabel('Accelerometer of Sensor - 2 (X)')
        ax.grid(True)

        buffer.seek(0)  # Reset buffer position to the beginning
        fig.savefig(buffer, format='png')
        plot4 = buffer.getvalue()
        plot4 = base64.b64encode(plot4).decode('utf-8').replace('\n', '')
        
        fig, ax = plt.subplots()
        ax.plot(time, accel_y2)
        ax.set_xlabel('Time')
        ax.set_ylabel('Accelerometer of Sensor - 2 (Y)')
        ax.grid(True)

        buffer.seek(0)  # Reset buffer position to the beginning
        fig.savefig(buffer, format='png')
        plot5 = buffer.getvalue()
        plot5 = base64.b64encode(plot5).decode('utf-8').replace('\n', '')
        
        fig, ax = plt.subplots()
        ax.plot(time, accel_z2)
        ax.set_xlabel('Time')
        ax.set_ylabel('Accelerometer of Sensor - 2 (Z)')
        ax.grid(True)

        buffer.seek(0)  # Reset buffer position to the beginning
        fig.savefig(buffer, format='png')
        plot6 = buffer.getvalue()
        plot6 = base64.b64encode(plot6).decode('utf-8').replace('\n', '')
        
        fig, ax = plt.subplots()
        ax.plot(time, accel_x3)
        ax.set_xlabel('Time')
        ax.set_ylabel('Accelerometer of Sensor - 3 (X)')
        ax.grid(True)

        buffer.seek(0)  # Reset buffer position to the beginning
        fig.savefig(buffer, format='png')
        plot7 = buffer.getvalue()
        plot7 = base64.b64encode(plot7).decode('utf-8').replace('\n', '')
        
        fig, ax = plt.subplots()
        ax.plot(time, accel_y3)
        ax.set_xlabel('Time')
        ax.set_ylabel('Accelerometer of Sensor - 3 (Y)')
        ax.grid(True)

        buffer.seek(0)  # Reset buffer position to the beginning
        fig.savefig(buffer, format='png')
        plot8 = buffer.getvalue()
        plot8 = base64.b64encode(plot8).decode('utf-8').replace('\n', '')
        
        fig, ax = plt.subplots()
        ax.plot(time, accel_z3)
        ax.set_xlabel('Time')
        ax.set_ylabel('Accelerometer of Sensor - 3 (Z)')
        ax.grid(True)

        buffer.seek(0)  # Reset buffer position to the beginning
        fig.savefig(buffer, format='png')
        plot9 = buffer.getvalue()
        plot9 = base64.b64encode(plot9).decode('utf-8').replace('\n', '')
        
        fig, ax = plt.subplots()
        ax.plot(time, gyro_x1)
        ax.set_xlabel('Time')
        ax.set_ylabel('Gyroscope of Sensor - 1 (X)')
        ax.grid(True)

        buffer.seek(0)  # Reset buffer position to the beginning
        fig.savefig(buffer, format='png')
        plot10= buffer.getvalue()
        plot10 = base64.b64encode(plot10).decode('utf-8').replace('\n', '')
        
        fig, ax = plt.subplots()
        ax.plot(time, gyro_y1)
        ax.set_xlabel('Time')
        ax.set_ylabel('Gyroscope of Sensor - 1 (Y)')
        ax.grid(True)

        buffer.seek(0)  # Reset buffer position to the beginning
        fig.savefig(buffer, format='png')
        plot11= buffer.getvalue()
        plot11 = base64.b64encode(plot11).decode('utf-8').replace('\n', '')
        
        fig, ax = plt.subplots()
        ax.plot(time, gyro_z1)
        ax.set_xlabel('Time')
        ax.set_ylabel('Gyroscope of Sensor - 1 (Z)')
        ax.grid(True)

        buffer.seek(0)  # Reset buffer position to the beginning
        fig.savefig(buffer, format='png')
        plot12= buffer.getvalue()
        plot12 = base64.b64encode(plot12).decode('utf-8').replace('\n', '')
        
        fig, ax = plt.subplots()
        ax.plot(time, gyro_x2)
        ax.set_xlabel('Time')
        ax.set_ylabel('Gyroscope of Sensor - 2 (X)')
        ax.grid(True)

        buffer.seek(0)  # Reset buffer position to the beginning
        fig.savefig(buffer, format='png')
        plot13= buffer.getvalue()
        plot13 = base64.b64encode(plot13).decode('utf-8').replace('\n', '')
        
        fig, ax = plt.subplots()
        ax.plot(time, gyro_y2)
        ax.set_xlabel('Time')
        ax.set_ylabel('Gyroscope of Sensor - 2 (Y)')
        ax.grid(True)

        buffer.seek(0)  # Reset buffer position to the beginning
        fig.savefig(buffer, format='png')
        plot14= buffer.getvalue()
        plot14 = base64.b64encode(plot14).decode('utf-8').replace('\n', '')
        
        fig, ax = plt.subplots()
        ax.plot(time, gyro_z2)
        ax.set_xlabel('Time')
        ax.set_ylabel('Gyroscope of Sensor - 2 (Z)')
        ax.grid(True)

        buffer.seek(0)  # Reset buffer position to the beginning
        fig.savefig(buffer, format='png')
        plot15= buffer.getvalue()
        plot15 = base64.b64encode(plot15).decode('utf-8').replace('\n', '')
        
        fig, ax = plt.subplots()
        ax.plot(time, gyro_x3)
        ax.set_xlabel('Time')
        ax.set_ylabel('Gyroscope of Sensor - 3 (X)')
        ax.grid(True)

        buffer.seek(0)  # Reset buffer position to the beginning
        fig.savefig(buffer, format='png')
        plot16= buffer.getvalue()
        plot16 = base64.b64encode(plot16).decode('utf-8').replace('\n', '')
        
        fig, ax = plt.subplots()
        ax.plot(time, gyro_y3)
        ax.set_xlabel('Time')
        ax.set_ylabel('Gyroscope of Sensor - 3 (Y)')
        ax.grid(True)

        buffer.seek(0)  # Reset buffer position to the beginning
        fig.savefig(buffer, format='png')
        plot17= buffer.getvalue()
        plot17 = base64.b64encode(plot17).decode('utf-8').replace('\n', '')
        
        fig, ax = plt.subplots()
        ax.plot(time, gyro_z3)
        ax.set_xlabel('Time')
        ax.set_ylabel('Gyroscope of Sensor - 3 (Z)')
        ax.grid(True)

        buffer.seek(0)  # Reset buffer position to the beginning
        fig.savefig(buffer, format='png')
        plot18= buffer.getvalue()
        plot18 = base64.b64encode(plot18).decode('utf-8').replace('\n', '')

        buffer.close()
        
        return render(request, 'home.html', {'plot1': plot1, 'time': time, 'plot2': plot2, 'plot3': plot3, 'plot4': plot4, 'plot5': plot5,
                                            'plot6': plot6, 'plot7': plot7, 'plot8': plot8, 'plot9': plot9, 'plot10': plot10, 'plot11': plot11,
                                           'plot12': plot12, 'plot13': plot13, 'plot14': plot14, 'plot15': plot15, 'plot16': plot16, 'plot17': plot17,
                                          'plot18': plot18})
    else:
        return render(request, 'home.html', {})
