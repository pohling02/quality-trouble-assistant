# DNS name resolution fails

Category: Network

## Symptoms
- Could not resolve host
- Ping by IP works but ping by name fails

## Cause
The DNS server is unreachable or misconfigured, or a stale cache holds a bad entry.

## Fix
1. Run nslookup or dig against the name
2. Flush the DNS cache
3. Try a different DNS server to isolate the problem
4. Check the hosts file for wrong entries
