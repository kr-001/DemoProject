Django Intern Assignment
API EndPoints in the project:
1.Work Api
```
def work(request):
   works = Work.objects.order_by().values('work_type').distinct()
   payload = {'works' : works}
   return render(request , 'allWorks.html' , payload)
```
Explaination:
"work" API  retrieves a list of distinct work types from the Work model in the Django app and renders them in an HTML template called allWorks.html.
The Work object is a model in the Django app that represents a work. The order_by() method is used to order the retrieved Work objects in ascending order by default, which is equivalent to ordering by their primary key. The values() method is then used to retrieve only the work_type attribute of each Work object, which is the type of work. Finally, the distinct() method is used to ensure that only unique work types are returned in the works variable.
The payload dictionary is then created to store the list of work types, which will be used to display them on the template.
Finally, the render() function is called with the request object, the name of the HTML template (allWorks.html), and the payload dictionary as parameters. This function returns an HTTP response that renders the template with the provided payload data.
Overall, this API provides a way to retrieve a list of distinct work types from the Work model in the Django app and display them on a web page. This could be useful, for example, in a dropdown menu for filtering works by type.

2. Filter data by work type.
```
def work_by_type(request,work_type):
   works = Work.objects.filter(work_type = work_type)
   print(works)
   payload = {'works' : works , 'work_type' : work_type}
   return render(request , 'workType.html',payload)

```
Explaination: 
This "work_by_type"  API  takes a GET request with a work_type parameter and returns a filtered list of works of that type.
The Work object is a model in the Django app, and the filter() method is used to retrieve all objects of Work type that match the provided work_type parameter. The resulting list of works is stored in the works variable.
The payload dictionary is then created to store the list of works and the work_type parameter, which will be used to display the correct work type on the template.
Finally, the render() function is called with the request object, the name of the HTML template (workType.html), and the payload dictionary as parameters. This function returns an HTTP response that renders the template with the provided payload data.
Overall, this API provides a simple way to retrieve and display works of a specific type on a web page.

3. Search By Artist Name API
```
def search(request):
      query = request.GET.get('query')
      data = Artist.objects.filter(name__icontains=query)
      return render(request , 'search.html' , {'query' : query , 'data' : data})
```
Explaination:
'search' api  performs a search on the Artist model in the Django app based on a query parameter that is passed in a GET request. It then renders an HTML template called search.html with the search results and the original query that was searched for.
The query variable is retrieved from the GET request using the GET.get() method, which retrieves the value of the query parameter. This parameter is usually entered by the user in a search box on the website.
The Artist object is a model in the Django app that represents an artist. The filter() method is used to retrieve all Artist objects that have a name attribute containing the query string, ignoring case sensitivity.
The render() function is then called with the request object, the name of the HTML template (search.html), and a dictionary that contains the original search query (query) and the search results (data) as parameters. This function returns an HTTP response that renders the template with the provided data.
Overall, this API provides a way to search for artists in the Artist model based on a query parameter and display the results on a web page. This could be useful for creating a search functionality on a website that has a list of artists.

```
For Admin Login use:
 username:admin
 password:Admin@198
```
4. User Registration
```def register(request):
    if request.method=='POST':
        email = request.POST.get('email')
        username=request.POST['username']
        pass1 = request.POST['pass1']
        pass2= request.POST['pass2']
        print(User.objects.filter(username=username))
        
        if pass1==pass2:
          if User.objects.filter(email=email).exists():
            return redirect('/register')
          elif User.objects.filter(username=username).exists():
            return redirect('/register')
          else:
            user = User.objects.create_user(email=email,username=username,password=pass1)
            user.save();
            return redirect('/')
    else:
        return render(request,'register.html')
 ```

Explanation: API endpoint for user registration. It is designed to receive an HTTP request from user through  a web broswer
The function first checks if the request method is 'POST'. This is because in web development, the POST method is typically used for submitting data to a server for processing, while the GET method is used for retrieving data from a server. In this case, the function expects to receive data from a user registration form submitted via POST.
The function then extracts the email, username, password1, and password2 fields from the POST request using the request.POST.get() method. It checks whether the username is already taken by querying the User database using the User.objects.filter() method. If the username already exists, the function redirects the user back to the registration page.
If the username is unique, the function then checks if the two passwords entered by the user match. If the passwords match, it checks if the email is already taken by querying the User database using the User.objects.filter() method. If the email already exists, the function redirects the user back to the registration page.
If both the username and email are unique and the passwords match, the function creates a new User object using the User.objects.create_user() method and saves it to the database using the user.save() method. Finally, the function redirects the user to the homepage ('/').
If the request method is not 'POST', the function renders the registration form using the render() method and the 'register.html' template.


4.1 Client Table Creation by Signals
This is my signals.py file
```
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from app.models import Client

@receiver(post_save,sender=User)
def create_client(sender , instance , created , **kwargs):
    if created:
        Client.objects.create(user=instance,name=instance.username)
```
Explanation: This is a Python function that is designed to listen to the "post_save" signal from the User model in Django, which is triggered every time a User instance is created or updated. When the signal is triggered, the function checks if the User instance was just created (not updated), by checking the "created" argument. If the instance was just created, the function creates a new Client object and associates it with the User instance by setting the "user" attribute to the newly created User instance and setting the "name" attribute to the username of the User instance.
This function can be used to automatically create related objects for a User instance when it is created, without having to manually create them in the view or form. In this case, it creates a Client object that is associated with the User instance, and sets the name of the Client to be the same as the username of the User instance
The "@receiver" decorator is used to register the function as a receiver of the "post_save" signal from the User model. The "sender" argument specifies the model that sends the signal, which in this case is the User model. The "instance" argument contains the User instance that was just saved, and the "created" argument is a boolean value that indicates whether the instance was just created or updated. The "**kwargs" argument allows for additional keyword arguments to be passed to the function if needed.
 
 THANK YOU!!
