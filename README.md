# chat-app-django
To see the WebApp at https://adi-chating-app.herokuapp.com/
as this webapp is hosted with the help of Heroku
In this chat-APP there is auth(login/signup)  funtion for user .
user can post a chat with a tital to show to everyone .
user can also see others post and like them and comment on anypost and user can also see his/her all post and others users all post also.


https://user-images.githubusercontent.com/67204555/178143037-d3eb61f7-c741-43e9-a666-ce6628abfb0f.mp4

🔍 Deep dive into my Django Chat Application: Technical Details 🔍

Architecture & Implementation:
- Built with Django 3.0.7 using MVT architecture
- User Authentication: Leveraged Django's auth system with custom views for register/login flows
- Database Models:
  • Full_chat: Stores posts with content, messages, and image support
  • Comment: Linked to posts for conversation threads
  • User: Built on Django's User model with extended functionality

Key Features:
- CRUD operations for posts (create, read, update, delete)
- Real-time like functionality with ManyToMany relationships
- Image upload capability with proper storage configuration
- Follow system to track user connections
- Session management for persistent authentication

Deployment:
- Successfully hosted on Heroku with WhiteNoise for static files
- PostgreSQL integration for production database

This project helped me master Django fundamentals while exploring relational database design in a practical application.
