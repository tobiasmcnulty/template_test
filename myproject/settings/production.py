from myproject.settings.staging import *

# There should be only minor differences from staging

DATABASES['default']['NAME'] = 'myproject_production'

EMAIL_SUBJECT_PREFIX = '[Myproject Prod] '

