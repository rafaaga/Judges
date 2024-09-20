#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <limits>

using namespace std;

double solve(int n, double cal, vector<int>& courses, map<pair<int, double>, double>& mem) {
    double ans;
    if (mem.find({n, cal}) != mem.end()) ans = mem[{n, cal}];
    else {
        if (n == 0 && cal > 0) ans = numeric_limits<double>::infinity();
        else if (cal <= 0) ans = 0;
        else {
            ans = min(solve(n - 1, cal, courses, mem), solve(n - 1, cal - (courses[n - 1]/10.0), courses, mem) + courses[n - 1]);
        }
        mem[{n,cal}] = ans;
    }
    return ans;
}

int main() {
    int cases;
    cin >> cases;
    for (int _ = 0; _ < cases; _++) {
        map<pair<int, double>, double> mem;
        double calmin;
        int p;
        cin >> calmin >> p;
        vector<int> courses(p);
        for (int i = 0; i < p; i++) cin >> courses[i];
        double res = solve(p, calmin/10.0, courses, mem);
        if (res == numeric_limits<double>::infinity()) cout << "NO SOLUTION" << endl;
        else cout << res << endl;
    }
    return 0;
}
