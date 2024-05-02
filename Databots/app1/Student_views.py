from django.shortcuts import render,redirect,HttpResponse
from app1.models import Cource,Session_Year,CustomUser,Student,Staff,Subject,Staff_Notification,Staff_Leave,Staff_Feedback,Student_Feedback,Student_Leave
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app1.models import Student_Notification,Student
from app1.models import Student_Feedback,CustomUser,Student                                                                                                          


def HOME(request):
    return render(request,'Student/home.html')

def STUDENT_NOTIFICATION(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id= i.id
        # student_id = student_instance.cource_id
        notification = Student_Notification.objects.filter(student_id=student_id)
        
        context = {
            'notification': notification,
        }
        return render(request, 'Student/notification.html', context)

def STUDENT_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Student_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('student_notification')



def STUDENT_FEEDBACK(request):
    student_id= Student.objects.get(admin=request.user.id)

    feedback_history = Student_Feedback.objects.filter(student_id=student_id)

    context = {
        'feedback_history': feedback_history
    }
    return render(request, 'Student/feedback.html', context)

def STUDENT_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        
        student = Student.objects.get(admin = request.user.id)
        feedback = Student_Feedback(
            student_id=student,
            feedback=feedback,
            feedback_reply="",

        )                                                                                                                                                                                   
        feedback.save()
        return redirect('student_feedback')


def STUDENT_LEAVE(request):
    student = Student.objects.get(admin=request.user.id)
        
    student_leave_history = Student_Leave.objects.filter(student_id=student)
    context = {
            'student_leave_history':student_leave_history
        }
  
    return render(request, 'Student/apply_leave.html',context)
    # return render(request, 'Student/apply_leave.html')
    # return render(request, 'Student/apply_leave.html')

def STUDENT_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        
        student_id = Student.objects.get(admin = request.user.id)
        
        student_leave = Student_Leave(
            student_id=student_id,
            date =leave_date,
            message=leave_message,
        )
        student_leave.save()
        messages.success(request,'Leave Are Successfully Sent !!')
        return redirect('student_leave')
        
  
