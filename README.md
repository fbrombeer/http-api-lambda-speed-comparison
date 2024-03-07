# http-api-lambda vs. FastAPI + Mangum Speed Comparison

This project showcases the gain in execution duration by using http-api-lambda instead of FastAPI + Mangum for api development on AWS lambda.

## How to use
1. run `cdk deploy` to deploy the stack (2 AWS lambda functions with function urls)
2. paste the output urls of `cdk deploy` into `invoke.py`
3. run `invoke.py` to invoke both lambdas 100 times
4. view results in AWS metrics