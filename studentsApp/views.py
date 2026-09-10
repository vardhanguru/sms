from django.shortcuts import render

# Create your views here.

def dashboard(request):

    # dashboard shows all the students data

    data = {
    'students' : [
    {
        'name': 'Mahesh',
        'age': 29,
        'address': 'Hyderabad',
        'email': 'mahesh@gmail.com'
    },
    {
        'name': 'Rahul',
        'age': 21,
        'address': 'Bangalore',
        'email': 'rahul@gmail.com'
    },
    {
        'name': 'Priya',
        'age': 22,
        'address': 'Chennai',
        'email': 'priya@gmail.com'
    },
    {
        'name': 'Arjun',
        'age': 20,
        'address': 'Mumbai',
        'email': 'arjun@gmail.com'
    },
    {
        'name': 'Sneha',
        'age': 23,
        'address': 'Delhi',
        'email': 'sneha@gmail.com'
    },
    {
        'name': 'Kiran',
        'age': 21,
        'address': 'Pune',
        'email': 'kiran@gmail.com'
    },
    {
        'name': 'Anjali',
        'age': 22,
        'address': 'Hyderabad',
        'email': 'anjali@gmail.com'
    },
    {
        'name': 'Ravi',
        'age': 24,
        'address': 'Vijayawada',
        'email': 'ravi@gmail.com'
    },
    {
        'name': 'Pooja',
        'age': 20,
        'address': 'Kolkata',
        'email': 'pooja@gmail.com'
    },
    {
        'name': 'Vikram',
        'age': 23,
        'address': 'Jaipur',
        'email': 'vikram@gmail.com'
    }
]}


    return render(request, 'dashboard.html', context=data)

def show(request):

    data = {'subscribed':False, 'content':{'movie':'1', 'show':'Big Boss', 'series':'ST'},
            'show_when_not_subscribed':{'movies':600, 'shows': 1000, 'series':1000},
            'fruits': ['apple', 'banana', 'grapes', 'oranges']}


    return render(request, 'show.html', context=data)