# npm install fails behind a proxy

Category: Proxy

## Symptoms
- npm install fails with ETIMEDOUT, ECONNRESET or ENOTFOUND

## Cause
npm has no proxy configured, or the proxy blocks the registry.

## Fix
1. Run npm config set proxy http://proxy-host:port
2. Run npm config set https-proxy http://proxy-host:port
3. Confirm the registry URL with npm config get registry
4. Retry the install
