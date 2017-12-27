# -*- coding: utf-8 -*-
#
from django.utils.translation import ugettext as _

# PUSH_SYSTEM_USER_PERIOD_LOCK_KEY = "PUSH_SYSTEM_USER_PERIOD_KEY"
PUSH_SYSTEM_USER_PERIOD_TASK_NAME = _("PUSH SYSTEM USER TO CLUSTER PERIOD: {}")
PUSH_SYSTEM_USER_MANUAL_TASK_NAME = _("PUSH SYSTEM USER TO CLUSTER MANUALLY: {}")
PUSH_SYSTEM_USER_TASK_NAME = _("PUSH SYSTEM USER TO CLUSTER: {}")
# PUSH_SYSTEM_USER_LOCK_KEY = "PUSH_SYSTEM_USER_TO_CLUSTER_LOCK_{}"
PUSH_SYSTEM_USER_ON_CHANGE_TASK_NAME = _("PUSH SYSTEM USER ON CHANGE: {}")
PUSH_SYSTEM_USER_ON_CREATE_TASK_NAME = _("PUSH SYSTEM USER ON CREATE: {}")
PUSH_SYSTEM_USERS_ON_ASSET_CREATE_TASK_NAME = _("PUSH SYSTEM USERS ON ASSET CREAT: {}")


UPDATE_ASSETS_HARDWARE_TASK_NAME = _('UPDATE ASSETS HARDWARE INFO')
UPDATE_ASSETS_HARDWARE_MANUAL_TASK_NAME = _('UPDATE ASSETS HARDWARE INFO MANUALLY')
UPDATE_ASSETS_HARDWARE_ON_CREATE_TASK_NAME = _('UPDATE ASSETS HARDWARE INFO ON CREATE')
# UPDATE_ASSETS_HARDWARE_PERIOD_LOCK_KEY = "UPDATE_ASSETS_HARDWARE_PERIOD_LOCK_KEY"
UPDATE_ASSETS_HARDWARE_PERIOD_TASK_NAME = _('UPDATE ASSETS HARDWARE INFO PERIOD')
UPDATE_ASSETS_HARDWARE_TASKS = [
   {
       'name': UPDATE_ASSETS_HARDWARE_TASK_NAME,
       'action': {
           'module': 'setup'
       }
   }
]

# TEST_ADMIN_USER_CONN_PERIOD_LOCK_KEY = "TEST_ADMIN_USER_CONN_PERIOD_KEY"
TEST_ADMIN_USER_CONN_PERIOD_TASK_NAME = _("TEST ADMIN USER CONN PERIOD: {}")
TEST_ADMIN_USER_CONN_MANUAL_TASK_NAME = _("TEST ADMIN USER CONN MANUALLY: {}")
TEST_ADMIN_USER_CONN_TASK_NAME = _("TEST ADMIN USER CONN: {}")
ADMIN_USER_CONN_CACHE_KEY = "ADMIN_USER_CONN_{}"
TEST_ADMIN_USER_CONN_TASKS = [
    {
        "name": "TEST_ADMIN_CONNECTIVE",
        "action": {
            "module": "ping",
        }
    }
]

ASSET_ADMIN_CONN_CACHE_KEY = "ASSET_ADMIN_USER_CONN_{}"
TEST_ASSET_CONN_TASK_NAME = _("ASSET CONN TEST MANUAL")

TEST_SYSTEM_USER_CONN_PERIOD_LOCK_KEY = "TEST_SYSTEM_USER_CONN_PERIOD_KEY"
TEST_SYSTEM_USER_CONN_PERIOD_TASK_NAME = _("TEST SYSTEM USER CONN PERIOD: {}")
TEST_SYSTEM_USER_CONN_MANUAL_TASK_NAME = _("TEST SYSTEM USER CONN MANUALLY: {}")
SYSTEM_USER_CONN_CACHE_KEY = "SYSTEM_USER_CONN_{}"
TEST_SYSTEM_USER_CONN_TASKS = [
   {
       "name": "TEST_SYSTEM_USER_CONNECTIVE",
       "action": {
           "module": "ping",
       }
   }
]

TASK_OPTIONS = {
    'timeout': 10,
    'forks': 10,
}