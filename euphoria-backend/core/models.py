from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class CustomUser(AbstractUser):
    USER_TYPES = (
        ('teacher', 'Teacher'),
        ('parent', 'Parent'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)


# Class Section Model
class ClassSection(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Student Model
class Student(models.Model):
    name = models.CharField(max_length=255)
    class_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE)
    parent = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'parent'})

    def __str__(self):
        return f"{self.name} ({self.class_section})"


# ✅ Parent Uploaded Semester Model (For Semester-Wise Results)
class ParentUploadedSemester(models.Model):
    SEMESTER_CHOICES = [
        ('Semester 1', 'Semester 1'),
        ('Semester 2', 'Semester 2'),
        ('Annual', 'Annual'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="uploaded_semesters")
    semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES)
    year = models.PositiveIntegerField()  # Ensuring only positive values
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'parent'})
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.semester} ({self.year})"


# ✅ Parent Uploaded Subject Result Model (Each Subject for a Semester)
class ParentUploadedSubjectResult(models.Model):
    semester = models.ForeignKey(ParentUploadedSemester, on_delete=models.CASCADE, related_name="subject_results")
    subject = models.CharField(max_length=100)
    marks_obtained = models.PositiveIntegerField()  # Prevents negative values
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.semester.student.name} - {self.subject}: {self.marks_obtained}/{self.total_marks}"


# ✅ Parent Uploaded Result Document (Optional PDF Upload)
class ParentUploadedResult(models.Model):
    semester = models.ForeignKey(ParentUploadedSemester, on_delete=models.CASCADE, related_name="uploaded_documents")
    document = models.FileField(upload_to="parent_uploaded_results/", blank=True, null=True)  # Optional file upload
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for {self.semester.student.name} - {self.semester.semester} ({self.semester.year})"


# ✅ Test Result Model (Teacher Uploaded Test Results)
class TestResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks_obtained = models.IntegerField()
    total_marks = models.IntegerField()
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'teacher'})

    def __str__(self):
        return f"{self.student.name} - {self.subject}: {self.marks_obtained}/{self.total_marks}"


# ✅ Fee Payment Model (Tracks Monthly Fee Payments)
class FeePayment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'month')

    def __str__(self):
        return f"{self.student.name} - {self.month}: {self.amount_paid}"


# ✅ Fee Record Model (Tracks Total and Remaining Fees)
class FeeRecord(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    total_fees = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    remaining_fees = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.student.name} - Total: {self.total_fees}, Remaining: {self.remaining_fees}"


# ✅ Attendance Model (Tracks Student Attendance)
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"


# ✅ Notice Model (Posted by Teachers)
class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'teacher'})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# ✅ Review Model (Parent or Public Reviews)
class Review(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100, blank=True, null=True)
    review = models.TextField()
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name} - {self.created_at.strftime('%Y-%m-%d')}"
