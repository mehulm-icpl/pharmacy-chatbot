from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User,auth
from django.http import JsonResponse
from django.contrib.auth import login as user_login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Feedback

# Create your views here.
def index(request):
    return render(request,"index.html",{})

def about(request):
    return render(request,"about.html",{})

def ChatBot(request):
    if request.method == 'POST':
        symptom = request.POST.get('symptom', '').lower()  # Convert input to lowercase for case-insensitive matching
        response = ""

        if "headache" in symptom:
            response = "You can take ibuprofen or acetaminophen for your headache."
        elif "cold" in symptom:
            response = "You can take Dolo-650 or Doxylamine for your cold."
        elif "fever" in symptom:
            response = "Try taking ibuprofen and drink plenty of fluids to reduce your fever."
        elif "sore throat" in symptom:
            response = "Gargling with warm salt water can help soothe your sore throat."
        elif "cough" in symptom:
            response = "You can try cough syrup or lozenges to ease your cough."
        elif "diarrhea" in symptom:
            response = "Drink plenty of fluids and avoid dairy and fatty foods to help with diarrhea."
        elif "nausea" in symptom:
            response = "Try ginger tea or over-the-counter anti-nausea medication for relief."
        elif "vomiting" in symptom:
            response = "Stay hydrated and avoid solid foods until vomiting subsides."
        elif "back pain" in symptom:
            response = "Apply heat or cold packs and consider over-the-counter pain relievers for back pain."
        elif "stomach ache" in symptom:
            response = "Avoid spicy and fatty foods, and consider over-the-counter antacids for stomach ache."
        elif "poorva" in symptom:
            response = "Hello poorva how are you! 🌚👻"
        else:
            response = "I'm sorry, I'm not sure what medication to recommend for that symptom."

        return render(request, 'Chatbot.html', {'response': response})
    else:
        return render(request, 'Chatbot.html')


def medicine(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        photo = request.POST.get('photo')

        feedback = Feedback(name=name, price=price, photo=photo)
        feedback.save()
    return render(request, "medicine.html",{})


def order(request):
    return render(request, "order.html",{})

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Feedback = feedback(name=name, phone=phone, email=email, messages=message)
        Feedback.save()
    return render(request, "Feedback.html",{})

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        data = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username,
                                        password=password1)
        data.save()
        return redirect('login')
    return render(request, "signup.html", {})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
    return render(request, "login.html",{})

def Logout(request):
    logout(request)
    return redirect('login')