#[2] Quản lý sinh viên
import venv
class quan_ly_sinh_vien:
    def __init__(self, name, student_id, courses):
        self.name = name
        self.student_id = student_id
        self.courses = courses
    def Add_courses(self, n):
        for i in range(n):
            courses.append(input())
        self.courses = courses
    def hien_thi_tt(self):
        print("Name: ", self.name)
        print("Student_id: ", self.student_id)
        print("courses: ", self.courses)
print("Nhap so luong khoa hoc: ")   
n = int(input())
courses = list()
print("Nhap ten khoa hoc")
for i in range(n):
    courses.append(input())
a = quan_ly_sinh_vien("Thanh", 1358, courses)
a.hien_thi_tt()
print("Nhap so luong khoa hoc muon them")
x = int(input())
a.Add_courses(x)
a.hien_thi_tt()

        
