from django.db import models

# Create your models here.
class Result(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE)
    classroom = models.ForeignKey('classrooms.Classroom', on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    remarks = models.TextField(blank=True, null=True)
    term = models.IntegerField()
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        unique_together = ('student', 'subject', 'term', 'year')

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} ({self.year})"

