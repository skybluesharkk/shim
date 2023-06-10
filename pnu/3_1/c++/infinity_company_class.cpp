#include "iostream"
#include "string"

using namespace std;

class Employee {
protected:
    string name;
    int age;
    string position;
    int rank;

public:
    Employee(string name,int age, string position, int rank):
            name(name),age(age),position(position),rank(rank){}

    Employee(const Employee& employee) {
        name = employee.name;
        age = employee.age;
        position = employee.position;
        rank = employee.rank;
    }

    Employee() {}

    virtual void print_info() {
        cout<<name<<position<<age<<calculate_pay()<<endl;
    }
    virtual int calculate_pay() {
        return 200 + rank * 50;
    }
};

class Manager : public Employee {
    int year_of_service;

public:
    Manager(string name, int age,string position,int rank,int year_of_service)
    : Employee(name,age,position,rank),year_of_service(year_of_service) {}

    Manager(const Manager& manager)
    : Employee(manager.name,manager.age,manager.position,manager.rank){
        year_of_service = manager.year_of_service;
    }

    Manager() : Employee() {}

    int calculate_pay() override { return 200 + rank*50+5*year_of_service;}
    void print_info() override {
        cout<<name<<position<<age<<year_of_service<<calculate_pay()<<endl;

    }
};

class EmployeeList {
    int alloc_employee;

    int current_employee;

    Employee** employee_list;


public:
    EmployeeList(int alloc_employee) : alloc_employee(alloc_employee){
        employee_list = new Employee * [alloc_employee];
        current_employee = 0;
    }

    void add_employee(Employee* employee){
        employee_list[current_employee] = employee;
        current_employee++;
    }

    int current_employee_num(){ return current_employee; }

    void print_employee_info() {
        int total_pay = 0;
        for (int i=0;i<current_employee;i++){
            employee_list[i]->print_info();
            total_pay += employee_list[i]->calculate_pay();
        }
        cout<<"total"<<total_pay<<endl;
    }
    ~EmployeeList() {
        for(int i=0;i<current_employee;i++){
            delete employee_list[i];
        }
        delete[] employee_list;
    }
};
int main(){
    EmployeeList emp_list(10);
    emp_list.add_employee(new Employee("노홍철",34,"평사원",1));
    emp_list.add_employee(new Employee("하하",34,"평사원",1));
    emp_list.add_employee(new Manager("유재석",41,"부장",7,12));
    emp_list.add_employee(new Manager("정준하",43,"과장",4,15));
    emp_list.add_employee(new Manager("박명수",43,"차장",5,13));
    emp_list.add_employee(new Employee("정형돈",36,"대리",2));
    emp_list.add_employee(new Employee("길",36,"인턴",-2));
    emp_list.print_employee_info();
    return 0;
}
