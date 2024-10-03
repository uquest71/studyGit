import time
import os

def print_clock():
    try:
        while True:
            # 현재 시간을 받아오는 코드
            current_time = time.strftime("%H:%M:%S", time.localtime())

            # 콘솔을 지워서 시계가 갱신되는 것처럼 보이게 함
            os.system('cls' if os.name == 'nt' else 'clear')

            print(current_time)
            time.sleep(1)
    except KeyboardInterrupt:
        # 프로그램 종료 시 처리
        print("\nClock stopped.")

print_clock()
