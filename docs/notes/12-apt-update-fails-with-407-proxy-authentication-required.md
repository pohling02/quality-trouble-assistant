# apt update fails with 407 proxy authentication required

Category: Proxy

## Symptoms
- apt update shows 407 or cannot connect to repositories

## Cause
The apt proxy is missing or the credentials are wrong or expired.

## Fix
1. Create /etc/apt/apt.conf.d/95proxy with Acquire::http::Proxy and Acquire::https::Proxy
2. Check the username and password, URL-encoding special characters
3. Run apt update again
