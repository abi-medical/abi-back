import boto3

from django.conf import LazySettings

settings = LazySettings()


def get_route_53_client(
        aws_access_key_id=settings.AWS_ROUTE_53_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_ROUTE_53_SECRET_ACCESS_KEY
):

    return boto3.client(
        'route53',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )


def get_all_record_sets(aws_route_53_default_zone=settings.AWS_ROUTE_53_HOSTED_ZONE_ID):
    """
from abi_back.tenant_configuration import route_53_utils
r = route_53_utils.get_all_record_sets()
    :return: 
    """

    return get_route_53_client().get_hosted_zone(
        Id=aws_route_53_default_zone
    )


def insert_record(
        name,
        value,
        aws_route_53_default_zone=settings.AWS_ROUTE_53_HOSTED_ZONE_ID,
        record_type='A'
):
    """
from abi_back.tenant_configuration import route_53_utils
r = route_53_utils.insert_record('t1', '165.227.196.62')
    :param name: 
    :param value: 
    :param aws_route_53_default_zone: 
    :param record_type: 
    :return: 
    """
    if settings.MAIN_HOST not in name:
        name = "{}.{}.".format(name, settings.MAIN_HOST)
    return get_route_53_client().change_resource_record_sets(
        HostedZoneId=aws_route_53_default_zone,
        ChangeBatch={
            'Comment': 'add %s -> %s' % (name, value),
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': name,
                        'Type': record_type,
                        'TTL': 300,
                        'ResourceRecords': [
                            {
                                'Value': value
                            }
                        ]
                    }
                }
            ]
        }
    )
