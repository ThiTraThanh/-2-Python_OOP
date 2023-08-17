#[2] Quản lý sinh viên
import venv
class quan_ly_sinh_vien:
    def __init__(self, name, student_id, courses):
        self.name = name
        self.student_id = student_id
        self.courses = courses
    def Add_courses(self, new_courses): 
        self.courses += new_courses
        self.new_courses = new_courses
    def hien_thi_tt(self):
        print("Name: ", self.name)
        print("Student_id: ", self.student_id)
        print("courses: ", self.courses)
    
courses = ["khoa hoc 1", "khoa hoc 2", "khoa hoc 3"]
a = quan_ly_sinh_vien("Thanh", 1358, courses)
a.hien_thi_tt()
new_courses = ["khoa hoc 4", "khoa hoc 5"]
a.Add_courses(new_courses)
a.hien_thi_tt()

        
