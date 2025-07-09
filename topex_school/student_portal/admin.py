from django.contrib import admin
from .models import (
    StudentProfile, FeeStructure, BillingStatement,
    Payment, SemesterRegistration, Transcript
)

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_id', 'phone', 'emergency_contact_name')
    search_fields = ('user__username', 'student_id')

@admin.register(FeeStructure)
class FeeStructureAdmin(admin.ModelAdmin):
    list_display = ('program', 'semester', 'amount')
    search_fields = ('program', 'semester')

@admin.register(BillingStatement)
class BillingStatementAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'amount_due', 'is_paid')
    list_filter = ('is_paid',)
    search_fields = ('student__username',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount', 'payment_date', 'receipt_number')
    search_fields = ('student__username', 'receipt_number')

@admin.register(SemesterRegistration)
class SemesterRegistrationAdmin(admin.ModelAdmin):
    list_display = ('student', 'semester', 'registered_on')
    search_fields = ('student__username', 'semester')

@admin.register(Transcript)
class TranscriptAdmin(admin.ModelAdmin):
    list_display = ('student', 'unit', 'grade', 'semester')
    search_fields = ('student__username', 'unit', 'semester')
