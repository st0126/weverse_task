import pytest
from playwright.sync_api import Page, expect
import random
import string

######### 프로필 페이지 진입하여 WID 추출은 인증 완료된 계정으로 로그인이 필요하여 assignment2_test.에서 진행하였습니다.#########
###시현 영상 첨부 하였습니다.###

# 홈페이지 이동
def go_site(page):
    page.goto("https://weverse.io/")
    try:
        popup = page.get_by_role("button", name="3일간 보지 않기")
        popup.click()
    except:
        pass  # 팝업 없으면 무시

# 회원가입 화면 이동
def move_page(page):
    sign_btn = page.get_by_role("button", name="Sign in")
    sign_btn.click()

# 이메일 생성
def user_email(page:Page):
    email_input = page.get_by_placeholder("your@email.com")
    email_input.click()
    id = "qa" + ''.join(random.choices(string.digits, k=6)) + "@benx.com" # qa??????@benx.com 메일형식
    email_input.fill(id)
    page.locator('button:has-text("이메일로 계속하기")').click()
    page.locator('button:has-text("가입하기")').click()
    return id

# 비밀번호 생성
def user_password(page:Page):
    pw_input = page.get_by_placeholder("새로운 비밀번호", exact=True)
    pw_input.click()
    base = string.ascii_letters + string.digits + "!@#$%^&*"
    while True:
        length = random.randint(8,32)             # 8~32자
        pw = ''.join(random.choices(base, k=length))
        if (any(c.isalpha() for c in pw) and      # 영문 포함 여부
            any(c.isdigit() for c in pw) and      # 숫자 포함 여부
            any(c in "!@#$%^&*" for c in pw)):    # 특수 문자 포함 여부
            break
    pw_input.fill(pw)

    confirmPassword_input = page.get_by_placeholder("새로운 비밀번호 확인") # 비밀번호 확인
    confirmPassword_input.click()
    confirmPassword_input.fill(pw)
    page.locator('button:has-text("다음")').click()
    return pw

def nick_name(page:Page):
    page.locator('button:has-text("다음")').click()

def check(page:Page):
    try:
        page.get_by_label("모두 동의 합니다.").check()
    except:
        page.locator('text=모두 동의 합니다.').click()  # get_by_label 실패시, 대체 로케이터로 처리

    page.locator('button:has-text("다음")').click()
    page.get_by_role("button", name="확인", exact=True).click()



def test_flow(browser):
    for i in range(3):                          # 계정 대량 생성 고려 range(n) 원하는 수 입력
        context = browser.new_context()         # 각각의 독립적인 저장소
        page = context.new_page()               # 독집적인 저장소에서 새 페이지 오픈
        go_site(page)
        move_page(page)
        email = user_email(page)
        pw = user_password(page)
        nick_name(page)
        check(page)
        print(f"\nid: {email}"f"\npw: {pw}")
        context.close()                         # 브라우저 정리 후 닫기


# 실행 명령어 %pytest assignment_test.py -s --headed --slowmo 500 실행
