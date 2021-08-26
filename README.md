# lambda-yaml-validator
This is a yaml validator lambda function. I used it to validate YAML config files before deploying to environments on AWS AppConfig 

> default_lint.yaml: yaml validation rules to be usued by the function

> lambda_function.py: Python 3.8 Lambda function to deploy to AWS

> lambda_function_local.py: Python 3.8 script to check config locally 


## Install dependency locally to package/
pip3 install --target ./package yamllint

## Package the dependencies installed in package/
cd package
zip -r ../my-deployment-package.zip .

## Return to project base dir
cd ..

## Package Lambda function and Config with it's dependencies
zip -g my-deployment-package.zip lambda_function.py default_lint.yml

## Deploy to Lambda
aws lambda update-function-code --function-name <aws_lambda_function_name> --zip-file fileb://my-deployment-package.zip

## Reference:
https://github.com/adrienverge/yamllint
