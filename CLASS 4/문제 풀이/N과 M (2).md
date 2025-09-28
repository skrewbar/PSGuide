# 문제
![[s3.svg|tier]] [N과 M (2)](https://www.acmicpc.net/problem/15650)
# 풀이
이때까지 만든 집합에 포함되지 않는 수들만 새로 넣으면서 크기가 $M$이 될 때 출력해주면 됩니다.

사전 순으로 증가하는 순서로 출력해야 하므로 수들도 작은 것 부터 큰 것 순서대로 넣으면 됩니다.

$N$개 중 $M$개를 고른 수열의 개수는 $N! / (N - M)!$이고 수를 넣을 때 수열에 포함되는지 확인하는 데 $\mathcal{O}(N)$이므로 시간 복잡도 $\mathcal{O}(N \times N! / (N - M)!)$에 해결할 수 있습니다.

수열에 포함되었는지 기록하는 배열을 따로 하나 만들어서 전달하면 더 빠르게 해결할 수 있지만 이 문제에서는 제한이 충분히 작으므로 어떤 방식을 사용해도 괜찮습니다.
# 코드
## Python
```python
N, M = map(int, input().split())


def backtrack(seq: list[int]):
    if len(seq) == M:
        print(*seq)

    for i in range(1, N + 1):
        if not i in seq:
            seq.append(i)
            backtrack(seq)
            seq.pop()


backtrack([])
```
## C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int N, M;

void backtrack(vector<int>& seq) {
    if (seq.size() == M) {
        for (int i : seq)
            cout << i << ' ';
        cout << '\n';

        return;
    }

    for (int i = 1; i <= N; i++) {
        bool contains = false;
        for (int j : seq) {
            if (i == j) {
                contains = true;
                break;
            }
        }

        if (contains)
            continue;

        seq.push_back(i);
        backtrack(seq);
        seq.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;

    vector<int> seq;
    backtrack(seq);

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
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br;
    static BufferedWriter bw;

    static int N, M;

    public static void backtrack(ArrayList<Integer> seq) throws IOException {
        if (seq.size() == M) {
            for (int i : seq) {
                bw.write(i + " ");
            }
            bw.write('\n');
            return;
        }

        for (int i = 1; i <= N; i++) {
            if (!seq.contains(i)) {
                seq.add(i);
                backtrack(seq);
                seq.remove(seq.size() - 1);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer tk = new StringTokenizer(br.readLine());
        N = Integer.parseInt(tk.nextToken());
        M = Integer.parseInt(tk.nextToken());

        backtrack(new ArrayList<>());

        bw.close();
    }
}
```