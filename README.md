# 历史街区服务概览

历史街区开放日历、问卷和闸机计数。当前总览只按入口加总记录数。

样例数据均为本地合成记录，不对应真实个人、媒体、机构或交易。项目使用 Python 3.11.14 标准库，数据随项目保存，不访问外部服务。

## 使用

在项目根目录运行 `python3 -m app summary` 查看按当前基础口径生成的 JSON 总览。

## 验证

运行 `python3 -m unittest discover -s tests -v` 和 `python3 -m compileall -q app tests`。

## 结构

`data/data.json` 保存领域记录与基础汇总口径；`app/storage.py` 读取并检查数据形状；`app/analysis.py` 计算基础分组统计；`app/service.py` 组合数据读取和统计；`tests/` 验证产品入口及无效数据处理。

## 工作台

`python3 -m app attendance` 统计实际开放入口的进入次数；`python3 -m app survey --key 2026-05-01` 核对各抽样点的邀请和回应；`python3 -m app staffing` 按入场次数与时段容量对照给出排班复核标记。关闭时段单列。

入口上报的 `token` 可跨入口关联，缺标识仍是合法闸机记录。预约席位的 `reserved` 不是场地实际到访；`attended` 表示活动核销。`comparisons` 是活动方登记的前后对照时段，会随活动改期修订。问卷回应按采样点记录，逛过多入口的人可能被重复邀请。

操作数据在 `data/workbench.json`。工作台涉及的领域代码：`attendance` 根据入口调整汇总客流, `sampling` 统计调查回执, `capacity` 根据开放时段和客流发出排班告警。已有总览仍使用 `data/data.json`。
