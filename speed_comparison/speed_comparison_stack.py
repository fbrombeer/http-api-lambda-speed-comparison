from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_lambda_python_alpha as _lambda_alpha,
    CfnOutput as cfn_output,
)
from constructs import Construct

class SpeedComparisonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fastapi_mangum_handler = _lambda_alpha.PythonFunction(self, "fastapi-mangum",
                                               entry="./fastapi-mangum",
                                               runtime=_lambda.Runtime.PYTHON_3_12,
                                               architecture=_lambda.Architecture.ARM_64
                                               )
        
        fastapi_mangum_url = fastapi_mangum_handler.add_function_url(auth_type=_lambda.FunctionUrlAuthType.NONE)

        http_api_lambda_handler = _lambda_alpha.PythonFunction(self, "http-api-lambda",
                                               entry="./http-api-lambda",
                                               runtime=_lambda.Runtime.PYTHON_3_12,
                                               architecture=_lambda.Architecture.ARM_64
                                               )
        
        http_api_lambda_url = http_api_lambda_handler.add_function_url(auth_type=_lambda.FunctionUrlAuthType.NONE)
        
        
        cfn_output(self, "fastapi_mangum_url", value=fastapi_mangum_url.url)
        cfn_output(self, "http_api_lambda_url", value=http_api_lambda_url.url)