# SSL certificate verify failed behind a corporate proxy

Category: Proxy

## Symptoms
- Errors such as CERTIFICATE_VERIFY_FAILED or self-signed certificate in certificate chain

## Cause
The proxy inspects HTTPS traffic and re-signs it with its own certificate, which the tool does not trust.

## Fix
1. Get the proxy root CA certificate from the network or IT team
2. Point the tool to it, for example REQUESTS_CA_BUNDLE or SSL_CERT_FILE
3. Or add it to the system trust store
4. Do not disable certificate verification permanently
