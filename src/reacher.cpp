#include <string>
#include <algorithm>
#include <utility>

class Date {
private:
    int year;
    int month;
    int day;
public:
    Date(int day, int month, int year) {
        this->day = day;
        this->month = month;
        this->year = year;
    }

    Date() {
        this->year = 2021;
        this->month = 4;
        this->day = 12;
    }

    int get_year() const {
        return this->year;
    }

    void set_year(int _year) {
        this->year = _year;
    }

    int get_month() const {
        return this->month;
    }

    void set_month(int _month) {
        this->month = _month;
    }

    int get_day() const {
        return this->day;
    }

    void set_day(int _day) {
        this->day = _day;
    }
};

class Gender {
private:
    char type;
public:
    Gender() {
        this->type = 'u';
    }

    explicit Gender(char type) {
        if (tolower(type) != 'm' && tolower(type) != 'f' && tolower(type) != 'u') {
            throw std::exception("gender type has to be either 'm' or 'f' or 'u'!");
        }
        this->type = type;
    }

    explicit Gender(std::string type) {
        std::transform(type.begin(), type.end(), type.begin(), tolower);
        if (type != "male" && type != "female" && type != "unknown") {
            throw std::exception("gender type has to be either 'male' or 'female' or 'unknown'!");
        }
        type == "male" ? this->type = 'm' : this->type = 'f';
    }

    std::string get_gender() const {
        if (type == 'u') return "universitate eboy cringe kid / unknown";
        return (type == 'm') ? "male" : "female";
    }
};

class Address {
private:
    int number;
    std::string street_name;
public:
    Address(int number, std::string street_name) {
        this->number = number;
        this->street_name = std::move(street_name);
    }

    Address() {
        this->number = 0;
        this->street_name = "Groove Street";
    }
};

class Person {
private:
    long cnp;
    std::string name;
    std::string surname;
    Date birth_date;
    Gender gender;
    Address address;
    float height;
    std::string eye_color;
public:
    Person(long cnp, std::string name, std::string surname, Date birth_date, Gender gender, Address address, float height, std::string eye_color) {
        this->cnp = cnp;
        this->name = std::move(name);
        this->surname = std::move(surname);
        this->birth_date = birth_date;
        this->gender = gender;
        this->address = std::move(address);
        this->height = height;
        this->eye_color = std::move(eye_color);
    }
    
    ~Person() {
        delete[] &this->name;
        delete[] &this->surname;
        delete[] &this->eye_color;
        delete &this->birth_date;
        delete &this->gender;
        delete &this->address;
    }

    long get_cnp() const {
        return this->cnp;
    }

    void set_cnp(long _cnp) {
        this->cnp = _cnp;
    }

    std::string get_name() {
        return this->name;
    }

    void set_name(std::string &_name) {
        this->name = _name;
    }

    std::string get_surname() {
        return this->surname;
    }

    void set_surname(std::string &_surname) {
        this->surname = _surname;
    }

    Date* get_birth_date() {
        return &this->birth_date;
    }

    void set_birth_date(Date &_date) {
        this->birth_date = _date;
    }

    Gender* get_gender() {
        return &this->gender;
    }

    void set_gender(Gender &_gender) {
        this->gender = _gender;
    }

    Address* get_address() {
        return &this->address;
    }

    void set_address(Address &_address) {
        this->address = _address;
    }

    float get_height() const {
        return this->height;
    }

    void set_height(float _height) {
        this->height = _height;
    }

    std::string get_eye_color() {
        return this->eye_color;
    }

    void set_eye_color(std::string &_eye_color) {
        this->eye_color = _eye_color;
    }
};

int main(int argc, char* argv[]) {

}
