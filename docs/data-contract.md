# 袋视图与原像

key为string或null，非null按Unicode精确相等。L包含row_id/key/region/reading，R包含row_id/key/category，reading为整数或null，以reading_scale为显示分母。row_id仅表内唯一，update旧新row_id须相同，key可变。每批先验证全部旧像与批前状态一致，同一表同row_id每批最多一个变更。

分组键(region,category)保留null类型，region为string。COUNT(*)统计左连接输出行的重数，COUNT(reading)只统计非null，SUM整数精确，MIN按整数序；所有非null计数为0时SUM和MIN为null。L没有匹配则产生一行R全null扩展，即使同组有另一条R真实null分类也不额外区分聚合组。输出关联行差分以(L.row_id,R.row_id或缺匹配标志)为来源，不能把真实null字段当缺行。

访问统计包含本批实际扫描的join key和基表row_id，允许内存键预算或落盘，但不能扫描未受影响键来计算小delta。初始工具不维护连接索引。
