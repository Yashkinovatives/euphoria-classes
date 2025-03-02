from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class CustomUser(AbstractUser):
    USER_TYPES = (
        ('teacher', 'Teacher'),
        ('parent', 'Parent'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

class ClassSection(models.Model):
    name = models.CharField(max_length=50)  # Example: "5th Standard"
    
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=255)
    class_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE)
    parent = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'parent'})

    def __str__(self):
        return f"{self.name} ({self.class_section})"

class TestResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks_obtained = models.IntegerField()
    total_marks = models.IntegerField()
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'teacher'})

    def __str__(self):
        return f"{self.student.name} - {self.subject}: {self.marks_obtained}/{self.total_marks}"

# Monthly Fee Payment Tracking
class FeePayment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)  # Example: "January 2025"
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'month')  # Ensure no duplicate month payments

    def __str__(self):
        return f"{self.student.name} - {self.month}: {self.amount_paid}"

class FeeRecord(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    total_fees = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Total yearly fee
    remaining_fees = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Remaining fee to be paid

    def __str__(self):
        return f"{self.student.name} - Total: {self.total_fees}, Remaining: {self.remaining_fees}"

# Attendance Tracking
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    class Meta:
        unique_together = ('student', 'date')  # Prevent duplicate attendance records

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"

# Add to your models.py file
class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'teacher'})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title