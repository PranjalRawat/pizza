from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView, CreateView,DetailView, ListView
from .forms import PizzaModelForm
from .models import Pizza
from django.urls import reverse_lazy

class PizzaDetailView(DetailView):
    template_name = "pizza/detail_view.html"

    queryset = Pizza.objects.all()

    def get_object(self):
        pk = self.kwargs.get("pk")
        return Pizza.objects.get(id=pk)

class PizzaListView(ListView):
    template_name = "pizza/list_view.html"
    queryset = Pizza.objects.all()
    

#Create
class PizzaCreateView(CreateView):

    form_class = PizzaModelForm
    template_name = 'pizza/create_view.html'
    success_url = "/"


#Update
class PizzaUpdateView(UpdateView):
    queryset = Pizza.objects.all()
    form_class = PizzaModelForm
    template_name = "pizza/update_view.html"
    success_url = "/"


#Delete
class PizzaDeleteView(DeleteView):
    model = Pizza
    template_name = "pizza/delete_confirm.html"
    success_url = reverse_lazy("list")
