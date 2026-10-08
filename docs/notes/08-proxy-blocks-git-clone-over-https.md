# Proxy blocks git clone over HTTPS

Category: Proxy

## Symptoms
- git clone hangs or fails with 'Failed to connect' or 'Could not resolve host'

## Cause
Git is not configured to use the proxy.

## Fix
1. Run git config --global http.proxy http://proxy-host:port
2. Run git config --global https.proxy http://proxy-host:port
3. Retry the clone
4. Remove the setting when you leave the proxied network: git config --global --unset http.proxy
