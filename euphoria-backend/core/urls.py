from django.urls import path
from core.views import (
    signup, login, teacher_dashboard, parent_dashboard,
    enroll_student, add_test_result, get_student_results, get_students,
    get_class_sections, add_monthly_fee, get_monthly_fee_status, set_total_fees, mark_attendance, update_attendance,
    get_student_attendance, add_notice, get_notices, delete_notice, update_notice, get_reviews, add_review, delete_review,
    upload_student_result, get_uploaded_results, get_uploaded_result_details, delete_uploaded_result,verify_teacher_code,get_student_attendance_history,
    get_student_fees_history,delete_uploaded_result_by_teacher,get_parent_uploaded_results,bulk_mark_attendance
)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path("verify-teacher/", verify_teacher_code, name="verify_teacher_code"),
    path('teacher-dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('parent-dashboard/', parent_dashboard, name='parent_dashboard'),
    path('parent/enroll-student/', enroll_student, name='enroll_student'),
    path('test-results/add/', add_test_result, name='add_test_result'),
    path('students/', get_students, name='get_students'),
    path('class-sections/', get_class_sections, name='get_class_sections'),
    path('parent/test-results/', get_student_results, name='get_student_results'),
    path('teacher/set-total-fees/', set_total_fees, name='set_total_fees'),
    path('teacher/add-monthly-fee/', add_monthly_fee, name='add_monthly_fee'),
    path('parent/monthly-fee-status/', get_monthly_fee_status, name='get_monthly_fee_status'),
    path('teacher/mark-attendance/', mark_attendance, name='mark_attendance'),
    path('teacher/update-attendance/', update_attendance, name='update_attendance'),
    path('parent/student-attendance/', get_student_attendance, name='get_student_attendance'),
    path('teacher/add-notice/', add_notice, name='add_notice'),
    path('notices/', get_notices, name='get_notices'),
    path('teacher/delete-notice/<int:notice_id>/', delete_notice, name='delete_notice'),
    path('teacher/update-notice/<int:notice_id>/', update_notice, name='update_notice'),
    path('reviews/', get_reviews, name='get_reviews'),
    path('reviews/add/', add_review, name='add_review'),
    path('teacher/delete-review/<int:review_id>/', delete_review, name='delete_review'),
    path('parent/upload-result/', upload_student_result, name='upload_student_result'),

    # Teacher View Results
    path('teacher/view-results/', get_uploaded_results, name='get_uploaded_results'),
    path('teacher/view-result/<int:semester_id>/', get_uploaded_result_details, name='get_uploaded_result_details'),

    # Parent Delete Results
    path('parent/delete-result/<int:semester_id>/', delete_uploaded_result, name='delete_uploaded_result'),

    path('teacher/student-attendance/<int:student_id>/', get_student_attendance_history, name='get_student_attendance_history'),
    path('teacher/student-fees/<int:student_id>/', get_student_fees_history, name='get_student_fees_history'),
    path('teacher/delete-result/<int:semester_id>/', delete_uploaded_result_by_teacher, name='delete_uploaded_result_by_teacher'),

    path('parent/view-uploaded-results/', get_parent_uploaded_results, name='get_parent_uploaded_results'),
    path("teacher/bulk-mark-attendance/", bulk_mark_attendance, name="bulk_mark_attendance"),


]
