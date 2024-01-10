# Totally-Ordered-Multicasting
distributed system that focused on Totally Ordered Multicasting
Totally Ordered Multicasting
• Lamport's algorithm was used to accomplish completely ordered multicasting.
• Each of the procedures carried out local activities, allocated unique sequence numbers to them, and distributed events to other operations.
• Message delivery was handled by communication threads, and event ordering was handled by a logical clock.
• Two threads were deployed per process, one for communication and one for event delivery.
• Testing included establishing processes to provide three updates and ensuring that message ordering was consistent.
Key Learnings
• Socket Programming: Learned how to use sockets to build communication between processes.
• Concurrency and Parallelism: Concurrent execution was achieved by mastering the use of threads and multiprocessing.
• Distributed Algorithms: Understanding and implementation of Lamport's technique for entirely ordered multicasting and the vector clock algorithm for causally ordered events have been improved.
• Locking Schemes: Decentralized and distributed locking methods were effectively devised and compared, with synchronization and coordination taken into account. Issues Encountered
• Synchronization Challenges: Handled the complexity of synchronizing threads and processes in order to support concurrent access without conflicts.
• Debugging in Distributed Systems: Due to the asynchronous nature of processes, I faced difficulties debugging bugs in a distributed system.
Conclusion
The distributed systems project implementation gave important hands-on experience in creating and deploying various distributed system components. It went over core topics including message ordering, vector clocks, and distributed locking, as well as how to solve problems in the context of distributed computing. Overall, the project successfully bridged the theoretical and practical knowledge gaps in the domain of distributed systems.
