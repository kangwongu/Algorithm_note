student_num = int(input())

for i in range(student_num):
    subject_list = list(map(int, input().split())) # 과목 수, 과목 점수 입력
    average = sum(subject_list[1:]) / subject_list[0] # 과목 평균

    # 평균을 넘는 학생 수 구하기
    over_average_student = 0
    for score in subject_list[1:]:
        if score > average:
            over_average_student += 1

    # 평균을 넘는 학생들의 비율 구하기
    ratio = (over_average_student / subject_list[0]) * 100
    print('%.3f%%' %ratio)
    # %는 %%로 표기해야 정상 출력