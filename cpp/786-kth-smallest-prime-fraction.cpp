#include <algorithm>
#include <vector>

struct HeapEntry
{
    int p;
    int q;
    float fraction;

    HeapEntry() = default;

    HeapEntry(int p, int q) : p(p), q(q), fraction((p * 1.0f) / (q * 1.0f)) {};
};

class Solution {
public:
    std::vector<int> kthSmallestPrimeFraction(std::vector<int>& arr, int k) {
        std::vector<HeapEntry> heap;
        auto compare = [](HeapEntry& a, HeapEntry& b){
            return a.fraction < b.fraction;
        };
        for (size_t i = 0; i < arr.size(); i++)
        {
            for (size_t j = 0; j < arr.size(); j++)
            {
                HeapEntry entry(arr[i], arr[j]);
                heap.push_back(entry);
                std::push_heap(heap.begin(), heap.end(), compare);
                if (heap.size() <= k) continue;
                std::pop_heap(heap.begin(), heap.end(), compare);
                heap.pop_back();
            }
        }
        return {heap[0].p, heap[0].q};
    }
};