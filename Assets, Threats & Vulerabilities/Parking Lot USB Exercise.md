# Parking Lot USB drive

## Scenario
You are part of the security team at Rhetorical Hospital and arrive to work one morning. On the ground of the parking lot, you find a USB stick with the hospital's logo printed on it. There’s no one else around who might have dropped it, so you decide to pick it up out of curiosity.

You bring the USB drive back to your office where the team has virtualization software installed on a workstation. Virtualization software can be used for this very purpose because it’s one of the only ways to safely investigate an unfamiliar USB stick. The  software works by running a simulated instance of the computer on the same workstation. This simulation isn’t connected to other files or networks, so the USB drive can’t affect other systems if it happens to be infected with malicious software.
## Solution

|Points| Description|
|---|---|
|Contents | Jorge's USB contains a combination of personal and work documents. However, Jorge might not want to release his personal files. The work files contain some information about new hires and the employees' schedules on it, potentially with their ID numbers on it, which could be useful to attackers.|
|Attacker mindset | Attackers may be able to use the information from the USB to target employees of the hospital. Through the personal information found on the USB, attackers could imitate Jorge's relative or friend to get valuable information out of him.|
|Risk analysis | The USB drive could contain a number of preloaded viruses, backdoors, ransomware, spyware, and more. When the USB drive is connected, the malware can automatically install itself onto the system, compromising the device. An employee plugging the USB into their work/personal laptop could fall victim to any of the malicious software previously mentioned. A threat actor could further use this opportunity to find more information they could use for their purposes.|
