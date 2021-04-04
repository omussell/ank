+++
title = "ANK"
template = "index.html"
page_template = "page.html"
sort_by = "weight"
+++

The Signal protocol is good, but its limited to usage with Signal the app.

Email is better as a messaging platform, but its old and frought with issues.

Some email providers are centralised, because the average person doesnt care, and just wants email without faff. Other organisations want to self host because of trust and downtime. Likewise some organisations have compliance or security requirements so they have to self host. 

Email is incredibly hard to self host at the moment. ISPs and big mail providers block residential IP blocks because of the high likelihood of spam.

Need to consider the problems shown on https://craphound.com/spamsolutions.txt

Proposed Solution:

- JMAP protocol
- Signal protocol
- Strict enforcement of SPF/DKIM/DMARC/More acronyms...
- Rust + Rocket + Diesel for prod, Go for POC
- Simple config, setup etc. Give it a domain name, it checks itself to make sure ^ acronyms are in place, then starts. 


Use DNSSEC+DANE?
Store signal keys in key transparency? Thats how people find out emails addresses of others and find out the keys

Should we support HTML? It can be used as attack vector, scripts, malicious images, tracking pixels etc. Maybe a subset of HTML? Or Gemini? Or just plain text...?
Use go for POC, and use existing signal C library with CGO

How to handle user authentication? user+pass, LDAP? oauth?

Key transparency

- Have a hash of the email address with its signal key(s). A hash rather than the email address itself so that it isnt publicly exposed.
- Should it be a global system like DNS, or one maintained per domain? Maybe both? DNS is public for public facing email, then individual orgs have their own internal DNS for internal only traffic.

POC

- Use Go
- Preferable to use Rust because its nice, but its hard. 
- Dont use fancy protobufs or GRPC. Just HTTPS + JSON.
- Thought about using Python since I can already do it. It'll be a pain in the butt. No autoformatting. Classes, testing, and typing are all annoying to use.
- Go might not have all the features, but if we're just doing DNS, HTTPS, JSON and some crypto stuff, it should be fine.
