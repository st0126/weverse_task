import pytest
from playwright.sync_api import Page, expect

###자동화 스크립트 실행하여 로그인 시도 시 "비정상적인 접근으로 감지" 메시지 출력되어 로그인이 불가합니다. WID 값은 개발자 도구 Fetch/XHR 통하여 확인은 진행하였습니다.###
###시현 영상 및 wid 값 첨부하였습니다.###

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

# 기가입 된 계정 email 하드 코딩
def login_email(page:Page):
    email_input = page.get_by_placeholder("your@email.com")
    email_input.click()
    id = "tw02485@naver.com" # 기가입 메일 입력
    email_input.fill(id)
    page.locator('button:has-text("이메일로 계속하기")').click()
    return id

# 기가입 된 계정 pw 하드 코딩
def login_password(page:Page):
    pw_input = page.get_by_role("textbox", name="비밀번호")
    pw_input.click()
    pw = "!qkdtmd753" # 기가입 패스워드 입력
    pw_input.fill(pw)
    page.locator('button:has-text("로그인")').click()
    return pw


def test_flow(page):
        go_site(page)
        move_page(page)
        email = login_email(page)
        pw = login_password(page)
        print(f"\nid: {email}"f"\npw: {pw}")

# 실행 명령어 %pytest assignment2_test.py -s --headed --slowmo 500 실행