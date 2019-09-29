from django.urls import path,include
from .import views
urlpatterns = [
    path('home/', views.home,name="home"),
    path('course/', views.Course,name="course"),
    path('source/', views.Source,name="source"),
    path('student_registration/', views.student_registration,name="student_registration"),
    path('walkins/', views.walkins,name="walkins"),
    path('callings/', views.Callings,name="callings"),
    path('counselling/', views.counselling,name="counselling"),
    path('joining/', views.Joining,name="joining"),
    path('calling_result/', views.calling_result,name="calling_result"),
    path('counselling_result/', views.counselling_result,name="counselling_result"),
    path('student/', views.Student,name="student"),
    path('login/', views.Login,name="login"),
    path('logout/',views.Logout,name="logout"),
    path('current_status/<pk>',views.current_status,name="current_status"),
    path('dead/<pk>',views.dead,name="dead"),
    path('join/',views.join,name="join"),
    path('willing/',views.willing,name="willing"),
    path('walkins_update/<pk>',views.walkinsupdate,name="walkins_update"),
    path('walkins_delete/<pk>',views.walkinsdelete,name="walkins_delete"),
    path('student_delete/<pk>',views.studentdelete,name="student_delete"),
    path('student_update/<pk>',views.studentupdate,name="student_update"),

]
