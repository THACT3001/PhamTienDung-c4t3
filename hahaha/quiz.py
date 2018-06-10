# lua_chon = {
#     "question": "A hoc TK co truyen thong code dem. A code dem co dung hay khong?",
#     "choices": ["A. Co", "B. Khong"],
#     "right_choice": "A"
# }
question_pack = [
    #1
    {
        "question": "Do you recognize your teacher?",
        "choices": ["A. Co", "B. Khong"],
        "right_choice": "A"
    },
    #2
    {
        "question": "Co di muon khong?",
        "choices": ["A. Co", "B. Khong"],
        "right_choice": "A"
    },
    #3
    {
        "question": "Tro giang co dep trai khong?",
        "choices": ["A. Co", "B. Khong"],
        "right_choice": "A"
    }
]

correct_answer_count = 0

for lua_chon in question_pack:

    print(lua_chon["question"])
    print()
    for choice in lua_chon["choices"]:
        print(choice)

    while True:
        tra_loi = input("Answer?").upper()
        if tra_loi == lua_chon["right_choice"]:
            print("Bingo")
            correct_answer_count = correct_answer_count + 1
            break
        else:
            print("Meh")
# print(question_pack[-1]["choices"][1])

print("So cau hoi ban da tra loi dung la: ", correct_answer_count)
print("Phan tram tra loi dung la: ", 100*correct_answer_count/len(question_pack), "%")