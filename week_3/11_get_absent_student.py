all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    # 구현해보세요!
    student_dict = {}
    for key in all_array:
        # 딕셔너리에 모든 학생의 이름 : True를 저장
        student_dict[key] = True

    for key in present_array:
        # 딕셔너리에 저장되어 있는 모든 학생의 이름 : True를 삭제
        del student_dict[key]

    # 딕셔너리에 있는 key값들을 가져옮
    for key in student_dict.keys():
        return key

print(get_absent_student(all_students, present_students))