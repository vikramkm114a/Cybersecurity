# Wireshark - Analyze your first packet with Wireshark

## Scenario
In this scenario, you’re a security analyst investigating traffic to a website.

You’ll analyze a network packet capture file that contains traffic data related to a user connecting to an internet site. The ability to filter network traffic using packet sniffers to gather relevant information is an essential skill as a security analyst.

You must filter the data in order to:

1. Identify the source and destination IP addresses involved in this web browsing session,
2. Examine the protocols that are used when the user makes the connection to the website, and
3. Analyze some of the data packets to identify the type of information sent and received by the systems that connect to each other when the network data is captured.

An overview of the key property columns listed for each packet: 
* `No` : The index number of the packet in this packet capture file.
* `Time`: The timestamp of the packet.
* `Source`: The source IP address.
* `Destination`: The destination IP address.
* `Protocol`: The protocol contained in the packet.
* `Length`: The total length of the packet.
* `Info`: Some infomation about the data in the packet (the payload) as interpreted by Wireshark.

## Solutions 
1. Identify the source and destination IP addresses involved in this web browsing session.
* On the title bar, type `ip.addr == 142.250.1.139` to filter for traffic associated with a specific IP address. Select the first packet that contains `TCP` on the info field. `addr` means either the source or the destination IP. 

![Wireshark1](https://github.com/user-attachments/assets/d2472f5b-0742-40ec-a177-ec8a10a10f78)

![Wireshark2](https://github.com/user-attachments/assets/9ea4b964-1c87-4657-8104-7f159223f77e)


* On the title bar, type `ip.src == 142.250.1.139` to filter for traffic associated with a specific IP address. `src` means it is where the packet comes from.
  
![Wireshark3](https://github.com/user-attachments/assets/a9cc6e75-f6db-4f17-bf8f-ad5f2a8544e2)


  
* On the title bar, type `ip.dst == 142.250.1.139` to filter for traffic associated with a specific IP address. `dst` means it is where the packet goes to.

![Wireshark4](https://github.com/user-attachments/assets/b4566968-aad6-4916-86c4-c67f3ec8c58a)


* On the title bar, type `eth.addr == 42:01:ac:15:e0:02` to filter for traffic associated with a specific Ethernet MAC address. `addr` means either the source or the destination IP. 

![Wireshark5](https://github.com/user-attachments/assets/0e9beb68-1d5a-4df3-9927-8e1fe9ac6d46)


2. Examine the protocols that are used when the user makes the connection to the website.
* The TCP destination port of this TCP packet is 80 when `ip.addr == 142.250.1.139` which contains the initial web request to an HTPP website that will typically be listening on TCP port 80.

![Wireshark6](https://github.com/user-attachments/assets/a26b99d9-f152-41c5-8e79-b0e9bf859346)


* The protocol destination port is TCP when Etherenet address was `42:01:ac:15:e0:02`. Source address is `172.21.224.2` and the destination address is `35.235.244.34`. 

![Wireshark7](https://github.com/user-attachments/assets/07ad9f65-b7f7-49fc-a2b5-c649350e39b0)


3. Analyze the data packet to identify the type of information sent and received by the systems that connect to each other when the network data is captured.
* On the title bar, type `tcp.port == 80` to filter for traffic associated with a specific port number. `tcp.port == 80` means only the tcp port is 80 will be shown. 
  
![Wireshark8](https://github.com/user-attachments/assets/5d3f0b1b-7154-4094-9a24-5e1afa131760)


* When the filter `tcp.port == 80` sets in play, the time to live is 64.
* `Time to Live`: A field in the Internet Protocol (IP) header that indicates the maximum amount of time an IP packet is allowed to exist in the network before it is discarded if it has not reached its destination. TTL is used to prevent packets from circulating indefinitely in the network, which could happen in the case of routing loops. It can be used as a basic security measure to limit how far packets can propagate through the network.
  
![chrome_iI9QT2BqWs](https://github.com/Kwangsa19/Ketmanto-Cybersecurity-Portfolio/assets/135963482/1fe9ba32-926b-42f3-a39e-49da54240058)


* When the filter `tcp.port == 80` sets in play, the Frame Number is 37 and Frame Length is 54 bytes.
* `Frame Number`: This is essentially the sequence number of a packet within a particular capture. It helps you identify and refer to packets more easily. In your case, a frame number of 37 means it's the 37th packet captured since the beginning of the capture session. This number is assigned sequentially as packets are captured, starting with the number 1 for the first packet.

* `Frame Length`: This indicates the size of the packet, including all headers and payload, measured in bytes. The frame length of 54 bytes means the total size of the packet is 54 bytes. This size includes everything from the lowest layer (physical layer) up to the highest layer present in the packet that Wireshark can decode. It's useful for understanding the size of the data being transmitted and can help in various analyses, such as identifying potential issues with packet sizes that might indicate fragmentation or other problems.

![chrome_xSk2HRghJg](https://github.com/Kwangsa19/Ketmanto-Cybersecurity-Portfolio/assets/135963482/107d084b-361e-4f74-98ea-c90c93fe1cae)







## Conclusion
We now have practical experience using Wireshark to

* open saved packet capture files,
* view high-level packet data, and
* use filters to inspect detailed packet data.
