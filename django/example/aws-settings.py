from . import secrets
from .settings import *


SECRET_KEY = secrets.SECRET_KEY

DEBUG = False

ALLOWED_HOSTS = ['*']

AWS_STORAGE_BUCKET_NAME = 'matts-zappa-static'
AWS_S3_REGION_NAME = 'ap-southeast-2'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
