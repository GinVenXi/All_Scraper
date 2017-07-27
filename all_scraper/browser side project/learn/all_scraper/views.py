from django.core.paginator import PageNotAnInteger

from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import render, render_to_response
from all_scraper.reverse_models import AmazonProductKeywordsRank, AmazonProduct, AmazonSeller, AmazonProductImage, \
    JdProducts, JdKeywords, JdProductReview, SinaPages, SinaDownloadQueue, TencentDownloadQueue, TencentPages, \
    TaobaoKeywords, TaobaoProducts, TaobaoSellerPage

# Create your views here.

def home(request):
    string = "World!"
    return render(request, "all_scraper/home.html", {'string': string})

def hello(request):
    search_input = request.GET["search_input"]
    platform = request.GET["platform"]
    content = request.GET["content"]
    if (platform == "amz"):
        if (content == "keyword"):
            lists = []
            keywords = AmazonProductKeywordsRank.objects.filter(keywords=search_input)
            for i in keywords:
                lists.append(AmazonProduct.objects.get(asin=i.asin))
        elif (content == "product"):
            lists = AmazonProduct.objects.filter(asin=search_input)
        elif (content == "seller"):
            lists = AmazonSeller.objects.filter(seller_id=search_input)
    elif (platform == "tb"):
        if (content == "keyword"):
            lists = []
            keywords = TaobaoKeywords.objects.filter(keyword=search_input)
            for i in keywords:
                try:
                    items = TaobaoProducts.objects.filter(product_id=i.product_id)
                    if (len(items) > 1):
                        for i in items:
                            lists.append(i)
                    else:
                        lists.append(TaobaoProducts.objects.get(product_id=i.product_id))
                except:
                    pass
        elif (content == "product"):
            lists = TaobaoProducts.objects.filter(product_id=search_input)
        elif (content == "seller"):
            lists = TaobaoSellerPage.objects.filter(seller_id=search_input)
    elif (platform == "jd"):
        if (content == "keyword"):
            lists = []
            keywords = JdKeywords.objects.filter(keyword=search_input)
            for i in keywords:
                try:
                    items = JdProducts.objects.filter(sku=i.sku)
                    if (len(items)>1):
                        for i in items:
                            lists.append(i)
                    else:
                        lists.append(JdProducts.objects.get(sku=i.sku))
                except:
                    pass
        elif (content == "product"):
            lists = JdProducts.objects.filter(sku=search_input)
        elif (content == "seller"):
            lists = AmazonSeller.objects.filter(seller_id=search_input)
        elif (content == "review"):
            lists = JdProductReview.objects.filter(product_id=search_input)
    elif (platform == "sina"):
        lists = []
        news = SinaDownloadQueue.objects.filter(type=search_input)
        for i in news:
            try:
                lists.append(SinaPages.objects.get(url_id=i.url_id))
                # print (SinaPages.objects.get(url_id=i.url_id))
            except:
                pass
    elif (platform == "tencent"):
        lists = []
        news = TencentDownloadQueue.objects.filter(type=search_input)
        for i in news:
            try:
                lists.append(TencentPages.objects.get(url_id=i.url_id))
                # print (TencentPages.objects.get(url_id=i.url_id))
            except:
                pass
    count = len(lists)
    # print count
    page_count = 25
    paginator = Paginator(lists, page_count)
    curr_page = request.GET["page"]
    # print (curr_page)
    try:
        contacts = paginator.page(curr_page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    if (count % 25 == 0):
        num_pages = count / 25
    else:
        num_pages = count / 25 + 1
    # print (num_pages)
    last_page = int(num_pages)
    # print (last_page)
    int_curr_page = int(curr_page)
    # print (int_curr_page)
    if (int_curr_page == 0):
        has_previous = False
    else:
        has_previous = True
    if (int_curr_page == int(num_pages)):
        has_next = False
    else:
        has_next = True
    previous_page_number = int_curr_page - 1
    next_page_number = int_curr_page + 1
    return render_to_response("all_scraper/hello.html", locals())