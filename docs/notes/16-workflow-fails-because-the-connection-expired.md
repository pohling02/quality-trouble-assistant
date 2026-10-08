# Workflow fails because the connection expired

Category: Workflow

## Symptoms
- Runs fail with 401 or 403
- A flow that used to work suddenly fails

## Cause
The account password changed, a token expired, or the connection owner lost access.

## Fix
1. Open the connection and sign in again
2. Use a service account instead of a personal account for shared flows
3. Confirm the account still has permission to the data source
4. Resubmit the failed runs
