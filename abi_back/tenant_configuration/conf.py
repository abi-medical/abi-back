from base import conf

from . import messages

TENANT_PREFIX = "TENANT"


TENANT_LIST_URL_NAME = TENANT_PREFIX + conf.LIST_SUFFIX
TENANT_CREATE_URL_NAME = TENANT_PREFIX + conf.CREATE_SUFFIX
TENANT_DETAIL_URL_NAME = TENANT_PREFIX + conf.DETAIL_SUFFIX
TENANT_UPDATE_URL_NAME = TENANT_PREFIX + conf.UPDATE_SUFFIX
TENANT_DELETE_URL_NAME = TENANT_PREFIX + conf.DELETE_SUFFIX
