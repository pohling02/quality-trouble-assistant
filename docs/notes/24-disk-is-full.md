# Disk is full

Category: System

## Symptoms
- No space left on device
- Applications crash when writing files

## Cause
Logs, caches, old Docker images or large temporary files have filled the disk.

## Fix
1. Check usage with df -h and du -sh *
2. Clear package caches, old logs and temp files
3. Run docker system prune after checking what it will delete
4. Set up log rotation to prevent a repeat
