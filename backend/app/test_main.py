# 로컬 환경에 저장된 html 파일을 읽어들여서 키워드를 추출하는 test_main 파일

from pathlib import Path
from bs4 import BeautifulSoup
from keyword_extractor import KeywordExtractor  # 작성한 키워드 추출기 클래스 임포트
import time

# 키워드 추출기 초기화
keyword_extractor = KeywordExtractor()

def read_article_text(file_path):
    """로컬 파일에서 HTML 기사를 읽고 텍스트를 추출하는 함수"""
    article_path = Path('C:/Users/leejo/OneDrive/바탕 화면/Langchain_env/data/articles/sample2.html') # 추후 웹 환경에서 html 파일 읽어들이는 코드로 대체
    if not article_path.exists():
        raise FileNotFoundError("Article file not found.")
    
    # HTML 파일을 읽고 BeautifulSoup으로 파싱
    with open(article_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # HTML 구조에서 텍스트를 추출 (예: #dic_area로 추출)
    soup = BeautifulSoup(html_content, "html.parser")
    article_text = soup.select_one("#dic_area").get_text(strip=True) # 파일 내 텍스트를 읽어들일 css. 
    
    return article_text

def test_keyword_extraction(file_path):
    """로컬 파일에서 키워드를 추출하여 결과를 출력하는 테스트 함수"""
    # 기사 텍스트 읽기
    article_text = read_article_text(file_path)
    
    # 키워드 추출
    keywords = keyword_extractor.extract_keywords(article_text)
    
    # 결과 출력
    print("추출된 키워드:", keywords)

# 테스트 실행
if __name__ == "__main__":
    sample_file_path = "../data/articles/sample.html"  # sample.html 파일의 경로
    test_keyword_extraction(sample_file_path)
