#include <functional>
#include <mutex>
#include <condition_variable>
#include <future>

std::mutex gMutex;
std::condition_variable gCdVar;

std::future_status status;

class H2O {
private:
    int m_hydrogenCount;
public:
    H2O() : m_hydrogenCount(0) {}

    void hydrogen(std::function<void()> releaseHydrogen) {
        std::unique_lock<std::mutex> lock(gMutex);
        gCdVar.wait(lock, [&]{ return this->m_hydrogenCount < 2; });
        releaseHydrogen();
        this->m_hydrogenCount += 1;
        gCdVar.notify_all();
    }

    void oxygen(std::function<void()> releaseOxygen) {
        std::unique_lock<std::mutex> lock(gMutex);
        gCdVar.wait(lock, [&]{ return this->m_hydrogenCount == 2; });
        releaseOxygen();
        this->m_hydrogenCount = 0;
        gCdVar.notify_all();
    }
};