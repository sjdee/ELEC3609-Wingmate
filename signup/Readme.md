# SIGNUP APPLICATION

This folder is for one of the many django applications of the wingmate project.

This Signup application **supports 3 pages**: *login, registration and logout*. 

The templates folder contains the html **templates for Login and Registration** which extend on the "Base HTML" pages which are a part of the main django application and are present in `wingmate > templates`.

The register page has custom css, register.css in `wingmate > signup > static > signup > css`.

Most importantly, this application **renders a signup form** everytime the register page is requested using the forms.py. When the request is recived by views.py, it creates an object of the SignUpForm class present in forms.py. 