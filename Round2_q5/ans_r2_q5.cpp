#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
const long long NR = 36000, MR = 60;
long long n, m, a[NR], last[NR], rec[NR], tran[MR][NR], u[NR], dp[MR][NR], val[NR];

int main()
{
    int ieee;
    int count = 0;
    vector<long long> ans_array;
    cin >> ieee;
    for (int lums = 1; lums <= ieee; lums++)
    {
        scanf("%lld%lld", &n, &m);
        for (long long i = 1; i <= n; i++)
        {
            scanf("%lld", &a[i]);
        }
        for (long long i = 1; i <= n; i++)
        {
            last[i] = rec[a[i]];
            rec[a[i]] = i;
        }
        for (long long i = 1; i <= n; i++)
        {
            for (long long k = m; k >= 1; k--)
            {
                long long l = max(tran[k][i - 1], k - 1), r;
                if (tran[k + 1][i] == 0)
                {
                    r = i - 1;
                }
                else
                {
                    r = tran[k + 1][i];
                }
                for (long long j = l; j <= r; j++)
                {
                    if (u[j + 1] != i)
                    {
                        u[j + 1] = i;
                        val[j + 1] += (last[i] < j + 1);
                    }
                    if (dp[k][i] < dp[k - 1][j] + val[j + 1])
                    {
                        dp[k][i] = dp[k - 1][j] + val[j + 1];
                        tran[k][i] = j;
                    }
                }
            }
        }
        count++;
        ans_array.push_back(dp[m][n]);
    }

    for (int i = 0; i < count; i++)
    {
        cout << "Case #" << i + 1 << ": " << ans_array[i] << endl;
    }

    return 0;
}