# 每日计划 - Daily Planner Specification

## 1. Concept & Vision

一款极简主义的每日计划应用，融合日式禅意美学与功能实用性。界面干净留白，交互流畅自然，让用户专注于任务本身而非工具。柔和的色调与克制的动效营造出宁静专注的氛围。

## 2. Design Language

### Aesthetic Direction
日式极简 + 北欧功能主义。大面积留白，柔和的色彩，精致的细节。

### Color Palette
```
--bg-primary: #FAFAFA        /* 主背景：温暖的米白 */
--bg-secondary: #F5F5F5      /* 次级背景 */
--bg-card: #FFFFFF           /* 卡片背景 */
--text-primary: #2D2D2D      /* 主要文字 */
--text-secondary: #8A8A8A     /* 次要文字 */
--text-muted: #C0C0C0        /* 淡化文字 */
--accent: #7B9E87            /* 薄荷绿强调色 - 专注、平静 */
--accent-light: #E8F0EA      /* 强调色浅 */
--danger: #E57373            /* 删除/危险 */
--timeline-track: #E0E0E0    /* 时间轴轨道 */
--completed: #D4D4D4         /* 已完成状态 */
```

### Typography
- **Body**: "Noto Sans SC" (中文正文) - 清晰易读
- **Monospace**: "JetBrains Mono" (时间数字) - 现代等宽

### Motion Philosophy
- 过渡动画: 200-300ms ease-out
- 滑动手势: 平滑跟随，带惯性
- 倒计时数字: 每秒平滑减少
- 完成动画: 淡出 + 收缩

## 3. Layout & Structure

### 页面结构
```
┌─────────────────────────────────┐
│  [时长模式]    [时间轴模式]       │  ← 模式切换 Tab
├─────────────────────────────────┤
│                                 │
│   Task Cards Area               │
│                                 │
│   + 添加新计划                   │
│                                 │
├─────────────────────────────────┤
│  🏠 首页    ✓ 固定    👤 我的    │  ← 底部导航
└─────────────────────────────────┘
```

## 4. Features

### 时长模式
- 每个任务独立倒计时
- 点击卡片开始/暂停
- 倒计时结束自动从页面删除
- 左滑显示删除按钮

### 时间轴模式
- 添加后自动对齐到时间轴（按开始时间排序）
- 竖向显示在屏幕中
- 点击复选框变灰 + 删除线

### 护眼提醒
- 每30分钟弹出一次
- 显示远眺提示 + 眼球动画
- 3秒后自动消失

### 固定任务页
- 3列方块按钮网格
- 点击变灰（已完成）
- "+" 按钮添加新任务
- 长按删除

### 数据持久化
- localStorage 存储
- 跨天保留
- 每日任务按日期分开，新天自动清空

## 5. Technical Approach

- 纯 HTML + CSS + JavaScript (单文件)
- CSS Variables 管理主题
- localStorage 持久化
- Page Visibility API 优化计时器
