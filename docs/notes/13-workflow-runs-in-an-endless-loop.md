# Workflow runs in an endless loop

Category: Workflow

## Symptoms
- The same flow triggers again and again
- Run history fills up quickly
- Items are updated repeatedly

## Cause
The flow is triggered by an item update and also updates that same item, which fires the trigger again.

## Fix
1. Add a trigger condition so the flow only runs when a specific field changes
2. Use a status or flag field to skip items already processed
3. Update only the fields that need changing
4. Turn off the flow while testing the fix with one record
