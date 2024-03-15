# P2P network implementation
 This is a start to my python implementation of how a p2p network should be. This is more of a journal or diary on my journey to this implementation rather than a definitive answer, so all suggestions and criticism are welcome!

## What is a P2P network?
It is a decentralized network architecture where the participants named “peers” share resources, services, or information directly with each other, without the need for a centralized server.
In a P2P network, each participant acts both as a client and a server, contributing resources such as computing power, disk storage, or network bandwidth to the network.

There are many real-world applications of the P2P network:
1. Bit-torrent: which allows file sharing
2. SETI@home: allows distributed computing
3. Blockchains: allows the distribution of content
4. Communications: such as Skype

#### Key features of a decentralized network:
1. There is no single point of failure in a P2P network. Each peer is equal and can communicate directly with the other peers
2. P2P networks can scale effectively because new peers can join without putting additional strain on a central server.
3. Since there is no central server, P2P networks are often more resilient to failures or attacks, as the network can continue to function even if some peers are offline.
4. Participants in this type of network can share their own resources(such as bandwidth, processing power, or storage space) to provide services of content to other in the network.

#### While the are widely used in many application due to their distributed nature, they also pose challenges such as:
1. Security: P2P networks face security threats like malware, unauthorised access, and data breaches due to direct peer-to-peer communication.
2. Quality of Service (QoS): Ensuring consistent service quality is challenging due to network variability and dynamic peer availability, impacting real-time applications like communication and streaming.
3. Scalability: While highly scalable, managing large networks poses challenges in coordination, resource allocation, and routing protocols.
4. Content Availability and Integrity: Maintaining content availability and integrity is difficult as peers join or leave dynamically, affecting the decentralised file-sharing applications.
5. Fairness and Incentives: Incentivizing participation and preventing free-riding or malicious behaviour requires robust mechanisms to ensure network stability and efficiency.
6. Legal and Regulatory issues: P2P networks counter legal challenges such as copyright infringement and data protection compliance, especially in file-sharing and content distribution.
7. Network Heterogeneity: Managing resource utilization across peers with varying capabilities is quite complex and requires optimisation for network efficiency.
