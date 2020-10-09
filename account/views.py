from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from .models import *
from .forms import AddressForm, UserForm
from registerItem.models import *
from django.contrib.auth.models import Group
from django.views.generic import ListView
from email.message import EmailMessage
import smtplib
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# from registerItem.forms import StockForm, ItemForm


# Create your views here.
# @unauthenticated_user
@method_decorator(login_required, name='dispatch')
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
@method_decorator(login_required, name='dispatch')
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


# def registerPage(request):
#     try:
#         user_form = CreateUserForm(request.POST or None, request=request)
#         if user_form.is_valid():
#             user_form.save()
#             username = user_form.cleaned_data.get('username')
#             password = user_form.cleaned_data.get('password1')
#             email = user_form.cleaned_data.get('email')
#             fn = user_form.cleaned_data.get('first_name')
#             # print(username)
#             # print(password)
#             my_mail = EmailMessage()
#             my_mail['from'] = "Huye District"
#             my_mail["to"] = email
#             my_mail['subject'] = " E-System Credentials"
#             email_content = f'Dear {fn.upper()}, Thank you, you have received this email because you have ' \
#                             f'registered in Huye E-System  you can use the following username and password ' \
#                             f'to login in the system.  ' \
#                             f'Username: {username}  Password: {password}. ' \
#                             f'from Huye District'
#
#             my_mail.set_content(email_content)
#             with smtplib.SMTP(host="smtp.gmail.com", port=587) as help:
#                 help.ehlo()
#                 help.starttls()
#                 help.login("auca.system@gmail.com", "Ingabire@067")
#                 help.send_message(my_mail)
#                 # print("All have done cleary (@)")
#                 user_form = CreateUserForm(request=request)
#             messages.success(request, "User Created Successfully..")
#     except ValueError:
#         user_form = CreateUserForm(request=request)
#
#     context = {'user_form': user_form}
#     return render(request, 'register.html', context)
@login_required()
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
@login_required()
def userProfile(request):
    user = request.user
    form = CreateUserForm(instance=user)
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'registration/profile.html', context)
@login_required()
def user_profiling(request):
    data = User.objects.filter(username=request.user.username)
    context = {'data': data}
    return render(request, 'profiling.html', context)


# ================change password =================
@login_required()
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("login")
        else:
            return redirect("change_password")
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, "change_password.html", {'form': form})




# the login
# @unauthenticated_user
# @login_required()
def homePage(request):
    return render(request, 'registration/home.html')


# display of * user
@login_required()
def allUser(request):
    users = User.objects.all()

    context = {'users': users}
    return render(request, 'allUsers.html', context)


# update user
@login_required()
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
@login_required()
def deleteUser(request, pk):
    form = User.objects.get(id=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form.delete()
            return redirect('users')
    context = {'form': form}
    return render(request, 'user/deleteUser.html', context)

@login_required()
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
@login_required()
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

@login_required()
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


# # @login_required(login_url='login')
# # @allowed_users(allowed_roles=['Admin'])
# def dashboard2(request):
#     context = {}
#     return render(request, 'dashboard2.html', context)
@method_decorator(login_required, name='dispatch')
class Dashboard2(ListView):
    model = Stock
    template_name = 'dashboard2.html'

    def get_context_data(self, *, object_List=None, **kwargs):
        context = super(Dashboard2, self).get_context_data(**kwargs)
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


# ====================generate reports and print excel/pdf ================

# def karamaReportGererate(request):
#     data = Item.objects.filter()