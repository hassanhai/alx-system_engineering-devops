Description of infrastructure elements:

Load balancer:

An additional load balancer is added to distribute incoming web traffic to multiple web servers. This ensures optimal utilization of resources by eliminating single points of failure, improves responsiveness, and improves fault tolerance.

Configuration of distribution algorithms and load balancers:

Load balancers can be configured with different distribution algorithms. B. Round Robin, Least Connections or Weighted Round Robin. Round-robin distributes incoming requests to each server in turn. Least Connections routes traffic to the server with the fewest active connections. Weighted Round Robin assigns servers based on predefined weights.

Active/active and active/passive setups:

An active/active setup contains multiple active instances that share the load. Each instance handles requests independently, which improves scalability and fault tolerance. In an active/passive setup, one instance is active while the others are in standby mode. If the active instance fails, the standby instance takes over.

Database primary replica cluster:

In this setup, the primary (master) database node handles data writes and updates. Replica nodes (slave nodes) replicate data from the primary node and serve reads. This improves read scalability and provides data redundancy for failover.

Differences between application primary and replica nodes:

The primary node is responsible for processing writes and thus represents the authoritative source of data for your application. Replica nodes are used for read operations and offload read traffic from the primary node to improve read performance. However, due to replication lag, the data on the replica node may lag slightly behind the primary node.

Infrastructure issues:

Single point of failure (SPOF):

SPOFs can exist in many places, such as load balancers, databases, and web servers. Failure of any of these components can result in a service outage. Redundancy and failover mechanisms should be implemented to mitigate this risk. Security issues:

Without a firewall, your infrastructure is exposed to potential attacks and unauthorized access. Implementing a firewall improves security by allowing you to control incoming and outgoing traffic. Additionally, without HTTPS, the data exchanged between the user and her website remains unencrypted and vulnerable to eavesdropping and tampering attempts.

Lack of oversight:

Without monitoring, it becomes difficult to identify performance bottlenecks, system failures, or potential security breaches. Monitoring tools are critical for real-time visibility into infrastructure health and performance, enabling proactive troubleshooting and response.
