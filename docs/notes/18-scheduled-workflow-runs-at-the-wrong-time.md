# Scheduled workflow runs at the wrong time

Category: Workflow

## Symptoms
- A daily job runs hours earlier or later than expected

## Cause
The schedule uses a different time zone from the one the team expects.

## Fix
1. Check the time zone setting in the recurrence trigger
2. Set it explicitly instead of using UTC by default
3. Remember daylight saving changes
4. Verify with one test run
