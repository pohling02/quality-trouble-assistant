# High CPU usage from a runaway process

Category: System

## Symptoms
- Fans run loudly and the system is slow
- One process uses most of a CPU core

## Cause
A process is stuck in a loop or doing heavy work, possibly after a bad update.

## Fix
1. Identify it with top, htop or Task Manager
2. Check its logs and recent changes
3. Restart the process or service
4. If it returns, update or roll back the software
