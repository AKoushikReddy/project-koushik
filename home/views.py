from .forms import HomeForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from .models import Post


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/first.html'

    def get(self, request, *args, **kwargs):
        form = HomeForm()
        posts = Post.objects.all()
        return render(request, self.template_name, {'form': form, 'posts': posts})

    def post(self, request, *args, **kwargs):
        form = HomeForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.user = request.user
            p.save()
            return redirect('/home')
        return render(request, self.template_name, {'form': form})

    # def home_view(request):


#     inst = Post.objects.get(user=request.user)
#     if request.method == "POST":
#         form = HomeForm(request.POST, instance=inst)
#         if form.is_valid():
#             form.save()
#             return redirect('/home')
#     else:
#         form = HomeForm(instance=inst)
#         return render(request, 'home/first.html', {'form': form})



