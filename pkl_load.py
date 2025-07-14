# vulnerable_loader.py 실행
import pickle

print("'malicious.pkl' 파일을 로드합니다...")

try:
    with open("malicious.pkl", "rb") as f:
        pickle.load(f) # <--- 바로 이 시점에서 악성 코드가 실행됩니다.
except Exception as e:
    print(f"오류 발생: {e}")

print("파일 로드가 완료되었습니다. (계산기가 실행되었을 수 있습니다)")