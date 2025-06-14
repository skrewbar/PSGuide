# 문제
![[s4.svg|tier]] [ATM](https://www.acmicpc.net/problem/11399)
# 풀이
인출하는 데 오래 걸리는 사람 $i$와 빨리 걸리는 사람 $j$가 있습니다.
만약 $i$가 $j$보다 먼저 인출한다면 시간의 합은 $2P_i + P_j$가 됩니다.
만약 $j$가 $i$보다 먼저 인출한다면 시간의 합은 $P_i + 2P_j$가 됩니다.
$P_i > P_j$이므로 빨리 걸리는 사람이 먼저 인출하는 것이 이득입니다.

사람이 세 명 이상이어도 비슷한 원리로 증명할 수 있습니다.
$N$명의 사람이 있을 때, $i$가 $1$번째로 인출한다면 답에 $NP_i$가 더해집니다.
$i$가 $2$번째로 인출한다면 답에 $(N-1)P_i$가 더해집니다. 따라서 $P_i$가 작은 사람부터 인출하는 것이 이득입니다.
# 코드
## Python
```python
n = input()
p = sorted(map(int, input().split()))

for i in range(1, n):
    p[i] += p[i - 1]

print(sum(p))
```
## C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> p(n);
    for (int i = 0; i < n; i++)
        cin >> p[i];
    
    ranges::sort(p);
    int answer = p[0];
    for (int i = 1; i < n; i++) {
        p[i] += p[i - 1];
        answer += p[i];
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
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer tk = new StringTokenizer(br.readLine());
        int p[] = new int[n];
        for (int i = 0; i < n; i++)
            p[i] = Integer.parseInt(tk.nextToken());
        
        Arrays.sort(p);
        int answer = p[0];
        for (int i = 1; i < n; i++) {
            p[i] += p[i-1];
            answer += p[i];
        }

        bw.write(answer + "");
        bw.close();
    }
}
```