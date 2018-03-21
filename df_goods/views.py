from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    goodstype = GoodsType.objects.all()
    # print(goodstype[0])
    # print(goodstype[0])
    # print(goodstype[0])
    # print(goodstype[0])
    # print(goodstype[0])
    # print(goodstype[0])
    type0 = goodstype[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = goodstype[0].goodsinfo_set.order_by('-gclick')[0:4]

    type1 = goodstype[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = goodstype[1].goodsinfo_set.order_by('-gclick')[0:4]

    type2 = goodstype[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = goodstype[2].goodsinfo_set.order_by('-gclick')[0:4]

    type3 = goodstype[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = goodstype[3].goodsinfo_set.order_by('-gclick')[0:4]

    type4 = goodstype[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = goodstype[4].goodsinfo_set.order_by('-gclick')[0:4]

    type5 = goodstype[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = goodstype[5].goodsinfo_set.order_by('-gclick')[0:4]
    # print(goodstype[0].id)
    # print(goodstype[1].id)
    # print(goodstype[2].id)
    # print(goodstype[3].id)
    # print(goodstype[4].id)
    # print(goodstype[5].id)

    context = {
        'title': '首页',
        'goodstype0': goodstype[0].id,
        'goodstype1': goodstype[1].id,
        'goodstype2': goodstype[2].id,
        'goodstype3': goodstype[3].id,
        'goodstype4': goodstype[4].id,
        'goodstype5': goodstype[5].id,
        'type0': type0, 'type01': type01,
        'type1': type1, 'type11': type11,
        'type2': type2, 'type21': type21,
        'type3': type3, 'type31': type31,
        'type4': type4, 'type41': type41,
        'type5': type5, 'type51': type51
    }
    return render(request, 'df_goods/index.html', context)


def detail(request, id):
    goodstype = GoodsType.objects.all()
    goodsinfo = GoodsInfo.objects.get(id=int(id))
    newsinfo = GoodsInfo.objects.filter(gtype=goodsinfo.gtype).order_by('-id')[0:2]
    gtitle = goodsinfo.gtitle
    gprice = goodsinfo.gprice
    gImage = goodsinfo.gImage
    gunit = goodsinfo.gunit
    gclick = goodsinfo.gclick
    gdescriptioni = goodsinfo.gdescriptioni
    gstore = goodsinfo.gstore
    gcontent = goodsinfo.gcontent
    context = {
        'goodstype': goodstype,
        'newsinfo': newsinfo,
        'gtitle': gtitle, 'gprice': gprice, 'gImage': gImage,
        'gunit': gunit, 'gclick': gclick, 'gdescriptioni': gdescriptioni,
        'gstore': gstore, 'gcontent': gcontent
    }
    return render(request, 'df_goods/detail.html', context)


def list(request, tid, pindex, sort):
    # goods = GoodsInfo.objects.filter(gtype=int(tid))
    typeid =GoodsType.objects.get(pk=int(tid))
    newsinfo = GoodsInfo.objects.filter(gtype=int(tid)).order_by('-id')[0:2]
    goods = []
    if sort=='0':
        print(sort)
        goods = GoodsInfo.objects.filter(gtype=int(tid)).order_by('-id')
    elif sort=='1':
        goods = GoodsInfo.objects.filter(gtype=int(tid)).order_by('-gprice')
    elif sort=='2':
        goods = GoodsInfo.objects.filter(gtype=int(tid)).order_by('-gclick')
    # print(goods)
    pagenator = Paginator(goods, 2)
    page = pagenator.page(int(pindex))
    context = {'goodsinfo': goods,
               'sort': sort,
               'goodstype': typeid,
               'newsinfo': newsinfo,
               }
    return render(request, 'df_goods/list.html', context)