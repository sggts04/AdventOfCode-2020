#include <bits/stdc++.h>
using namespace std;

void solve() {
    map<int, int> m;
    int c, turn=1, last=0, lastog = 0;
    bool first = true;
    while(cin>>c) {
        lastog = m[c];
        m[c] = turn;
        last = c;
        turn++;
    }
    while(1) {
        int ans = 0;
        if(first) {
            ans = 0;
        } else {
            ans = (turn-1) - lastog;
        }

        if(m[ans]==0) {
            first = true;
        } else {
            first = false;
        }
        last = ans;
        lastog = m[ans];
        m[ans] = turn;
        turn++;
        cout<<turn<<" - "<<ans<<endl;
        if(turn==2021) break;
    }
}

int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    long long t=1;
    //cin>>t;
    while(t--) {
        solve();
    }
    return 0;
}