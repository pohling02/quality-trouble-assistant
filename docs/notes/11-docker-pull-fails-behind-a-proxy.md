# Docker pull fails behind a proxy

Category: Proxy

## Symptoms
- docker pull times out or cannot reach the registry

## Cause
The Docker daemon does not have proxy settings, since shell variables do not apply to it.

## Fix
1. Configure the proxy in the Docker daemon or Docker Desktop settings
2. Restart Docker
3. Retry the pull
4. Pass proxy build args if the failure happens during docker build
