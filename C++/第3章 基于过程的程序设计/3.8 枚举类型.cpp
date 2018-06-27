#include <iostream>
using namespace std;

//1 使用常量关联打开文件的不同状态
const int input=1;
const int output=2;
const int append=3;
bool open_file(string file_name,int open_type);
open_file("Phoniex_and_the_crane",append);

//2 定义代替上述作用的枚举类型
enum open_modes{input=1,output,append};
bool open_file(string file_name,open_modes om);
open_file("Phoniex_and_the_crane",append);

//3 不能传递整数值
open_file("Jonah",1);//错误！

//4 可以声明枚举类型对象，代替枚举成员
open_modes om=input;
om=append;
open_file("TailTell",om);

//5 不能打印枚举成员名称
cout<<input<<endl;//只能打印出对应的整数值

//6 不能使用枚举类型进行迭代
for(open_modes ix=input;ix!=append;++ix){
    //todo
}//错误！

//7 缺省赋值的枚举类型
enum Forms{shape,sphere,cylinder,polygon};

//8 显式赋值的枚举类型
enum Points{point2d=2,point2w,point3d=3,point3w};

//9 必要时，枚举类型会自动变为算术类型
const int array_size=1024;
int crunk_size=array_size*point2d;

//Conclusion:枚举类型和int，char等一样是一个类型，集合形式的类型。