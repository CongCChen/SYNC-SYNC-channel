### 论文拟补充内容
1. 复现WB channel(发送方修改缓存行，接收方使用驱逐集测量替换缓存行的时间)，发现其在沙盒下无效
2. 指出其设计缺陷，提出有效的跨沙盒回写隐蔽信道应该遵循的设计原则(由于发送方只读，因此可以采用回写+修改&回写模式来传输信息)
3. 基于所提出的设计原则，修改WB channel，使其可以在沙盒场景下工作（回写方式，测试一下CLWB指令）
4. 提出一种称为SYNC+SYNC的跨沙盒软件回写隐蔽信道，测试其性能并优化
5. **补充SYNC+SYNC的性能评估（标准偏差和标准误差）**
6. 测试其他平台（macOS、BSD、Windows Cygwin）
7. 针对所提出的隐蔽信道，设计有效的缓解措施

**WB channel:** Abusing Cache Line Dirty States to Leak Information in Commercial Processors(HPCA 2022)

### 1. 重新测试数据（每个slot含50组），完成fdatasync的标准偏差和标准误差测试
![微信图片_20231027125638](https://github.com/CongCChen/WB-MWB-channel/assets/37946054/95b745e6-3928-41f4-bd98-69381593d8e8)


### 2. 继续试验其他可能的平台
linux文件同步原语：sync、fsync、syncfs、fdatasync、msync。

POSIX（Portable Operating System Interface，可移植操作系统接口）是一个标准化的操作系统接口规范，旨在提供可移植性和互操作性。它定义了一组操作系统接口函数、命令和工具，并规定了这些接口的行为和语义。POSIX标准涵盖了许多操作系统领域，包括文件系统、进程管理、线程、信号处理、网络编程等。通过遵循POSIX标准，开发人员可以编写可移植的应用程序，这些应用程序可以在符合POSIX标准的操作系统上运行，而不需要进行大量的修改。

POSIX标准的实现可以在各种操作系统上找到，包括类UNIX系统（如Linux、BSD、macOS等）以及其他操作系统（如Windows的一些子系统）。这些实现通常提供了对POSIX接口的库和工具，使开发者能够在不同的平台上进行跨平台开发。需要注意的是，虽然Windows操作系统本身并不符合POSIX标准，但是在Windows上可以通过一些软件或子系统来实现对POSIX接口的支持，例如Cygwin、MSYS2、Windows Subsystem for Linux（WSL）等。这样开发者就可以在Windows平台上使用POSIX接口进行开发。
POSIX标准对于促进软件的可移植性和互操作性起到了重要作用，使得开发者能够更方便地编写跨平台的应用程序，并且能够在不同的操作系统上共享和重用代码。
