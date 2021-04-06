from django.http import HttpResponse
from django.shortcuts import render
#def index(request):
    #return HttpResponse("<body style=background-color:white;<body> <h1 style=color:black;>About Yourself<h1> <h2 style=color:Green;>My Name Is Shivam Sharma <br>I am Student Of Oriental institute of science & technology bhopal <br>Age is:- 24 <br>Gender:- Male <br> Enrollment:-0105CA193D53<h2><h1>My Hobie's<h1><h2 style=color:blue;>may Best Hobie is Participate the cultural function<br>Other is listen the cultural song and Bhajans<h2><br><p>My LinkedIn Profile:- <a href=https://www.linkedin.com/in/shivam-sharma-5a7122174>LinkedIn.com <a><p><br><p>My Instagram Profile:- <a href=https://instagram.com/shivam_sharma_madhavgarh?igshid=15xi2m36qbkia>instagram.com<a><p><br><p>Send email:-<a href=mailto:shivamsharmamdh@gmail.com>Email.com<a><p><br><p>My Facebook Profile:-<a href=https://www.facebook.com/lallan.tiwari.73>Facebook.com<a><p>")
def index(request):
  return render(request, 'index.html')
  