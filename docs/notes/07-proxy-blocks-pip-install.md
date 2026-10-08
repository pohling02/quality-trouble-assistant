# Proxy blocks pip install

Category: Proxy

## Symptoms
- pip install times out or shows connection errors
- Browser works but the terminal does not

## Cause
The terminal does not know the proxy settings that the browser uses.

## Fix
1. Set HTTP_PROXY and HTTPS_PROXY environment variables
2. Or run pip install --proxy http://proxy-host:port package
3. Add the proxy to pip.conf or pip.ini to make it permanent
4. Retry with -v to see which host fails
