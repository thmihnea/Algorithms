#include <iostream>
#include <functional>
#include <string>

#define INITIAL_HASH_SIZE 2

template <class K, class V>
class Node 
{
private:
    Node<K, V>* next;
    K key;
    V value;
public:
    Node(const K& key, const V& value) : key(key), value(value), next(nullptr) {}
    Node(K&& key, V&& value) : key(std::move(key)), value(std::move(value)), next(nullptr) {}
    Node() : key(), value(), next(nullptr) {}
    ~Node() {}

    Node<K, V>* GetNext() 
    {
        return this->next;
    }

    void SetNext(Node<K, V>* next) 
    {
        this->next = next;
    }

    void SetValue(const V& value) 
    {
        this->value = value;
    }

    const K& GetKey() const 
    {
        return this->key;
    }

    const V& GetValue() const 
    {
        return this->value;
    }
};

template <class K, class V>
class HashTable 
{
private:
    Node<K, V>** array;
    int max_size;
    int size;
    
    int hash(const K& key, int table_size) const 
    {
        return std::hash<K>{}(key) % table_size;
    }
    
    void resize() 
    {
        int new_size = this->max_size;
        if (this->size > 3 * this->max_size / 4) 
        {
            new_size = 2 * new_size;
        } else if (this->size < this->max_size / 4) 
        {
            new_size = new_size / 2;
        }
        if (new_size == this->max_size) 
        {
            return;
        }

        auto new_array = new Node<K, V>*[new_size];
        for (int i = 0; i < new_size; ++i) 
        {
            new_array[i] = nullptr;
        }

        for (int i = 0; i < this->max_size; ++i) 
        {
            Node<K, V>* node = this->array[i];
            while (node != nullptr) 
            {
                auto next = node->GetNext();
                int new_index = hash(node->GetKey(), new_size);
                node->SetNext(new_array[new_index]);
                new_array[new_index] = node;
                node = next;
            }
        }

        delete[] this->array;
        this->array = new_array;
        this->max_size = new_size;
    }
    
public:
    HashTable() : max_size(INITIAL_HASH_SIZE), size(0) 
    {
        this->array = new Node<K, V>*[INITIAL_HASH_SIZE];
        for (int i = 0; i < this->max_size; ++i) 
        {
            this->array[i] = nullptr;
        }
    }

    ~HashTable() 
    {
        for (int i = 0; i < this->max_size; ++i) 
        {
            Node<K, V>* node = this->array[i];
            while (node != nullptr) 
            {
                Node<K, V>* to_delete = node;
                node = node->GetNext();
                delete to_delete;
            }
        }
        delete[] this->array;
    }

    const V& get(const K& key)
    {
        int index = hash(key, this->max_size);
        Node<K, V>* current = this->array[index];
        while (current != nullptr)
        {
            if (current->GetKey() == key)
            {
                return current->GetValue();
            }
            current = current->GetNext();
        }
        throw std::runtime_error("Key was not found!");
    }

    void put(const K& key, const V& value) 
    {
        int index = hash(key, this->max_size);
        Node<K, V>* current = this->array[index];
        while (current != nullptr) 
        {
            if (current->GetKey() == key) 
            {
                current->SetValue(value);
                return;
            }
            current = current->GetNext();
        }
        
        Node<K, V>* node = new Node<K, V>(key, value);
        node->SetNext(this->array[index]);
        this->array[index] = node;

        this->size++;
        this->resize();
    }
};

int main() 
{
    std::cin.tie(nullptr);
    std::ios_base::sync_with_stdio(true);

    auto table = HashTable<int, std::string>();
    table.put(1, "test1");
    table.put(2, "test2");

    std::cout << "\n" << table.get(1) << " " << table.get(2) << "\n";
}
