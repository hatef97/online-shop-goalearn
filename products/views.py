from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from .models import Product

from .forms import ProductForms


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 4
    template_name = 'products/product_list.html'
    context_object_name = 'product_list'


@login_required
def product_detail_view(request, pk):
    products = get_object_or_404(Product, pk=pk)

    return render(request, 'products/product_detail.html',
                  {'products': products,
                   })


class CreateNewProduct(LoginRequiredMixin, generic.CreateView):
    model = Product
    form_class = ProductForms
    template_name = "products/add_product.html"

    def form_valid(self, form):
        creator = form.save(commit=False)
        creator.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Product
    form_class = ProductForms
    template_name = "products/add_product.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Product
    template_name = 'products/delete_product.html'
    success_url = reverse_lazy("product_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
