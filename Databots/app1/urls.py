# from django.contrib import admin
from django.urls import path 
from . import views,Hod_views,Staff_views,Student_views

# from django.conf import settings
# from django.conf.urls.static  import static      
# from .import views,Hod_views,Staff_views,Student_views
urlpatterns = [
    path('base',views.BASE, name='base'),
    
    #login
    path('',views.LOGIN, name='login'),
    path('dologin/',views.doLogin, name='doLogin'),
    path('dologout/',views.doLogout, name='logout'),
    
    #Profile update
    path('profile',views.PROFILE, name='profile'),
    path('profile/update',views.PROFILE_UPDATE, name='profile_update'),
    
    #Hod panel url
    
    path('Hod/home',Hod_views.HOME, name='Hod_home'),
    path('Hod/Student/add',Hod_views.ADD_STUDENT, name='add_student'),
    path('Hod/Student/view',Hod_views.VIEW_STUDENT, name='view_student'),
    path('Hod/Student/edit/<str:id>',Hod_views.EDIT_STUDENT, name='edit_student'),
    path('Hod/Student/update/',Hod_views.UPDATE_STUDENT, name='update_student'),
    path('Hod/Student/delete/<str:admin>',Hod_views.DELETE_STUDENT, name='delete_student'),
    
    path('Hod/Staff/add',Hod_views.ADD_STAFF, name='add_staff'),
    path('Hod/Staff/view',Hod_views.VIEW_STAFF, name='view_staff'),
    path('Hod/Staff/edit/<str:id>',Hod_views.EDIT_STAFF, name='edit_staff'),
    path('Hod/Staff/update/',Hod_views.UPDATE_STAFF, name='update_staff'),
    path('Hod/Staff/delete/<str:admin>',Hod_views.DELETE_STAFF, name='delete_staff'),
    
    path('Hod/Cource/add',Hod_views.ADD_COURCE, name='add_cource'),
    path('Hod/Cource/view',Hod_views.VIEW_COURCE, name='view_cource'),
    path('Hod/Cource/edit/<str:id>',Hod_views.EDIT_COURCE, name='edit_cource'),
    path('Hod/Cource/update',Hod_views.UPDATE_COURCE, name='update_cource'),
    path('Hod/Cource/delete/<str:id>',Hod_views.DELETE_COURCE, name='delete_cource'),
    
    
    path('Hod/Subject/add',Hod_views.ADD_SUBJECT, name='add_subject'),
    path('Hod/Subject/view',Hod_views.VIEW_SUBJECT, name='view_subject'),
    path('Hod/Subject/edit/<str:id>',Hod_views.EDIT_SUBJECT, name='edit_subject'),
    path('Hod/Subject/update',Hod_views.UPDATE_SUBJECT, name='update_subject'),
    path('Hod/Subject/delete/<str:id>',Hod_views.DELETE_SUBJECT, name='delete_subject'),
    
    
    path('Hod/Session/add',Hod_views.ADD_SESSION, name='add_session'),
    path('Hod/Session/view',Hod_views.VIEW_SESSION, name='view_session'),
    path('Hod/Session/edit/<str:id>',Hod_views.EDIT_SESSION, name='edit_session'),
    path('Hod/Session/update',Hod_views.UPDATE_SESSION, name='update_session'),
    path('Hod/Session/delete/<str:id>',Hod_views.DELETE_SESSION, name='delete_session'),
    
    
    path('Hod/Staff/Send_Notification',Hod_views.STAFF_SEND_NOTIFICATION, name='staff_send_notification'),
    path('Hod/Staff/Save_Notification',Hod_views.STAFF_SAVE_NOTIFICATION, name='save_staff_notification'),
    
    
    
    path('Hod/Student/Send_Notification',Hod_views.STUDENT_SEND_NOTIFICATION, name='student_send_notification'),
    path('Hod/Student/Save_Notification',Hod_views.SAVE_STUDENT_NOTIFICATION, name='save_student_notification'),
    
    
    path('Hod/Staff/Leave_view',Hod_views.STAFF_LEAVE_VIEW, name='staff_leave_view'),
    path('Hod/Staff/Approve_leave/<str:id>',Hod_views.STAFF_APPROVE_LEAVE, name='staff_approve_leave'),
    path('Hod/Staff/Disapprove_leave/<str:id>',Hod_views.STAFF_DISAPPROVE_LEAVE, name='staff_disapprove_leave'),
    
    path('Hod/Student/Leave_view',Hod_views.STUDENT_LEAVE_VIEW, name='student_leave_view'),
    path('Hod/Student/Approve_leave/<str:id>',Hod_views.STUDENT_APPROVE_LEAVE, name='student_approve_leave'),
    path('Hod/Student/Disapprove_leave/<str:id>',Hod_views.STUDENT_DISAPPROVE_LEAVE, name='student_disapprove_leave'),
    
    
    path('Hod/Staff/feedback',Hod_views.STAFF_FEEDBACK, name='staff_feedback_reply'),
    path('Hod/Staff/feedback/save',Hod_views.STAFF_FEEDBACK_SAVE, name='staff_feedback_reply_save'),
    
    
    
    
    
    path('Hod/Student/feedback',Hod_views.STUDENT_FEEDBACK, name='get_student_feedback'),
    path('Hod/Student/feedback/reply/save',Hod_views.REPLY_STUDENT_FEEDBACK, name='reply_student_feedback'),
    # This is a Staff panel url
    path('Staff/home',Staff_views.HOME, name='staff_home'),
    
    
    path('Staff/Notifications',Staff_views.NOTIFICATIONS, name='notifications'),
    path('Staff/mark_as_done/<str:status>',Staff_views.STAFF_NOTIFICATION_MARK_AS_DONE, name='staff_notification_mark_as_done'),
    path('Staff/Apply_leave',Staff_views.STAFF_APPLY_LEAVE, name='staff_apply_leave'),
    path('Staff/Apply_leave_save',Staff_views.STAFF_APPLY_LEAVE_SAVE, name='staff_apply_leave_save'),

    path('Staff/Feedback',Staff_views.STAFF_FEEDBACK, name='staff_feedback'),
    path('Staff/Feedback/Save',Staff_views.STAFF_FEEDBACK_SAVE, name='staff_feedback_save'),

    path('Staff/Take_Attendance',Staff_views.STAFF_TAKE_ATTENDANCE, name='staff_take_attendance'),
    path('Staff/Save_Attendance',Staff_views.STAFF_SAVE_ATTENDANCE, name='staff_save_attendance'),
    
    
    # This is a Student panel url   
    path('Student/home',Student_views.HOME, name='student_home'),
    path('Student/Notifications',Student_views.STUDENT_NOTIFICATION,name='student_notification'),
    path('Student/mark_as_done/<str:status>',Student_views.STUDENT_NOTIFICATION_MARK_AS_DONE, name='student_notification_mark_as_done'),
    path('Student/Feedback',Student_views.STUDENT_FEEDBACK, name='student_feedback'),
    path('Student/Feedback/Save',Student_views.STUDENT_FEEDBACK_SAVE, name='student_feedback_save'),


    path('Student/apply_for_leave',Student_views.STUDENT_LEAVE, name='student_leave'),
    path('Student/leave_save',Student_views.STUDENT_LEAVE_SAVE, name='student_leave_save'),
    
    
    
]