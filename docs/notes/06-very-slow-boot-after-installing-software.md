# Very slow boot after installing software

Category: Boot

## Symptoms
- Boot takes several minutes
- Many applications start automatically

## Cause
Too many startup programs or services, or a service waiting on a network resource that is unavailable.

## Fix
1. List startup items and services
2. Disable non-essential ones
3. Check for services waiting on network mounts or proxy settings
4. Measure boot time again to confirm the improvement
