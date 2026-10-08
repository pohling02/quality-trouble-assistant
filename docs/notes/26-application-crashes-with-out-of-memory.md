# Application crashes with out of memory

Category: System

## Symptoms
- Process killed by the OOM killer
- MemoryError or the system becomes unresponsive

## Cause
The application holds too much data in memory, has a leak, or the memory limit is too low.

## Fix
1. Check memory use over time with free -m or a profiler
2. Process data in batches or streams
3. Fix objects that are never released
4. Increase the memory limit only after the cause is understood
