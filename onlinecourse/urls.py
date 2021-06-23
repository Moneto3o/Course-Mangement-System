from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='', view=views.CourseListView.as_view(), name='index'),
    path('homework/', view=views.HomeworkView.as_view(), name='homework'),
    path('homework/<int:pk>/', views.HomeworkDetailView.as_view(), name='homework_details'),
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    # ex: /onlinecourse/5/
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    # ex: /enroll/5/
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),
    path('<int:homework_id>/check/', views.check, name='check'),
    #path('show/', views.show, name='show'),
    path('<int:course_id>/submit/', views.submit, name='submit'),
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='result'),
    # <HINT> Create a route for submit view
    path('<int:homework_id>/submithomework/', views.submithomework, name='submithomework'),
    #path('homework/<int:homework_id>/homeworkanswer/<int:homeworkanswer_id>/result/', views.show_homework_result,name='homeworkresult'),
    # <HINT> Create a route for show_exam_result view

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
