from django.shortcuts import render
from django.db.models import Count, Sum, ExpressionWrapper, F, DecimalField
from .models import *
import time
from functools import cache

@cache
def index(request):
    start_time = time.time()
    summary = OrderDetails.objects.values('orderid') \
        .annotate(total=Sum(ExpressionWrapper(F('unitprice') * F('quantity')
        , output_field=DecimalField())))
    context = {"summary":summary}
    print("--- %s seconds ---" % (time.time() - start_time))
    return render(request, "index.html", context)
    
