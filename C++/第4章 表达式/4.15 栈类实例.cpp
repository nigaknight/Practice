#include <iostream>
#include <vector>
using namespace std;

//1 创建一个只支持int类型的栈，包含压入、弹出、判断空满和判断长度的功能
class iStack{
    public:
        iStack(int capacity):_stack(capacity),_top(0){}
        bool pop(int &value);
        bool push(int value);
        bool full();
        bool empty();
        int size();
        void display();
    private:
        int _top;
        vector<int> _stack;
};

//2 判断长度的函数的定义
inline int iStack::size(){return _top;}

//3 判断栈空的函数的定义
inline bool iStack:empty(){
    return _top?false:true;
}

//4 判断栈满的函数的定义
inline bool iStack:full(){
    return _top<_stack.size()-1?false:true;
}

//5 弹出函数的定义
bool iStack:pop(int &top_value){
    if(empty())
        return false;
    top_value=_stack[--_top];
    cout<<"pop()"<<top_value<<endl;
    return ture;
}

//6 压入函数的定义
bool iStack:push(int value){    
    cout<<"push("<<value<<")\n";
    if(full())
        return false;
    _stack[_top++]=value;
    return true;
}

//7 查看栈的内容的函数的定义
void iStack:display(){
    if(!size())
        {cout<<"(0)\n"<<endl;return;}
    cout<<"("<<size()<<")(bot: ";
    for(int ix=0;ix<_top;++ix)
        cout<<_stack[ix]<<" ";
    cout<<" :top)\n";
}