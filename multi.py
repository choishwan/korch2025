# multithreading를 사용함, 물리적으로 cpu 코어를 활용하여 병렬처리 / 연산이 많으면 이걸로!

import multiprocessing
import time as t

#작업 5초
def long_task():
    for w in range(5):
        print(f"일하는 중...{w+1}")
        t.sleep(1)

if __name__== "__main__":

    start = t.time()
    print("=====start====")

    processes = []
    for n in range(5):
        p = multiprocessing.Process(target=long_task) # 스레드 객체 생성
        
        processes.append(p) # 스레드 객체를 리스트에 저장
    for p in processes:
        p.start() # 스레드 시작
    for p in processes:
        p.join() # 스레드가 끝날 때까지 기다림 


    print("======end=====")
    print(f"총 작업 시간: {t.time() - start:.2f}초")