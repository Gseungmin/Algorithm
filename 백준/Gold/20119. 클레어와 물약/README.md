# [Gold I] 클레어와 물약 - 20119 

[문제 링크](https://www.acmicpc.net/problem/20119) 

### 성능 요약

메모리: 253304 KB, 시간: 1128 ms

### 분류

너비 우선 탐색(bfs), 그래프 이론(graphs), 그래프 탐색(graph_traversal), 위상 정렬(topological_sorting)

### 문제 설명

<p>세상에는 <em>N</em>종류의 물약이 있고 클레어는 <em>M</em>개의 레시피를 알고있다.</p>

<p>레시피는 (<em>x<sub>1</sub></em>, <em>x</em><sub><em>2</em>,</sub> ..., <em>x<sub>k</sub></em>) → <em>r</em> 형태로 표현할 수 있고 <em>x<sub>1</sub></em>번, <em>x<sub>2</sub></em>번 ..., <em>x<sub>k</sub></em>번 물약을 모두 섞어서 <em>r</em>번 물약을 만들 수 있다는 뜻이다.</p>

<p>현재 클레어에게는 <em>y<sub>1</sub></em>번, <em>y<sub>2</sub></em>번, ..., <em>y<sub>L</sub></em>번 물약만 있다. 만들 수 있는 물약들을 전부 알아내주자.</p>

<p>클레어가 가지고 있는 각 종류의 물약의 양은 무한대라고 가정하자.</p>

### 입력 

 <p>첫 번째 줄에는 세상에 존재하는 물약의 종류의 수 <em>N</em> (3 ≤ <em>N</em> ≤ 200,000) 과 클레어가 알고 있는 레시피의 개수 M (1 ≤ <em>M</em> ≤ 200,000) 이 주어진다.</p>

<p>다음 <em>M</em>개의 줄에는 각각의 줄마다 레시피의 정보 <em>k<sub>i</sub></em>, <em>x<sub>i1</sub></em>, <em>x</em><sub><em>i2</em>, ..., </sub><em>x<sub>ik<sub>i</sub></sub></em>, <em>r<sub>i</sub></em> (1 ≤ <em>k<sub>i</sub></em> < N, 1 ≤ <em>x<sub>ij</sub></em>, <em>r<sub>i</sub></em> ≤ <em>N</em>, <em>x<sub>ij</sub></em> ≠ <em>r<sub>i</sub></em>) 가 주어지며 이는 (<em>x<sub>i1</sub></em>, <em>x</em><sub><em>i2</em>, ..., </sub><em>x<sub>ik<sub>i</sub></sub></em>) → <em>r<sub>i</sub></em> 형태의 레시피를 의미한다.</p>

<p><em>M+2</em> 번째 줄에는 현재 클레어가 가지고 있는 물약 종류의 수 <em>L</em> (1 ≤ <em>L</em> < N) 이 주어진다.</p>

<p><em>M+3</em> 번째 줄에는 <em>y<sub>1</sub></em>, <em>y<sub>2</sub></em>, ..., <em>y<sub>L </sub></em>(1 ≤ <em>y<sub>i</sub></em> ≤ <em>N</em>) 이 주어진다.</p>

<p>모든 <em>k<sub>i</sub></em>의 합은 400,000을 넘지 않는다.</p>

### 출력 

 <p>첫 번째 줄에 클레어가 만들 수 있는 물약의 개수를 출력한다.</p>

<p>두 번째 줄에는 만들 수 있는 물약의 번호를 오름차순으로 출력한다.</p>

