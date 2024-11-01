#include <thread>
#include <condition_variable>
#include <functional>
#include <mutex>
#include <future>

std::mutex gMutex;
std::condition_variable gCdVar;

class ZeroEvenOdd {
private:
    int n;
    int m_next;
    bool m_zero_turn;

public:
    ZeroEvenOdd(int n) : n(n), m_next(1), m_zero_turn(true) {}

    void zero(std::function<void(int)> printNumber) {
        for (int i = 0; i < n; ++i) {
            std::unique_lock<std::mutex> lock(gMutex);
            gCdVar.wait(lock, [&] { return m_zero_turn; });
            printNumber(0);
            m_zero_turn = false;
            gCdVar.notify_all();
        }
    }

    void even(std::function<void(int)> printNumber) {
        for (int i = 2; i <= n; i += 2) {
            std::unique_lock<std::mutex> lock(gMutex);
            gCdVar.wait(lock, [&] { return !m_zero_turn && m_next % 2 == 0; });
            printNumber(m_next++);
            m_zero_turn = true;
            gCdVar.notify_one();
        }
    }

    void odd(std::function<void(int)> printNumber) {
        for (int i = 1; i <= n; i += 2) {
            std::unique_lock<std::mutex> lock(gMutex);
            gCdVar.wait(lock, [&] { return !m_zero_turn && m_next % 2 != 0; });
            printNumber(m_next++);
            m_zero_turn = true;
            gCdVar.notify_one(); 
        }
    }
};
