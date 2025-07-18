# 파이썬 Pickle 역직렬화 취약점 데모

이 프로젝트는 파이썬의 `pickle` 모듈을 사용한 역직렬화(deserialization) 과정에서 발생할 수 있는 원격 코드 실행(RCE) 취약점을 보여주기 위한 데모입니다.

## 설명

파이썬의 `pickle` 모듈은 객체 직렬화 및 역직렬화를 위한 강력한 도구이지만, 신뢰할 수 없는 소스에서 생성된 pickle 데이터를 역직렬화할 경우 심각한 보안 위협이 될 수 있습니다.

이 데모는 악의적으로 조작된 pickle 파일을 로드할 때, 시스템에서 계산기 애플리케이션이 실행되는 것을 보여줍니다.

- `mal_gen.py`: 계산기를 실행하는 악성 페이로드가 포함된 `malicious.pkl` 파일을 생성합니다.
- `pkl_load.py`: `malicious.pkl` 파일을 로드하여 취약점을 트리거합니다.

## 실행 방법

1.  **악성 Pickle 파일 생성:**

    ```bash
    python mal_gen.py
    ```

    이 명령을 실행하면 `malicious.pkl` 파일이 생성됩니다.

2.  **취약점 시연:**

    ```bash
    python pkl_load.py
    ```

    이 스크립트를 실행하면 `pickle.load()`가 호출되는 순간, 운영 체제에 따라 계산기가 실행됩니다.

## 보안 경고

**절대로 신뢰할 수 없거나 검증되지 않은 소스에서 받은 pickle 파일을 로드하지 마십시오.**

악의적인 사용자는 pickle 파일을 통해 시스템에서 임의의 코드를 실행하여 데이터를 탈취하거나 시스템을 손상시킬 수 있습니다.

## 탐지 방법

```bash
pip install picklescan
picklescan -p ./malicious.pkl
```
```
/path/to/malicious.pkl: dangerous import 'nt system' FOUND
----------- SCAN SUMMARY -----------
Scanned files: 1
Infected files: 1
Dangerous globals: 1
```


---
*이 프로젝트는 교육 목적으로만 제작되었습니다.*
