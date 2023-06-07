#include "iostream"
#include <cmath>
#include <string.h>

using namespace std;

class Mystring {
    char* string_content;
    int string_length;
    int memory_capacity;

public:
    Mystring(int capacity);
    Mystring(const char* str);
    Mystring(const Mystring& str);
    ~Mystring();

    int capacity() const;
    void reserve(int size);
    int length() const;

    void print() const;
    void println() const;
    char at(int i)const;
    Mystring& assign(const Mystring& str);
    Mystring& assign(const char* str);
    Mystring& insert(int roc, const Mystring& str);
    Mystring& insert(int loc, const char* str);
    Mystring& insert(int roc,char c);

    Mystring& erase(int loc, int num);

    int find(int find_from, Mystring& str) const;
    int find(int find_from, const char* str) const;
    int find(int find_from, char c) const;

    int compare(const Mystring& str) const;
    bool operator==(Mystring& str);
};
Mystring::Mystring(int capacity) {
    string_content = new char[capacity];
    string_length = 0;
    memory_capacity = capacity;
}

Mystring::Mystring(const char *str) {
    string_length = 0;
    while (str[string_length++]) { }

    memory_capacity = string_length;
    string_content = new char[string_length];

    for (int i=0;i!=string_length;i++) string_content[i] = str[i];
}
Mystring::Mystring(const Mystring &str) {
    string_length = str.string_length;
    string_content = new char[string_length];
    for (int i = 0; i != string_length; i++)
        string_content[i] = str.string_content[i];
}
Mystring::~Mystring(){ delete[] string_content;}
int Mystring::length() const {return string_length;}

void Mystring::print() const {
    for (int i=0;i!=string_length;i++){
        cout<<string_content[i];
    }
}
void Mystring::println() const {
    for (int i=0;i!=string_length;i++){
        cout<<string_content[i];
    }
    cout<<endl;
}
Mystring& Mystring::assign(const Mystring &str) {
    if(str.string_length>string_length){
        delete[] string_content;

        string_content = new char[str.string_length];
        memory_capacity = str.string_length;
    }
    for(int i=0;i!=str.string_length;i++){
        string_content[i] = str.string_content[i];
    }

    string_length = str.string_length;

    return *this;
}
Mystring& Mystring::assign(const char* str) {
    int str_length = strlen(str);
    if(str_length>string_length){
        delete[] string_content;

        string_content = new char[str_length];
        memory_capacity = str_length;
    }
    for(int i=0;i!=str_length;i++){
        string_content[i] = str[i];
    }

    string_length = str_length;

    return *this;
}
int Mystring::capacity() const {return memory_capacity;}
void Mystring::reserve(int size) {
    if (size>memory_capacity){
        char *prev_string_content = string_content;

        string_content = new char[size];
        memory_capacity = size;
        for(int i=0;i!=string_length;i++){
            string_content[i] = prev_string_content[i];
        }
        delete[] prev_string_content;
    }
}
char Mystring::at(int i) const {
    if (i>=string_length || i<0)
        return NULL;
    else
        return string_content[i];
}
Mystring& Mystring::insert(int loc, const char *str) {
    Mystring temp(str);
    return insert(loc, temp);
}
Mystring& Mystring::insert(int loc,char c){
    Mystring temp(c);
    return insert(loc,temp);
}
Mystring& Mystring::insert(int loc,const Mystring& str){
    if (loc<0 || loc > string_length) return *this;

    if (string_length + str.string_length > memory_capacity){

        if(string_length+ str.string_length >memory_capacity){
            memory_capacity *=2;
        }else{
            memory_capacity = string_length + str.string_length;
        }

        char* prev_string_content = string_content;
        string_content = new char[memory_capacity];

        int i;
        for(i=0;i<loc;i++){
            string_content[i] = prev_string_content[i];
        }
        for(int j=0;j!=str.string_length;j++){
            string_content[i+j] = str.string_content[j];
        }
        for(;i<string_length;i++){
            string_content[str.string_length + i] = prev_string_content[i];
        }
        delete[] prev_string_content;

        string_length = string_length + str.string_length;
        return *this;
    }
    for(int i=string_length-1;i>=loc;i--){
        string_content[i + str.string_length] = string_content[i];
    }

    for(int i=0;i<str.string_length;i++)
        string_content[i+loc] = str.string_content[i];

    string_length = string_length + str.string_length;
    return *this;
}
Mystring& Mystring::erase(int loc, int num) {
    if (num<0||loc<0||loc>string_length) return *this;
    for(int i= loc+num;i<string_length;i++){
        string_content[i-num] = string_content[i];
    }

    string_length -=num;
    return *this;
}
int Mystring::find(int find_from, Mystring& str) const {
    int i, j;
    if (str.string_length == 0) return -1;
    for (i = find_from; i <= string_length - str.string_length; i++) {
        for (j = 0; j < str.string_length; j++) {
            if (string_content[i + j] != str.string_content[j]) break;
        }
        if (j == str.string_length) return i; }
    return -1;
}
int Mystring::find(int find_from, const char* str) const { Mystring temp(str);
    return find(find_from, temp);
}
int Mystring::find(int find_from, char c) const {
    Mystring temp(c);
    return find(find_from, temp);
}
int Mystring::compare(const Mystring& str) const {
// (*this) - (str) 을수행해서그1, 0, -1 로그결과를리턴한다 // 1 은(*this) 가사전식으로더뒤에온다는의미. 0 은두문자열
// 이같다는의미, -1 은(*this) 가사전식으로더앞에온다는의미이다.
    for (int i = 0; i < std::min(string_length, str.string_length); i++) {
        if (string_content[i] > str.string_content[i])
            return 1;
        else if (string_content[i] < str.string_content[i]) return -1;
    }
    if (string_length == str.string_length) return 0;
    else if (string_length > str.string_length)
        return 1;
    return -1;
}
bool Mystring::operator==(Mystring &str) {
    return !compare(str);
}
int main() {
    Mystring str1("a word");
    Mystring str2("sentence");
    Mystring str3("sentence");
    if (str1 == str2)
        std::cout << "str1 와 str2 같다." << std::endl;
    else
        std::cout << "st1 와 str2 는 다르다." << std::endl;
    if (str2 == str3)
        std::cout << "str2 와 str3 는 같다." << std::endl;
    else
        std::cout << "st2 와 str3 는 다르다" << std::endl; }
