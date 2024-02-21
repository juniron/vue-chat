from selenium import webdriver
from bs4 import BeautifulSoup

# Base URL
base_url = "https://www.ssafy.com/ksp/servlet/swp.board.controller.SwpBoardServlet?p_process=select-board-view&p_menu_cd=M0202&p_tabseq=226507&p_seq="

# Chrome 브라우저 열기
driver = webdriver.Chrome()

try:
    # 결과를 저장할 파일 생성
    with open("output.txt", "w", encoding="utf-8") as file:

        # seq 값에 대해 반복
        for seq in range(1, 123):  # seq=1 부터 seq=122 까지

            # 현재 페이지 URL 생성
            current_url = base_url + str(seq)

            # 웹페이지 열기
            driver.get(current_url)

            # Selenium의 경우 페이지가 완전히 로드될 때까지 기다려주는 것이 좋습니다.
            driver.implicitly_wait(5)  # 예: 5초 기다림

            # 현재 페이지의 HTML 가져오기
            html = driver.page_source

            # BeautifulSoup을 사용하여 HTML 파싱
            soup = BeautifulSoup(html, 'html.parser')

            # 모든 텍스트 가져오기
            paragraphs = soup.find_all('p')

            # 문단별로 텍스트 추출하여 리스트에 저장
            extracted_text_list = [p.get_text() for p in paragraphs]

            # 추출된 텍스트 출력 (각 문단은 새로운 줄로 나눠짐)
            extracted_text = '\n'.join(extracted_text_list)

            # 결과를 파일에 추가
            file.write(f"--- Page {seq} ---\n")
            file.write(extracted_text + "\n\n")

            print(f"페이지 {seq}의 내용을 저장했습니다.")

    print("모든 페이지의 내용을 output.txt로 저장했습니다.")

except Exception as e:
    print("에러 발생: ", e)

finally:
    # 브라우저 종료
    driver.quit()
