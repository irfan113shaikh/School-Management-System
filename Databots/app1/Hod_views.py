from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from app1.models import Cource,Session_Year,CustomUser,Student,Staff,Subject,Staff_Notification,Staff_Leave,Staff_Feedback,Student_Notification,Student_Feedback,Student_Leave
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    cource_count = Cource.objects.all().count()
    subject_count = Subject.objects.all().count()
    
    
    student_gender_male = Student.objects.filter(gender = 'male').count()
    student_gender_female = Student.objects.filter(gender = 'female').count()
    print(student_gender_male,student_gender_female)
    
    context= {
        'student_count': student_count,
        'staff_count': staff_count,
        'cource_count': cource_count,
        'subject_count': subject_count,
        'student_gender_male': student_gender_male,
        'student_gender_female': student_gender_female,
        
    }
    return render(request,'Hod/home.html',context)

@login_required(login_url='/')
def ADD_STUDENT(request):
    cource = Cource.objects.all()
    session_year = Session_Year.objects.all()
    
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        cource_id = request.POST.get('cource_id')
        session_year_id = request.POST.get('session_year_id')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email is already Taken!! ')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username is already Taken!! ')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()
            cource = Cource.objects.get(id = cource_id)
            session_year = Session_Year.objects.get(id = session_year_id)
            
            student = Student(
                admin = user,
                address = address,
                session_year_id = session_year,
                cource_id = cource,
                gender = gender,
            )
            
            student.save()
            messages.success(request,user.first_name + ' ' +user.last_name +  ' Successfully Saved !!! ')
            return redirect('add_student')
            
            
        
        
        
        # print(profile_pic,first_name,last_name,email,username,password,cource_id,session_year_id)
    
    context = {
        'cource':cource,
        'session_year':session_year,
    }
    
    
    
    return render(request,'Hod/add_student.html',context)



@login_required(login_url='/')
def VIEW_STUDENT(request):
    student = Student.objects.all()
    
    context={
        'student':student
    }
    return render(request,'Hod/view_student.html',context)

@login_required(login_url='/')
def EDIT_STUDENT(request,id):
    student = Student.objects.filter(id = id)
    cource = Cource.objects.all()
    session_year = Session_Year.objects.all()
    context = {
        'student':student,
        'cource':cource,
        'session_year':session_year,
    }
    return render(request,'Hod/edit_student.html',context)


@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id =request.POST.get('student_id')
        
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        cource_id = request.POST.get('cource_id')
        session_year_id = request.POST.get('session_year_id')
        
        user =CustomUser.objects.get(id = student_id)
        user.profile_pic = profile_pic
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        
        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()
        
        student = Student.objects.get(admin = student_id)
        student.address = address
        student.gender = gender
        
        cource = Cource.objects.get(id = cource_id)
        student.cource_id = cource
        
        session_year = Session_Year.objects.get(id = session_year_id)
        student.session_year_id = session_year
        
        student.save()
        messages.success(request,'Record Are Successfully Updated !!')
        return redirect('view_student')
        
    return render(request,'Hod/update_student.html')


@login_required(login_url='/')
def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request,'Record Are Successfully Deleted !!')
    return redirect('view_student')

@login_required(login_url='/')
def ADD_COURCE(request):
    if request.method == "POST":
        cource_name = request.POST.get('cource_name')
        
        cource = Cource(
            name = cource_name,
        )
        
        cource.save()
        messages.success(request,'Cource Are Successfully Added !!')
        return redirect('add_cource')
    return render(request,'Hod/add_cource.html')

@login_required(login_url='/')
def VIEW_COURCE(request):
    cource = Cource.objects.all()
    context = {
        'cource':cource,
    }
    return render(request,'Hod/view_cource.html',context)

@login_required(login_url='/') 
def EDIT_COURCE(request,id):
    cource = Cource.objects.get(id = id)
    
    contex={
        'cource':cource
    }
    return render(request,'Hod/edit_cource.html',contex)

@login_required(login_url='/')
def UPDATE_COURCE(request):
    if request.method == "POST":
        name = request.POST.get('name')
        cource_id = request.POST.get('cource_id')     
        cource = Cource.objects.get(id = cource_id)
        cource.name = name
        cource.save()
        messages.success(request,'Cource Are Successfully Updated !!')
        return redirect('view_cource')
    return render(request,'Hod/edit_cource.html')

@login_required(login_url='/')
def DELETE_COURCE(request,id):
    cource = Cource.objects.get(id = id)
    cource.delete()
    messages.success(request,'Cource Are Successfully Deleted !!')
    return redirect('view_cource')

@login_required(login_url='/')
def ADD_STAFF(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email is already Taken!! ')
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username is already Taken!! ')
            return redirect('add_staff')
        else:
            user = CustomUser(first_name = first_name,last_name=last_name,username=username,email=email,profile_pic=profile_pic,user_type=2)
            user.set_password(password)
            user.save()
            
            
        staff = Staff(
            admin = user,
            address = address,
            gender = gender,
            
        )
        staff.save()
        messages.success(request,'Staff are Successfully Added !! ')
        return redirect('add_staff')
    return render(request,'Hod/add_staff.html')

@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Staff.objects.all()
    context = {
        'staff':staff,
    }
    return render(request,'Hod/view_staff.html',context)

@login_required(login_url='/')
def EDIT_STAFF(request,id):
    staff = Staff.objects.get(id = id)
    context = {
        'staff':staff
    }

    return render(request,'Hod/edit_staff.html',context)


@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        
        user = CustomUser.objects.get(id = staff_id)
        user.username =username
        user.first_name =first_name
        user.last_name =last_name
        user.email =email
        
        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
            
        user.save()
        
        staff = Staff.objects.get(admin = staff_id)
        staff.gender = gender
        staff.address = address
        
        staff.save()
        messages.success(request,'Staff is Successfully Updated !! ')
        return redirect('view_staff')
   
    return render(request,'Hod/edit_staff.html')


@login_required(login_url='/')
def DELETE_STAFF(request,admin):
    staff = CustomUser.objects.get(id = admin)
    staff.delete()
    messages.success(request,'Record is Successfully Deleted!! ')
    return redirect('view_staff')
   
   
@login_required(login_url='/')  
def ADD_SUBJECT(request):
    cource = Cource.objects.all()
    staff = Staff.objects.all()
    
    if request.method=="POST":
        subject_name = request.POST.get('subject_name')
        cource_id = request.POST.get('cource_id')
        staff_id = request.POST.get('staff_id')
        
        cource = Cource.objects.get(id = cource_id)
        staff = Staff.objects.get(id = staff_id)
        
        subject = Subject(
            name = subject_name,
            cource = cource,
            staff = staff,
        )
        
        subject.save()
        messages.success(request,'Subject is Successfully Added!! ')
        return redirect('add_subject')
        
    context= {
        'cource':cource,
        'staff':staff,
    }
    return render(request,'Hod/add_subject.html',context)

@login_required(login_url='/')
def VIEW_SUBJECT(request):
    subject = Subject.objects.all()
    context= {
        'subject': subject
    }
    return render(request,'Hod/view_subject.html',context)

@login_required(login_url='/')
def EDIT_SUBJECT(request,id):
    subject = Subject.objects.get(id = id)
    cource = Cource.objects.all()
    staff = Staff.objects.all()
    context = {
           'subject':subject,
           'cource':cource,
           'staff':staff,
    }
    return render(request,'Hod/edit_subject.html',context)

@login_required(login_url='/')
def UPDATE_SUBJECT(request):
    if request.method == "POST":
        subject_id =request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        cource_id = request.POST.get('cource_id')
        staff_id = request.POST.get('staff_id')
        
        cource = Cource.objects.get(id = cource_id)
        staff = Staff.objects.get(id = staff_id)
        
        subject = Subject(
            id = subject_id,
            name = subject_name,
            cource = cource,
            staff = staff,
        )
        subject.save()
        messages.success(request,'Subject are Successfully Updated!! ')
        return redirect('view_subject')
    
    
@login_required(login_url='/')
def DELETE_SUBJECT(request,id):
    subject = Subject.objects.get(id = id)
    subject.delete()
    messages.success(request,'Subject are Successfully Deleted!! ')
    return redirect('view_subject')

@login_required(login_url='/')
def ADD_SESSION(request):
    if request.method == "POST":
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')
        
        session = Session_Year(
            session_start = session_year_start,
            session_end = session_year_end,
        )
        
        session.save()
        messages.success(request,'Session are Successfully Created!! ')
        return redirect('add_session')
    return render(request,'Hod/add_session.html')

@login_required(login_url='/')
def VIEW_SESSION(request):
    session = Session_Year.objects.all()
    context={
        'session':session
    }
    return render(request,'Hod/view_session.html',context)

@login_required(login_url='/')
def EDIT_SESSION(request,id):
    session = Session_Year.objects.filter(id = id)
    context={
        'session':session
    }
    return render(request,'Hod/edit_session.html',context)


@login_required(login_url='/')
def UPDATE_SESSION(request):
    if request.method == "POST":
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')
        
        session = Session_Year(
            id = session_id,
            session_start = session_year_start,
            session_end = session_year_end,
        )
        session.save()
        messages.success(request,'Session are Successfully Updated!! ')
        return redirect('view_session')
    return render(request,'Hod/update_session.html')


@login_required(login_url='/')
def DELETE_SESSION(request,id):
    session = Session_Year.objects.get(id = id)
    session.delete()
    messages.success(request,'Session are Successfully Deleted!! ')
    return redirect('view_session')

@login_required(login_url='/')
def STAFF_SEND_NOTIFICATION(request):
    staff = Staff.objects.all()
    see_notification = Staff_Notification.objects.all().order_by('-id')[0:5]
    context = {
        'staff':staff,
        'see_notification':see_notification,
    }
    return render(request, 'Hod/staff_notification.html',context)

@login_required(login_url='/')
def STAFF_SAVE_NOTIFICATION(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        print(staff_id)
        message = request.POST.get('message')
        
        staff = Staff.objects.get(admin = staff_id)
        notification = Staff_Notification(
            staff_id=staff,
            message= message,
        )
        notification.save()
        messages.success(request,'Notification are Successfully Send !! ')
        return redirect('staff_send_notification')


#Staff apply view function

@login_required(login_url='/')
def STAFF_LEAVE_VIEW(request):
    staff_leave = Staff_Leave.objects.all()
    context = {
        'staff_leave':staff_leave
    }
    return render(request, 'Hod/staff_leave.html',context)

#Student apply view function

def STUDENT_LEAVE_VIEW(request):
    student_leave = Student_Leave.objects.all()
    context = {
        'student_leave':student_leave
    }
    return render(request, 'Hod/student_leave.html',context)

# Staff Approve function
@login_required(login_url='/')
def STAFF_APPROVE_LEAVE(request,id):
    leave = Staff_Leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('staff_leave_view')
    
    # return render(request, 'Hod/staff_leave.html')
    
    
#Student Approve function

def STUDENT_APPROVE_LEAVE(request,id):
    leave = Student_Leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('student_leave_view')
    
    # return render(request, 'Hod/staff_leave.html')

# Staff disapprove function
@login_required(login_url='/')
def STAFF_DISAPPROVE_LEAVE(request,id):
    leave = Staff_Leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('staff_leave_view')

#Student disapprove function
def STUDENT_DISAPPROVE_LEAVE(request,id):
    leave = Student_Leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('student_leave_view')
    
    


    
def STAFF_FEEDBACK(request):
    feedback = Staff_Feedback.objects.all()
    feedback_history = Staff_Feedback.objects.all().order_by('-id')[0:5]
    context ={
        'feedback':feedback,
        'feedback_history':feedback_history,
    }
    
    return render(request, 'Hod/staff_feedback.html',context)





def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')
        
        feedback = Staff_Feedback.objects.get(id = feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        
        return redirect("staff_feedback_reply")
        
  
def STUDENT_SEND_NOTIFICATION(request):
    student = Student.objects.all()
    notification = Student_Notification.objects.all()
    context = {
        'student':student,
        'notification':notification,
    }
    return render(request, 'Hod/student_notification.html',context)

def SAVE_STUDENT_NOTIFICATION(request):
    if request.method == "POST":
        message = request.POST.get('message')
        student_id = request.POST.get('student_id')
        
        
        student = Student.objects.get(admin = student_id)
        stud_notifications = Student_Notification(
            student_id= student,
            message= message,
        )
        stud_notifications.save()
        messages.success(request,'Student Notification are Successfully sent !! ')
        return redirect('student_send_notification')
    
def STUDENT_FEEDBACK(request):
    feedback = Student_Feedback.objects.all()
    feedback_history = Student_Feedback.objects.all().order_by('-id')[0:5]
    context ={
        'feedback':feedback,
        'feedback_history':feedback_history,
    }
    
    return render(request, 'Hod/student_feedback.html',context)

        
def REPLY_STUDENT_FEEDBACK(request):
    if request.method == "POST":
        feedback_id =request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')
        
        feedback = Student_Feedback.objects.get(id = feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        return redirect('get_student_feedback')
    return None
    
    
    
    
    
