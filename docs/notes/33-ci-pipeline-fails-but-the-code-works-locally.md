# CI pipeline fails but the code works locally

Category: Development

## Symptoms
- Tests pass on a laptop but fail in the pipeline

## Cause
The CI environment differs in versions, environment variables, working directory or available services.

## Fix
1. Compare tool and dependency versions
2. Add missing secrets or variables to the CI settings
3. Start required services such as the database in the pipeline
4. Reproduce locally with the same container image
