#coding: utf-8
'''
创建人：Javen
创建时间：
'''
from Models.Mapper.Abstract import Model_Mapper_Abstract
class Model_Mapper_AmazonProductReviewVideo(Model_Mapper_Abstract):
    def __init__(self):
        super(Model_Mapper_AmazonProductReviewVideo, self).__init__()

    def save(self, data):
        searchData = {
            'region': data['region'],
            'review_id': data['review_id'],
        }
        result = self.findData("all", "amazon_product_review_video", searchData)
        if (result):
            result = self.update("amazon_product_review_video", data, searchData)
        else:
            result = self.insert("amazon_product_review_video", data)
        return result