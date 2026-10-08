# Black screen after boot with a GPU driver problem

Category: Boot

## Symptoms
- System powers on and the fans run, but the display stays black
- Display works in safe mode or on integrated graphics only

## Cause
The GPU driver failed to load, is corrupted, or conflicts with the kernel or OS build.

## Fix
1. Boot in safe mode or with the basic display driver
2. Remove the GPU driver completely using the vendor uninstaller
3. Reinstall a driver version known to match the OS
4. Check system logs for GPU driver load errors
