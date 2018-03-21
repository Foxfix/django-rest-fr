# DJANGO REST API

    http://ec2-52-53-163-153.us-west-1.compute.amazonaws.com/api/hello-viewset/

Allow to add any name and receive answer Hello name
  
Allow: GET, POST, HEAD, OPTIONS
*************************************
  
    http://ec2-52-53-163-153.us-west-1.compute.amazonaws.com/api/profile/

Allow to add new user

Allow: GET, POST, HEAD, OPTIONS

You can change/DELETE only your own data by adding your id

     http://ec2-52-53-163-153.us-west-1.compute.amazonaws.com/api/profile/<id>

*************************************

    http://ec2-52-53-163-153.us-west-1.compute.amazonaws.com/api/login/

Allow to login with given auth token

Allow: POST, OPTIONS

![Image alt](https://github.com/Foxfix/django-rest-fr/blob/master/login.png)

Can be tested with Modify Headers in Chrome

just add your token into header
*************************************

    http://ec2-52-53-163-153.us-west-1.compute.amazonaws.com/api/feed/

Allow to add and see info

Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS

You can DELETE only your info by adding your id

    http://ec2-52-53-163-153.us-west-1.compute.amazonaws.com/api/feed/<id>

