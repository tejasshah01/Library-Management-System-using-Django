from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from LMSapp_admin.forms import Customer_issue_book,user_login
from LMSapp_admin.models import issued_book

from django.contrib.auth import authenticate,login,logout
# Create your views here.

def User_login(request):
    if request.method=='POST':
        user_log=user_login(request.POST)
        if user_log.is_valid():
            email=user_log.cleaned_data['email']
            password1=user_log.cleaned_data['password1']
            user=authenticate(email=email,password=password1)
            if user is not None:
                login(request,user)
                return redirect('book_details')
    else:
        user_log=user_login()
    return render(request,'login.html',context={'user_log':user_log})
def user_logout(request):
    logout(request)
    return redirect ('login')



def issuebook(request):
    if request.method=='POST':
        issue=Customer_issue_book(request.POST)
        if issue.is_valid():
           issue.save()
           issue=Customer_issue_book()


    else:
        issue=Customer_issue_book()
    return render(request,'issue_book.html',context={'issue':issue})

def view_issuebook(request):
    book=issued_book.objects.filter(is_active=True)
    return render(request,'bookdetails.html',context={'book':book})

def edit_issuebook(request,id):
    if request.method=='POST':
        book=issued_book.objects.get(id=id)
        Edit_issuebook=Customer_issue_book(request.POST,instance=book)
        if Edit_issuebook.is_valid():
           Edit_issuebook.save()
           return redirect ('book_details')
    else:
        
        book=issued_book.objects.get(id=id)
        Edit_issuebook=Customer_issue_book(instance=book)
    return render(request,'update_book.html',context={'Edit_issuebook':Edit_issuebook})

def delete_book(request,id):
    if request.method=='POST':
        delete_book=issued_book.objects.get(pk=id)
        delete_book.is_active=False
        delete_book.save()
        return redirect('book_details')
    
def search(request):
    Search=request.GET.get('Search')
    print(Search)
    searchs=issued_book.objects.filter(name__icontains =Search)
    return render(request,'search.html',context={'search':searchs})

       





