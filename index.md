---
title: "PSGuide"
---
안녕하세요, 여러분의 PS 가이드를 맡게 된 skuru라고 합니다.
# PS란?
PS는 문제 해결(Problem Solving)의 줄임말로, 여기서는 **알고리즘 문제 해결**을 뜻합니다.
# PS를 하는 이유
보통 코딩 테스트를 준비하거나 알고리즘 문제 해결 대회를 준비하기 위해서 PS를 합니다.
물론 재밌어서 하는 경우도 있습니다. 제가 그렇습니다 :)
# 시작하기
PS는 온라인으로 문제를 채점해주는 [백준](https://www.acmicpc.net/)을 이용해서 주로 공부합니다.
하지만 백준에는 문제의 난이도가 매겨져 있지 않습니다. 그래서 solved.ac라는 서비스를 이용해서 난이도 정보를 제공받아야 합니다. [help.solved.ac:시작하기](https://help.solved.ac/ko/getting-started/link-account)를 참고해서 계정을 만들어 주세요. 같이 적혀있는 다른 가이드들도 읽어보면 좋습니다.
# 문제 풀기
가입을 마쳤다면 이제 백준에서 문제를 풀어 봅시다. 첫 번째 문제인 [1000번: A+B](https://www.acmicpc.net/problem/1000)를 풀어 봅시다.
먼저 문제가 요구하는 사항에 맞게 코드를 작성합니다.
```python
a, b = map(int, input().split())  # a, b를 공백으로 나눠서 입력받기
print(a + b)  # 더해서 출력
```
코드를 전부 작성했다면 "제출" 버튼을 누른 뒤 자신이 작성한 코드의 언어를 알맞게 선택합니다.
그리고 작성한 코드의 내용을 전부 붙여넣기 한 후 하단의 제출 버튼을 다시 누르면 됩니다.

코드를 올바르게 작성했다면 <span class="ac"></span>를 받고, 잘못 작성했다면 <span class="wa"></span> 또는 <span class="ce"></span> 등 다른 결과를 받습니다. 만약 틀렸다면 게시판의 [이 문제를 틀렸다면](https://www.acmicpc.net/board/view/114024)과 [BOJ 101](https://www.acmicpc.net/blog/view/55)를 읽어보세요.

모르는 문제를 오래 붙잡고 있는 것은 좋지 않습니다. 2시간 이상 고민하는 것을 추천하지 않습니다.
문제를 풀지 못하겠다면 인터넷에 답을 검색해서 풀어도 됩니다.
단, 소스코드를 그대로 베껴서 제출하는 것은 [허용되지 않으니](https://solved.ac/rules) 유의해 주세요.
[관련된 글](https://www.acmicpc.net/board/view/48727)
# 새싹 문제
만약 백준이 처음이라면 [새싹 문제](https://solved.ac/problems/sprout)부터 모두 풀어봅시다.
앞으로 새싹 문제는 모두 풀어봤다고 가정하고 설명할 거예요.
# 공부하기
> [!success] 문제 풀이
> 풀이가 필요하다고 생각되는 문제들에 Python, C++, Java로 풀이를 적어두었습니다.

> [!info] 예제 코드
> 예제 코드는 의사 코드와 비슷한 Python으로만 작성되어 있습니다.
> 하지만 파이썬을 잘 몰라도 충분히 이해할 수 있어요.

우리의 목표는 [solved.ac:CLASS](https://solved.ac/class)의 **CLASS 3 에센셜**까지 취득하는 것입니다.
CLASS에 대한 자세한 내용은 [help.solved.ac:CLASS](https://help.solved.ac/ko/stats/class)를 참고해 주세요.
CLASS 1은 단순 사고력 문제 위주이므로 CLASS 2부터 시작하겠습니다. [CLASS 1 에센셜](https://solved.ac/class/1e)을 모두 풀고 나서 [[CLASS 2]]를 읽어 주세요.