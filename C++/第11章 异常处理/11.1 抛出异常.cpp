#include <iostream>
#include <vector>
using namespace std;
//栈类实例iStack,构造函数，私有成员，公有函数
class iStack{
    public:
        iStack(int capacity):_stack(capacity),_top(0){};
        bool pop(int &top_value);
        bool push(int value);
        bool empty();
        bool full();
        void display();
        int size();
    private:
        vector<int> _stack;
        int _top;
};
//栈类的实例化
iStack stack(20);
//定义压入时栈满和弹出时栈空的异常类
class popOnEmpty{};
class pushOnFull{};
//抛出异常：必须抛出一个异常对象（表达式是一个异常对象构造函数）
int main(){
    throw popOnEmpty();
//抛出枚举类型的异常对象
    return 0;
}
//使用异常处理重写pop()和push()函数
void iStack::pop(int &top_value){
    if(empty())
        throw popOnEmpty();
    top_value=_stack[--_top];//这里--在前面，所以实际--top表达式的值为栈顶值，将栈顶值弹出后，栈顶位置-1
    cout<<"iStack::pop():"<<top_value<<endl;
}
void iStack::push(int value){
    if(full())
        throw pushOnFull();
    _stack[_top++]=value;//这里++在后面，将栈顶位置+1后，赋给其压进来的值
}
    