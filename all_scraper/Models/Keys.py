#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'javen'
__mtime__ = '17-3-30'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from Models.Abstract import Model_Abstract
class Model_Keys(Model_Abstract):

    # downloadqueue表 键
    downloadqueue_key = ['id','ac_download_queue_id','region','type','value','status','priority','scrape_count','upload_status','upload_count','last_updated_time','time']
    mobiledownloadqueue_key = ['id','ac_mobile_download_queue_id','region','type','value','status','priority','scrape_count','upload_status','upload_count','last_updated_time','time']

    # news_downloadqueue表 键
    news_downloadqueue_key = ['id', 'url_id', 'title', 'url', 'type', 'status', 'last_updated_time']

    # amazon_product表 键
    product_key = ['id', 'region', 'asin', 'variation_parentage', 'parent_asin', 'status', 'title', 'description',
           'detail_page_url', 'category', 'browse_node', 'sales_rank', 'rating', 'review_count', 'price', 'shipping',
           'list_price', 'fulfillment', 'seller_id', 'seller_name', 'first_available_date', 'last_updated_time',
           'bestseller_node_id', 'is_fba', 'offer_count', 'variation_count']

    # amazon_product_image表 键
    image_key = ['id', 'region', 'asin', 'url', 'width', 'height', 'position']

    # amazon_seller表 键
    seller_key = ['id', 'region', 'seller_id', 'name', 'logo_url', 'rating', 'last_30_days_positive_feedback_ratio',
           'last_90_days_positive_feedback_ratio', 'last_12_months_positive_feedback_ratio',
           'lifetime_positive_feedback_ratio', 'last_30_days_neutral_feedback_ratio',
           'last_90_days_neutral_feedback_ratio', 'last_12_months_neutral_feedback_ratio',
           'lifetime_neutral_feedback_ratio', 'last_30_days_negative_feedback_ratio',
           'last_90_days_negative_feedback_ratio', 'last_12_months_negative_feedback_ratio',
           'lifetime_negative_feedback_ratio', 'last_30_days_feedback_count', 'last_90_days_feedback_count',
           'last_12_months_feedback_count', 'lifetime_feedback_count']

    # amazon_seller_product表 键
    sellerProducts_key = ['id', 'region', 'seller_id', 'asin', 'status', 'rank', 'price', 'list_price', 'seller_name',
                          'seller_logo_url', 'seller_logo_width', 'seller_logo_height', 'seller_rating',
                          'seller_last_12_months_positive_feedback_ratio', 'seller_lifetime_feedback_count',
                          'search_index', 'bestseller_node_id']

    # amazon_seller_product_offer表 键
    sellerProductOffers_key = ['id', 'region', 'seller_id', 'asin', 'item_id', 'status', 'price', 'shipping',
                               'condition', 'fulfillment', 'inventory']

    # amazon_product_keywords_rank
    rankdata_key = ['id', 'region', 'asin', 'keywords', 'node_id', 'rank', 'page_id', 'page_position',
                    'last_updated_time']

    # amazon_product_keywords_ad
    addata_key = ['id', 'region', 'asin', 'keywords', 'node_id', 'position', 'page_id', 'page_position',
                  'ad_position_type', 'ad_position', 'last_updated_time']

    # amazon_top_reviewer
    topreviewer_key = ['id', 'region', 'top_reviewer_id', 'name', 'rank', 'review_count', 'helpful_vote_count',
           'helpful_vote_ratio']

    # keywords
    keywords_key = ['id', 'region', 'name', 'monthly_amazon_search_volume', 'amazon_product_search_count']