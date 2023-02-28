from django.shortcuts import render, get_object_or_404
from .models import Student, Group

from django.db.models import Q, F, Count

from icecream import ic


# Create your views here.


def students_view(request, pk=None) -> render:
    template_ = "students_all.html"
    if pk:
        template_ = "student_detail.html"
        student = get_object_or_404(Student, pk=pk)
        context = {"student": student}
    else:
        groups = Group.objects.all()
        students = Student.objects.select_related("group").all

        max_cols = 0

        for group_item in groups:
            students_len = len(Student.objects.select_related('group').filter(Q(group=group_item.pk)))

            if max_cols < students_len:
                max_cols = students_len

        context = {
            "students": students,
            "groups": groups,
            "max_cols": max_cols,
        }
    return render(request=request, template_name=template_, context=context)
