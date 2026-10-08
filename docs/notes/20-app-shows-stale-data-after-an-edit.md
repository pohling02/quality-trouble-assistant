# App shows stale data after an edit

Category: App

## Symptoms
- A saved change does not appear in the gallery or list until the app restarts

## Cause
The app is reading a cached collection or has not refreshed the data source.

## Fix
1. Call Refresh on the data source after saving
2. Rebuild the local collection after changes
3. Avoid copying large data into collections unless needed
