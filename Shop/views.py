from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from Shop.forms import CallRequestsForm
from cart.forms import CartAddProductForm
from .models import Category, Post


class About(View):
    def get(self, request):
        return render(request, 'Shop/about.html')


class Payment(View):
    def get(self, request):
        return render(request, 'Shop/payment.html')


class Guarantee(View):
    def get(self, request):
        return render(request, 'Shop/guarantee.html')


class Delivery(View):
    def get(self, request):
        return render(request, 'Shop/delivery.html')


class ShopMixin:
    def recommendation(self):
        return Post.objects.all()[:4:5]


class PostView(ShopMixin, ListView):
    paginate_by = 9
    model = Post
    template_name = 'Shop/Shop.html'

    # def get_queryset(self):
    #     return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        category = Category.objects.all()
        context.update({'category': category})
        return context


class Index(View):
    def get(self, request):
        return render(request, 'Shop/index.html')


class PostDetail(DetailView):
    model = Post
    template_name = 'Shop/product-single.html'
    slug_url_kwarg = 'post_slag'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        cart_product_form = CartAddProductForm()
        context.update({'cart_product_form': cart_product_form})
        return context


class PostListView(ShopMixin, ListView):
    paginate_by = 9
    model = Post
    template_name = 'Shop/Shop.html'

    def get_queryset(self):
         # return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')
        return Post.objects.filter(category__in=Category.objects.get(slug=self.kwargs.get("slug")).get_descendants(include_self=True))

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        category = Category.objects.all()
        context.update({'category': category})
        return context


class Search(ListView):
    template_name = "Shop/Shop.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get("q"))[:9]

    def get_context_data(self, *args, **kwargs):
        context = super(Search, self).get_context_data(*args, **kwargs)
        category = Category.objects.all()
        context.update({'category': category})
        context["q"] = self.request.GET.get("q")
        return context


def call(request):
    status = ""
    if request.method == 'POST':
        form = CallRequestsForm(request.POST)
        if form.is_valid():
            status = "Ваше сообщение отправлено, спасибо!"
            form.save()
        else:
            status = "форма не валідна"

    form = CallRequestsForm()
    data = {'form': form,
            'status': status}

    return render(request, 'Shop/call_requests.html', data)

