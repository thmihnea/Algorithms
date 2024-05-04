#include <vector>
#include <algorithm>

using std::vector, std::sort;

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int boats_count = 0;
        while (people.size() > 0)
        {
            int last = people[people.size() - 1];
            int first = people[0];
            people.pop_back();
            boats_count++;
            if (last + first <= limit && people.size() > 0)
            {
                people.erase(people.begin());
            }
        }
        return boats_count;
    }
};