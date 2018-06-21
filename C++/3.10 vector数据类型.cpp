//vector类是内置数组的一种替代表示，属于C++标准库

//1、为了使用vector，必须包含相关头文件
#include <vector>
#include <iostream>
#include <string>
using namespace std;
//2、数组习惯vector的定义：定义一个已知长度的vector
vector<int> ivec(10);
//这和下列内置数组的定义相似
int ia[10];
//3、可以使用下标操作符访问vector的元素

//下面程序是将vector的元素通过下标操作符一一赋值给内置数组的元素
void simple_example(){
    const int elem_size=10;
    vector<int> ivec(elem_size);
    int ia[elem_size];
    for(int ix=0;ix<elem_size;++ix){
        ia[ix]=ivec[ix];
    }
}
//4、可以使用size()获得vector的大小，也可以使用empty()判断数组是否为空

//下面程序是打印vector数组中的元素
void print_vector(vector<int> ivec){
    if(ivec.empty())
        return;
    for(int ix=0;ix<ivec.size();++ix){
        cout<<ivec[ix]<<' ';
    }
}
//5、可以为vector的每一个元素提供一个显示的初始值来实现初始化
vector<int> ivec2(10,-1);
//6、可以将vector初始化为一个已有数组的全部或一部分
int ib[6]={0,1,5,24,-123,43};
vector<int> ivec3(ia,ia+6);
vector<int> ivec4(&ia[2],&ia[5]);
//7、vector可被另一个vector初始化，或被赋给另一个vector
vector<string> svec;
void init_and_assign(){
    vector<string> user_names(svec);
    svec=user_names;
}
//8、STL方法vector的定义：定义一个空vector
int main(){
    vector<string> text; 
    string word;
    //9、使用push_back()向vector中插入元素 text,word
    while(cin>>word){
        text.push_back(word);
    }
    //下面程序仍然使用下标操作符迭代访问元素
    cout<<"words read are: \n";
    for(int ix=0;ix<text.size();++ix){
        cout<<text[ix]<<' ';
    }
    cout<<endl;
    //10、使用vector的begin()和end()所返回的迭代器
    cout<<"words read are: \n";
    for(vector<string>::iterator it=text.begin();it!=text.end();++it){
        cout<<*it<<' ';
    }
    cout<<endl;
}





