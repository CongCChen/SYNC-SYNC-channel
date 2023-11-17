## 2023.10.28工作汇报
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

## 工作汇报

### 1.完成标准偏差和标准误差的测试并画图

![image](https://github.com/CongCChen/SYNC-SYNC-channel/assets/37946054/70c3166b-255c-49f4-b168-4f04bb893694)

### 2. VMware安装macOS系统
下载vmware workstation 17pro并激活，vmware workstation 17默认没有解锁macOS的安装选项，需要unlocker来解锁
```
https://github.com/DrDonk/unlocker/releases
```
解锁完成后先不要启动虚拟机！

打开macOS 12.vmx文件，添加一下内容
```
cpuid.0.eax = "0000:0000:0000:0000:0000:0000:0000:1011"
cpuid.0.ebx = "0111:0101:0110:1110:0110:0101:0100:0111"
cpuid.0.ecx = "0110:1100:0110:0101:0111:0100:0110:1110"
cpuid.0.edx = "0100:1001:0110:0101:0110:1110:0110:1001"
cpuid.1.eax = "0000:0000:0000:0001:0000:0110:0111:0001"
cpuid.1.ebx = "0000:0010:0000:0001:0000:1000:0000:0000"
cpuid.1.ecx = "1000:0010:1001:1000:0010:0010:0000:0011"
cpuid.1.edx = "0000:0111:1000:1011:1111:1011:1111:1111"
vhv.enable = "FALSE"
vpmc.enable = "FALSE"
vvtd.enable = "FALSE"
```
### 3. Windows 安装cygwin64并测试同步函数

<img width="453" alt="0118170881a25296aa205df6747dee0" src="https://github.com/CongCChen/SYNC-SYNC-channel/assets/37946054/0a077741-7b9b-497c-b81e-5a6f6286fc0e">

**可能的原因:** Cygwin 并不是一个原生的 Linux 系统，它是在 Windows 上提供类似于 Linux/Unix 环境的兼容层。在 Cygwin 中，它使用一种称为 "DLL 代理" 的技术来拦截和转发系统调用，将 Linux/Unix 的系统调用转换为适应 Windows 内核的调用，从而在 Windows 上提供类似于 Linux 的 POSIX 兼容环境，并且可以运行许多基于 Linux 的程序和工具。

### 4. 在macOS上测试同步函数（macOS12.5虚拟机）

<img width="466" alt="a7580cc90db126b18d8ff4e9e9b88a0" src="https://github.com/CongCChen/SYNC-SYNC-channel/assets/37946054/d9158e93-69d0-49e3-ac64-32c04bc6ef4a">

### 5. 修改省重点研发申请书（已完成）

### 6. 修改论文（研究背景、研究动机、优化、试验评估）

### 7. 继续做自动化漏洞挖掘的实验（融合逐出集到突变地址中）


## 2023.11.18工作汇报

### 1. 完成单指令地址突变程序

### 2. 修改论文（对比工作）

### 3. 测试侧信道攻击（网站指纹）
数据收集（Prime+Probe攻击收集每个网站缓存行访问时间）、建模（CNN、LSTM）

* cookies.sqlite-wal 是 Mozilla Firefox 浏览器中的一个文件，它是用于存储浏览器的 Cookie 数据的 SQLite 数据库的写入日志文件。
* data.safe.bin 文件存放的是经过加密保护的匿名化数据，这些数据可能包括用户的一些使用习惯、浏览器性能指标等。
* places.sqlite 是 Mozilla Firefox 浏览器中的一个文件，它是存储浏览器历史记录和书签数据

只能观察到打开新的网站，不能观察到网站类型

