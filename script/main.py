import argparse
import boto3
import json
from datetime import datetime

def start():
    parser = argparse.ArgumentParser()
    parser.add_argument('-aws_access_key_id', type=str, required=True)
    parser.add_argument('-aws_secret_access_key', type=str, required=True)
    parser.add_argument('-aws_session_token', type=str, required=True)
    parser.add_argument('-region_name', type=str, required=True)
    parser.add_argument('-log_group_name_prefix', type=str, required=True)
    parser.add_argument('-filter_pattern', type=str, required=True)

    args = parser.parse_args()

    session = boto3.session.Session(
        aws_access_key_id=args.aws_access_key_id,
        aws_secret_access_key=args.aws_secret_access_key,
        aws_session_token=args.aws_session_token,
        region_name=args.region_name
    )
    client=session.client('logs')

    #default returns the latest log group created
    response=client.describe_log_groups(
        logGroupNamePrefix=args.log_group_name_prefix,
        limit=1
    )
    latest_log_group_name=response['logGroups'][0]['logGroupName']
    latest_log_group_creation_timestamp=response['logGroups'][0]['creationTime']
    latest_log_group_creation_datetime=datetime.fromtimestamp(latest_log_group_creation_timestamp/1000.0)
    print('latest_log_group_name ',latest_log_group_name)
    print('latest_log_group_creation_datetime ',latest_log_group_creation_datetime)

    response = client.describe_log_streams(
        logGroupName= latest_log_group_name,
    #     logStreamNamePrefix='string',
        orderBy='LastEventTime',
        descending=True,
        limit=1
    )
    latest_log_stream_name = response['logStreams'][0]['logStreamName']
    latest_log_stream_timestamp = response['logStreams'][0]['creationTime']
    latest_log_stream_datetime = datetime.fromtimestamp(latest_log_stream_timestamp/1000.0)
    print('latest_log_stream_name ',latest_log_stream_name)
    print('latest_log_stream_creation_datetime ',latest_log_stream_datetime)

    response = client.filter_log_events(
        logGroupName=latest_log_group_name,
        logStreamNames=[latest_log_stream_name],
        filterPattern=args.filter_pattern,
        limit=50,
        interleaved=False
    )

    print("Log(s) as below:")
    print(response)