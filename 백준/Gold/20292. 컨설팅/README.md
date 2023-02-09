# [Gold IV] 컨설팅 - 20292 

[문제 링크](https://www.acmicpc.net/problem/20292) 

### 성능 요약

메모리: 119076 KB, 시간: 180 ms

### 분류

자료 구조(data_structures), 그리디 알고리즘(greedy), 해시를 사용한 집합과 맵(hash_set), 구현(implementation), 트리를 사용한 집합과 맵(tree_set)

### 문제 설명

<p>Sogang ICPC Team에서는 학회원들을 돕기 위해 Sogang Program Consulting Team(이하 SPC Team)을 만들었다. SPC Team은 학회원들과 화목하게 지내게 될 날만을 상상하며 에러가 발생한 코드를 무료로 디버깅해주는 컨설팅을 바로 시작했다.</p>

<p>그러던 어느 날, 기세등등했던 SPC Team의 모두를 당황시킨 코드가 등장했다. 아무리 봐도 정상적인 코드인데, 원하는 데이터를 얻을 수 없었던 것이다. 하지만 포기를 모르는 SPC Team은 계속해서 디버깅을 시도한 끝에, 한 번에 여러 줄의 명령이 실행되고 있었다는 사실을 알게 되었다! 이 상황을 이해하기 위해 다음 예시를 살펴보자.</p>

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;"><code>1: WRITE A TO B
2: WRITE B TO C
3: READ B
4: READ C
5: EXIT</code></pre>

<p>위 코드는 문제가 된 학회원의 코드이다. 명령어가 순서대로 실행되면 전혀 문제가 없을 코드지만, 줄 1–4가 동시에 실행된다면 문제가 생긴다. 메모리 A에서 메모리 B로 데이터가 옮겨지지도 않았는데 두 번째 줄이 실행되면, 메모리 C에 무슨 데이터가 들어갈지 알 수 없다. 이러한 문제를 확인한 SPC Team은 다음과 같이 컨설팅을 해 주었다.</p>

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">1: WRITE A TO B
2: WAIT
3: WRITE B TO C
4: WAIT
5: READ B
6: READ C
7: EXIT
</pre>

<p>위와 같이, 중간에 <code>WAIT</code>를 삽입하여 <code>WRITE A TO B</code>와 <code>WRITE B TO C</code>가 동시에 실행되는 것을 막아준다면, 메모리 C에 어떤 데이터가 들어갈지 명확해진다! 위 코드에 대한 컨설팅을 끝마친 SPC Team은 문제가 발생할 수 있는 경우를 다음과 같이 세 가지로 분류했다.</p>

<ul>
	<li>READ with WRITE
	<ul>
		<li><code>WRITE A TO B</code>와 <code>READ B</code>가 동시에 실행되면, 메모리 B의 데이터가 확실하지 않으므로 두 명령어 사이에 <code>WAIT</code>가 있어야 한다.</li>
		<li><code>WRITE A TO B</code>와 <code>WRITE B TO C</code>가 동시에 실행되면, 메모리 C의 데이터가 확실하지 않으므로 두 명령어 사이에 <code>WAIT</code>가 있어야 한다.</li>
	</ul>
	</li>
	<li>WRITE with WRITE
	<ul>
		<li><code>WRITE A TO C</code>와 <code>WRITE B TO C</code>가 동시에 실행되면, 메모리 C의 데이터가 확실하지 않으므로 두 명령어 사이에 <code>WAIT</code>가 있어야 한다.</li>
		<li><code>WRITE A TO B</code>와 다른 <code>WRITE A TO B</code>가 동시에 실행되는 것은 문제가 없지만, 프로그램의 안정성을 위해 두 명령어 사이에 <code>WAIT</code>가 있어야 한다.</li>
	</ul>
	</li>
	<li>교착 상태
	<ul>
		<li><code>WRITE A TO B</code>와 <code>WRITE B TO A</code>가 동시에 실행되면, 메모리 A와 메모리 B의 값이 확실하지 않으므로 두 명령어 사이에 <code>WAIT</code>가 있어야 한다.</li>
	</ul>
	</li>
</ul>

<p>이 문제를 겪고 있는 학회원들이 지속적으로 SPC Team에 컨설팅 문의를 신청하고 있다. 반복되는 작업에 지친 SPC Team은 위와 같은 상황을 알아서 탐지하여 컨설팅해주는 프로그램을 만들고자 한다. 하지만 너무나도 바쁜 나머지, 유능한 프로그래머인 당신에게 프로그램의 제작을 의뢰했다. 너무나도 마음이 상냥한 당신은 이 의뢰를 거절할 수 없다!</p>

### 입력 

 <p>입력으로 최대 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mtext class="mjx-n"><mjx-c class="mjx-cA0"></mjx-c></mjx-mtext><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mtext> </mtext><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10\ 000$</span></mjx-container>줄의 명령어가 주어지며, WRITE문, READ문, EXIT문으로 구성된다. EXIT문은 마지막에 한 번만 주어진다.</p>

<p>각 명령어는 다음과 같이 정의되며, 메모리 이름은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>–<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container>글자의 알파벳 대문자로 구성되어 있다.</p>

<ul>
	<li><span style="color:#e74c3c;"><code>WRITE A TO B</code></span>: 메모리 A의 내용을 메모리 B로 옮긴다. 이 때, 메모리 A는 READ 상태가 된다.</li>
	<li><span style="color:#e74c3c;"><code>READ A</code></span>: 메모리 A의 데이터를 읽는다.</li>
	<li><span style="color:#e74c3c;"><code>EXIT</code></span>: 프로그램을 종료한다.</li>
</ul>

<p><code>WRITE A TO A</code>같이 동일한 메모리로 WRITE를 수행하는 경우는 없다.</p>

### 출력 

 <p>WAIT을 최소로 사용한 컨설팅 결과를 기존 명령어들의 순서를 유지하여 출력한다.</p>

<p>한 줄에 하나의 명령어만 출력해야 하며, 만약 그러한 컨설팅 결과가 여러 개라면 그 중 하나를 출력한다.</p>

