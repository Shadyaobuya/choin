from django.shortcuts import redirect, render

from leadership.models import Transaction, Wallet
from .forms import UpdateProfileForm,UserProfileForm
from .models import Student
from django.core.exceptions import ObjectDoesNotExist
# @login_required



def student_profile(request):
    try:
        userprofile = request.user.userprofile
    except ObjectDoesNotExist:
        userprofile = Student(user=request.user)
        
    if request.method == 'POST':
        user_form = UpdateProfileForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile.user)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            #user.username = user.email
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('student-home')
    else:
        profile_form = UserProfileForm(instance=request.user.userprofile)
        user_form = UpdateProfileForm(instance=request.user)
    args = {
        'user_form': user_form, # basic user form
        'profile_form': profile_form # user profile form
        }
    return render(request, 'student_profile.html', args)

def student_transactions(request):
    transactions = Transaction.objects.all().filter(receiver = request.user.username)
    choinBalance = sum(transactions.values_list('value', flat=True))

    wallet = Wallet.objects.all()
    for object in wallet:
        if object.owner:
            wallet.update(owner = request.user.username , choinBalance = choinBalance)

        else:
            wallet.create(owner = request.user.username , choinBalance = choinBalance)
            wallet.save()    


    return render(request,'student_transactions.html',{'transactions':transactions,'wallet':wallet})      

def student_home(request):
    return render(request,'student_home.html')
def redeem(request):
    bal = Wallet.objects.all().filter(owner = request.user.username)

    return render(request,'redeem.html',{'bal':bal})
def redeem_failed(request):
    return render(request,'RedeemFailed.html')
def redeem_success(request):
    return render(request,'RedeemSucceed.html')


# def the_wallet(request):
#     transactions = Transaction.objects.all().filter(receiver = request.user.username)

    
#     choinBalance = sum(transactions.values_list('value', flat=True))
#     balance,created= Wallet.objects.update_or_create(

#         owner = request.user.username,
#         choinBalance = choinBalance,
           
#            )
#     balance.save()
#     return render(request,'wallet.html',{'balance':balance})    
   