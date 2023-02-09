# [Gold III] 전설의 JBNU - 12757 

[문제 링크](https://www.acmicpc.net/problem/12757) 

### 성능 요약

메모리: 139956 KB, 시간: 1248 ms

### 분류

이분 탐색(binary_search), 자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set)

### 문제 설명

<p>전설의 프로그래머 윤준하는 독자적인 데이터베이스 시스템 JBNU(Jeong Bo Neoh Um)를 만들었다.</p>

<p>준하가 생각한 데이터베이스의 기본 골자는 데이터에 접근하기 위한 Key와 그 데이터를 나타내는 Value로 구성되어 있다. 사용자는 Key를 알고 있어야만 원하는 데이터에 접근할 수 있다.</p>

<p>하지만 준하는 건망증이 심해 Key를 매번 잊어버리기 일쑤였다. 따라서 준하는 JBNU를 개조하여 잘못된 Key를 입력하더라도 그 잘못된 Key와 제일 근접한 Key를 찾아주는 메커니즘을 도입하였다.</p>

<p>Key와 Value는 항상 정수로 되어있다. 가장 근접한 Key란 두 수의 차이가 가장 작은 Key를 의미한다. 또한, 정보의 정확성을 위해 두 수의 차이가 K보다 큰 경우는 Key로 인정하지 않기로 하였다.</p>

<p>프로젝트 베끼기의 달인 승균이는 데이터베이스 시간에 JBNU를 모방하기로 했다. 그러나 준하는 전설이기 때문에 그가 만든 프로그램은 찾을 방법이 없었고, 하는 수 없이 같은 조원인 당신에게 맡기려고 한다.</p>

<p>JBNU의 초기 데이터 상태가 주어질 때, 데이터 추가, 수정 및 검색을 지원하는 프로그램을 작성해보자.</p>

### 입력 

 <p>첫 줄에는 초기 데이터의 개수인 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>100</mn><mo>,</mo><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(N(1 \le N \le 100,000)\)</span></mjx-container> 과 명령 횟수인 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>M</mi><mo>≤</mo><mn>100</mn><mo>,</mo><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(M(1 \le M \le 100,000)\)</span></mjx-container>, 가장 근접한 Key까지의 거리의 제한인 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>K</mi><mo>≤</mo><mn>10</mn><mo>,</mo><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(K(1 \le K \le 10,000)\)</span></mjx-container>가 주어진다. </p>

<p>입력의 둘째 줄부터 N개의 줄에는 초기 데이터인 Key와 Value 값이 주어진다. 모든 Key와 Value는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>000</mn><mo>,</mo><mn>000</mn><mo>,</mo><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(1,000,000,000\)</span></mjx-container> 이하의 음이 아닌 정수이다. 같은 Key를 갖는 데이터는 없다.</p>

<p>다음 M개의 줄에는 아래와 같은 명령이 주어진다.</p>

<ul>
	<li>1 Key Value : 해당 Key와 Value를 가진 데이터를 추가한다. Key가 이미 존재하는 입력은 주어지지 않는다.</li>
	<li>2 Key Value : 해당 Key로 검색된 데이터를 Value로 변경한다. 조건을 만족하는 유일한 Key가 없는 경우 무시한다.</li>
	<li>3 Key : 해당 Key로 검색된 데이터를 출력한다. 조건을 만족하는 Key가 없는 경우 -1을 출력한다. 만약 해당하는 Key가 두 개 이상 존재한다면 ?를 출력한다. 모든 출력은 개행을 포함해야 한다.</li>
</ul>

### 출력 

 <p>각 줄에 걸쳐 3번 명령에 대한 결과를 출력한다.</p>

