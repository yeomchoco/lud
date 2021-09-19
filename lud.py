import os
import sys
from bs4 import BeautifulSoup
from selenium import webdriver


def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)


# 첫 화면
os.system("clear")
print("\n\n✦✦✦✦✦ LUD ✡︎ Login ٩(•̤̀ᵕ•̤́๑)૭ ✦✦✦✦✦\n\n")
print("[ 로그인 시 안내 사항 ]\n")
print("[0] 로그인 도중 키보드나 마우스를 조작하지 마세요!")
print("[1] 로그인에 성공하면 이 창으로 돌아와주세요.\n")
print("➤ 로그인하려면 ENTER 키를 눌러주세요\n")

while True:
    press = input()
    if press == "":
        break

while True:
    # 로그인 시도
    os.system("clear")
    print("\n\n✦✦✦✦✦ LUD ✡︎ Login ٩(•̤̀ᵕ•̤́๑)૭ ✦✦✦✦✦\n\n")
    print("➤ Login...\n")
    try:
        driver = webdriver.Chrome("lib/chromedriver")
        driver.get("https://www.learnus.org/login.php")

        elem_login = driver.find_element_by_name("username")
        # elem_login.clear()
        elem_login.send_keys("2017123077")

        elem_login = driver.find_element_by_name("password")
        # elem_login.clear()
        elem_login.send_keys("980220")

        xpath = """//*[@id="ssoLoginForm"]/div/div[2]/input"""
        driver.find_element_by_xpath(xpath).click()
        break
    except Exception:
        driver.close()
        print("✘✘✘ 로그인 실패!! 다시 시도해주세요... ✘✘✘\n")
        print("➤ 다시 시도하려면 ENTER 키를 눌러주세요\n")
        press = input()
        if press == "":
            continue


def it_is_mine():

    # 로그인 성공
    os.system("clear")
    print("\n\n✦✦✦✦✦ LUD ✡︎ Login Succeeded ٩(•̤̀ᵕ•̤́๑)૭✧ ✦✦✦✦✦\n\n")
    print("[ 다운로드 시 안내 사항 ]\n")
    print("[0] 도중에 크롬창을 종료하지 마세요!")
    print("[1] 할 일이 모두 끝나면 자동으로 닫힙니다.\n")
    print("➤ 진행하려면 ENTER 키를 눌러주세요\n")

    while True:
        press = input()
        if press == "":
            break

    # 다운로드 화면
    os.system("clear")
    print("\n\n✦✦✦✦✦ LUD ✡︎ Download ٩(•̤̀ᵕ•̤́๑)૭✧ ✦✦✦✦✦\n\n")

    while True:
        try:
            driver.get(input("➤ 동영상 주소를 알려주세요: "))
            break
        except Exception:
            print("\n✘✘✘ 올바른 주소를 입력해주세요... ✘✘✘\n")
            print("➤ 다시 시도하려면 ENTER 키를 눌러주세요\n")
            press = input()
            if press == "":
                continue

    while True:
        try:
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            # print(soup)
            target = soup.find_all("source")[0]["src"]
            break
        except Exception:
            print("\n✘✘✘ 파싱 실패!! 다시 시도해주세요... ✘✘✘\n")
            print("➤ 다시 시도하려면 ENTER 키를 눌러주세요\n")
            press = input()
            if press == "":
                continue

    while True:
        try:
            save_name = input("\n➤ 어떤 이름으로 저장할까요? (ENG/확장자제외): ")
            break
        except Exception:
            print("\n✘✘✘ 올바른 이름을 입력해주세요... ✘✘✘\n")
            print("➤ 다시 시도하려면 ENTER 키를 눌러주세요\n")
            press = input()
            if press == "":
                continue

    ffmpeg = "lib/ffmpeg"

    # 로딩 화면
    os.system("clear")
    print("\n\n✦✦✦✦✦ LUD ✡︎ Download ٩(•̤̀ᵕ•̤́๑)૭✧ ✦✦✦✦✦\n\n")

    while True:
        print("➤ Please wait...\n")
        try:
            os.system(
                f"{ffmpeg} -hide_banner -loglevel error -i {target} -bsf:a aac_adtstoasc -c copy {save_name}.mp4"
            )
            break
        except Exception:
            print("✘✘✘ 변환 실패!! 다시 시도해주세요... ✘✘✘\n")
            print("➤ 다시 시도하려면 ENTER 키를 눌러주세요\n")
            press = input()
            if press == "":
                continue

    # 알림음
    os.system("say 초코야 다돼써")

    # 성공 화면
    def succeed():
        os.system("clear")
        print("\n\n✦✦✦✦✦ LUD ✡︎ Download Succeeded ٩(•̤̀ᵕ•̤́๑)૭ ✦✦✦✦✦\n\n")
        print("[0] 폴더열기\t[1] 재생하기\t[2] 하나 더\t[3] 나가기\n\n")

        while True:
            press = input("➤ 다음 작업을 알려주세요: ")
            if press == "0":
                os.system("open .")
            elif press == "1":
                os.system(f"open {save_name}.mp4")
            elif press == "2":
                it_is_mine()
            elif press == "3":
                driver.close()
                os.system("killall Terminal")
            else:
                print("\n✘✘✘ 올바른 번호를 입력해주세요... ✘✘✘\n")
                print("➤ 다시 시도하려면 ENTER 키를 눌러주세요\n")
                press = input()
                if press == "":
                    succeed()
            succeed()

    succeed()


it_is_mine()
