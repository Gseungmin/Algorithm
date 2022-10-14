# [Gold II] 그래프의 줄기 - 24461 

[문제 링크](https://www.acmicpc.net/problem/24461) 

### 성능 요약

메모리: 137032 KB, 시간: 312 ms

### 분류

그래프 이론(graphs), 구현(implementation), 위상 정렬(topological_sorting)

### 문제 설명

<p>그래프에서 사이클이란, 한 정점에서 같은 정점까지, 반복되는 간선이 없으며, 길이가 $0$이 아닌 경로이다.</p>

<p>사이클이 존재하지 않는 그래프가 주어진다.</p>

<p>우리는 이 그래프의 정점 중에서 연결된 간선이 하나인 정점을 <strong>가장자리 정점</strong>이라고 정의하자.</p>

<p>이 그래프의 <strong>가장자리 정점</strong>을 동시에 없애는 행동을 반복하면서, 그래프가 일직선의 모양이 되면 남아있는 정점의 집합을 <strong>그래프의 줄기</strong>라고 정의하자. 단, 가장자리 정점의 개수가 둘 이하라면 그래프가 일직선 모양이라고 한다.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 640px; height: 360px;"></p>

<p>위 그림과 같은 그래프가 있다고 할 때, 아래와 같이 <strong>가장자리 정점과 연결된 간선</strong>을 빨간색으로 표시하면 아래와 같다.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 640px; height: 360px;"></p>

<p>빨간색 간선과 연결된 가장자리 정점의 연결을 끊으면 아래 그림과 같이 일직선 모양으로 연결된 <strong>그래프의 줄기</strong>가 남는다. 만약 그래프가 일직선 모양이 되었다면, <strong>가장자리 정점</strong>이 더 존재하더라도 더 이상 <strong>가장자리 정점</strong>들을 없애지 않는다.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 640px; height: 360px;"></p>

<p>이때 <strong>그래프의 줄기</strong>를 이루는 정점을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>입력의 첫 번째 줄에는 처음 그래프의 정점의 수 $N$이 주어진다. $(2 \le N \le 100\,000)$</p>

<p>이후 $N-1$줄에 걸쳐 각 간선으로 연결된 두 정점의 번호 $a, b$가 입력된다. $(0 \le a,\ b < N,\ a \ne b)$</p>

### 출력 

 <p>출력의 첫 번째 줄에 <strong>그래프의 줄기</strong>를 이루는 정점의 번호들을 오름차순으로 정렬하고 공백으로 구분하여 출력한다.</p>

