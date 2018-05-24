import os

ADMINS = [
    ('ma0', 'ma0@contraslash.com'),
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# S3 Configuration
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# Route 53 Configuration
AWS_ROUTE_53_HOSTED_ZONE_ID = os.environ.get("AWS_ROUTE_53_HOSTED_ZONE_ID", "")
AWS_ROUTE_53_ACCESS_KEY_ID = os.environ.get("AWS_ROUTE_53_ACCESS_KEY_ID", "")
AWS_ROUTE_53_SECRET_ACCESS_KEY = os.environ.get("AWS_ROUTE_53_SECRET_ACCESS_KEY", "")
AWS_ROUTE_53_DEFAULT_TENANT_IP = os.environ.get("AWS_ROUTE_53_DEFAULT_TENANT_IP", "")


STATICFILES_LOCATION = 'abi_back/static'
STATICFILES_STORAGE = 'abi_back.storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)


RAVEN_CONFIG = {
    'dsn': 'http://74e1ef01fe214ffb8cc47c6d90a06896:dcbfe10c41744c50bbbdaf105900926d@logging.contraslash.com/12',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    # 'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
}
