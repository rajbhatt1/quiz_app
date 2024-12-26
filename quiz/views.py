from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.http import HttpResponse


# Create your views here.
# def home(request, category_id):
#     try:
#         category = Quiz.objects.get(id=category_id)
#     except Quiz.DoesNotExist:
#         # Handle the case where the category does not exist
#         return render(request, 'Quiz/home.html', {'error': 'Category not found'})
#     questions = QuesModel.objects.filter(category=category)
#     correct=0
#     total=0
#     if request.method == 'POST':
#         print(request.POST)
        
        
#         for q in questions:
#             total+=1
#             ans = request.POST.get(str(q.id))
#             print(q.ans)
#             print()
#             if ans == str(q.op):
#                 correct+=1
            
                
        
#         context = {
#             'user': request.user.username,
#             'correct':correct,
#             'total':total
#         }
#         return render(request,'Quiz/home.html',context)
#     else:
#         questions=QuesModel.objects.all()
#         context = {
#             'questions':questions
#         }
#         return render(request,'Quiz/home.html',context)

def home(request, category_id):
    # Get questions based on category_id
    user = request.user
    category = category1.objects.get(id=category_id)
    if request.method == 'POST':
        form = QuizForm(request.POST, category_id=category_id)
        if form.is_valid():
            # Calculate score
            correct = 0
            total = 0
            for question in QuesModel.objects.filter(category_id=category_id):
                total += 1
                selected_answer = form.cleaned_data.get(f'question_{question.id}')
                if selected_answer == question.ans:
                    correct += 1

            obj = Quizhistory.objects.create(category = category,score = correct, user = user)

            context = {
                'time': request.POST.get('timer'),
                'score': correct,
                'total': total,
                'quiz': category1.objects.get(id=category_id)
            }
            return render(request, 'quiz/home.html', context)
    else:
        form = QuizForm(category_id=category_id)

    return render(request, 'quiz/home.html', {'form': form})

def categoryview(request):
    if request.user.is_staff:
        if(request.method=='POST'):
            form=categoryform(request.POST)
            if form.is_valid():
                form.save()
                return redirect('category')
        else:
            form=categoryform
        context={'form':form}
        return render(request,'Quiz/addQuestion.html',context)

def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('addQuestion')
        context={'form':form}
        return render(request,'Quiz/addQuestion.html',context)
    
def select_Quizview(request):
    categories = category1.objects.all()
    if request.method == 'POST':
        category_id = request.POST.get('category')
        if category_id:
            # Redirect to the 'home' view with the selected category_id
            return redirect('home', category_id=category_id)
        return redirect('home')
    return render(request,'Quiz/select_Quiz.html',{'categories':categories})

@login_required
def user_details(request):
    user = request.user
    taken_quiz = Quizhistory.objects.filter(user=user)
    total_attempts = taken_quiz.count()
    context = {'total_attempts':total_attempts, 'take_quiz':taken_quiz}
    return render(request,'quiz/userdetails.html',context)

def quiz_history(request):
    # if request.user.is_staff and request.user.is_authenticated:  
        taken_quiz = Quizhistory.objects.all()
        # print('Data:',taken_quiz)
        context = {'take_quiz':taken_quiz}
        return render(request,'quiz/userdata.html',context)








