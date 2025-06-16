# 문제
![[g5.svg|tier]] [Z](https://www.acmicpc.net/problem/1074)
유명한 웰노운 분할 정복 문제입니다.
# 풀이
격자판을 4개로 쪼개서 어디에 위치하는지 확인한 다음 $N$을 1 낮춘 문제를 푸는 방식으로 구할 수 있습니다.

예를 들어 $N = 5$인 경우 전체 격자를 4개로 나눴을 때 격자판 하나의 크기는 $2^4 \times 2^4$ 입니다. $r$이 $2^4$보다 작고 $c$가 $2^4$보다 크거나 같은 경우 답이 적어도 $2^4 \times 2^4$ 이상이 됨을 알 수 있습니다. 제2사분면을 모두 방문하고 나서야 제1사분면을 탐색할 수 있기 때문입니다. 그렇다면 이 문제의 답은 $N = 4$인 격자판에서 $(r - 2^4, c - 2^4)$의 방문 순서를 구한 뒤 $2^8$을 더해서 구할 수 있습니다.

같은 방식으로 재귀적으로 격자판을 쪼개면서 답을 구하면 됩니다.
# 코드
## Python
```python
n, r, c = map(int, input().split())
n = 1 << n
answer = 0

while n >= 2:
    n >>= 1  # n //= 2

    if r < n and c >= n:  # 제2사분면
        c -= n
        answer += n * n
    elif r >= n and c < n:  # 제3사분면
        r -= n
        answer += n * n * 2
    elif r >= n and c >= n:  # 제4사분면
        c -= n
        r -= n
        answer += n * n * 3

print(answer)
```
## C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, r, c;
    cin >> n >> r >> c;
    n = 1 << n;

    int answer = 0;

    while (n >= 2) {
        n >>= 1;

        if (r < n and c >= n) {  // 제2사분면
            c -= n;
            answer += n * n;
        } else if (r >= n and c < n) {  // 제3사분면
            r -= n;
            answer += n * n * 2;
        } else if (r >= n and c >= n) {  // 제4사분면
            c -= n;
            r -= n;
            answer += n * n * 3;
        }
    }

    cout << answer;

    return 0;
}
```
## Java
```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    static final int POS_LIM = 100_001;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer tk = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(tk.nextToken()), r = Integer.parseInt(tk.nextToken()),
                c = Integer.parseInt(tk.nextToken());

        n = 1 << n;

        int answer = 0;

        while (n >= 2) {
            n >>= 1;

            if (r < n && c >= n) { // 제2사분면
                c -= n;
                answer += n * n;
            } else if (r >= n && c < n) { // 제3사분면
                r -= n;
                answer += n * n * 2;
            } else if (r >= n && c >= n) { // 제4사분면
                c -= n;
                r -= n;
                answer += n * n * 3;
            }
        }

        bw.write(answer + "");
        bw.close();
    }
}
```