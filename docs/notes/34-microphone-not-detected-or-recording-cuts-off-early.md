# Microphone not detected or recording cuts off early

Category: Audio

## Symptoms
- The app records silence or stops too soon
- Device missing in the input list

## Cause
Wrong default input device, missing permission, or a silence threshold that is too aggressive.

## Fix
1. Check the default input device and privacy permissions
2. Test recording with a separate tool
3. Adjust the silence threshold and timeout in the code
4. Log the audio levels to tune the values
