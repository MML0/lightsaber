import socket
import cv2
import numpy as np

esp_ip = [
    {'ip': '192.168.43.102', 'revers': False},
    {'ip': '192.168.43.103', 'revers': False},
    {'ip': '192.168.43.104', 'revers': False},
    {'ip': '192.168.43.106', 'revers': False},
    {'ip': '192.168.43.107', 'revers': False},
    {'ip': '192.168.43.108', 'revers': False},
    {'ip': '192.168.43.111', 'revers': False},
    {'ip': '192.168.43.112', 'revers': False},
    {'ip': '192.168.43.113', 'revers': False},
    {'ip': '192.168.43.114', 'revers': False},
    {'ip': '192.168.43.115', 'revers': False},
    {'ip': '192.168.43.116', 'revers': False},
    {'ip': '192.168.43.117', 'revers': False},
    {'ip': '192.168.43.118', 'revers': False},
    {'ip': '192.168.43.119', 'revers': False},
    {'ip': '192.168.43.120', 'revers': False},
    {'ip': '192.168.43.121', 'revers': False},
    {'ip': '192.168.43.123', 'revers': False},
    {'ip': '192.168.43.145', 'revers': False},
    {'ip': '192.168.43.168', 'revers': False},
    {'ip': '192.168.43.191', 'revers': False},
    {'ip': '192.168.43.202', 'revers': False},
    {'ip': '192.168.43.203', 'revers': False},
    {'ip': '192.168.43.204', 'revers': False},
    {'ip': '192.168.43.205', 'revers': False},
    {'ip': '192.168.43.206', 'revers': False},
    {'ip': '192.168.43.207', 'revers': False},
    {'ip': '192.168.43.208', 'revers': False},
    {'ip': '192.168.43.209', 'revers': False},
]


# Define ESP devices
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

pixel_bytes = bytearray(140*3)
def send_columns_to_esps():
    esp_ip = [
        {'ip': '192.168.43.191', 'revers': False},
        {'ip': '192.168.43.145', 'revers': False},
        {'ip': '192.168.43.123', 'revers': False},
        {'ip': '192.168.43.168', 'revers': False},
        {'ip': '192.168.43.102', 'revers': False},
        {'ip': '192.168.43.107', 'revers': False},
        {'ip': '192.168.43.104', 'revers': False},
        {'ip': '192.168.43.108', 'revers': False},
        {'ip': '192.168.43.106', 'revers': False},
        {'ip': '192.168.43.103', 'revers': False},
        {'ip': '192.168.43.209', 'revers': False},
        {'ip': '192.168.43.111', 'revers': False},
        {'ip': '192.168.43.112', 'revers': False},
        {'ip': '192.168.43.113', 'revers': False},
        {'ip': '192.168.43.114', 'revers': False},
        {'ip': '192.168.43.115', 'revers': False},
        {'ip': '192.168.43.116', 'revers': False},
        {'ip': '192.168.43.117', 'revers': False},
        {'ip': '192.168.43.118', 'revers': False},
        {'ip': '192.168.43.119', 'revers': False},
        {'ip': '192.168.43.120', 'revers': False},
        {'ip': '192.168.43.121', 'revers': False},
        {'ip': '192.168.43.202', 'revers': False},
        {'ip': '192.168.43.203', 'revers': False},
        {'ip': '192.168.43.204', 'revers': False},
        {'ip': '192.168.43.205', 'revers': False},
        {'ip': '192.168.43.206', 'revers': False},
        {'ip': '192.168.43.207', 'revers': False},
        {'ip': '192.168.43.208', 'revers': False},
        {'ip': '192.168.43.12', 'revers': False},
        {'ip': '192.168.43.158', 'revers': False},
        {'ip': '192.168.43.172', 'revers': False},
        {'ip': '192.168.43.148', 'revers': False},
        {'ip': '192.168.43.137', 'revers': False},
        {'ip': '192.168.43.194', 'revers': False},
        {'ip': '192.168.43.100', 'revers': False},
        {'ip': '192.168.43.176', 'revers': False},
    ]

    # Load image from file (e.g., saved from TOP)
    image_path = "jpg_out/snapshot.png"
    frame = cv2.imread(image_path)

    if frame is None:
        print("Failed to read image.")
        return

    # Resize to width = 70 if it's larger
    h, w, _ = frame.shape
    print( frame.shape)
    if w > 70:
        frame = cv2.resize(frame, (70, h), interpolation=cv2.INTER_AREA)
        h, w, _ = frame.shape

    # Send to each ESP (in round-robin or mapped logic)
    for i, esp in enumerate(esp_ip):
        row  = i*(h//len(esp_ip))
        print(row)
        column_data = frame[row, :, :]  # shape (h, 3)
        for col in range(w):
            r, g, b = column_data[col]
            pixel_bytes[col*3] = int(float(b)/1)
            pixel_bytes[col*3+1] = int(float(g)/1)
            pixel_bytes[col*3+2] = int(float(r)/1)

        # Add header byte
        data = b'\xAA'+ pixel_bytes[:3*w]
        print(len(data)/3)

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
    