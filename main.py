
import boto3 

print ('Init script ...')

session = boto3.Session(profile_name='cayambe')

cf_client = session.client('cloudformation')
#cf_client = boto3.client('cloudformation')

response = cf_client.list_stacks(
    StackStatusFilter=[
        'CREATE_IN_PROGRESS',
        'CREATE_FAILED',
        'CREATE_COMPLETE',
        'ROLLBACK_IN_PROGRESS',
        'ROLLBACK_FAILED',
        'ROLLBACK_COMPLETE',
        'DELETE_IN_PROGRESS',
        'DELETE_FAILED',
        'UPDATE_IN_PROGRESS',
        'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS',
        'UPDATE_COMPLETE',
        'UPDATE_FAILED',
        'UPDATE_ROLLBACK_IN_PROGRESS',
        'UPDATE_ROLLBACK_FAILED',
        'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS',
        'UPDATE_ROLLBACK_COMPLETE',
        'REVIEW_IN_PROGRESS',
        'IMPORT_IN_PROGRESS',
        'IMPORT_COMPLETE',
        'IMPORT_ROLLBACK_IN_PROGRESS',
        'IMPORT_ROLLBACK_FAILED',
        'IMPORT_ROLLBACK_COMPLETE'
    ]
)
stack_summaries = response['StackSummaries']

for stack in stack_summaries:
    if stack['StackName'] != 'usrv-poc-fis-ci':
        print('Eliminado ' + stack['StackName'] + '...')
        response = cf_client.delete_stack(
            StackName=stack['StackName']
        )

print ('End cloudformation client ...')



