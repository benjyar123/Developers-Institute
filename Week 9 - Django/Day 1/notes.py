def add(request):
    if request.method == "GET":
        return render(request, 'classroom/add.html', {'form': StudentForm()})
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("Student Saved!")
from django.views import View
class StudentAdd(View):
    def get(self, request):
        return render(request, 'classroom/add.html', {'form': StudentForm()})
    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Student Saved!") (edited) 