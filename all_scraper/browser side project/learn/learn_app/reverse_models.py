# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AmazonBrowseNodeRank(models.Model):
    region = models.CharField(max_length=6)
    type = models.CharField(max_length=13)
    department = models.CharField(max_length=32)
    node_id = models.BigIntegerField()
    rank = models.TextField()
    last_updated_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'amazon_browse_node_rank'


class AmazonKeywordsAd(models.Model):
    region = models.CharField(max_length=6)
    keywords = models.CharField(max_length=128)
    node_id = models.BigIntegerField()
    ad = models.TextField()
    last_updated_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'amazon_keywords_ad'
        unique_together = (('region', 'keywords', 'node_id'),)


class AmazonKeywordsRank(models.Model):
    region = models.CharField(max_length=6)
    keywords = models.CharField(max_length=128)
    node_id = models.BigIntegerField()
    rank = models.TextField()
    last_updated_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'amazon_keywords_rank'
        unique_together = (('region', 'keywords', 'node_id'),)


class AmazonKeywordsSuggest(models.Model):
    id = models.BigAutoField(primary_key=True)
    keywords_id = models.IntegerField()
    parent_keywords_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'amazon_keywords_suggest'
        unique_together = (('keywords_id', 'parent_keywords_id'),)


class AmazonProduct(models.Model):
    region = models.CharField(max_length=6)
    asin = models.CharField(max_length=10)
    variation_parentage = models.CharField(max_length=6)
    parent_asin = models.CharField(max_length=10, blank=True, null=True)
    status = models.IntegerField()
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    detail_page_url = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=64, blank=True, null=True)
    browse_node = models.CharField(max_length=64, blank=True, null=True)
    sales_rank = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    review_count = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    shipping = models.CharField(max_length=64, blank=True, null=True)
    list_price = models.IntegerField(blank=True, null=True)
    fulfillment = models.CharField(max_length=3, blank=True, null=True)
    seller_id = models.CharField(max_length=14, blank=True, null=True)
    seller_name = models.CharField(max_length=64, blank=True, null=True)
    first_available_date = models.DateField(blank=True, null=True)
    last_updated_time = models.DateTimeField()
    bestseller_node_id = models.BigIntegerField(blank=True, null=True)
    is_fba = models.IntegerField(blank=True, null=True)
    offer_count = models.SmallIntegerField()
    variation_count = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'amazon_product'
        unique_together = (('region', 'asin'),)


class AmazonProductImage(models.Model):
    id = models.BigAutoField(primary_key=True)
    region = models.CharField(max_length=6)
    asin = models.CharField(max_length=10)
    url = models.CharField(max_length=128)
    width = models.SmallIntegerField(blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'amazon_product_image'
        unique_together = (('region', 'asin', 'url'),)


class AmazonProductKeywordsAd(models.Model):
    region = models.CharField(max_length=6)
    asin = models.CharField(max_length=10)
    keywords = models.CharField(max_length=128)
    node_id = models.BigIntegerField()
    position = models.SmallIntegerField()
    page_id = models.SmallIntegerField()
    page_position = models.SmallIntegerField()
    ad_position_type = models.IntegerField()
    ad_position = models.IntegerField()
    last_updated_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'amazon_product_keywords_ad'


class AmazonProductKeywordsRank(models.Model):
    region = models.CharField(max_length=6)
    asin = models.CharField(max_length=10)
    keywords = models.CharField(max_length=128)
    node_id = models.BigIntegerField()
    rank = models.SmallIntegerField()
    page_id = models.SmallIntegerField()
    page_position = models.SmallIntegerField()
    last_updated_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'amazon_product_keywords_rank'


class AmazonProductReview(models.Model):
    region = models.CharField(max_length=6)
    review_id = models.CharField(max_length=16)
    asin = models.CharField(max_length=10)
    customer_id = models.CharField(max_length=16, blank=True, null=True)
    customer_name = models.CharField(max_length=64, blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    helpful_yes = models.IntegerField(blank=True, null=True)
    helpful_no = models.IntegerField(blank=True, null=True)
    is_verified = models.IntegerField(blank=True, null=True)
    is_image_included = models.IntegerField(blank=True, null=True)
    is_video_included = models.IntegerField(blank=True, null=True)
    last_updated_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'amazon_product_review'
        unique_together = (('region', 'review_id'),)


class AmazonProductReviewImage(models.Model):
    region = models.CharField(max_length=6)
    review_id = models.CharField(max_length=16)
    url = models.CharField(max_length=128)
    width = models.SmallIntegerField(blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'amazon_product_review_image'
        unique_together = (('region', 'review_id', 'url'),)


class AmazonProductReviewVideo(models.Model):
    region = models.CharField(max_length=6)
    review_id = models.CharField(max_length=16)
    url = models.CharField(max_length=128)
    image_url = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amazon_product_review_video'
        unique_together = (('region', 'review_id', 'url'),)


class AmazonSeller(models.Model):
    region = models.CharField(max_length=6)
    seller_id = models.CharField(max_length=16)
    name = models.CharField(max_length=128, blank=True, null=True)
    logo_url = models.CharField(max_length=128, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    last_30_days_positive_feedback_ratio = models.IntegerField(blank=True, null=True)
    last_90_days_positive_feedback_ratio = models.IntegerField(blank=True, null=True)
    last_12_months_positive_feedback_ratio = models.IntegerField(blank=True, null=True)
    lifetime_positive_feedback_ratio = models.IntegerField(blank=True, null=True)
    last_30_days_neutral_feedback_ratio = models.IntegerField(blank=True, null=True)
    last_90_days_neutral_feedback_ratio = models.IntegerField(blank=True, null=True)
    last_12_months_neutral_feedback_ratio = models.IntegerField(blank=True, null=True)
    lifetime_neutral_feedback_ratio = models.IntegerField(blank=True, null=True)
    last_30_days_negative_feedback_ratio = models.IntegerField(blank=True, null=True)
    last_90_days_negative_feedback_ratio = models.IntegerField(blank=True, null=True)
    last_12_months_negative_feedback_ratio = models.IntegerField(blank=True, null=True)
    lifetime_negative_feedback_ratio = models.IntegerField(blank=True, null=True)
    last_30_days_feedback_count = models.IntegerField(blank=True, null=True)
    last_90_days_feedback_count = models.IntegerField(blank=True, null=True)
    last_12_months_feedback_count = models.IntegerField(blank=True, null=True)
    lifetime_feedback_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amazon_seller'
        unique_together = (('region', 'seller_id'),)


class AmazonSellerProduct(models.Model):
    region = models.CharField(max_length=6)
    seller_id = models.CharField(max_length=14)
    asin = models.CharField(max_length=10)
    status = models.IntegerField()
    rank = models.SmallIntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    list_price = models.IntegerField(blank=True, null=True)
    seller_name = models.CharField(max_length=128, blank=True, null=True)
    seller_logo_url = models.CharField(max_length=128, blank=True, null=True)
    seller_logo_width = models.SmallIntegerField(blank=True, null=True)
    seller_logo_height = models.SmallIntegerField(blank=True, null=True)
    seller_rating = models.IntegerField(blank=True, null=True)
    seller_last_12_months_positive_feedback_ratio = models.IntegerField(blank=True, null=True)
    seller_lifetime_feedback_count = models.IntegerField(blank=True, null=True)
    search_index = models.CharField(max_length=32, blank=True, null=True)
    bestseller_node_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amazon_seller_product'
        unique_together = (('region', 'seller_id', 'asin'),)


class AmazonSellerProductOffer(models.Model):
    region = models.CharField(max_length=6)
    seller_id = models.CharField(max_length=14)
    asin = models.CharField(max_length=10)
    item_id = models.CharField(max_length=32, blank=True, null=True)
    status = models.IntegerField()
    price = models.IntegerField(blank=True, null=True)
    shipping = models.CharField(max_length=64, blank=True, null=True)
    condition = models.CharField(max_length=21, blank=True, null=True)
    fulfillment = models.CharField(max_length=3, blank=True, null=True)
    inventory = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amazon_seller_product_offer'
        unique_together = (('region', 'seller_id', 'asin', 'item_id'),)


class AmazonTopReviewer(models.Model):
    region = models.CharField(max_length=6)
    top_reviewer_id = models.CharField(max_length=16)
    name = models.CharField(max_length=64, blank=True, null=True)
    rank = models.SmallIntegerField(blank=True, null=True)
    review_count = models.IntegerField(blank=True, null=True)
    helpful_vote_count = models.IntegerField(blank=True, null=True)
    helpful_vote_ratio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amazon_top_reviewer'
        unique_together = (('region', 'top_reviewer_id'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Config(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DownloadQueue(models.Model):
    ac_download_queue_id = models.IntegerField()
    region = models.IntegerField()
    type = models.IntegerField()
    value = models.CharField(max_length=64)
    status = models.IntegerField()
    priority = models.IntegerField()
    scrape_count = models.IntegerField()
    upload_status = models.IntegerField()
    upload_count = models.IntegerField()
    last_updated_time = models.DateTimeField(blank=True, null=True)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'download_queue'


class Keywords(models.Model):
    region = models.CharField(max_length=6)
    name = models.CharField(max_length=128)
    monthly_amazon_search_volume = models.IntegerField(blank=True, null=True)
    amazon_product_search_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keywords'
        unique_together = (('name', 'region'),)


class LearnAppPerson(models.Model):
    value = models.CharField(max_length=30)
    region = models.SmallIntegerField()
    type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'learn_app_person'


class Log(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    module = models.CharField(max_length=64)
    priority = models.IntegerField()
    message = models.TextField()
    created_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'log'


class Proxy(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    type = models.CharField(max_length=32)
    status = models.CharField(max_length=8)
    host = models.CharField(max_length=64)
    port = models.SmallIntegerField(blank=True, null=True)
    username = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    count = models.IntegerField()
    robot_check_count = models.IntegerField()
    active_time = models.DateTimeField(blank=True, null=True)
    inactive_time = models.DateTimeField(blank=True, null=True)
    recover_failed_count = models.IntegerField(blank=True, null=True)
    last_robot_check_url = models.CharField(max_length=255, blank=True, null=True)
    last_robot_check_useragent_id = models.IntegerField(blank=True, null=True)
    last_robot_check_time = models.DateTimeField(blank=True, null=True)
    last_used_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'proxy'


class ProxyStatus(models.Model):
    proxy_id = models.SmallIntegerField()
    region = models.SmallIntegerField()
    status = models.CharField(max_length=8)
    count = models.IntegerField()
    robot_check_count = models.IntegerField()
    active_time = models.DateTimeField(blank=True, null=True)
    inactive_time = models.DateTimeField(blank=True, null=True)
    recover_failed_count = models.IntegerField(blank=True, null=True)
    last_robot_check_url = models.CharField(max_length=255, blank=True, null=True)
    last_robot_check_useragent_id = models.IntegerField(blank=True, null=True)
    last_robot_check_time = models.DateTimeField(blank=True, null=True)
    last_used_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'proxy_status'
        unique_together = (('proxy_id', 'region'),)


class Scrape(models.Model):
    download_queue_id = models.IntegerField()
    method = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255)
    proxy_id = models.SmallIntegerField(blank=True, null=True)
    begin_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'scrape'


class UploadQueue(models.Model):
    region = models.IntegerField()
    type = models.IntegerField()
    value = models.CharField(max_length=64)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'upload_queue'


class Useragent(models.Model):
    value = models.CharField(max_length=255)
    count = models.IntegerField()
    robot_check_count = models.IntegerField()
    last_used_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'useragent'
