# Users can see items they should not access

Category: App

## Symptoms
- Every user sees all records
- Role restrictions are inconsistent

## Cause
Access is checked only in the app interface, or the data source permissions are too broad.

## Fix
1. Filter data by the current user's role or ID at the data source
2. Set permissions on the list or table, not only the app
3. Hide screens and buttons as a second layer, not the only one
4. Test with an account for each role
