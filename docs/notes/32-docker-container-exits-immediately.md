# Docker container exits immediately

Category: Development

## Symptoms
- docker ps shows no container
- docker ps -a shows Exited (1)

## Cause
The main process crashed or finished, often because of a missing environment variable or a wrong command.

## Fix
1. Read docker logs container_name
2. Check CMD and ENTRYPOINT
3. Pass required environment variables
4. Run an interactive shell in the image to test the command
