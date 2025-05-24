import socket
import cv2
import numpy as np

esp_ip = [
    # {'ip': '192.168.43.102', 'revers': False},
    # {'ip': '192.168.43.103', 'revers': False},
    # {'ip': '192.168.43.104', 'revers': False},
    # {'ip': '192.168.43.106', 'revers': False},
    # {'ip': '192.168.43.107', 'revers': False},
    # {'ip': '192.168.43.108', 'revers': False},
    # {'ip': '192.168.43.111', 'revers': False},
    {'ip': '192.168.43.112', 'revers': False},
    # {'ip': '192.168.43.113', 'revers': False},
    # {'ip': '192.168.43.114', 'revers': False},
    # {'ip': '192.168.43.115', 'revers': False},
    # {'ip': '192.168.43.116', 'revers': False},
    # {'ip': '192.168.43.117', 'revers': False},
    # {'ip': '192.168.43.118', 'revers': False},
    # {'ip': '192.168.43.119', 'revers': False},
    # {'ip': '192.168.43.120', 'revers': False},
    # {'ip': '192.168.43.121', 'revers': False},
    # {'ip': '192.168.43.123', 'revers': False},
    # {'ip': '192.168.43.145', 'revers': False},
    # {'ip': '192.168.43.168', 'revers': False},
    # {'ip': '192.168.43.191', 'revers': False},
    # {'ip': '192.168.43.202', 'revers': False},
    # {'ip': '192.168.43.203', 'revers': False},
    # {'ip': '192.168.43.204', 'revers': False},
    # {'ip': '192.168.43.205', 'revers': False},
    # {'ip': '192.168.43.206', 'revers': False},
    # {'ip': '192.168.43.207', 'revers': False},
    # {'ip': '192.168.43.208', 'revers': False},
    # {'ip': '192.168.43.209', 'revers': False},
]


# Define ESP devices
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

pixel_bytes = bytearray(140*3)
def send_columns_to_esps():
    esp_ip = [
        {'ip': '192.168.43.119', 'revers': False},
        {'ip': '192.168.43.137', 'revers': False},

        {'ip': '192.168.43.182', 'revers': False},
        {'ip': '192.168.43.132', 'revers': False},
        {'ip': '192.168.43.118', 'revers': False},
        {'ip': '192.168.43.129', 'revers': False},
        {'ip': '192.168.43.143', 'revers': False},
        {'ip': '192.168.43.131', 'revers': False},
        {'ip': '192.168.43.162', 'revers': False},
        {'ip': '192.168.43.110', 'revers': False},
        {'ip': '192.168.43.181', 'revers': False},
        {'ip': '192.168.43.149', 'revers': False},
        {'ip': '192.168.43.166', 'revers': False},
        {'ip': '192.168.43.169', 'revers': False},
        {'ip': '192.168.43.134', 'revers': False},
        {'ip': '192.168.43.127', 'revers': False},
        {'ip': '192.168.43.160', 'revers': False},
        {'ip': '192.168.43.185', 'revers': False},
        {'ip': '192.168.43.155', 'revers': False},
        {'ip': '192.168.43.107', 'revers': False},
        {'ip': '192.168.43.177', 'revers': False},
        {'ip': '192.168.43.147', 'revers': False},
        {'ip': '192.168.43.189', 'revers': False},
        {'ip': '192.168.43.148', 'revers': False},
        {'ip': '192.168.43.112', 'revers': False},
        {'ip': '192.168.43.156', 'revers': False},
        {'ip': '192.168.43.138', 'revers': False},
        {'ip': '192.168.43.102', 'revers': False},
        {'ip': '192.168.43.135', 'revers': False},
        {'ip': '192.168.43.139', 'revers': False},
        {'ip': '192.168.43.140', 'revers': False},
        {'ip': '192.168.43.116', 'revers': False},


        {'ip': '192.168.43.164', 'revers': False},
        {'ip': '192.168.43.154', 'revers': False},
        {'ip': '192.168.43.159', 'revers': False},
        {'ip': '192.168.43.174', 'revers': False},
        {'ip': '192.168.43.175', 'revers': False},
        {'ip': '192.168.43.183', 'revers': False},
        {'ip': '192.168.43.190', 'revers': False},
        {'ip': '192.168.43.167', 'revers': False},
        {'ip': '192.168.43.186', 'revers': False},
        {'ip': '192.168.43.152', 'revers': False},
        {'ip': '192.168.43.144', 'revers': False},
        {'ip': '192.168.43.187', 'revers': False},
        {'ip': '192.168.43.152', 'revers': False},
        {'ip': '192.168.43.146', 'revers': False},
        {'ip': '192.168.43.172', 'revers': False},
        {'ip': '192.168.43.157', 'revers': False},
        {'ip': '192.168.43.178', 'revers': False},
        {'ip': '192.168.43.184', 'revers': False},
        {'ip': '192.168.43.168', 'revers': False},
        {'ip': '192.168.43.142', 'revers': False},
        {'ip': '192.168.43.141', 'revers': False},
        {'ip': '192.168.43.100', 'revers': False},
        {'ip': '192.168.43.153', 'revers': False},
        {'ip': '192.168.43.180', 'revers': False},
        {'ip': '192.168.43.163', 'revers': False},
        {'ip': '192.168.43.133', 'revers': False},
        {'ip': '192.168.43.111', 'revers': False},
        {'ip': '192.168.43.150', 'revers': False},
        {'ip': '192.168.43.145', 'revers': False},
        {'ip': '192.168.43.158', 'revers': False},
        {'ip': '192.168.43.117', 'revers': False},
        {'ip': '192.168.43.113', 'revers': False},
        {'ip': '192.168.43.105', 'revers': False},
        {'ip': '192.168.43.121', 'revers': False},
        
        {'ip': '192.168.43.191', 'revers': False},
        {'ip': '192.168.43.106', 'revers': False},
        {'ip': '192.168.43.126', 'revers': False},
        {'ip': '192.168.43.101', 'revers': False},
        {'ip': '192.168.43.179', 'revers': False},
        {'ip': '192.168.43.124', 'revers': False},
        {'ip': '192.168.43.108', 'revers': False},
        {'ip': '192.168.43.193', 'revers': False},
        # {'ip': '192.168.43.177', 'revers': False},
        {'ip': '192.168.43.188', 'revers': False},
        {'ip': '192.168.43.104', 'revers': False},
        {'ip': '192.168.43.200', 'revers': False},
        {'ip': '192.168.43.115', 'revers': False},
        {'ip': '192.168.43.114', 'revers': False},
        {'ip': '192.168.43.122', 'revers': False},
        {'ip': '192.168.43.103', 'revers': False},
        {'ip': '192.168.43.128', 'revers': False},
        {'ip': '192.168.43.192', 'revers': False},
        {'ip': '192.168.43.120', 'revers': False},
        {'ip': '192.168.43.123', 'revers': False},
        {'ip': '192.168.43.130', 'revers': False},
        {'ip': '192.168.43.170', 'revers': False},
        
    ]

    # Load image from file (e.g., saved from TOP)
    image_path = "jpg_out/snapshot.png"
    frame = cv2.imread(image_path)

    if frame is None:
        print("Failed to read image.")
        return

    # Resize to width = 70 if it's larger
    h, w, _ = frame.shape
    # print( frame.shape)
    if w > 70:
        frame = cv2.resize(frame, (70, h), interpolation=cv2.INTER_AREA)
        h, w, _ = frame.shape

    # Send to each ESP (in round-robin or mapped logic)
    for i, esp in enumerate(esp_ip):
        row  = i*(h//len(esp_ip))
        # print(row)
        column_data = frame[row, :, :]  # shape (h, 3)
        for col in range(w):
            r, g, b = column_data[col]
            pixel_bytes[col*3] = int(float(b)/1)
            pixel_bytes[col*3+1] = int(float(g)/1)
            pixel_bytes[col*3+2] = int(float(r)/1)

        # Add header byte
        data = b'\xAA'+ pixel_bytes[:3*w]
        # print(len(data)/3)

        try:
            sock.sendto(data, (esp['ip'], 8266))
            # sock.close()
        except Exception as er:
            print(f"Failed to send to {esp['ip']}: {er}")

def onOffToOn(channel, sampleIndex, val, prev):
    # print("Triggered: Grabbing frame and sending to ESPs")
    top = op('out1')  # TouchDesigner TOP
    top.save("jpg_out/snapshot.png")
    send_columns_to_esps()

def whileOn(channel, sampleIndex, val, prev):
    return

def onOnToOff(channel, sampleIndex, val, prev):
    return

def whileOff(channel, sampleIndex, val, prev):
    return

def onValueChange(channel, sampleIndex, val, prev):
    return
    