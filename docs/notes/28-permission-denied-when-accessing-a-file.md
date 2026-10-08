# Permission denied when accessing a file

Category: System

## Symptoms
- Permission denied when reading, writing or running a file

## Cause
The user lacks read, write or execute permission, or the file has the wrong owner.

## Fix
1. Inspect with ls -l
2. Change ownership with chown or permissions with chmod as needed
3. Avoid chmod 777 as a shortcut
4. Confirm the user belongs to the required group
