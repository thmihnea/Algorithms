#include <iostream>
#include <queue>
#include <unordered_map>

int main(int argc, char* argv[]) {
    std::queue<int> queue;
    std::unordered_map<int, bool> map = {};
    int n, arr[200001];
    std::cin >> n;
    for (int i = 1; i <= n; i++) {
        int x;
        std::cin >> x;
        queue.push(x);
        map[x] = true;
    }
    for (int i = 1; i <= n; i++) {
        std::cin >> arr[i];
        int x = arr[i];
        if (map.at(x)) {
            int count = 1;
            while (queue.front() != x) {
                map[queue.front()] = false;
                queue.pop();
                count++;
            }
            queue.pop();
            std::cout << count << " ";
        }
        else std::cout << 0 << " ";
    }
}
