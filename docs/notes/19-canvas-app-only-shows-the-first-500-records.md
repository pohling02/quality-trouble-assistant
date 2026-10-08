# Canvas app only shows the first 500 records

Category: App

## Symptoms
- A list or search is missing items
- A delegation warning appears in the editor

## Cause
The formula is not delegable to the data source, so only the first records (default limit 500) are processed.

## Fix
1. Read the delegation warning on the formula
2. Rewrite the filter with delegable functions and operators
3. Increase the data row limit only as a temporary measure
4. Move heavy filtering to the data source or a view
