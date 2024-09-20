# Controls and Compliance Assessment 

## Case Study

This scenario is based on a fictional company:

Botium Toys is a small U.S. business that develops and sells toys. The business has a single physical location, which serves as their main office, a storefront, and warehouse for their products. However, Botium Toy’s online presence has grown, attracting customers in the U.S. and abroad. As a result, their information technology (IT) department is under increasing pressure to support their online market worldwide. 

The manager of the IT department has decided that an internal IT audit needs to be conducted. She expresses concerns about not having a solidified plan of action to ensure business continuity and compliance, as the business grows. She believes an internal audit can help better secure the company’s infrastructure and help them identify and mitigate potential risks, threats, or vulnerabilities to critical assets. The manager is also interested in ensuring that they comply with regulations related to internally processing and accepting online payments and conducting business in the European Union (E.U.).   

The IT manager starts by implementing the National Institute of Standards and Technology Cybersecurity Framework (NIST CSF), establishing an audit scope and goals, listing assets currently managed by the IT department, and completing a risk assessment. The goal of the audit is to provide an overview of the risks and/or fines that the company might experience due to the current state of their security posture.

Your task is to review the IT manager’s scope, goals, and risk assessment report. Then, perform an internal audit by completing a controls and compliance checklist. 

## Scenario
Botium Toys: Scope, Goals, and Risk Assessment Report

### Scope 
The scope of this audit is defined as the entire security program at Botium
Toys. This includes their assets like employee equipment and devices, their internal
network, and their systems. You will need to review the assets Botium Toys has and the
controls and compliance practices they have in place.

### Goals
Assess existing assets and complete the controls and compliance checklist to
determine which controls and compliance best practices that need to be implemented
to improve Botium Toys’ security posture.

### Current assets
Assets managed by the IT Department include:
* On-premises equipment for in-office business needs
* Employee equipment: end-user devices (desktops/laptops, smartphones),
remote workstations, headsets, cables, keyboards, mice, docking stations,
surveillance cameras, etc.
* Storefront products available for retail sale on site and online; stored in the
company’s adjoining warehouse
* Management of systems, software, and services: accounting,
telecommunication, database, security, ecommerce, and inventory
management
* Internet access
* Internal network
* Data retention and storage
* Legacy system maintenance: end-of-life systems that require human
monitoring

### Risk assessment

#### Risk description
Currently, there is inadequate management of assets. Additionally, Botium Toys does
not have all of the proper controls in place and may not be fully compliant with U.S. and
international regulations and standards.

#### Control best practices
The first of the five functions of the NIST CSF is Identify. Botium Toys will need to
dedicate resources to identify assets so they can appropriately manage them.
Additionally, they will need to classify existing assets and determine the impact of the
loss of existing assets, including systems, on business continuity.

#### Risk score
On a scale of 1 to 10, the risk score is 8, which is fairly high. This is due to a lack of
controls and adherence to compliance best practices.

#### Additional comments
The potential impact from the loss of an asset is rated as medium, because the IT
department does not know which assets would be at risk. The risk to assets or fines
from governing bodies is high because Botium Toys does not have all of the necessary
controls in place and is not fully adhering to best practices related to compliance
regulations that keep critical data private/secure. Review the following bullet points for
specific details:
* Currently, all Botium Toys employees have access to internally stored data and
may be able to access cardholder data and customers’ PII/SPII.
* Encryption is not currently used to ensure confidentiality of customers’ credit
card information that is accepted, processed, transmitted, and stored locally in
the company’s internal database.
* Access controls pertaining to least privilege and separation of duties have not
been implemented.
* The IT department has ensured availability and integrated controls to ensure
data integrity.
* The IT department has a firewall that blocks traffic based on an appropriately
defined set of security rules.
* Antivirus software is installed and monitored regularly by the IT department.
* The IT department has not installed an intrusion detection system (IDS).
* There are no disaster recovery plans currently in place, and the company does
not have backups of critical data.
* The IT department has established a plan to notify E.U. customers within 72
hours if there is a security breach. Additionally, privacy policies, procedures, and
processes have been developed and are enforced among IT department
members/other employees, to properly document and maintain data.
* Although a password policy exists, its requirements are nominal and not in line
with current minimum password complexity requirements (e.g., at least eight
characters, a combination of letters and at least one number; special
characters).
* There is no centralized password management system that enforces the
password policy’s minimum requirements, which sometimes affects
productivity when employees/vendors submit a ticket to the IT department to
recover or reset a password.
* While legacy systems are monitored and maintained, there is no regular
schedule in place for these tasks and intervention methods are unclear.
* The store’s physical location, which includes Botium Toys’ main offices, store
front, and warehouse of products, has sufficient locks, up-to-date
closed-circuit television (CCTV) surveillance, as well as functioning fire
detection and prevention systems.

#### Additional Info 

Controls within cybersecurity are grouped into three main categories: 
1. Administrative/Managerial controls
2. Technical controls
3. Physical/Operational controls

Control types include, but are not limited to:
1. Preventative (preventing an incident from occurring in the first place)
2. Corrective (restoring an asset after an incident)
3. Detective (Determining whether an incident has occurred or is in progress)
4. Deterrent (Discouraging attacks)

## Controls Assessment Checklist

Does Botium Toys currenly have this control in place? 

| Yes / No | Control | Explanation |
| :-------        |    :---:   | :---     |
| No | Least Privilege | Preventative; Access controls pertaining to least privilege have not been implemented. This has to be changed to reduce the risk of breach. |
| No | Disaster Recovery Plans | Corrective; At the moment, there is no plan for handling disaster. Implementing this ensures the business continuity. |
| ? | Password policies | Preventative; A password policy exists, yet the requirements don't meet security standards and put the identity management access at risk. |
| No | Separation of duties | Preventative; Access controls pertaining to separation of duties have not been implemented. |
| Yes | Firewall | Preventative; The organization has a firewall to block traffic based on an appropriately defined set of security rules. |
| No | Intrusion detection system (IDS) | Detective; The IT department has not installed an intrusion detection system (IDS). This would help IT team to identify possible intrusions by threat actors. |
| No | Backups | Corrective; The company does not have backups of critical data. They have to implement the backup plan, such as incremental, full, or partial to prevent future data loss. |
| Yes | Antivirus software | Corrective; The antivirus software is active and regulary monitored by IT team. |
| ? | Manual monitoring, maintenance, and intervention for legacy systems | Preventative/corrective; While legacy systems are monitored and maintained, there is no regular schedule in place for these tasks and intervention methods are unclear. |
| No | Encryption | Deterrent; Encryption is not currently used to ensure confidentiality of customers’ credit card information that is accepted, processed, transmitted, and stored locally in the company’s internal database. |
| No | Password management system | Corrective; There is no centralized password management system that enforces the password policy’s minimum requirements, which sometimes affects productivity when employees/vendors submit a ticket to the IT department to recover or reset a password. |
| Yes | Locks (offices, storefront, warehouse) | Preventative; The store’s physical location, which includes Botium Toys’ main offices, store front, and warehouse of products, has sufficient locks.|
| Yes | Closed-circuit television (CCTV) surveillance | Preventative/detective; The store’s physical location, which includes Botium Toys’ main offices, store front, and warehouse of products, has  up-to-date closed-circuit television (CCTV) surveillance. |
| Yes | Fire detection/prevention (fire alarm, sprinkler system, etc.) | Preventative/detective; The organization has these. However, the team should maintain it and establish a plan on how to use it. |

## Compliance Checklist
Does Botium Toys currenly adhrere to this compliance best practice? 


* Payment Card Industry Data Security Standard (PCI DSS)

| Yes/ No | Best Practice | Explanation |
| :---        |    :---:   | :---     |
| No | Only authorized users have access to customers’ credit card information. | At the moment, all employees have access to it, which is a bad practice in the business.  |
| No | Credit card information is stored, accepted, processed, and transmitted internally, in a secure environment. | It is not encrypted and violates law and regulations. |
| No | Implement data encryption procedures to better secure credit card transaction touchpoints and data. | No, the encryption has not taken place yet. |
| No | Adopt secure password management policies. | The password management policies are not secure. |


* GDPR
  
| Yes/ No | Best Practice | Explanation |
| :---        |    :---:   | :---     |
| No | E.U. customers’ data is kept private/secured. | The organization does not apply GDPR practice. Thus, it puts them at risk of being fined by the EU government. |
| Yes | There is a plan in place to notify E.U. customers within 72 hours if their data is compromised/there is a breach. | The IT department has established a plan to notify E.U. customers within 72 hours if there is a security breach. |
| Yes | Privacy policies are maintained properly.| According to the scenario, it has been enforced by the IT Team members and other staff. |


* System and Organizations Controls 

| Yes/ No | Best Practice | Explanation |
| :---        |    :---:   | :---     |
| No | User access policies are established | Employees have access to internally stored data which means the access policy has not been applied. |
| No | Sensitive data (PII/SPII) is confidential/private. | Currently, all Botium Toys employees have access to internally stored data and may be able to access cardholder data and customers’ PII/SPII. |
| Yes | Data integrity ensures the data is consistent, complete, accurate, and has been validated. | The IT department has ensured availability and integrated controls to ensure data integrity. | 
| No | Data is available to individuals authorized to access it. | Currently, all the employees can access all the data. |

## Recommendations (optional)

After researching Botium Toys's security posture, the analysts agreed that the security practice is far from the expectation. It lacks of protection of confidentialiy of sensitive information. The following are:
1. Least privilege
2. Disaster recovery plan
3. Password policies
4. Encryption
5. Password management system

To address gaps in compliance, Botium needs to implement and establish the policies that can address the issues listed above. Botium also needs to update its assets so the additional control can be identified as soon as possible to improve their security practice. 
