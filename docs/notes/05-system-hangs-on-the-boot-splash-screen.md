# System hangs on the boot splash screen

Category: Boot

## Symptoms
- Boot progress freezes on the logo spinner
- Safe mode boots fine

## Cause
A startup service or driver hangs while loading, often after new software was installed.

## Fix
1. Boot into safe mode
2. Review boot and system logs for the last service that started
3. Disable or uninstall the recently added software or service
4. Reboot normally and watch startup time
