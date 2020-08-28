from django.urls import path
from . import views

urlpatterns =[
    #Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginUser, name='loginUser'),
    path('logout/', views.logoutUser, name='logoutUser'),
    #TOdos
    path('home/', views.home, name='home'),
    path('create/', views.createTodos, name='createTodos'),
    path('current/', views.currentTodos, name='currentTodos'),
    path('completed/', views.completedTodos, name='completedTodos'),
    path('todo/<int:todo_pk>/', views.viewTodo, name='viewTodo'),
    path('todo/<int:todo_pk>/complete/', views.completeTodos, name='completeTodos'),
    path('todo/<int:todo_pk>/delete/', views.deleteTodos, name='deleteTodos'),

]

