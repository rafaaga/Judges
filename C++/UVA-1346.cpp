#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve(vector<vector<double>> songs, int N, int S) {
    int ans = 0;
    vector<pair<double, int>> l;
    for (int i = 0; i < N; i++) {
        double val = songs[i][1] / songs[i][2];
        l.push_back(make_pair(val, songs[i][0]));
    }
    sort(l.begin(), l.end());
    ans = l[S-1].second;
    return ans;
}

int main() {
    int N;
    while (cin >> N) {
        vector<vector<double>> songs;
        while (songs.size() < N) {
            vector<double> data(3);
            for (int i = 0; i < 3; i++) {
                cin >> data[i];
            }
            songs.push_back(data);
        }
        int S;
        cin >> S;
        int ans = solve(songs, N, S);
        cout << ans << endl;
    }
    return 0;
}
