from django import forms
from .models import Course


class EnrollCourseForm(forms.Form):
    course_code = forms.CharField(max_length=20)

    def clean_course_code(self):
        code = self.cleaned_data['course_code'].strip().upper()
        if Course.objects.filter(code=code).exists():
            return code
        else:
            raise forms.ValidationError(
                "That is not a valid course (or we just don't have it in our database). Please also ensure your format is correct, Ex: Econ 2010")
