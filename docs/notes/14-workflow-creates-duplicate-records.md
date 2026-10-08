# Workflow creates duplicate records

Category: Workflow

## Symptoms
- Two or more identical rows appear for one event
- Duplicates appear only sometimes

## Cause
The flow triggers twice, the create step is retried, or there is no check for an existing record.

## Fix
1. Check run history for double triggers
2. Look up an existing record by a unique key before creating
3. Set concurrency control to 1
4. Add a unique constraint where the data source allows it
