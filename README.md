# ANK

End-to-end encrypted email using the JMAP and Signal protocols. Powered by Rust, Rocket and Diesel.

The Signal protocol is good, but its limited to usage with Signal the app.

Email is better as a messaging platform, but its old and frought with issues.


Some email providers are centralised, because the average person doesnt care, and just wants email without faff. Other organisations want to self host because of trust and downtime. Likewise some organisations have compliance or security requirements so they have to self host. 

Email is incredibly hard to self host at the moment. ISPs and big mail providers block residential IP blocks because of the high likelihood of spam.

Need to consider the problems shown on https://craphound.com/spamsolutions.txt

Proposed Solution:

- JMAP protocol
- Signal protocol
- Strict enforcement of SPF/DKIM/DMARC/More acronyms...
- Rust + Rocket + Diesel
- Simple config, setup etc. Give it a domain name, it checks itself to make sure ^ acronyms are in place, then starts. 


