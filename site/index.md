An independent implementation of the Signal protocol

Used with the client/server for sending messages. Maybe an email replacement using JMAP.

## Implementation

I'm uncertain on which programming language to use. I have experience with Python, but I dont like it.

The system created should be working well on the first release. I want this to be very reliable software that only gets patched or new releases for things like security issues and major language updates. We shouldnt be constantly adding new features.

### Python
- Easy to write, already know the language
- Modern tools want to use async with everything. FastAPI, HTTPX etc. but async support is flakey
- Imports are a pain
- Lots of boilerplate code.
- Messy repo, lots of stuff wants to exist at the top level
- Interpreted, slow performance
- Dynamically typed. Recent introduction of type hints are awkward. Not fully supported, and relies on support in 3rd party libraries.
- New versions released often, and not supported for long
- Means inevitably needs to be rewritten in a better language in future

### Rust
- Picking up steam, getting lots of community support
- Syntax is weird, similar to C/C++
- Memory safe, prevents you from making a lot of security mistakes
- Slow compilation speed
- Small binaries
- Compiled
- Statically typed
- Ownership / borrowing memory model
- New versions released often, and not supported for long
- Optimised implementation of BLAKE3
- Libsodium wrapper
- Lots of community support so its going to be easier to get help online

### Golang
- Small language so its easy to learn, but limits you
- Fast compilation speed
- Large binaries
- Garbage collected
- Compiled
- Statically typed
- Supported by Google. Lots of weight behind it, but might get binned at any time.
- Wants error handling and logging on every function
- New versions released often but high levels of backwards compatibility

### Ada / Spark
- Designed from the beginning for critical and high security environments
- Spark is a formally analysable subset of Ada
- SparkNaCl exists, and is of very high quality and speed
- SparkSkein apparently exists, which is Skein, a SHA3 contender. However, I cant find the implementation. The site appears to be down and the links are dead.
- Very verbose
- Compiled
- Statically typed
- New versions released every 10 years.


The signal protocol seems to use sha-512 in some places. If there is an implementation of this, we can just use that. Or otherwise we could swap it out for something like [BLAKE3](https://github.com/BLAKE3-team/BLAKE3) which is apparently much faster. There are C and Rust implementations in this repo.


### Notes

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
- No JMAP, just JSON
- No authentication, but user separation
- Basic KT implementation, stored in redis or in memory
- Messages stored in database like sqlite for testing

This stage is to determine if we even want to use JMAP and Signal, or just much simpler implementation
Could we instead use HTTP/JSON + public keys? Have the server serve the users public key. Like S/MIME but without the BS.
How do you put HTML messages into JSON? Serialized? Not a good idea, look at EFAIL. Maybe just markdown instead, then client can render it.