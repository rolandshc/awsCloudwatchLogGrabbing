A simple cli tool for grabbing latest AWS Cloudwatch log events from latest logStream and latest logGroup and filtering the result with search string.

Built with Python3, Poetry, Boto3, argparse

1. install poetry if you do not have it.
2. cd to this project directory in terminal
3. run `poetry install`
4. run `poetry shell`
5. Navigate to your AWS Environment and login
6. Get the AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN
7. Replace the `log_group_name_prefix` and `filter_pattern` with string you want to search
8. In the cell run the command (update the command with your parameters): `aws-log -aws_access_key_id AWS_ACCESS_KEY_ID -aws_secret_access_key AWS_SECRET_ACCESS_KEY -aws_session_token AWS_SESSION_TOKEN -region_name us-east-1 -log_group_name_prefix YOUR_PREFIX -filter_pattern "YOUR_STRING"`
