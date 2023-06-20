from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ListingForm
from .models import User ,  Bid ,Category,Listing,Comment


def addBid(request, list_id):
    newBid = request.POST['newBid']
    listingData = Listing.objects.get(pk=list_id)
    isOwner = request.user.username == listingData.owner.username
    if int(newBid) > listingData.price.bid:
        updateBid = Bid(user=request.user, bid=int(newBid))
        updateBid.save()
        listingData.price = updateBid
        listingData.save()
        return redirect("index")
    else:
       return redirect("index")
##Update Auction

def update_auction(request,list_id):
    update_lists = Listing.objects.get(pk = list_id)
    form  = ListingForm(request.POST or None, instance = update_lists)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render (request,"auctions/update_auction.html",{
     "update_lists":update_lists,
     "form":form
    })

#Delete Auction List
def delete_auction(request,list_id):
    update_lists = Listing.objects.get(pk = list_id)
    update_lists.delete()
    return redirect ("index")

def show_listing(request,list_id):
    lists = Listing.objects.get(pk = list_id)
    

def auctions_user(request):
    return render(request, "auctions/index.html")

def index(request):
    listing_list = Listing.objects.all()
   
    return render(request, "auctions/index.html", {
       "listing_list":listing_list
    })

def category(request):
    if request.method == "POST":
        category = Category.objects.all()
        listing = Listing.objects.filter(
            active = True, 
            category = Category.objects.get(
                name = request.POST["category"]
            )
        )
        return render(request, "auctions/index.html", {
        "category": category,
        "listings": listing
        })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_auction(request):
    submitted = False
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/create_auction?submitted=True')
    else:
        form = ListingForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "auctions/create_auction.html",{
        "form":form, "submitted":submitted
    })



