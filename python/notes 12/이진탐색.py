"""
코딩반 학생들에게 이진 탐색을 설명하던 선생님은 
이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.

짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 
이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.

예를 들어 책이 총 400쪽이면, 
검색 구간의 왼쪽 l=1, 
오른쪽 r=400이 되고, 
중간 페이지 c= int((l+r)/2)로 계산한다.

찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.

A는 300, B는 50 쪽을 찾아야 하는 경우, 
다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾아가면 된다.


첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000
"""

T = int(input())

def BS(P,l,r):
    c = int((l+r)/2)
    while c == A or c== B:
        if c != A and c != B:
            
        elif c == A and c == B:
            return 0
        elif c == A and c != B:
            return A
        elif c != A and c == B:
            return B

    
for tc in range(1,T+1):
    P,A,B = map(int,input().split())
    l = 1
    r = P
    print("#{tc} {BS(P,A,B)}")