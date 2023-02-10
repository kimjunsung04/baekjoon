import requests
import os


def get_solvedac_data(user_id: str, page: int = 1) -> dict:
    return requests.get(
        f"https://solved.ac/api/v3/search/problem?query=solved_by:{user_id}&page={page}&sort=level&direction=desc"
    ).json()


def get_solvedac_data_all(user_id: str) -> dict:
    all_probles = []
    temp_data = get_solvedac_data(user_id=user_id, page=1)
    if temp_data["count"] > 50:
        all_probles.extend(temp_data["items"])
        if temp_data["count"] // 50 == 0 and temp_data["count"] % 50 != 0:
            loop_val = temp_data["count"] // 50 + 1
        else:
            loop_val = temp_data["count"] // 50
        for page in range(2, loop_val + 2):
            all_probles.extend(get_solvedac_data(user_id=user_id, page=page)["items"])
    return all_probles


def get_local_data(path: str) -> list:
    local_file_datas = []
    black_list_file = ["missing_detecter.py"]
    white_list_ext = ["py", "cpp", "java", "gs", "ada"]
    black_list_folder = [".git", ".idea"]
    for root, _, files in os.walk(path):
        local_file_datas.extend(
            int(file.split(".")[0].replace("(PyPy3)", ""))
            for file in files
            if (
                file.split(".")[-1] in white_list_ext
                and root.split("\\")[-1] not in black_list_folder
                and file not in black_list_file
            )
        )
    return local_file_datas


local_file_datas = get_local_data(path="D:\\Desktop\\github\\baekjoon")
all_probles = get_solvedac_data_all(user_id="kimjunsung04")

for problem in all_probles:
    if problem["problemId"] not in local_file_datas:
        print(
            f"{problem['problemId']} : {problem['titleKo']}\nhttps://www.acmicpc.net/problem/{problem['problemId']}"
        )
