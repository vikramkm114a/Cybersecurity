# Analyze your second & third packet with Wireshark

## Scenario
In this activity, you’ll be putting your new Wireshark skills to the test by analyzing two PCAPs, which increase in difficulty.

### Wireshark Activity Questions
#### PCAP 1
1. Which protocol was used over port 3942?
2. What is the IP address of the host that was pinged twice?
3. How many DNS query response packets were captured?
4. What is the IP address of the host which sent the most number of bytes?

#### PCAP 2
1. What is the WebAdmin password?
2. What is the version number of the attacker’s FTP server?
3. Which port was used to gain access to the victim Windows host?
4. What is the name of a confidential file on the Windows host?
5. What is the name of the log file that was created at 4:51 AM on the Windows host?

## Solutions
#### PCAP 1
1. Apply the following filter: tcp.port==3942 || udp.port==3942. Upon reviewing each of the packets on the list you will notice that they all use UDP.
<img width="1440" alt="Screenshot 2025-04-21 at 7 00 13 PM" src="https://github.com/user-attachments/assets/de14151f-935b-488e-9202-5274f51dccf3" />

2. Pings use ICMP packets, so that's what we filter for. Remember, Wireshark is case sensitive. Apply the following filter: icmp. Look under Source, which is where we can find the IP address of the host. Notice that there is one particular IP that was pinged twice: 8.8.4.4
<img width="1440" alt="Screenshot 2025-04-21 at 7 01 03 PM" src="https://github.com/user-attachments/assets/6ec30555-16fb-4f98-a13c-feb2c08eb86b" />

3. Filter for dns && ip.dst == 192.168.1.7 and look at the bottom right corner of the application to see the number of packets on the list. There are a total of 90 packets.
<img width="1440" alt="Screenshot 2025-04-21 at 7 01 30 PM" src="https://github.com/user-attachments/assets/28fce60d-d580-407f-a513-1fdf403a326a" />

4. On the top menu bar of Wireshark application, click on the Statistic menu then Endpoint.
Another menu will pop-up. On menu tab, click on IPv4. Filter for 'Tx Bytes' (Transfer Bytes) because we are looking for the sender. The IP address we are looking for is 115.178.9.18
<img width="1440" alt="Screenshot 2025-04-21 at 6 58 33 PM" src="https://github.com/user-attachments/assets/8d87e87a-1e29-4325-8ac6-dbd9a7eb820b" />


#### PCAP 2
1. Press Ctrl+F and search for the String "WebAdmin". Ensure the correct parameters are selected: Packet Details, String. Searching in the Info column, click on packet No.4123 and inspect the packet header. Under 'Line-based text data:' we will see the WebAdmin Password: sbt123.
<img width="1440" alt="Screenshot 2025-04-21 at 7 14 22 PM" src="https://github.com/user-attachments/assets/87edc1f0-ece6-459e-9879-9cae7f1bd033" />

2. 

