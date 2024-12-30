from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from student.models import Student
from django.urls import reverse_lazy

# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_form.html'
    fields = ['first_name', 'last_name', 'middle_name', 'email', 'sex', 'phone_number', 'address']
    success_url = reverse_lazy('student_create')

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'middle_name', 'email', 'sex', 'phone_number', 'address']
    template_name = 'student_form.html'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'

