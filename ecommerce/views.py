from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render

from ecommerce.forms import *
from ecommerce.models import Ticket


@login_required
def home_view(request):
    user = request.user
    orders = user.order_set.all()
    orders_info_spent = orders.all().aggregate(Sum('price'))['price__sum']

    now = timezone.now()
    orders_week = orders.filter(ticket__end_date__gte=now - timezone.timedelta(weeks=1))
    orders_week_spent = orders_week.aggregate(Sum('price'))['price__sum']

    orders_month = orders.filter(ticket__end_date__gte=now - timezone.timedelta(weeks=4))
    orders_month_spent = orders_month.aggregate(Sum('price'))['price__sum']

    orders_year = orders.filter(ticket__end_date__gte=now - timezone.timedelta(days=365))
    orders_year_spent = orders_year.aggregate(Sum('price'))['price__sum']

    return render(request, 'ecommerce/home.html', {
        'orders': orders,
        'orders_info_price': orders_info_spent,
        'week': {'orders': orders_week, 'spent': orders_week_spent},
        'month': {'orders': orders_month, 'spent': orders_month_spent},
        'year': {'orders': orders_year, 'spent': orders_year_spent}
    })


@login_required
def tickets_view(request):
    search = request.GET.get('title')
    orders_qs = request.user.order_set.all()

    if search:
        orders_qs = orders_qs.filter(ticket__title__icontains=search)

    paginator = Paginator(orders_qs, 1)
    page = request.GET.get('page')

    try:
        orders = paginator.page(page)
    except:
        return HttpResponseRedirect(f"""?page=1&title={search}""" if search else
                                    '?page=1')
    print(orders_qs)

    return render(request, 'ecommerce/tickets.html', {
        'orders': orders,
        'page': paginator.page(page)
    })


@login_required
def cart_view(request):
    order_form = OrderForm()

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            user = request.user
            # ticket = Ticket.objects.get(title=order_form.save(commit=False))
            order_form.save()

    return render(request, 'ecommerce/cart.html', {
        'order_form': order_form
    })
