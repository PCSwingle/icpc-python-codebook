#pragma region template
#include <cassert>
#include <bits/stdc++.h>

#define umap unordered_map
#define uset unordered_set
#define ll long long
#define vi vector<int>
#define vll vector<ll>

#define all(x) x.begin(), x.end()
#define len(x) ((ll) x.size())
#define append push_back
#define concat(v1, v2) v1.insert(v1.end(), all(v2))

#define minIt(it) *ranges::min_element(it)
#define maxIt(it) *ranges::max_element(it)
#define reverseIt(it) ranges::reverse(it)
#define findIt(it, k) ranges::find(it, k)
#define countIt(it, k) ranges::count(it, k)
#define printIt(it) print("{{"); bool first = true; for (auto& v : it) { if (!first) print(", "); print("{}", v); first = false; } print("}}\n");

#define rep(i, n) for(ll i = 0; i < n; i++)
#define rrep(i, n) for(ll i = n - 1; i > -1; i--)

#define repse(i, s, e) for(ll i = s; i < e; i++)
#define rrepse(i, s, e) for(ll i = e - 1; i > s - 1; i--)

#define repstep(i, s, e, step) for(ll i = s; i < e; i += step)

#define YES() println("YES");
#define NO() println("NO");
#define flush() cout.flush();

using namespace std;

int indexIt(auto&& c, auto&& k) {
    auto it = findIt(c, k);
    return it == end(c) ? -1 : distance(begin(c), it);
}

ll input() {
    ll x;
    cin >> x;
    return x;
}

string inputS() {
    string s;
    cin >> s;
    return s;
}

vll inputV(ll n) {
    vll v;
    rep(i, n) {
        v.append(input());
    }
    return v;
}

// (__int128)
#pragma endregion

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    ll tc = 1;
    tc = input();
    rep(t, tc) {

    }

    return 0;
}