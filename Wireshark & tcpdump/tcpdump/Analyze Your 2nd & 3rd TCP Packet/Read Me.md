# Analyze your second & third packet with TCPDump

## Scenario
In this activity, you’ll be putting your new TCPDump skills to the test by analyzing two PCAPs.

### TCPDump Activity Questions
#### PCAP 4
1. How many UDP packets have been captured?
2. How many TCP packets have both the SYN and ACK flags set?
3. Which version of Chrome was used to connect to securityblue.team?
4. How many packets have a TTL value of 38?

#### PCAP 5
1. What is the name of the PNG file on the webserver at 192.168.56.111?
2. Which version of OpenSSH is running on the server?
3. On which port is the .zip file being served?
4. When was a packet with a TCP checksum value of 53203 captured? (Format: xx:xx:xx.xxxxxx)

## Solutions
#### PCAP 4

1. Use the following command: tcpdump -r SBT-PCAP4.pcap udp | wc -l <br/>
   Answer: 3290
<img width="1440" alt="Screenshot 2025-04-22 at 11 03 07 PM" src="https://github.com/user-attachments/assets/8bce603a-78e5-4763-a33e-5dc5c70239a8" />

2. SYN + ACK = 00010010, which is 18 in decimal form. Use the following command: tcpdump -r SBT-PCAP4.pcap "tcp[tcpflags] == 18" | wc -l <br/>
Answer: 20
<img width="1440" alt="Screenshot 2025-04-22 at 11 10 52 PM" src="https://github.com/user-attachments/assets/d8267e86-5fa0-48fe-a1b7-13942d4603d9" />

3. Use the following command: tcpdump -r SBT-PCAP4.pcap -vvv | grep -i chrome. Alternatively you can also use tcpdump -r SBT-PCAP4.pcap -vvAls0 | grep 'User-Agent:' <br/>
Answer: 80.0.3987.87
<img width="1440" alt="Screenshot 2025-04-22 at 11 38 06 PM" src="https://github.com/user-attachments/assets/431b1f04-a5a9-43bb-aac2-c2b12ba664da" />

#### PCAP 5
1. 
