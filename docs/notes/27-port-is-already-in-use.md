# Port is already in use

Category: System

## Symptoms
- Address already in use when starting a server

## Cause
Another process, or an old instance of the same app, is listening on that port.

## Fix
1. Find the process with lsof -i :PORT or netstat
2. Stop it or choose a different port
3. Check for orphan containers or background jobs
