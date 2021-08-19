# ok-derby
《赛马娘》（ウマ娘: Pretty Derby）辅助 🐎🖥 

基于 [auto-derby](https://github.com/NateScarlet/auto-derby) 可视化操作/设置 启动器  一键包

### 便捷，好用的 auto_derby 管理器！

![image-20210819100302921](https://cdn.jsdelivr.net/gh/Akegarasu/PicRepo/picgo/image-20210819100302921.png)

![image-20210819100402636](https://cdn.jsdelivr.net/gh/Akegarasu/PicRepo/picgo/image-20210819100402636.png)

## 功能

- [x] 支持客户端
  - [x] DMM （前台）
  - [x] _实验性_ 安卓 ADB 连接（后台）开发基于 1080x1920 分辨率
- [x] 团队赛 (Team race)
  - [x] 有胜利确定奖励时吃帕菲
- [x] 日常赛 (Daily race)
- [x] PvP 活动赛 (Champions meeting)
- [x] 传奇赛 (Legend race)
  - [x] 自动领奖励
- [x] 活动抽奖转盘 (Roulette derby)
- [x] 自定义限时商店处理
  - [x] 插件 limited_sale_buy_everything：自动买下所有物品
  - [x] 插件 limited_sale_buy_first_3：自动买前 3 个物品
  - [x] 插件 limited_sale_close：直接跳过限时商店提示窗口
- [x] 育成 (Nurturing)
  - [x] 自动选择训练
    - [x] 基于当前属性
    - [x] 基于训练效果
    - [x] 基于训练等级
    - [ ] 基于精确体力消耗
    - [ ] 基于羁绊值获取量
    - [x] 暑期集训保留体力
    - [ ] 年末抽奖前消耗体力
    - [x] 插件 avoid_high_failure_rate_trains: 避免参加失败率>30%的训练
  - [x] 遇到新事件选项请求人工处理，后续相同事件使用相同选择
  - [x] 自动参加比赛
    - [x] 预估比赛结果，如果不能仅靠属性拿冠军则暂停请求人工确认
    - [x] 自动选择比赛跑法
      - [x] 基于属性和适性
      - [ ] 基于对手跑法选择跑法（倾向人数少的跑法）
  - [x] 支持友人卡
    - [ ] 基于友人卡事件效果主动外出
- [x] 支持 [python 插件](https://github.com/NateScarlet/auto-derby/wiki/Plugins)

## 使用方法

在 release 中下载压缩包，点开即用

