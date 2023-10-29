Description of infrastructure elements:

Additional elements and their purpose:

Adding elements such as load balancers, firewalls, and monitoring tools will improve the reliability, security, and performance of your infrastructure. Load balancers distribute traffic and improve resource utilization. A firewall protects against unauthorized access. Monitoring tools provide insight for preventive maintenance.

Firewall:

A firewall is a security device that controls and monitors incoming and outgoing network traffic based on specified security rules. They prevent unauthorized access and protect your infrastructure from malicious activity.

Traffic served over HTTPS:

HTTPS (Hypertext Transfer Protocol Secure) encrypts data exchanged between a user and her website to ensure confidentiality and integrity. Prevent data interception, tampering, and interception by malicious attackers, increasing user privacy and trust.

Monitoring:

Monitoring involves collecting and analyzing data from various infrastructure components to ensure their health, performance and security. It helps detect anomalies, fix problems, and optimize resource usage. Collection of monitoring data:

Monitoring tools collect data using various methods, including agent-based monitoring and agentless monitoring. Agents are installed on servers to collect and send data to a central monitoring system. Agentless methods use network protocols to collect data directly from monitored resources.

Web Server QPS Monitoring:

To monitor the queries per second (QPS) of your web server, use a monitoring tool to track the number of incoming requests over a period of time. Monitoring tools collect data on the number of requests, response times, and other related metrics to help you evaluate your server's performance. Infrastructure issues:

Stop SSL at the load balancer level.

Terminating SSL at the load balancer means that encrypted HTTPS traffic is decrypted before being forwarded to your backend servers. This offloads SSL decryption from the server, but can expose potential security risks if your data is not properly protected. Traffic between the load balancer and servers is unencrypted, making it more vulnerable.

Single MySQL server for writing:

Relying on a single MySQL server for writes introduces a single point of failure. If the server fails, write operations stop. A replication setup with a primary node for writes and a replica node for reads is recommended to ensure availability.

Identical server with all components:

Servers with identical components can pose uniform vulnerabilities. If a vulnerability is found in one component, all servers are vulnerable. Variety of software versions and components helps reduce the impact of a single vulnerability across your entire infrastructure.
