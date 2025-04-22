# Wireshark - Analyze your second & third packet with Wireshark

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
