# 项目架构文档

## 项目概述

这是一个游戏开发者个人作品集网站，用于展示个人信息、游戏作品和简历经历。网站分为前台展示页面和后台管理页面。

**技术栈**: Vite + React 19 + TypeScript + TailwindCSS v4

---

## 目录结构

```
zip/
├── index.html          # 前台主页 - 个人作品集展示页面
├── admin.html          # 后台管理页面 - 内容管理系统
├── src/                # React 源码目录
│   ├── main.tsx        # React 应用入口
│   ├── App.tsx         # 根组件（当前为空）
│   └── index.css       # 全局样式（Tailwind 导入）
├── public/             # 静态资源目录
│   ├── data.json       # 网站数据源（个人信息、游戏、简历等）
│   └── admin.html      # 后台管理页面
├── package.json        # 项目依赖配置
├── vite.config.ts      # Vite 构建配置
├── tsconfig.json       # TypeScript 配置
├── .env.example        # 环境变量示例
├── metadata.json       # AI Studio 元数据
└── README.md           # 项目说明文档
```

---

## 文件详细说明

### 根目录文件

| 文件 | 功能说明 |
|------|----------|
| `index.html` | **前台主页** - 访客看到的个人作品集页面，包含 Hero 区、关于我、游戏作品集、简历时间线等模块 |
| `admin.html` | **后台管理页面** - 独立的内容管理系统，用于编辑网站数据，带密码保护（默认密码: admin123） |
| `package.json` | 项目依赖配置，包含 React、Vite、TailwindCSS、motion 动画库等 |
| `vite.config.ts` | Vite 构建配置，配置了 React 插件、Tailwind 插件、路径别名、API Key 环境变量注入 |
| `tsconfig.json` | TypeScript 编译器配置 |
| `metadata.json` | AI Studio 应用元数据 |

### src 目录

| 文件 | 功能说明 |
|------|----------|
| `main.tsx` | React 应用入口文件，挂载 App 组件到 #root 元素 |
| `App.tsx` | 根组件（当前为空，用于未来扩展） |
| `index.css` | 全局样式文件，仅包含 `@import "tailwindcss";` |

### public 目录

| 文件 | 功能说明 |
|------|----------|
| `data.json` | **网站数据源** - 包含所有展示内容的 JSON 文件 |
| `admin.html` | 后台管理页面的完整副本（独立运行） |

---

## 数据结构 (data.json)

```json
{
  "profile": {
    "name": "姓名",
    "title": "职位标题",
    "subtitle": "副标题",
    "avatar": "头像 emoji",
    "about": ["个人简介段落数组"],
    "socialLinks": [{"name": "链接名", "url": "链接地址"}],
    "skills": {
      "技能分类": ["技能标签数组"]
    }
  },
  "games": [
    {
      "id": 1,
      "title": "游戏名称",
      "icon": "图标 emoji",
      "image": "封面图 URL",
      "description": "游戏描述",
      "tech": ["技术标签数组"],
      "link": "游戏链接"
    }
  ],
  "resume": {
    "contact": { "email", "phone", "location", "github" },
    "target": { "position", "city", "salary", "type" },
    "education": [{ "school", "degree", "major", "year", "courses" }],
    "projects": [{ "name", "role", "time", "description" }],
    "activities": [{ "organization", "position", "time", "description" }]
  }
}
```

---

## 前台页面 (index.html) 功能模块

1. **Hero 区域** - 展示姓名、职位、行动按钮
2. **关于我** - 个人简介 + 技能标签网格
3. **项目与经历** - 时间线展示教育背景和项目经历
4. **游戏作品集** - 卡片网格展示，点击弹出详情弹窗
5. **Footer** - 社交链接和版权信息
6. **主题切换** - 明/暗模式切换
7. **导航栏** - 锚点导航 + 管理入口链接

---

## 后台管理页面 (admin.html) 功能模块

1. **认证系统** - 密码保护（默认 admin123），使用 localStorage 存储登录状态
2. **个人信息管理** - 编辑姓名、头像、标题、简介、社交链接、技能分类
3. **游戏作品管理** - 增删改游戏作品（名称、图标、描述、技术栈、链接）
4. **简历管理** - 联系方式、求职意向、教育背景、项目经历
5. **数据管理** - 导入/导出 JSON 数据
6. **主题切换** - 深色/浅色模式
7. **响应式布局** - 侧边栏在移动端可折叠

---

## 依赖说明

| 依赖 | 版本 | 用途 |
|------|------|------|
| react | ^19.0.0 | UI 框架 |
| react-dom | ^19.0.0 | React DOM 渲染 |
| @tailwindcss/vite | ^4.1.14 | Tailwind CSS 集成 |
| tailwindcss | ^4.1.14 | 原子化 CSS 框架 |
| @vitejs/plugin-react | ^5.0.4 | Vite React 插件 |
| vite | ^6.2.0 | 构建工具 |
| motion | ^12.23.24 | 动画库 |
| lucide-react | ^0.546.0 | 图标库 |
| @google/genai | ^1.29.0 | Gemini API 集成 |

---

## 运行指令

```bash
npm install          # 安装依赖
npm run dev          # 开发模式运行（端口 3000）
npm run build        # 生产构建
npm run preview      # 预览构建结果
npm run lint         # TypeScript 类型检查
npm run clean        # 清理构建产物
```

---

## 注意事项

- 后台管理默认密码为 `admin123`，可在 admin.html 中修改 `ADMIN_PASSWORD` 变量
- 数据存储采用 localStorage，导入新数据会覆盖现有内容
- 前台页面通过 fetch 请求 `/data.json` 获取数据
- 项目支持 Gemini API 集成（通过环境变量 `GEMINI_API_KEY` 配置）
