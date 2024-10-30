#include <mutex>
#include <condition_variable>

std::mutex gMutex;
std::condition_variable gCdVar;

class FooBar {
private:
    int n;
    bool mfoo;

public:
    FooBar(int n) {
        this->n = n;
        this->mfoo = true;
    }

    void foo(std::function<void()> printFoo) {
        
        for (int i = 0; i < n; i++) {
            std::unique_lock<std::mutex> lock(gMutex);
            gCdVar.wait(lock, [&]{return this->mfoo;});
        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();
            this->mfoo = !this->mfoo;
            gCdVar.notify_all();
        }
    }

    void bar(std::function<void()> printBar) {
        
        for (int i = 0; i < n; i++) {
            std::unique_lock<std::mutex> lock(gMutex);
            gCdVar.wait(lock, [&]{return !this->mfoo;});
        	// printBar() outputs "bar". Do not change or remove this line.
        	printBar();
            this->mfoo = !this->mfoo;
            gCdVar.notify_all();
        }
    }
};