# 문제
![[s2.svg|tier]] [N과 M (9)](https://www.acmicpc.net/problem/15663)
# 풀이
주어지는 $N$개의 자연수를 모두 정렬한 후 백트래킹 할 때 만든 수열과 각 수가 수열에 포함되는지를 저장하는 배열을 넘겨줍니다.

같은 값이 여러 개 있는 경우 아직 포함되지 않은 것 중 인덱스가 가장 작은 것만 추가하도록 하면 중복을 제거할 수 있습니다.
# 코드
## Python
```python
N, M = map(int, input().split())
nums = [0] + sorted(map(int, input().split()))


def backtrack(seq: list[int], contained: list[bool]):
    if len(seq) == M:
        print(*seq)

    for i in range(1, N + 1):
        if contained[i]:
            continue
        if nums[i - 1] == nums[i] and not contained[i - 1]:
            continue

        contained[i] = True
        seq.append(nums[i])
        backtrack(seq, contained)
        seq.pop()
        contained[i] = False


backtrack([], [False] * (N + 1))
```
## C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<int> nums;

void backtrack(vector<int>& seq, vector<bool>& contained) {
    if (seq.size() == M) {
        for (int i : seq)
            cout << i << ' ';
        cout << '\n';
        return;
    }

    for (int i = 1; i <= N; i++) {
        if (contained[i])
            continue;
        if (nums[i - 1] == nums[i] and not contained[i - 1])
            continue;

        contained[i] = true;
        seq.push_back(nums[i]);
        backtrack(seq, contained);
        seq.pop_back();
        contained[i] = false;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    nums = vector<int>(N + 1);

    for (int i = 1; i <= N; i++)
        cin >> nums[i];

    sort(nums.begin(), nums.end());

    vector<int> seq;
    vector<bool> contained(N + 1);
    backtrack(seq, contained);

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
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static int N, M;
    static int nums[];

    public static void backtrack(ArrayList<Integer> seq, boolean contained[]) throws IOException {
        if (seq.size() == M) {
            for (int i : seq)
                bw.write(i + " ");
            bw.write('\n');
            return;
        }

        for (int i = 1; i <= N; i++) {
            if (contained[i])
                continue;
            if (nums[i - 1] == nums[i] && !contained[i - 1])
                continue;

            contained[i] = true;
            seq.add(nums[i]);
            backtrack(seq, contained);
            seq.remove(seq.size() - 1);
            contained[i] = false;
        }
    }

    public static void main(String[] args) throws IOException {
        StringTokenizer tk = new StringTokenizer(br.readLine());
        N = Integer.parseInt(tk.nextToken());
        M = Integer.parseInt(tk.nextToken());

        nums = new int[N + 1];
        tk = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++)
            nums[i] = Integer.parseInt(tk.nextToken());
        
        Arrays.sort(nums);

        backtrack(new ArrayList<>(), new boolean[N + 1]);
        bw.close();
    }
}
```