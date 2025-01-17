# -*- coding: utf-8 -*-
"""Basic_Network_Sniffer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1splP0KLINDQ00VGcDjstM4r8xEXNop85
"""

pip install scapy

from scapy.all import sniff, IP, TCP

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        # Print out the IP source and destination
        print(f"IP Packet: {ip_layer.src} -> {ip_layer.dst}")

        # Check if the packet has a TCP layer
        if TCP in packet:
            tcp_layer = packet[TCP]
            # Print out the TCP source and destination ports
            print(f"TCP Packet: {ip_layer.src}:{tcp_layer.sport} -> {ip_layer.dst}:{tcp_layer.dport}")

# Start sniffing
print("Starting sniffer...")
sniff(prn=packet_callback, count=10)  # Change count to the number of packets you want to capture