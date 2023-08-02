### 论文拟补充内容
1. 测试WB channel(发送方修改缓存行，接收方使用驱逐集测量替换缓存行的时间)在沙盒下无效
2. 指出其设计缺陷，提出有效的跨沙盒回写隐蔽信道应该遵循的设计原则(由于发送方只读，因此可以采用回写+回写模式来传输信息)
3. 基于所提出的设计原则，修改WB channel，使其可以在沙盒场景下工作（回写方式，测试一下CLWB指令）
4. 提出一种新的跨沙盒软件回写隐蔽信道，测试并优化其性能
5. 针对所提出的隐蔽信道，设计有效的缓解措施

**WB channel:** Abusing Cache Line Dirty States to Leak Information in Commercial Processors(HPCA 2022)
