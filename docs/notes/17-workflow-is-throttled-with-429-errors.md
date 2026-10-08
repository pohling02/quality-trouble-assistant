# Workflow is throttled with 429 errors

Category: Workflow

## Symptoms
- Runs fail or slow down with 429 Too Many Requests

## Cause
Too many calls to a connector within a short time, for example inside a large loop.

## Fix
1. Reduce the number of calls by filtering data at the source
2. Add delays or lower the concurrency of loops
3. Batch operations where possible
4. Enable retry with a backoff policy
