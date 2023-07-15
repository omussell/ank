For initial version, should be purely plain text messages. We are going to be storing them inside a database so will need to be small amount of text.
No formatting, no attachments, no hypertext or images.
Can have links, but it will be plaintext.
Should use sqlite mainly
Postgres is future option but shouldnt necessarily be needed anyway, sqlite can cope.


DNS should store the servers public key or some form of signature so we dont have spam and so we dont have to use DKIM/DMARC/SPF etc. for validation.


Client is just http client via curl or python requests+typer cli
Eventually the client could be a TUI?


Its actually the same setup as SSH and SSHFP records
We want ANKFP records lol. Or just use SRV as usual
They're whats used to validate the server key

Would there be two servers, one for users to login/keys, and one for sending/receiving messages?
Need to log in to view the messages and decrypt them
Would we need client/device keys? Each client to have a key to associate with a user? Existing clients just need password, new clients need MFA to double check its the correct user. Or if reset password.
That would then require a server for managing users and their clients.

Used with the client/server for sending messages. Maybe an email replacement using JMAP.

## Implementation

The Signal protocol is good, but its limited to usage with Signal the app. There are open source libraries, but they havent been updated on Github in a long time. The recommended library is written in Java.

The Signal app also works based on phone numbers. It would be nicer to have an email address and password+MFA, then its device agnostic.

Email is better as a messaging platform, but its old and frought with issues.

Some email providers are centralised, because the average person doesnt care, and just wants email without faff. Other organisations want to self host because of trust and downtime. Likewise some organisations have compliance or security requirements so they have to self host. 

Email is incredibly hard to self host at the moment. ISPs and big mail providers block residential IP blocks because of the high likelihood of spam.

Need to consider the problems shown on https://craphound.com/spamsolutions.txt

Proposed Solution:

- JMAP protocol
- Signal protocol
- Strict enforcement of SPF/DKIM/DMARC/More acronyms...
- Initial proof of concept using Python+FastAPI+PyNaCl
- Eventually Rust or Ada/Spark + SparkNaCl for crypto and the server
- Simple config, setup etc. Give it a domain name, it checks itself to make sure ^ acronyms are in place, then starts. 


Use DNSSEC+DANE?
Store signal keys in key transparency? Thats how people find out emails addresses of others and find out the keys
Or maybe just a directory server that should be queried. Doesnt store the raw email address, it stores a hash of the email address. Returns if that email exists or not. Do we really need a blockchain merkle tree thingy to prove identity? Just DNSSEC+DANE of directory server domain name, have it run a server with TLS, and respond yes or no to a hash of the email address.

Should we support HTML? It can be used as attack vector, scripts, malicious images, tracking pixels etc. Maybe a subset of HTML? Or Gemini? Or just plain text...?

How to handle user authentication? user+pass, LDAP? oauth?

Key transparency

- Have a hash of the email address with its signal key(s). A hash rather than the email address itself so that it isnt publicly exposed.
- Should it be a global system like DNS, or one maintained per domain? Maybe both? DNS is public for public facing email, then individual orgs have their own internal DNS for internal only traffic.

https://sigstore.dev/

Force TLS connections between servers. Minimum TLS ver is 1.3. 


## Workflow

- Client validates the user email address, password and MFA credentials.
- Client checks DNS for the ANK server IP address of the recipient(s) domain(s). The DNS is secured by DNSSEC.
- The TLS certificate for the ANK server and the ANK key transparency (KT) server are stored in DNS, secured by DNSSEC.
- Client connects to the key transparency server for that domain and queries for the existence of the recipient(s) email address(es). The connection to the ANK KT server is secured with TLS.
- If valid, Client gets the recipient signal keys, and encrypts the message via the signal protocol
- The encrypted message is sent to the ANK server, over TLS.
- The server receives the message and stores it in the database.
- The recipients client retrieves this message from the server/database, over TLS.
- The recipient decrypts the message.


## Development Phases

### Phase 1

- Initial proof of concept using Python, FastAPI and curl
- Just super basic client/server with HTTP and JSON for sending and receiving messages
- Just JSON
- No authentication, but user separation
- Basic KT implementation, stored in redis or in memory
- Messages stored in database like sqlite for testing

This stage is to determine if we even want to use JMAP and Signal, or just much simpler implementation
Could we instead use HTTP/JSON + public keys? Have the server serve the users public key. Like S/MIME but without the BS.
How do you put HTML messages into JSON? Serialized? Not a good idea, look at EFAIL. Maybe just markdown instead, then client can render it.
