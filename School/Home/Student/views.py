from django.shortcuts import render
from django.db.models import Max
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404,redirect
from .models import Parent, Student,City, Department, Landrecord
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.db import connection
import oracledb

# from django.http import HttpResponse
from django.db import connection

def test_db(request):
    # import oracledb
    # oracledb.init_oracle_client(lib_dir=r"C:\path\to\instantclient_19_19")

 try:
        conn = oracledb.connect(
            user="scott",
            password="tiger",
            dsn="127.0.0.1:1521/xepdb1"  # Use your actual DSN here
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM emp")
        rows = cursor.fetchall()
        return JsonResponse({"status": "ok", "data": rows})
 except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})

    # try:
    #     with connection.cursor() as cursor:
    #         cursor.execute("SELECT * FROM scott.dept")
    #         rows = cursor.fetchall()
    #     return HttpResponse(f"✅ Django connection successful!<br>Rows: {rows}")
    # except Exception as e:
    #     return HttpResponse(f"❌ Django connection failed:<br>{str(e)}")


# def show_employees(request):
#     try:
#         emps = Emp.objects.all()
#         output = "<h2>Employees List:</h2><ul>"
#         for emp in emps:
#             output += f"<li>{emp.empno} - {emp.ename} - {emp.job} - {emp.sal}</li>"
#         output += "</ul>"
#         return HttpResponse(output)
#     except Exception as e:
#         return HttpResponse(f"❌ Error: {str(e)}")
def add_city(request):
       if request.method == 'POST':
         city_name = request.POST.get('city_name')
         max_code = City.objects.aggregate(Max('CITYCODE'))['CITYCODE__max']
         next_city_code = (max_code or 0) + 1
        # Save the city information
         city = City.objects.create(
            CITYCODE=next_city_code,
            CITYNAME=city_name
        )
         city.save()
         messages.success(request, "City added Successfully")
         return redirect('add_city')  # Make sure 'add_city' is the correct name in urls.py
       return render(request, 'students/add-city.html')
def add_department(request):
    
       if request.method == 'POST':
         department_name = request.POST.get('department_name')
         max_code = Department.objects.aggregate(Max('DEPARTMENTID'))['DEPARTMENTID__max']
         next_dept_code = (max_code or 0) + 1
        # Save the city information
         department = Department.objects.create(
            DEPARTMENTID=next_dept_code,
            DEPARTMENTNAME=department_name
        )
         department.save()
         messages.success(request, "department added Successfully")
         return redirect('add_department')  # Make sure 'add_city' is the correct name in urls.py
       return render(request, 'students/add-department.html')
def add_landrecord(request):
    cities = City.objects.all()
    departments = Department.objects.all()
    print('landrecord is called')
    if request.method == 'POST':
        # Handle form submission logic here
        max_code = Landrecord.objects.aggregate(Max('LANDRECORDNO'))['LANDRECORDNO__max']
        next_record_code = (max_code or 0) + 1
        land_name = request.POST.get('land_name')
        department_id = request.POST.get('department_id')
        city_code = request.POST.get('city_code')
        acquired_date = request.POST.get('date_of_acquire')
        comm_date = request.POST.get('date_of_comm')
        acq_acr = request.POST.get('acq_acr')
        acq_kanal = request.POST.get('acq_kanal')
        acq_marla = request.POST.get('acq_marla')
        to_be_acq_acr = request.POST.get('to_be_acq_acr')
        to_be_acq_kanal = request.POST.get('to_be_acq_kanal')
        to_be_acq_marla = request.POST.get('to_be_acq_marla')
        remarks = request.POST.get('remarks')
        picture = request.FILES.get('land_image')
        print(f"to_be_acq_acr {to_be_acq_acr} to_be_acq_kanal {to_be_acq_kanal} to_be_acq_marla {to_be_acq_marla}")

         # Save land record information
        land_record = Landrecord.objects.create(
            LANDRECORDNO=next_record_code,
            LANDNAME=land_name,
            DEPARTMENTID=Department.objects.get(DEPARTMENTID=department_id),
            CITYCODE=City.objects.get(CITYCODE=city_code),
            AQURIEDATE=acquired_date,
            COMMDATE=comm_date,
            ACQACR=acq_acr,
            ACQKANAL=acq_kanal,
            ACQMARLA=acq_marla,
            TOBEACQACR=to_be_acq_acr,
            TOBEACQKANAL=to_be_acq_kanal,
            TOBEACQMARLA=to_be_acq_marla,
            REMARKS=remarks,
            PICTURE=picture
        )
        
        messages.success(request, "Land record added Successfully")
    return render(request, 'students/add-landrecord.html', {'cities': cities,'departments': departments})
def add_student(request):
    if request.method == 'POST':
        # Handle form submission logic here
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        student_class = request.POST.get('student_class')
        religion = request.POST.get('religion')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')   
        student_image = request.FILES.get('student_image')

         # Retrieve parent data from the form
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        father_email = request.POST.get('father_email')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        mother_mobile = request.POST.get('mother_mobile')
        mother_email = request.POST.get('mother_email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')

         # save parent information
        parent = Parent.objects.create(
            father_name= father_name,
            father_occupation= father_occupation,
            father_mobile= father_mobile,
            father_email= father_email,
            mother_name= mother_name,
            mother_occupation= mother_occupation,
            mother_mobile= mother_mobile,
            mother_email= mother_email,
            present_address= present_address,
            permanent_address= permanent_address
        )

         # Save student information
        student = Student.objects.create(
            first_name= first_name,
            last_name= last_name,
            student_id= student_id,
            gender= gender,
            date_of_birth= date_of_birth,
            student_class= student_class,
            religion= religion,
            joining_date= joining_date,
            mobile_number = mobile_number,
            admission_number = admission_number,
            section = section,
            student_image = student_image,
            parent = parent
        )
        
        messages.success(request, "Student added Successfully")
    return render(request, 'students/add-student.html')


def student_list(request):
    
    student_list = Student.objects.select_related('parent').all()
   # unread_notification = request.user.notification_set.filter(is_read=False)
    context = {
        'student_list': student_list#
    }
    return render(request, "students/students.html", context)
    return render(request, 'students/students.html')
def view_student(request, slug):
    student = get_object_or_404(Student, student_id = slug)
    context = {
        'student': student
    }
    return render(request, "students/student-details.html", context)
def edit_student(request,slug):
    student = get_object_or_404(Student, slug=slug)
    parent = student.parent if hasattr(student, 'parent') else None

    
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        print('first name  ' + first_name)

        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        student_class = request.POST.get('student_class')
        religion = request.POST.get('religion')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')
        student_image = request.FILES.get('student_image')  if request.FILES.get('student_image') else student.student_image

        # Retrieve parent data from the form
        parent.father_name = request.POST.get('father_name')
        parent.father_occupation = request.POST.get('father_occupation')
        parent.father_mobile = request.POST.get('father_mobile')
        parent.father_email = request.POST.get('father_email')
        parent.mother_name = request.POST.get('mother_name')
        parent.mother_occupation = request.POST.get('mother_occupation')
        parent.mother_mobile = request.POST.get('mother_mobile')
        parent.mother_email = request.POST.get('mother_email')
        parent.present_address = request.POST.get('present_address')
        parent.permanent_address = request.POST.get('permanent_address')
        parent.save()

#  update student information

        student.first_name= first_name
        student.last_name= last_name
        student.student_id= student_id
        student.gender= gender
        student.date_of_birth= date_of_birth
        student.student_class= student_class
        student.religion= religion
        student.joining_date= joining_date
        student.mobile_number = mobile_number
        student.admission_number = admission_number
        student.section = section
        student.student_image = student_image
        student.save()
        #create_notification(request.user, f"Added Student: {student.first_name} {student.last_name}")
        
        return redirect("student_list")
    return render(request, "students/edit-student.html",{'student':student, 'parent':parent} )
def delete_student(request,slug):
    if request.method == "POST":
        student = get_object_or_404(Student, slug=slug)
        student_name = f"{student.first_name} {student.last_name}"
        student.delete()
        #create_notification(request.user, f"Deleted student: {student_name}")
        return redirect ('student_list')
    return HttpResponseForbidden()
def student_details(request):
    return render(request, 'students/student-details.html')