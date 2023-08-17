#[1] Quản lý sách
class quan_ly_sach:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
    def hien_thi_thong_tin(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Publication year: ", self.publication_year)

qlsach = quan_ly_sach("Đất rừng Phương Nam", "Đoàn Giỏi", 1945)
qlsach.hien_thi_thong_tin()

