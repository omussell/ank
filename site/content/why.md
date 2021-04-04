+++
title = "Why ANK?"
weight = 2
+++

## Backwards compatibility
Email has been plagued by problems from the beginning. Encryption of messages and trust of the network were not seen as vital. So it is plain text and anyone can email anyone.

## Complexity
Its grown to have lots of protocols and RFCs. It always needs backwards compatibility to work with all providers.

## Identity

An email address is often used as the core identity for people on the internet. Its the username, then services send an email with a special link to validate that the user owns that email address.

## Security

I've worked for big companies with high security requirements. They use self hosted MS Exchange because its the easiest option. A lot are now moving to O365 because they dont want the burden of managing email.


## Spam

We arent going to be eliminating spam. It'll be computationally more expensive/difficult because of the signal encryption.

It'll be harder to detect email addresses, but once they're known to a spammer they're not going to be blocked necessarily. Key Transparency might help in that bad domains could be blocked at the KT level.

Maybe we need a domain / organisation level signal key? To authenticate that the email came from that domains ANK servers and that domain.

A lot of the emails that I get are too complicated. What type of emails do I want? Bills/receipts from companies when I pay them. User authentication. Sending messages to people. Thats it. No images, no fancy borders and colours, no fuss, just text.




The Signal protocol is good, but its limited to usage with Signal the app.

Email is better as a messaging platform, but its old and frought with issues.

Some email providers are centralised, because the average person doesnt care, and just wants email without faff. Other organisations want to self host because of trust and downtime. Likewise some organisations have compliance or security requirements so they have to self host. 

Email is incredibly hard to self host at the moment. ISPs and big mail providers block residential IP blocks because of the high likelihood of spam.

Proposed Solution:

- [JMAP protocol](https://jmap.io/)
- [Signal protocol](https://signal.org/docs/)
- Strict enforcement of SPF/DKIM/DMARC/More acronyms...
- [Key transparency](https://github.com/google/keytransparency) for discovery of signal keys
- Rust + Rocket + Diesel for prod, Go for POC
- Simple config, setup etc. Give it a domain name, it checks itself to make sure ^ acronyms are in place, then starts. 

