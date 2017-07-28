#coding: utf-8
import json
from django import forms

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from pygments.lexers import web

from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.urls import reverse
# Create your views here.
from learn_app.models import User
from learn_app.reverse_models import AmazonProductKeywordsRank, AmazonProduct, AmazonSeller, AmazonProductImage, \
    JdProducts, JdKeywords, JdProductReview, SinaPages, SinaDownloadQueue, TencentDownloadQueue, TencentPages, \
    TaobaoKeywords, TaobaoProducts, TaobaoSellerPage
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


#表单
class UserForm(forms.Form):
    # username = forms.CharField(label='用户名', max_length=100)
    # password = forms.CharField(label='密码', widget=forms.PasswordInput())
    username = forms.CharField(
        required=True,
        label='用户名',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
            }
        )
    )
    password = forms.CharField(
        required=True,
        label='密码',
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
            }
        )
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            cleaned_data = super(UserForm, self).clean()


def index(request):
    user_list = User.objects.all()
    return render_to_response('index.html',{'user_list': user_list})

#注册
def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render(request, 'regist.html',{'uf':uf})

#登陆
def login(request):
    if request.method == 'POST':
        print (request.body)
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/success/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/login1/')
    else:
        uf = UserForm()
    return render(request, 'login1.html', {'uf':uf})

def login1(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/index1/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/login1/')
    else:
        uf = UserForm()
    return render(request, 'login1.html', {'uf':uf})

def index1(request):
    return render(request, 'index1.html')

def main(request):
    return render(request, 'main.html')

def nav(request):
    return render(request, 'nav.html')

def button(request):
    return render(request, 'button.html')

def form(request):
    return render(request, 'form.html')

def table(request):
    return render(request, 'table.html')

def auxiliar(request):
    return render(request, 'auxiliar.html')

#登陆成功
def indexs(request):
    username = request.COOKIES.get('username','')
    return render_to_response('index1.html' ,{'username':username})

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

def sidebar(request):
    return render(request, 'sidebar_main.html')

def home(request):
    string = "World!"
    return render(request, "learn_app/home.html", {'string': string})

def page_test(request):
    search_input = request.GET["search_input"]
    platform = request.GET["platform"]
    content = request.GET["content"]
    if (platform == "amz"):
        if (content == "keyword"):
            products_list = []
            keywords_list = AmazonProductKeywordsRank.objects.filter(keywords=search_input)
            for i in keywords_list:
                products_list.append(AmazonProduct.objects.get(asin=i.asin))
    # else:
    #     keywords_list = AmazonProductKeywordsRank.objects.all()
    count = len(products_list)
    print count
    paginator = Paginator(products_list, 25)
    curr_page = request.GET["page"]
    print (curr_page)
    try:
        contacts = paginator.page(curr_page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    if (count%25 == 0):
        num_pages = count / 25
    else:
        num_pages = count / 25 + 1
    print (num_pages)
    last_page = int(num_pages)
    print (last_page)
    int_curr_page = int(curr_page)
    print (int_curr_page)
    if (int_curr_page==0):
        has_previous = False
    else:
        has_previous = True
    if (int_curr_page == int(num_pages)):
        has_next = False
    else:
        has_next = True
    previous_page_number = int_curr_page - 1
    next_page_number = int_curr_page + 1
    return render(request, 'learn_app/page_test.html', {'contacts': contacts,
                                                        'count': count,
                                                        'curr_page': curr_page,
                                                        'num_pages': num_pages,
                                                        'last_page': last_page,
                                                        'previous_page_number': previous_page_number,
                                                        'next_page_number': next_page_number,
                                                        'has_previous': has_previous,
                                                        'has_next': has_next
                                                        })



def ajax_list(request):
    a = range(100)
    return HttpResponse(json.dumps(a), content_type='application/json')


def ajax_dict(request):
    # name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    name_dict = [
        {"name": "xiaoming", "age": 20},
        {"name": "tuweizhong", "age": 24},
        {"name": "xiaoli", "age": 33},
    ]
    return HttpResponse(json.dumps(name_dict), content_type='application/json')



def hello(request):
    search_input = request.GET["search_input"]
    platform = request.GET["platform"]
    content = request.GET["content"]
    print (search_input)
    print (platform)
    print (content)
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
                items = TaobaoProducts.objects.filter(product_id=i.product_id)
                if (len(items) > 1):
                    for i in items:
                        lists.append(i)
                else:
                    lists.append(TaobaoProducts.objects.get(product_id=i.product_id))
        elif (content == "product"):
            lists = TaobaoProducts.objects.filter(product_id=search_input)
        elif (content == "seller"):
            lists = TaobaoSellerPage.objects.filter(seller_id=search_input)
    elif (platform == "jd"):
        if (content == "keyword"):
            lists = []
            keywords = JdKeywords.objects.filter(keyword=search_input)
            for i in keywords:
                items = JdProducts.objects.filter(sku=i.sku)
                if (len(items)>1):
                    for i in items:
                        lists.append(i)
                else:
                    lists.append(JdProducts.objects.get(sku=i.sku))
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
    return render_to_response("learn_app/hello.html", locals())