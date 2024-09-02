
from django.shortcuts import render,redirect,get_object_or_404
from . models import MenuCategory,Menu
from django.contrib import messages
from .forms import ReservationForm,SubscriberForm
from django.views import View
from django.utils import timezone




def home(request):
    
    return render(request,'home.html')

   


def base(request):
    return render(request,'home.html')



def menu_view(request):
    categories = MenuCategory.objects.prefetch_related('menu_items').all()
    return render(request, 'menu.html', {'categories': categories})


def location(request):
    return render(request,'location.html')








def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation_date = form.cleaned_data['date']
            if reservation_date < timezone.now().date():
                messages.error(request, 'The date cannot be in the past. Please choose a future date.')
            else:
                form.save()
                messages.success(request, 'Your reservation has been made successfully!')
                return redirect('home')  # Перенаправление на домашнюю страницу или другую страницу
        else:
            messages.error(request, 'There was an error with your reservation. Please try again.')
    else:
        form = ReservationForm()

    return render(request, 'reservation.html', {'form': form})

class MenuDetailView(View):
    def get(self, request, item_id):
        menu_item = get_object_or_404(Menu, id=item_id)
        return render(request, 'menu_detail.html', {'menu': menu_item})
    


    

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные формы в базу данных
            messages.success(request, 'Thank you for subscribing!')
            return redirect('home')  # Перенаправление на главную страницу после успешной подписки
    else:
        form = SubscriberForm()
    
    return render(request, 'footer.html', {'form': form})