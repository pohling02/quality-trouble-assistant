# Database connection refused

Category: Development

## Symptoms
- Connection refused or timeout from the application to the database

## Cause
The database is down, the host or port is wrong, or in containers the app uses localhost instead of the service name.

## Fix
1. Check that the database is running and listening
2. Verify host, port and credentials
3. In Docker Compose, use the service name as the host
4. Add a health check so the app waits for the database
