from django.urls import path
from . import views

urlpatterns = [
    
    path('home/<int:category_id>/',views.home,name='home'),
    path('addQuestion/',views.addQuestion,name='addQuestion'),
    path('category/',views.categoryview,name='category'),
    path('select_quiz/',views.select_Quizview,name='select_quiz'),
    path('user_details/',views.user_details,name='user_details'),
    path('user_data/',views.quiz_history,name='user_data'),
    
    

    
]
