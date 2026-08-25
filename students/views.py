from django.shortcuts import render,redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

#list student
def student_list(request):
    students= Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

#create / add student
def add_student(request):
    form = StudentForm()
    if request.method =="POST":
        form= StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request, 'students/form.html', {'form': form})
    # Update student
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')

    return render(request, 'students/form.html', {'form': form})

#delete student

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('list')

