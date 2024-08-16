from django.db import models

# Create your models here.
class SignupModel(models.Model):
    signname=models.TextField()
    signemail=models.EmailField()
    signpass=models.TextField()
    
    

    #  -->
    
    
    
    
    
    
#     <!-- <!DOCTYPE html>
# {% load static %}
# <html lang="en"  data-bs-theme="dark">
# <head>
#     <title>Disney+</title>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
#     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
#     <style>
#         #ind{
#             background-image: url("{% static 'images/disney_login.jpg' %}");
#             width: 100%;
#             height: 648px;
#         }

#         #indxlogbtn{
#             width: 217px;
#             box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
#             font-size: medium;
#             background-image: linear-gradient(to right, #0c57e2, #061f6b);
#             border: none;
#             padding: 5px;
#         }

#         #loader{
#             position: fixed;
#             top: 0;
#             bottom: 0;
#             left: 0;
#             right: 0;
#             z-index: 2147483647;
#         }

#     </style>
# </head>
# <body>
    
    
#     <div class="container-fluid">
#         <div class="row">
#             <div class="container-fluid" id="ind">
#                 <video id="loader" width="100%" height="400px" loop muted autoplay>
#                     <source src="{% static 'disneyintrovid.mp4' %}" type="video/mp4">
#                   </video>
#                    <center><img src="{% static 'images/disneylogo1.png' %}" alt="no" style="width: 186px; height: 110px; margin: 203px;"></center>
#                    <center><h3 style="margin-top: -127px; text-shadow: 9px 0px 10px black;"><b>Home of your favourites and more</b></h3></center><br>
#                    <center><button type="submit" id="indxlogbtn" class="btn"><a href="{% url 'login' %}" style="text-decoration: none; color:white;"><b>Log In</b> &#11166;</a> </button></center>
#             </div>



#         </div>
#     </div>
    
# </body>
# <script>
#     var element = document.getElementById("loader");
#     element.parentNode.removeChild(element);
# </script>
# </html> -->




# <!DOCTYPE html>
# {% load static %}
# <html lang="en" data-bs-theme="dark">
# <head>
#     <title>Disney+</title>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
#     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
#     <style>
#         #ind {
#             background-image: url("{% static 'images/disney_login.jpg' %}");
#             width: 100%;
#             height: 648px;
#         }

#         #indxlogbtn {
#             width: 217px;
#             box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
#             font-size: medium;
#             background-image: linear-gradient(to right, #0c57e2, #061f6b);
#             border: none;
#             padding: 5px;
#         }

#         #loader {
#             position: fixed;
#             top: 0;
#             bottom: 0;
#             left: 0;
#             right: 0;
#             z-index: 2147483647;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             background: black;
#         }

#         #main-content {
#             display: none;
#         }
#     </style>
# </head>
# <body>
#     <!-- Loader Video -->
  
#     <!-- Main Content -->
#     <div id="main-content">
#         <div class="container-fluid">
#             <div class="row">
#                 <div class="container-fluid" id="ind">
#                     <center><img src="{% static 'images/disneylogo1.png' %}" alt="no" style="width: 186px; height: 110px; margin: 203px;"></center>
#                     <center><h3 style="margin-top: -127px; text-shadow: 9px 0px 10px black;"><b>Home of your favourites and more</b></h3></center><br>
#                     <center><button type="submit" id="indxlogbtn" class="btn"><a href="{% url 'login' %}" style="text-decoration: none; color:white;"><b>Log In</b> &#11166;</a></button></center>
#                 </div>
#             </div>
#         </div>
#     </div>


# </body>
# </html>
