#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, lk, lt, hk, ht, ans;
    cin >> n;
    while(n != 0){
        bool empate = true;
        lk = 0;
        lt = 0;
        hk = n-1;
        ht = n-1;
        ans = 0;
        vector<int> tian(n);
        vector<int> king(n);
        for (int j = 0; j < n; j++) {
            cin >> tian[j];
        }
        for (int j = 0; j < n; j++) {
            cin >> king[j];
        }
        sort(tian.begin(), tian.end());
        sort(king.begin(), king.end());
        int i = 0;
        while(empate && i < n){
            if(tian[ht] > king[hk]){
                ans = ans + 200;
                ht--;
                hk--;
            }else if(tian[lt] > king[lk]){
                ans = ans + 200;
                lt++;
                lk++;
            }else if(tian[lt] < king[hk]){
                ans = ans - 200;
                lt++;
                hk--;
            }else{
                empate = false;
            }
            i++;
        }
        cout << ans << endl;
        cin >> n;
    }
    return 0;
}
