#include <thread>
#include <iostream>

void print()
{
    std::cout << "this was executed concurrently!" << '\n';
}

int main(int argc, char** argv)
{
    std::thread t1(&print);
    t1.join();
    return EXIT_SUCCESS;
}