---
title: 专业课C语言部分合集
tags:
  - 考研
  - C语言
cover: img/c.jpeg
abbrlink: 69ae16d2
date: 2022-08-07 13:48:20
---

## C语言合集

### 第一次作业

1.输入2个整数，求两数的平方和并输出。

```cpp
#include<iostream>
#include<cstdio>
using namespace std;
int main(){
    int a,b;
    cin>>a>>b;
    cout<< a*a + b*b <<endl;
    return 0;
}
```



2.输入一个圆半径(r)当r>=0时，计算并输出圆的面积和周长，否则，输出提示信息。

```cpp
#include<iostream>
#define PI 3.14
using namespace std;
int main(){
    int r;
    cin>>r;
    if(r>0){
        cout<<PI*r*r<<endl;
        cout<<2*PI*r<<endl;
    }else{
        cout<<"r必须大于等于0"<<endl;
    }
    return 0;
}
```

3.函数y=f(x)可表示为:
2x+1 (x<0)
y= 0 (x=0)
2x-1 (x>0)
编程实现输入一个x值，输出值。

```cpp
#include<iostream>
using namespace std;
int main(){
    int x;
    cin>>x;
    if(x<0){
        cout<<2*x+1<<endl;
    }else if(x==0){
        cout<<'0'<<endl;
    }else if(x>0){
        cout<<2*x-1;
    }
    return 0;
}
```

4、编写一个程序,从4个整数中找出最小的数,并显示此数。

```cpp
#include<iostream>
using namespace std;
int main(){
    int a,b,c,d,e,f,g;
    cin>>a>>b>>c>>d;
    e=min(a,b);
    f=min(e,c);
    g=min(d,f);
    cout<<g<<endl;
    return 0;
}
```

5.有一函数当x<0时y=1,当x>0时，y=3,当x=0时y=5，编程，从键盘输入一个x值，输出y值。

```cpp
#include<iostream>
using namespace std;
int main(){
    int x;
    cin>>x;
    if(x<0){
        cout<<1;
    }else if(x==0){
        cout<<5;
    }else{
        cout<<3;
    }
}
```

6.判断闰年

```cpp
#include<iostream>
using namespace std;
int main(){
    int year;
    cin>>year;
    if(year%4==0&&year%100!=0||year%400==0){
        cout<<year<<"是闰年"<<endl;
    }else{
                cout<<year<<"不是闰年"<<endl;
    }
    return 0;
}
```



7.判断输入字符是否为字母

```cpp
#include<iostream>
using namespace std;
int main(){
    char a;
    cin>>a;
    if(a>=65&&a<=90||a>=97&&a<=122){
        cout<<a<<"是字母";
    }else{
        cout<<a<<"不是字母";
    }
}

```



12.从键盘上输入一个百分制成绩score,按下列原则输出其等级: score>=90等级为A; 80<=score<90， 等级为B;70≤score<80,等级为C; 60<=score<70, 等级为D; score<60, 等级为E。

```cpp
#include<iostream>
using namespace std;
int main(){
    int score;
    cin>>score;
    switch(score/10){
        case 10:
        case 9:cout<<'A'<<endl;break;
        case 8:cout<<'B'<<endl;break;
        case 7:cout<<'C'<<endl;break;
        case 6:cout<<'D'<<endl;break;
        default:
        cout<<'E'<<endl;break;
    }
}
```

1.求n的阶乘
n的阶乘=n * n-1 * n-2 * n -3...* 2 *  1

```cpp
#include<iostream>
using namespace std;
int main(){
    int n,s=1;
    cin>>n;
    for(int i=1;i<=n;i++){
        s*=i;
    }
    cout<<s<<endl;
    return 0;
}

```

14.从键盘输入10个整数，统计其中正数、负数和零的个数，并在屏幕上输出。

```cpp
#include<iostream>
using namespace std;
int a[10];
int z,f,l;
int main(){
    for(int i=0;i<10;i++){
        cin>>a[i];
    }
    for(int i=0;i<10;i++){
        if(a[i]>0){
            z++;
        }else if(a[i]<0){
            f++;
        }else {
            l++;
        }
    }
    cout<<z<<" "<<f<<" "<<l<<endl;
    return 0;
}

```

求1~1000之间能被13整除的最大的数

```cpp
#include<iostream>
using namespace std;
int main(){
    int t;
    for(int i=1;i<100;i++){
        if(i*13>1000){
            t=i-1;
            break;
        }
    }
    cout<<t<<endl;
    return 0;
}

```

“水仙花数”是指一一个三位数,其各位数的立方之和正好等于该数本身,例如，153=1^3+5^3+3^3 ,请输出所有的水仙花数。

```cpp
#include<iostream>
using namespace std;
int main(){
    int a,b,c;
    for(int i=100;i<1000;i++){
        a=i/100;//百位
        b=i/10%10;//十位
        c=i%10;//个位
        if(i==a*a*a+b*b*b+c*c*c){
            cout<<i<<" ";
        }
    }
    return 0;
}

```

从键盘输入整数n，输出1+3+5+7+...+n,前n项的和。

```cpp
#include<iostream>
using namespace std;
int main(){
    int n,s=0;
    cin>>n;
    for(int i=1;i<=n;i+=2){
        s+=i;
    }
    cout<<s;
    return 0;
}


```

编写程序，求满足下列条件的最大的n:
1^2+2^2+3^2+.....+n^2< 1000

```cpp
#include<iostream>
using namespace std;
int main(){
    int s=0,t;
    for(int i=1;i<32;i++){
        if(s<1000){
            s+=i*i;
        }else{
            t=i-2;
            break;
        }
    }
    cout<<t<<endl;
    return 0;
}

#include<iostream>
using namespace std;
int main(){
    int s=0,t;
    for(int i=1;i<32;i++){
        s+=i*i;
        if(s>1000){
            t=i-1;
            break;
        }
    }
    cout<<t<<endl;
    return 0;
}

```

输入一批非0的数，直到输入0为止，计算其中奇数的平均值和偶数的乘积

```cpp
#include<iostream>
using namespace std;
#define N 100010
int main(){
    int a[N];
    int i=0,j=0,t=0,num,pj=0,ji=1;
    while(cin>>a[i]&&a[i]!=0){
        i++;
    }
    num=i-1;
    while(j<=num){
        if(a[j]%2){
            pj+=a[j];
            t++;
        }else{
            ji*=a[j];
        }
        j++;
    }
    cout<<pj*(1.0)/t<<" "<<ji<<endl;
    return 0;
}

```

### 第二次作业

1.求n的阶乘
n的阶乘=n * n-1 * n-2 * n -3...* 2 *  1

```cpp
#include<iostream>
using namespace std;
int main(){
    int n,s=1;
    cin>>n;
    for(int i=1;i<=n;i++){
        s*=i;
    }
    cout<<s<<endl;
    return 0;
}

```

14.从键盘输入10个整数，统计其中正数、负数和零的个数，并在屏幕上输出。

```cpp
#include<iostream>
using namespace std;
int z,f,l;
int main(){
    int a[10];
    for(int i=0;i<10;i++){
        cin>>a[i];
    }
    for(int i=0;i<10;i++){
        if(a[i]>0){
            z++;
        }else if(a[i]<0){
            f++;
        }else {
            l++;
        }
    }
    cout<<z<<" "<<f<<" "<<l<<endl;
    return 0;
}

```

求1~1000之间能被13整除的最大的数

```cpp
#include<iostream>
using namespace std;
int main(){
    int t;
    for(int i=1;i<100;i++){
        if(i*13>1000){
            t=i-1;
            break;
        }
    }
    cout<<t<<endl;
    return 0;
}

```

“水仙花数”是指一一个三位数,其各位数的立方之和正好等于该数本身,例如，153=1^3+5^3+3^3 ,请输出所有的水仙花数。

```cpp
#include<iostream>
using namespace std;
int main(){
    int a,b,c;
    for(int i=100;i<1000;i++){
        a=i/100;//百位
        b=i/10%10;//十位
        c=i%10;//个位
        if(i==a*a*a+b*b*b+c*c*c){
            cout<<i<<" ";
        }
    }
    return 0;
}

```

从键盘输入整数n，输出1+3+5+7+...+n,前n项的和。

```cpp
#include<iostream>
using namespace std;
int main(){
    int n,s=0;
    cin>>n;
    for(int i=1;i<=n;i+=2){
        s+=i;
    }
    cout<<s;
    return 0;
}


```

编写程序，求满足下列条件的最大的n:
1^2+2^2+3^2+.....+n^2< 1000

```cpp
#include<iostream>
using namespace std;
int main(){
    int s=0,t;
    for(int i=1;i<32;i++){
        if(s<1000){
            s+=i*i;
        }else{
            t=i-2;
            break;
        }
    }
    cout<<t<<endl;
    return 0;
}

#include<iostream>
using namespace std;
int main(){
    int s=0,t;
    for(int i=1;i<32;i++){
        s+=i*i;
        if(s>1000){
            t=i-1;
            break;
        }
    }
    cout<<t<<endl;
    return 0;
}

```

输入一批非0的数，直到输入0为止，计算其中奇数的平均值和偶数的乘积

```cpp
#include<iostream>
using namespace std;
#define N 100010
int main(){
    int a[N];
    int i=0,j=0,t=0,num,pj=0,ji=1;
    while(cin>>a[i]&&a[i]!=0){
        i++;
    }
    num=i-1;
    while(j<=num){
        if(a[j]%2){
            pj+=a[j];
            t++;
        }else{
            ji*=a[j];
        }
        j++;
    }
    cout<<pj/t<<" "<<ji<<endl;
    return 0;
}

```

pi的近似值

```cpp
#include<iostream>
#include<cmath>
using namespace std;
int main(){
    double pi=0;
    long i=1;
    while(i*i<=1e8){
        pi=pi+1.0/(i*i);
        i++;
    }
    pi=sqrt(6.0*pi);
    printf("%10.6f\n",pi);
    return 0;
}

```

九九乘法表

```cpp
#include<iostream>
using namespace std;
int main(){
    for(int i=1;i<10;i++){
        for(int j=1;j<=i;j++){
            cout<<j<<'*'<<i<<'='<<i*j<<" ";
            if(i==j)cout<<endl;
        }
    }
}

```

循环输出26个字母

```cpp
#include<iostream>
using namespace std;
int main(){
    char str;
    int i=0;
    while(i<=25){
        str='a'+i;
        cout<<str<<' ';
        i++;
    }
    cout<<endl;
    i=0;
    while(i<=25){
        str='A'+i;
        cout<<str<<' ';
        i++;
    }
    return 0;
}        

```

判断数字是几位数

```cpp
#include<iostream>
using namespace std;
int main(){
    int n,cnt=0;
    cin>>n;
    if(n==0){
        cnt=1;
        cout<<cnt<<endl;
        return 0;
    }
    while(n!=0){
        cnt++;
        n/=10;
    }
    cout<<cnt<<endl;
    return 0;
}

```

计算一个数是否可以为两个素数之和

```cpp
#include<iostream>
#include<cmath>
using namespace std;
int prime(int x){
    if(x<=3)return 1;
    for(int i=2;i<=sqrt(x);i++){
        if(x%i==0)
            return 0;
    }
    return 1;
}
int main(){
    int n;
    cin>>n;
    for(int i=2;i<(n/2);i++){
        if(prime(i)&&prime(n-i)){
            cout<<i<<" "<<n-i<<endl;
        }
    }
    cout<<"不可以"<<endl;
    return 0;
}

```

统计5的个数

```cpp
#include<iostream>
using namespace std;
const int N=100010;
int main(){
    int a[N];
    int i=0,cnt=0;
    while(cin>>a[i],a[i]!=0){
        if(a[i]==5){
            cnt++;
        }
    }
    cout<<cnt<<endl;
    return 0;
}

```

### 第三次作业

1. a+b>c=>3+4=7>5=>1 b==c =>0 1&&0  0 
2. a=3 a||b+c==>1 b-c==-1 ==> 1 1||-1=1
3. a>b 3>4==0 !0=1 !c=0 1&&0=0
4. x=a=1 !1=0 0&&任何都是0
5. a+b=7 !7=0 0+c-1=4 b+c/2=4+2=6 4&&6=1

运算符优先级比较

```cpp
#include<iostream>
using namespace std;
//算术运算符优先级>比较运算符>逻辑运算符
int main(){
    int a=3,b=4,c=5,x,y;
    cout<<(a+b>c&&b==c)<<"\n";
    cout<<(a||b+c&&b-c)<<endl;
    cout<<(!(a>b)&&!c)<<endl;
    cout<<(!(x=a)&&(y=b)&&0)<<endl;
    cout<<(!(a+b)+c-1&&b+c/2)<<endl;
    return 0;
}

```

2.从键盘输入一个小于1000的正数,要求输出它的平方根(如平方根不是整数,则输出其整数部分)。要求在输入数据后先对其进行检查是否为小于1000的正数。若不是,则要求重新输入。

```cpp
#include<iostream>
#include<cmath>
using namespace std;
int main(){
    int n,t;
    cin>>n;
    while(1){
        if(n>1000){
            cin>>n;
        }else{
            t=sqrt(n);
            cout<<t<<endl;    
            return 0;
        }
    }
    return 0;
}

```

3.输入一行字符,分别统计出其中英文字母、空格、数字和其他字符的个数。

```cpp
#include<iostream>
#include<cstring>
using namespace std;
#define N 100010
int main(){
    string a;
    int len,zm,kg,num,qt;
    zm=kg=num=qt=0;
    getline(cin,a);
    len=a.length();
    cout<<len<<endl;
    for(int i=0;i<len;i++){
        if(a[i]>='0'&&a[i]<='9'){
            num++;
        }else if(a[i]==' '){
            kg++;
        }else if(a[i]>=65&&a[i]<=90||a[i]>=97&&a[i]<=122){
            zm++;
        }else{
            qt++;
        }
    }
    cout<<"字母个数"<<zm<<"数字个数"<<num<<"空格个数"<<kg<<"其他字符"<<qt<<endl;
    return 0;
}

```

企业奖金

```cpp
#include<iostream>
using namespace std;
int main(){
    int i,bonus=0;
    cin>>i;
    if(i<=100000){
        bonus+=i*.1;
    }else if(i>100000&&i<=200000){
        bonus+=10000+(i-100000)*.075;
    }else if(i>200000&&i<=400000){
        bonus+=10000+7500+(i-200000)*.05;
    }else if(i>400000&&i<=600000){
        bonus+=10000+7500+10000+(i-400000)*.03;
    }else if(i>600000&&i<=1000000){
        bonus+=10000+7500+10000+6000+(i-600000)*.015;
    }else if(i>1000000){
        bonus+=10000+7500+10000+6000+6000+(i-1000000)*.01;
    }
    cout<<bonus<<endl;
    return 0;
}

#include<iostream>
using namespace std;
int main(){
    int i,bonus=0;
    cin>>i;
    switch(i/100000){
        case 0:bonus+=i*.1;break;
        case 1:bonus+=10000+(i-100000)*.075;break;
        case 2:bonus+=10000+7500+(i-200000)*.05;break;
        case 4:bonus+=10000+7500+10000+(i-400000)*.03;break;
        case 6:bonus+=10000+7500+10000+6000+(i-600000)*.015;break;
        case 10:bonus+=10000+7500+10000+6000+6000+(i-1000000)*.01;break;
    }
        cout<<bonus<<endl;
    return 0;
}

```

求1!+2!+3!+……20!

```cpp
#include<iostream>
using namespace std;
long factorial(int n){
    long s=1;
    for(int i=1;i<=n;i++){
        s*=i;
    }
    return s;
}
int main(){
    long n=0;
    for(int i=1;i<=20;i++){
        n+=factorial(i);
    }
    cout<<n<<endl;
}

```

7.两个乒乓球队进行比赛,各出3人。甲队为A,B,C3人,乙队为X,Y,Z 3人。已抽签决定比赛名单。有人向队员打听比赛的名单,A说他不和X比,C说他不和X,Z比,请编程序找出3对赛手的名单。

```cpp
#include<iostream>
using namespace std;
int main(){
    char a,b,c;
    for(a='x';a<='z';a++){
        for(b='x';b<='z';b++){
            if(a!=b){
                for(c='x';c<='z';c++){
                    if(c!=a&&c!=b){
                        if(a!='x'&&c!='x'&&c!='z'){
                            cout<<"a==="<<a<<endl;
                            cout<<"b==="<<b<<endl;
                            cout<<"c==="<<c<<endl;
                        }
                    }
                }
            }
        }
    }
    return 0;
}

```

输出下面图形

```cpp
   *
  ***
 *****
*******
 *****
  ***
   *

```

```cpp
#include<iostream>
using namespace std;
int main(){
    for(int i=1;i<=4;i++){
        for(int j=1;j<=4-i;j++){
            cout<<" ";
        }
        for(int j=1;j<=2*i-1;j++){
            cout<<"*";
        }
        cout<<endl;
    }
    for(int i=3;i>=1;i--){
        for(int j=1;j<=4-i;j++){
            cout<<" ";
        }
        for(int j=1;j<=2*i-1;j++){
            cout<<"*";
        }
        cout<<endl;
    }
    return 0;
}


```

### 第四次作业

大小写转换

```cpp
#include<iostream>
#include<cstring>
using namespace std;
int main(){
    string a;
    cin>>a;
    int len=a.size();
    // for(int i=0;i<len;i++){
    //     if(a[i]>=65&&a[i]<=90)
    //         a[i]=a[i]+32;
    //     else if(a[i]>=97&&a[i]<=122)
    //         a[i]=a[i]-32;
    // }
        for(int i=0;i<len;i++){
        if(a[i]>='A'&&a[i]<='Z')
            a[i]=a[i]+32;
        else if(a[i]>='a'&&a[i]<='z')
            a[i]=a[i]-32;
    }
    cout<<a<<endl;
    return 0;
}

```

输入一个数组，输出数组倒序的结果。

```cpp
#include<iostream>
#include<cstring>
using namespace std;
int main(){
    int a[10];
    for(int i=0;i<10;i++){
        cin>>a[i];
    }
    for(int i=9;i>=0;i--){
        cout<<a[i]<<" ";
    }
    return 0;
}

```

输入一个字符串,判断是否为回文串(回文串:从前向后输出与从后向前输出为相同的结果)

```cpp
#include<iostream>
#include<cstring>
using namespace std;
int main(){
    string a;
    getline(cin,a);
    int len=a.length();
    for(int i=0;i<len/2;i++){
        if(a[i]==a[len-1-i]){
            continue;
        }else{
            cout<<"不是回文串"<<endl;
            return 0;
        }
    }
    cout<<"是回文串"<<endl;
    return 0;
}

#include<iostream>
#include<cstring>
using namespace std;
const int N=100010;
int main(){
    char str[N];
    scanf("%s",str);
    int flag=1;
    int len=strlen(str);
    for(int i=0,j=len-1;i<=len/2;i++,j--){
        if(str[i]!=str[j]){
            flag=0;
            break;
        }
    }
    if(flag){
        cout<<"是回文串";
    }else{
        cout<<"不是回文串";
    }
    return 0;
}

```

输入一个字符串，将字符串中
(1) 字母a用*代替
(2) 将字母a去掉

```cpp
#include<iostream>
#include<cstring>
using namespace std;
int main(){
    string a;
    getline(cin,a);
    int len=a.size();
    for(int i=0;i<len;i++){
        if(a[i]=='a'){
            a[i]='*';
        }
    }
    cout<<a;
    return 0;
}

#include<iostream>
#include<cstring>
using namespace std;
int main(){
    string a;
    getline(cin,a);
    int len=a.size();
    for(int i=0;i<len;i++){
        while(a[i]=='a'){
            for(int j=i;j<len;j++){
                a[j]=a[j+1];
            }
            len-=1;
        }
    }
    cout<<a;
    return 0;
}

#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
const int N=100010;
int main(){
    char str[N];
    scanf("%s",str);
    int len=strlen(str);
    int i=0,pos=0;
    while(i<len){
        if(str[i]=='a'){
            while(str[i]=='a')
                i++;
        }
        else
            str[pos++]=str[i++];
            
    }
    str[pos]='\0';
    printf("%s",str);
    return 0;
}

#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
const int N=100010;
int main(){
    char str[N];
    // scanf("%s",str);
    cin>>str;
    int len=strlen(str);
    for(int i=0;i<len;i++){
        if(str[i]=='a')
            str[i]='*';
    }
    cout<<str;
    return 0;
}

```

输入一个字符串，将其中的大写变小写，小写变大写

```cpp
#include<iostream>
#include<cstring>
using namespace std;
int main(){
    string a;
    cin>>a;
    int len=a.size();
    // for(int i=0;i<len;i++){
    //     if(a[i]>=65&&a[i]<=90)
    //         a[i]=a[i]+32;
    //     else if(a[i]>=97&&a[i]<=122)
    //         a[i]=a[i]-32;
    // }
        for(int i=0;i<len;i++){
        if(a[i]>='A'&&a[i]<='Z')
            a[i]=a[i]+32;
        else if(a[i]>='a'&&a[i]<='z')
            a[i]=a[i]-32;
    }
    cout<<a<<endl;
    return 0;
}

```

数组调整，左奇右偶

```cpp
#include<iostream>
using namespace std;
const int N=100010;
int main(){
    int a[N];
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    int i=0;
    int j=n-1;
    while(i<j){
        while(i<j&&a[j]%2==0){
            j--;
        }
        while(i<j&&a[i]%2==1){
            i++;
        }
        if(i<j){
            swap(a[i],a[j]);
        }
    }
    
    for(int i=0;i<n;i++){
        cout<<a[i]<<" ";
    }
    return 0;
}

```

输入数据求最大值

```cpp
#include<iostream>
using namespace std;
const int N=100010;
int main(){
    int a[N];
    int n,max,position;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    max=a[0];
    for(int i=1;i<n;i++){
        if(a[i]>max){
            max=a[i];
            position=i;
        }
    }
    cout<<max<<" "<<1+position<<endl;
    return 0;
}


```

选择排序

```cpp
#include<iostream>
using namespace std;
int main(){
    // int a[10]={1,2,3,4,5,6,7,8,9,0};
    int a[10]={3,6,2,1,7,9,8,0,4,5};
    int max=0;
    for(int i=0;i<9;i++){
        max=i;
        for(int j=i+1;j<10;j++){
            if(a[max]<a[j])
                max=j;
        }
        swap(a[max],a[i]);
    }
    for(int i=0;i<10;i++)cout<<a[i]<<" ";
    return 0;
}

```

交换排序

```cpp
#include<iostream>
using namespace std;
int main(){
    int a[10],t;int i,j;
    for(i=0;i<10;i++)cin>>a[i];
    for(i=0;i<9;i++){
        for(j=i+1;j<10;j++){
            if(a[i]<a[j]){
                swap(a[i],a[j]);
            }
        }
    }
    for(i=0;i<10;i++)cout<<a[i]<<" ";
}


```

计算数组中有多少个不同的数

```cpp
#include<iostream>
using namespace std;
const int N=10010;
int a[10]={1,1,1,1,7,9,8,0,4,5};
int t;
int b[N];
int main(){
    int ans=0;
    for(int i=0;i<10;i++){
        if(b[a[i]]==0){
            b[a[i]]=1;
            ans++;
        }
    }
    cout<<ans<<endl;
    return 0;
    
}

```

前缀和

```cpp
#include<iostream>
using namespace std;
const int N=10010;
int premu[N];
int a[N];
int main(){
    int n,p,c,b,sum=0;
    cin>>n>>p;
    for(int i=1;i<=n;i++){
        cin>>a[i];
    }
    premu[1]=a[1];
    for(int i=2;i<n;i++){
        premu[i]=premu[i-1]+a[i];
    }
    for(int i=0;i<p;i++){
        cin>>c>>b;
        sum=premu[b]-premu[c-1];//c~b之间的值
        cout<<sum<<endl;
    }
}

```

输入a~g或A~G字符串 输出他们的笔画数之和

```cpp
#include<iostream>
using namespace std;
//辅助数组存储笔画数
int Arr[7]={3,2,1,2,3,3,1};
int arr[7]={1,1,1,2,1,2,1};

int main(){
    int sum=0;
    string a;
    cin>>a;
    for(int i=0;i<a.size();i++){
        if(a[i]>='a'&&a[i]<='g'){
            sum+=arr[a[i]-'a'];
        }
        else if(a[i]>='A'&&a[i]<='G'){
            sum+=Arr[a[i]-'A'];
        }
    }
    cout<<sum<<endl;
    return 0;
}

```

输出杨辉三角

```cpp
#include<iostream>
using namespace std;
int main(){
    int y[10][10],i,j;
    for(int i=0;i<10;i++)
        y[i][0]=y[i][i]=1;
    for(int i=2;i<10;i++)
        for(int j=1;j<=i-1;j++)
            y[i][j]=y[i-1][j]+y[i-1][j-1];
            for(int i=0;i<10;i++){
                for(int j=0;j<=i;j++)
                printf("%5d",y[i][j]);
                cout<<endl;
            }
            return 0;
}

```

### 第五次作业

最大公约数和最小公倍数

```cpp
#include<iostream>
using namespace std;
int gcd(int a,int b){
    return b?gcd(b,a%b):a;
}

int main(){
    int a,b;
    cin>>a>>b;
    int c=gcd(a,b);
    cout<<c<<" "<<a*b/c<<endl;
    return 0;
    
}



```

2.写一个函数，由键盘输入一个数，输出其是否为素数。

```cpp
#include<iostream>
#include<cmath>
using namespace std;
bool prime(int a){
     if(a==1) return 0;
     if(a==3||a==2) return 1;
     for(int i=2;i<=sqrt(a);i++)
     {
         if(a%i==0)
         {
             return 0;
         }
     }
     return 1;
}
int main(){
    int a;
    cin>>a;
    if(prime(a)){
        cout<<a<<"是素数"<<endl;
    }else{
        cout<<a<<"不是素数"<<endl;
    }
}

```

3.写一个函数，将输入的一个字符串按反序存放。在主函数中输入和输出字符串。

```cpp
#include<iostream>
using namespace std;
string inv(string a){
    string b;
    int len=a.size();
    for(int i=len-1,j=0;i>=0;i--,j++){
        b.push_back(a[i]);
    }
    return b;
}
int main(){
    string a,b;
    cin>>a;
    b=inv(a);
    cout<<b;
    return 0;
}

```

简单计算器

```cpp
#include<iostream>
using namespace std;
int add(int a,int b){
    return a+b;
}
int minu(int a,int b){
    return a-b;
}
int mul(int a,int b){
    return a*b;
}
int chu(int a,int b){
    return a/b;
}
int main(){
    int a,b,result;
    char c;
    cin>>a>>c>>b;
    switch(c){
        case '+': result=add(a,b);break;
        case '-': result=minu(a,b);break;
        case '*': result=mul(a,b);break;
        case '/': result=chu(a,b);break;
    }
    cout<<result<<endl;
    return 0;
}



```

 海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子?

```cpp
#include<iostream>
using namespace std;
int main(){
    int i;
    int j=1;
    int x;
    while(1){
        x=4*j;
        for(i=0;i<5;){
        if(x%4!=0)break;
        else{
            x=(x/4)*5+1;
            i++;
        }
    }
    j++;
    if(i==5)break;
    }
    printf("%d",x);
    return 0;
}


```

组合数Cnm

```cpp
#include<iostream>
using namespace std;
float f(int n){
    float fac=1;
    for(int i=1;i<=n;i++)
        fac*=i;
    return fac;
}
int main(){
    int n,m;
    float c;
    cin>>n>>m;
    cout<<f(m)/f(n)/f(m-n)<<endl;
    return 0;
}

```

求三角形的面积

```cpp
#include<iostream>
#include<cmath>
using namespace std;
float area(float a,float b,float c){
    float p,s;
    p=(a+b+c)/2;
    s=sqrt(p*(p-a)*(p-b)*(p-c));
    return s;
}
int main(){
    int a[10],b[10],c[10];
    float s[10];
    for(int i=0;i<10;i++){
        cin>>a[i]>>b[i]>>c[i];
        s[i]=area(a[i],b[i],c[i]);
        cout<<s[i]<<endl;
    }
}

```

求10个学生的平均分，最高分和最低分。

```cpp
#include<iostream>
using namespace std;
float max,min;
float average(float arr[],int n){
    float sum=arr[0];
    max=min=arr[0];
    for(int i=1;i<n;i++){
        if(arr[i]>max)max=arr[i];
        else if(arr[i]<min)min=arr[i];
        sum+=arr[i];
    }
    return sum/n;
}
int main(){
    int i;
    float aver,score[10];
    for(i=0;i<10;i++)
        cin>>score[i];
    aver=average(score,10);
    cout>>max>>" ">>min>>" ">>are<<endl;
    return 0;
}

```

写两个函数，分别求两个整数的最大公约数和最小公倍数，用主函数调用这两个函数并输出结果。

```cpp
#include<iostream>
using namespace std;
int max_ele(int a,int b){//最大公约数
    int result=1,minn;
    minn=min(a,b);
    for(int i=minn;i>=1;i--){
        if(a%i==0&&b%i==0){
            result=i;
            break;
        }
    }
    return result;
}
int min_time(int a,int b){//最大公约数
    int result,maxn;
    maxn=max(a,b);
    for(int i=maxn;i<=a*b;i++){
        if(i%a==0&&i%b==0){
            result=i;
            break;
        }
    }
    return result;
}
int main(){
    int a,b;
    cin>>a>>b;
    cout<<max_ele(a,b)<<endl<<min_time(a,b)<<endl;
    return 0;
}
```

写一个函数，由键盘输入一个数，输出其是否为素数

```cpp
#include<iostream>
#include<cmath>
using namespace std;
int is_sushu(int x){
    for(int i=2;i<=sqrt(x);i++){
        if(x%i==0)
            return 0;
    }
    return 1;
}
int main(){
    int a;
    cin>>a;
    if(is_sushu(a)){
        cout<<"是素数";
    }else{
        cout<<"不是素数";
    }
}
```

字符串逆序

```cpp
#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
const int N=10010;
void reserves(char a[],char b[]){
    int i,j,len;
    len=strlen(a);
    i=0;j=len;
    b[j--]='\0';
    while(i<len){
        b[j]=a[i];
        j--;i++;
    }
}
int main(){
    char str1[N],str2[N];
    scanf("%s",str1);
    reserves(str1,str2);
    cout<<str2;
    return 0;
    
}


```

### 第六次课作业

 用冒泡法对一组用户输入的整数进行排序。 

```cpp
#include<iostream>
#include<cstdio>
using namespace std;
/*
外层n-1次循环
每次循环都在待排序的序列中把最大的移到待排序的最后面1~n-i-1

*/
int main(){
    int a[10]={3,2,5,1,4,8,9,7,10,6};
    for(int i=0;i<9;i++){
        for(int j=1;j<=10-i-1;j++){
            if(a[j]>a[j-1])
            swap(a[j-1],a[j]);
        }
    }
    for(int i=0;i<10;i++)cout<<a[i]<<" ";
    return 0;
}


```

 2.将一个二维数组行和列的元素互换,存到另一个二维数组中。（数据类型可以是整型或者浮点型） 

```cpp
#include<iostream>
using namespace std;
int main(){
    int a[10][10]{
        {1,1,1,1,1,1,1,1,1,1},
        {0,1,1,1,1,1,1,1,1,1},
        {0,1,1,1,1,1,1,1,1,1},
        {0,1,2,1,1,1,1,1,1,1},
        {0,1,2,3,1,1,1,1,1,1},
        {0,1,2,3,4,1,1,1,1,1},
        {0,1,2,3,4,5,1,1,1,1},
        {0,1,2,3,4,5,6,1,1,1},
        {0,1,2,3,4,5,6,7,1,1},
        {0,1,2,3,4,5,6,7,8,1}
    };
    int b[10][10];
    for(int i=0;i<10;i++){
        for(int j=0;j<10;j++){
            b[j][i]=a[i][j];
        }
    }
    for(int i=0;i<10;i++){
        for(int j=0;j<10;j++){
            cout<<b[i][j]<<" ";
        }
        cout<<endl;
    }
    return 0;
}

```

 3.输出一个菱形图。 

```cpp
#include<iostream>
using namespace std;
int main(){
    for(int i=1;i<=4;i++){
        for(int j=1;j<=4-i;j++){
            cout<<" ";
        }
        for(int j=1;j<=2*i-1;j++){
            if(j==1||j==2*i-1)
            cout<<"*";
            else
            cout<<" ";
        }
        cout<<endl;
    }
    for(int i=3;i>=1;i--){
        for(int j=1;j<=4-i;j++){
            cout<<" ";
        }
        for(int j=1;j<=2*i-1;j++){
            if(j==1||j==2*i-1)
            cout<<"*";
            else
            cout<<" ";
        }
        cout<<endl;
    }
    return 0;
}

#include<iostream>
/*
用循环来控制输出格式
用字符数组
循环输出二维字符数组
*/
using namespace std;
int main(){
    char diamond[5][5]={{' ',' ','*'},{' ','*',' ','*'},{'*',' ',' ',' ','*'},{' ','*',' ','*'},{' ',' ','*'}};
    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
            cout<<diamond[i][j];
        }cout<<endl;
    }
    return 0;
}


```

 4.找出一个二维数组中的鞍点,即该位置上的元素在该行上最大、在该列上最小。也可能没有鞍点。 

```cpp
#include<iostream>
using namespace std;
/*
方法一
max 每一行最大值
每一列最小值
比较max[i]==min[j]

方法二：
1、判断这个值是否为行最大值
2、判断这个值是否为列最小值
3、对输入的数据进行循环同时满足1,2,这个数据就是靶点
*/
int main(){
    int a[5][5],rmax[5],cmin[5],rx[5],ry[5],cx[5],cy[5],t=0;
    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
            cin>>a[i][j];
        }
    }
    for(int i=0;i<5;i++){
        rmax[i]=a[i][0];
        for(int j=0;j<5;j++){
            if(rmax[i]<a[i][j]){
                rmax[i]=a[i][j];
                rx[i]=i;
                ry[i]=j;
            }
        }
    }
    for(int j=0;j<5;j++){
        cmin[j]=100000;
        for(int i=0;i<5;i++){
            if(cmin[j]>a[i][j]){
                cmin[j]=a[i][j];
                cx[j]=i;
                cy[j]=j;
            }
        }
    }
    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
            if(rx[i]==cx[j]&&ry[i]==cy[j]){
                cout<<rx[i]+1<<" "<<ry[i]+1<<" "<<a[i][j];
            }
        }
        cout<<endl;
    }
    return 0;
}

int row_max(int a[100][100],int m,int n,int i,int j){
    for(int p=0;p<n;p++){
        if(a[i][p]>a[i][j])
            return 0;
    }
    return 1;
}
int col_min(int a[100][100],int m,int n,int i,int j){
    for(int p=0;p<m;p++){
        if(a[p][j]<a[i][j])
            return 0;
    }
    return 1;
}
int main(){
    int m,n,a[100][100];
    cin>>m>>n;
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++)
            cin>>a[i][j];
    }
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(row_max(a,m,n,i,j)&&col_min(a,m,n,i,j)){
                cout<<a[i][j]<<" ";
            }
        }
    }
    return 0;
}




```

 5.写一个函数,输入一行字符,将此字符串中最长的单词输出。 

```cpp
#include<iostream>
#include<cstring>
using namespace std;
const int N=100010;
int main(){
    char a[N];
    scanf("%s",a);
    int len=strlen(a);
    // cout<<len<<endl;
    int i=0,length=0,temp,pos=0;
    while(i<len){
        if(a[i]>='a'&&a[i]<='z'||a[i]>='A'&&a[i]<='Z'){
            temp=0;
            while(a[i]>='a'&&a[i]<='z'||a[i]>='A'&&a[i]<='Z'){
                i++;
                temp++;
            }
            if(temp>length){
                length=temp;
                pos=i-1;
            }
        }else{
            i++;
        }
    }
    for(int i=pos-length+1;i<=pos;i++){
        cout<<a[i];
    }
    
    
    return 0;
}

```

 6、在主函数中输入n个等长的字符串。用另一函数对它们排序。然后在主函数输出这n个已排好序的字符串。(可以使用指针完成) 

```cpp
#include<iostream>
#include<cstring>
using namespace std;

void strsort(char str[][32],int n){
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-i-1;j++){
            if(strcmp(*(str+j),*(str+j+1))>0)
                swap(*(str+j),*(str+j+1));
                // char tmp[32];
                // strcpy(tmp, *(str + j));
                // strcpy(*(str + j), *(str + j+1));
                // strcpy(*(str + j+1), tmp);
        }
    }
    // for(int i=0;i<n;i++)cout<<str[i]<<endl;
}

int main(){
    int n;
    char str[32][32];
    cin>>n;
    for(int i=0;i<n;i++)scanf("%s",str[i]);
    strsort(str,n);
    for(int i=0;i<n;i++)cout<<str[i]<<endl;
    return 0;
}

```



 7.有两个磁盘文件“A”和“B”,各存放一行字母,今要求把这两个文件中的信息合并(按字母顺序排列),输出到一个新文件“C”中去 

```cpp
#include<iostream>
using namespace std;
/*
1. 打开a文件，读取a的数据，暂时存起来char,str[Maxn]
2. 打开b文件，读取b的数据，暂时存起来char,str[Maxn]
3. 排序

*/
int main(){
    FILE *fp;
    char a[100];
    if((fp=fopen("A.txt","r"))==NULL)//打开 test1 文件
    {
        printf("can't open file!\n");
        exit(0);
    }
    int i=0;
    a[i]=fgetc(fp);//把 fp 所指向的文件 test2 中的第一个字符读入到数组a[0]
    while(a[i]!=EOF)//若第一个字符不是结束符 EOF，则继续把指针 fp 指向的文件test1 中的字符逐个读入到数组 a，直至遇到标识符 EOF 结束循环
    {
        putchar(a[i]);
        i++;
        a[i]=fgetc(fp);
    }
    putchar('\n');
    fclose(fp);
    if((fp=fopen("B.txt","r"))==NULL)
    {
        printf("can't open file!\n");
        exit(0);
    }
    a[i]=fgetc(fp);//把 fp 所指向的文件 test2 中的第一个字符读入到数组a[0]
    while(a[i]!=EOF)//若第一个字符不是结束符 EOF，则继续把指针 fp 指向的文件test1 中的字符逐个读入到数组 a，直至遇到标识符 EOF 结束循环
    {
        putchar(a[i]);
        i++;
        a[i]=fgetc(fp);
    }
    a[i]='\0';
    putchar('\n');
    fclose(fp);
    
    int n=i;//此时 n 为数组 a 的长度
    int j,k,t;
    for(i=0;i<n-1;i++)//对数组 a 进行直接选择排序
    {
        for(j=i+1;j<n;j++)
        {
            if(a[i]>a[j])
            {
                t=a[i];
                a[i]=a[j];
                a[j]=t;
            }
        }
    }
    if((fp=fopen("C.txt","w"))==NULL)
    {
    printf("can't open file!\n");
    exit(0);
    }
    i=0;
    while(i<n)
    {
        fputc(a[i],fp);//在循环里，这条语句把数组 a 的所有字符写到文件指针变量fp 所指向的文件 C.txt 中
        putchar(a[i]);//在循环里，这条语句把数组 a 的所有字符显示到屏幕上i++;
        i++;
    }
    fclose(fp);//关闭文件 test3，防止它被误用
    putchar('\n');
    return 0;
}

```

 ### C语言测试卷

1.有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？ 

```cpp
#include<iostream>
using namespace std;
int main(){
    int i,j,k,t=0;
    for(i=1;i<5;i++){
        for(j=1;j<5;j++){
            for(k=1;k<5;k++){
                    if(i!=j&&i!=k&&j!=k){
                        cout<<i<<j<<k<<endl;
                        t++;
                    }
            }
        }
    }
    cout<<t;
    return 0;
}

```

 2.输入某年某月某日，判断这一天是这一年的第几天？ 

```cpp
#include<iostream>
using namespace std;
int main(){
    int a[13]{
        0,31,28,31,30,31,30,31,31,30,31,30,31
    };
    int year,month,day,t=0;
    cin>>year>>month>>day;
    if(year%4==0&&year%100!=0||year%400==0){
        a[2]=29;
    }else{
        a[2]=28;
    }
    for(int i=1;i<month;i++){
        t+=a[i];
    }
    t+=day;
    cout<<t<<endl;
    return 0;
}


```

 3.一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？ 

```cpp
#include<iostream>
using namespace std;
int main(){
    float a[10]={100},sum=0;
    for(int i=1;i<10;i++){
        a[i]=a[i-1]/2;
    }
    sum=a[0];
    for(int i=1;i<10;i++)sum+=a[i]*2;
    cout<<sum<<endl;
    cout<<a[9]/2;
    return 0;
}

```

 4.将一个八进制转换为十进制 (八进制数的长度可能很长在(长度在1~100之间)) 

```cpp
#include<iostream>

using namespace std;

int main()
{
    char s[1000];
    int i, num = 0;
    long sum = 0;
    cin>>s;
    for(i = 0; s[i]; i++)
    {
        num = s[i] - '0';
        sum = sum * 8 + num;
    }
    cout<<sum<<endl;
    return 0;
}
```

 5.计算字符串中子串出现的次数 。(先输入母串，后输入子串，以回车键隔开) 

```cpp
#include<iostream>
#include<cstring>
using namespace std;
int main(){
    char a[100],b[10];
    int len1,len2,t=0;
    scanf("%s%s",a,b);
    len1=strlen(a);
    len2=strlen(b);
    int i,j,k;
    for(i=0;i<=len1-len2;i++)
    {
        for(j=0,k=i;j<len2&&b[j]==a[k];j++,k++);
        if(j==len2)
            t++;
    }
    cout<<t;
    return 0;
}
```

 6.有五个学生，每个学生有3门课的成绩(English,C,math)，从键盘输入以上数据（包括学生号，姓名，三门课成绩），计算出平均成绩，将原有的数据和计算出的平均分数存放在磁盘文件"stud"中。 

```cpp
#include<iostream>
using namespace std;
typedef struct student{
    int sno;
    char name[10];
    float score[3];
    float avg;
}stu;

int main(){
    stu a[5];
    for(int i=0;i<5;i++){
        scanf("%d%s%f%f%f",&a[i].sno,a[i].name,&a[i].score[0],&a[i].score[1],&a[i].score[2]);
        a[i].avg=(a[i].score[0]+a[i].score[1]+a[i].score[2])/3;
    }
    
    FILE *fp;
    if((fp=fopen("stud.txt","w"))==NULL)
    {
        printf("can't open file!\n");
        exit(0);
    }
    for(int i=0;i<5;i++){
        fprintf(fp,"%d %s %f %f %f %f\n",a[i].sno,a[i].name,a[i].score[0],a[i].score[1], a[i].score[2],a[i].avg);
    }
    fclose(fp);//关闭文件 test3，防止它被误用
    
}
```

  7. 写一个计算酒店入住率的程序。程序应该从询问用户酒店有多少层开始。对于每一层，程序应该询问楼上有多少房间以及有多少房间被占用。 在用户数据输入后，程序应该显示酒店有多少房间，有多少房间已被占用，有多少房间未被占用，以及房间已被占用的百分比 

```cpp
#include<iostream>
using namespace std;
int main(){
    int lay;
    int sum[10],sums=0;
    int live[10],lives=0;
    cin>>lay;
    for(int i=1;i<=lay;i++){
        cin>>sum[i];
        cin>>live[i];
        sums+=sum[i];
        lives+=live[i];
    }
    cout<<sums<<" "<<lives<<""<<sums-lives<<" "<<1.0*lives/sums<<" ";
    return 0;
}
```

