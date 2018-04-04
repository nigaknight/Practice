//基于公式的线性表类LinearList
//包括的操作有构造、析构、是否为空、长度、寻找元素、寻找元素位置、删除元素、插入元素和将元素放入输出流OUT中
template <class T>
class LinearList{
    public:
        LinearList(int MaxListSize=10){}
        ~LinearList(){delete[] element;}
        bool IsEmpty() const {return length==0;}
        int length() const {return length;}
        bool Find(int k, T& x) const;
        int Search(const T& x) const;
        LinearList<T>& Delete(int k,T& x);
        LinearList<T>& Insert(int k,const T& x);
        void Output(ostream& out) const;
    private:
        int length;
        int MaxSize;
        T *element;
}