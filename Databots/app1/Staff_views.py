from django.shortcuts import render,redirect,HttpResponse
from app1.models import Cource,Session_Year,CustomUser,Student,Staff,Subject,Staff_Notification,Staff_Leave,Staff_Feedback,Attendence,Attendance_Report
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
@login_required(login_url='/')
def HOME(request):
    return render(request,'Staff/home.html')

@login_required(login_url='/')
def NOTIFICATIONS(request):
    staff = Staff.objects.filter(admin= request.user.id)
    # print(staff)
    for i in staff:
        staff_id = i.id
        notification = Staff_Notification.objects.filter(staff_id= staff_id)
        
        context={
            'notification':notification
        }
        return render(request,'Staff/notifications.html',context)
    # return render(request,'Staff/notifications.html')

@login_required(login_url='/')
def STAFF_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Staff_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('notifications')

@login_required(login_url='/')
def STAFF_APPLY_LEAVE(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id
        
        staf_leave_history = Staff_Leave.objects.filter(staff_id=staff_id)
        context = {
            'staf_leave_history':staf_leave_history
        }
  
        return render(request, 'Staff/apply_leave.html',context)
    return render(request, 'Staff/apply_leave.html')


@login_required(login_url='/')
def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        
        
        staff =Staff.objects.get(admin= request.user.id)
        
        leave = Staff_Leave(
            staff_id=staff,
            date=leave_date,
            message=leave_message,
            
        )
        leave.save()
        messages.success(request,'Leave Successfully Sent !!')
        return redirect('staff_apply_leave')
  
    # return render(request, 'Staff/apply_leave.html')
    
    
def STAFF_FEEDBACK(request):
    staff_id = Staff.objects.get(admin = request.user.id)
    
    feedback_history = Staff_Feedback.objects.filter(staff_id=staff_id)
    
    context = {
        'feedback_history':feedback_history
    }
    return render(request, 'staff/feedback.html',context)

def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        
        staff = Staff.objects.get(admin = request.user.id)
        feedback = Staff_Feedback(
            staff_id=staff,
            feedback=feedback,
            feedback_reply="",

        )                                                                                                                                                                                   
        feedback.save()
        return redirect('staff_feedback')
    # return render(request, 'staff/feedback.html')

@csrf_exempt
def STAFF_TAKE_ATTENDANCE(request):
    staff_id =Staff.objects.get(admin=request.user.id)
    
    
    subject = Subject.objects.filter(staff=staff_id)
    
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')
    
    get_subject = None
    get_session_year = None
    students=None
    
    if action is not None :
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            
            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)
            
            subject = Subject.objects.filter(id=subject_id)
            for i in subject:
                student_id = i.cource.id
                students = Student.objects.filter(cource_id=student_id)
    
    context = {
        'subject':subject,
        'session_year':session_year,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'action':action,
        'students':students
        
    }
    return render(request, 'Staff/take_attendance.html',context)

@csrf_exempt
def STAFF_SAVE_ATTENDANCE(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        attendance_date = request.POST.get('attendance_date')
        student_id = request.POST.getlist('student_id')
        
        get_subject = Subject.objects.get(id=subject_id)
        get_session_year = Session_Year.objects.get(id=session_year_id)
            
        attendance = Attendence(
            subject_id=get_subject,
            attendance_data=attendance_date,
            session_year_id=get_session_year,
            
        )
        attendance.save()
        
        for i in student_id:
            stud_id = i
            int_stud = int(stud_id)
            
            p_students = Student.objects.get(id=int_stud)
            attendance_report = Attendance_Report(
                student_id=p_students,
                attendance_id=attendance,
            )
            attendance_report.save()
            
    return redirect('staff_take_attendance')
        
      
   