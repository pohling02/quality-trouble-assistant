# SSH connection refused

Category: Network

## Symptoms
- ssh: connect to host port 22: Connection refused

## Cause
The SSH service is not running, a firewall blocks the port, or the wrong host or port is used.

## Fix
1. Check that sshd is running on the target
2. Verify the host, port and firewall rules
3. Test connectivity with ping and a port check
4. Read the server logs for rejected attempts
