
students = []
def add_student():
    student_id = input("Nhập mã sinh viên: ")
    student_name = input("Nhập tên sinh viên: ")
    student = {"Mã SV": student_id, "Tên SV": student_name}
    students.append(student)
    print("Sinh viên đã được thêm thành công.")

def delete_student():
    student_id = input("Nhập mã sinh viên để xóa: ")
    for student in students:
        if student["Mã SV"] == student_id:
            students.remove(student)
            print("Sinh viên đã được xóa thành công.")
            return
    print("Không tìm thấy sinh viên có mã", student_id)

def edit_student():
    student_id = input("Nhập mã sinh viên để sửa thông tin: ")
    for student in students:
        if student["Mã SV"] == student_id:
            new_name = input("Nhập tên mới cho sinh viên: ")
            student["Tên SV"] = new_name
            print("Thông tin của sinh viên đã được cập nhật thành công.")
            return
    print("Không tìm thấy sinh viên có mã", student_id)

def view_students():
    print("Danh sách sinh viên:")
    for student in students:
        print("Mã SV:", student["Mã SV"])
        print("Tên SV:", student["Tên SV"])
        print("-----------")

while True:
    print("Chọn chức năng:")
    print("1: Thêm sinh viên")
    print("2: Xóa sinh viên")
    print("3: Sửa sinh viên")
    print("4: Xem danh sách sinh viên")
    choice = input("Nhập lựa chọn (hoặc 'exit' để thoát): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        delete_student()
    elif choice == "3":
        edit_student()
    elif choice == "4":
        view_students()
    elif choice.lower() == "exit":
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")