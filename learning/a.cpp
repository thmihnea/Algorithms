#include <iostream>
#include <vector>
#include <thread>
#include <condition_variable>

template <typename T>
void print(T* array, uint32_t size)
{
    for (size_t i = 0; i < size; i++)
    {
        std::cout << array[i] << " ";
    }
    std::cout << '\n';
}

template <typename T>
void print(std::vector<T> vec)
{
    for (auto& entry : vec)
    {
        std::cout << entry << " ";
    }
    std::cout << '\n';
}

int main(int argc, char** argv)
{
    std::vector<int> v = {1, 2, 3, 4};
    print(v);
    return EXIT_SUCCESS;
}