# Postmortem Report for "Service Downtime Due to Database Outage"

## Issue Summary

- **Duration of Outage:**
  - Start Time: June 1, 2024, 14:30 UTC
  - End Time: June 1, 2024, 15:45 UTC
- **Impact:**
  - Service Affected: User Authentication Service
  - User Experience: Users were unable to log in, affecting 75% of active sessions
  - Percentage of Users Affected: Approximately 50%
- **Root Cause:**
  - The root cause of the outage was a misconfigured database failover procedure which led to both primary and secondary databases becoming unavailable simultaneously.

## Timeline

- **14:30 UTC:** Issue detected via monitoring alert indicating a spike in authentication failures.
- **14:32 UTC:** On-call engineer notified and begins investigation.
- **14:35 UTC:** Initial assumption was that there was a network issue causing database disconnection.
- **14:40 UTC:** Network team confirms no anomalies in network logs.
- **14:45 UTC:** Database team is engaged to investigate possible database issues.
- **14:50 UTC:** Database logs show simultaneous failover attempts causing a deadlock situation.
- **15:00 UTC:** Misleading investigation path considering a potential DDoS attack on the login service.
- **15:10 UTC:** Decision to manually restart both primary and secondary databases.
- **15:20 UTC:** Primary database restarted successfully but secondary remains unresponsive.
- **15:30 UTC:** Escalation to senior database administrators for advanced troubleshooting.
- **15:40 UTC:** Senior DBA identifies the misconfiguration in failover settings.
- **15:45 UTC:** Secondary database manually reconfigured and brought online. Issue resolved.

## Root Cause and Resolution

- **Root Cause:**
  - The primary and secondary databases were both configured to trigger a failover when the primary experienced a high load, leading to a situation where both attempted to take over as the primary, causing a deadlock and making both databases unavailable.
- **Resolution:**
  - The failover configuration was corrected to ensure that only one database can take the primary role at a time. This was achieved by setting a staggered failover policy with proper health checks and prioritization rules.

## Corrective and Preventative Measures

- **Improvements:**
  - Enhance monitoring and alerting to detect failover configuration issues proactively.
  - Implement automated health checks and circuit breakers to prevent simultaneous failover attempts.
  - Conduct regular failover drills to ensure configurations are correct and procedures are well-practiced.
- **Specific Tasks:**
  - **Task 1:** Patch the database failover configuration (Completed).
  - **Task 2:** Add detailed monitoring and alerting on failover attempts and database health status.
  - **Task 3:** Schedule regular failover drills to simulate various failure scenarios and ensure the system responds correctly.
  - **Task 4:** Update documentation and training materials for the engineering team to include the new failover configuration and procedures.
  - **Task 5:** Conduct a post-incident review meeting to discuss the outage, the root cause, and the steps taken to resolve it, ensuring all team members are aware of the changes.

By addressing the issues identified in this postmortem, we can reduce the likelihood of similar outages in the future and improve the reliability and resilience of our user authentication service.
