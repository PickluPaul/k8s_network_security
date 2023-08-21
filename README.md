# k8s_network_security

# Objective
The primary objective of this exercise is to enhance the security posture of a multi-tier application hosted within a Kubernetes cluster by implementing Network Policies.  We have a three-tier application running in a Kubernetes cluster. The application consists of a front-end, a back-end API, and a database layer. This exercise aims to establish controlled and secure communication between these components such that only required traffic is allowed with minimal disruption to existing services during implementation. This will help minimize the risk of lateral movement with the kubernetes cluster in case of a compromised pod.
Also, we aim to setup basic security logging and monitoring for the existing cluster using open source tooling

# Strategy
The key steps of our approach to attain this objective are:
Understanding Application Traffic Flow: We will start by analyzing the existing traffic patterns within the application. This will help us identify how the application front-end,  back-end API, and  database components communicate with each other.
Designing Network Policies: Based on the insights gained from the traffic flow analysis, we will design network policies to allow the communication with specific guidelines
Allowing Front-end to back-end API communication
Back-end API to Database communication
Restricting all other traffic
Implementing and Testing Policies: Once the policies are designed, we'll apply them to our  Kubernetes cluster. We would do rigorous testing to ensure that the policies function as intended. This is vital to guarantee that the right connections remain open and unauthorized ones are blocked.
Setting Up Basic Security Logging and Monitoring: As a proactive measure, we will implement basic logging and monitoring mechanisms. These tools will help us keep a watchful eye on our audit logs.
