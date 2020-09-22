from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from .models import *
from .forms import AddressForm, UserForm
from registerItem.models import *
from django.contrib.auth.models import Group
from django.views.generic import ListView


# from registerItem.forms import StockForm, ItemForm


# Create your views here.
# @unauthenticated_user
class Dashboard(ListView):
    model = Stock
    template_name = 'Dashboard.html'

    def get_context_data(self, *, object_List=None, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['computer_lap'] = Stock.objects.filter(category='Computer Laptop').count()
        context['laptop_given'] = Item.objects.filter(device__category='Computer Laptop').count()
        context['computer_desk'] = Stock.objects.filter(category='Computer Desktop').count()
        context['desktop_given'] = Item.objects.filter(device__category='Computer Desktop').count()

        context['printer'] = Stock.objects.filter(category='Printer').count()
        context['printer_given'] = Item.objects.filter(device__category='Printer').count()

        context['routers'] = Stock.objects.filter(category='4G Router').count()
        context['routers_given'] = Item.objects.filter(device__category='4G Router').count()

        context['scanners'] = Stock.objects.filter(category='Scanner').count()
        context['scanners_given'] = Item.objects.filter(device__category='Scanner').count()

        context['television'] = Stock.objects.filter(category='Television').count()
        context['television_given'] = Item.objects.filter(device__category='Television').count()

        context['decoder'] = Stock.objects.filter(category='Decoder').count()
        context['decoder_given'] = Item.objects.filter(device__category='Decoder').count()

        context['all_device'] = Stock.objects.filter(availability='Available').count()
        context['all_available_device'] = Stock.objects.filter(availability='Available').count()

        context['all_stocks'] = Stock.objects.all()

        """snippets for counting items on sector user dashboard"""

        context['sector_laptops'] = Item.objects.filter(device__category='Computer Laptop').filter(
            address=self.request.user.address).count()

        context['sector_Desktop'] = Item.objects.filter(device__category='Computer Desktop').filter(
            address=self.request.user.address).count()

        context['sector_printer'] = Item.objects.filter(device__category='Printer').filter(
            address=self.request.user.address).count()

        context['sector_routers'] = Item.objects.filter(device__category='4G Router').filter(
            address=self.request.user.address).count()

        context['sector_scanner'] = Item.objects.filter(device__category='Scanner').filter(
            address=self.request.user.address).count()

        context['sector_television'] = Item.objects.filter(device__category='Television').filter(
            address=self.request.user.address).count()

        context['sector_decoder'] = Item.objects.filter(device__category='Decoder').filter(
            address=self.request.user.address).count()

        context['device_given_sector'] = Item.objects.filter(
            address=self.request.user.address).count()

        return context


# the dashboard1

class Dashboard1(ListView):
    model = Stock
    template_name = 'Dashboard1.html'

    def get_context_data(self, *, object_List=None, **kwargs):
        context = super(Dashboard1, self).get_context_data(**kwargs)

        context['laptop_given'] = Item.objects.filter(device__category='Computer Laptop').count()

        context['desktop_given'] = Item.objects.filter(device__category='Computer Desktop').count()

        context['printer_given'] = Item.objects.filter(device__category='Printer').count()

        context['routers_given'] = Item.objects.filter(device__category='4G Router').count()

        context['scanners_given'] = Item.objects.filter(device__category='Scanner').count()

        context['television_given'] = Item.objects.filter(device__category='Television').count()

        context['decoder_given'] = Item.objects.filter(device__category='Decoder').count()
        context['total_device'] = Item.objects.count()

        context['items'] = Item.objects.all()

        return context


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'The User was successful created' + username)
            return redirect('register')

    context = {'form': form}
    return render(request, 'register.html', context)


# the user profile photo ##########################

def userProfile(request):
    user = request.user
    form = CreateUserForm(instance=user)
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'registration/profile.html', context)


# the login
# @unauthenticated_user
def homePage(request):
    return render(request, 'registration/home.html')


# display of * user
def allUser(request):
    users = User.objects.all()

    context = {'users': users}
    return render(request, 'allUsers.html', context)


# update user
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    form = CreateUserForm(instance=user)
    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')

    context = {'form': form}
    return render(request, 'user/updateUser.html', context)


# delete user

def deleteUser(request, pk):
    form = User.objects.get(id=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form.delete()
            return redirect('users')
    context = {'form': form}
    return render(request, 'user/deleteUser.html', context)


def address(request):
    form = AddressForm()
    if request.user.is_authenticated:

        if request.method == 'POST':
            form = AddressForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('address')
    addresses = Address.objects.all()

    context = {'form': form, 'addresses': addresses}
    return render(request, 'address.html', context)


# update the address ########################

def updateAddress(request, pk):
    add = Address.objects.get(id=pk)
    # form = AddressForm(instance=add)
    form = AddressForm(instance=add)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddressForm(request.method, instance=add)
            if form.is_valid():
                form.save()
                return redirect('address')

    context = {'form': form}
    return render(request, 'address/updateAddress.html', context)


def deleteAddress(request, pk):
    form = Address.objects.get(id=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form.delete()
            return redirect('address')

    context = {'form': form}
    return render(request, 'address/deleteAddress.html', context)


# the used for test
# @login_required(login_url='login')
def dashboard1(request):
    context = {}
    return render(request, 'dashboard1.html', context)


# @login_required(login_url='login')
# @allowed_users(allowed_roles=['Admin'])
def dashboard2(request):
    context = {}
    return render(request, 'dashboard2.html', context)
