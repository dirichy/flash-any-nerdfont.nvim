# flash-any.nvim Nerd Font icons

[English](README.md)

配合 [flash-any.nvim](https://github.com/dirichy/flash-any.nvim/tree/main)，
用 Nerd Font 图标名称及其前缀搜索图标。

![搜索跳转](https://github.com/dirichy/flash-any-nerdfont.nvim/releases/download/demos/table.gif)

[高清 MP4](https://github.com/dirichy/flash-any-nerdfont.nvim/releases/download/demos/table.mp4)

## 安装

需要 Neovim 0.11+、make 和 C 编译器。本包目前仅在本地整理，远程仓库与演示附件尚未发布。
先使用本地依赖；发布后可将其替换为 "dirichy/flash-any-nerdfont.nvim"。在 lazy.nvim 配置中添加：

```lua
{
  "dirichy/flash-any.nvim",
  branch = "main",
  version = false,
  dependencies = { "folke/flash.nvim", { dir = "/path/to/flash-any-nerdfont.nvim" } },
  build = "make",
  opts = { sources = { "nerdfont" } },
  keys = {
    { "s", mode = { "n", "x", "o" }, function() require("flash-any").jump() end },
  },
}
```

## 使用

1. 按 `s`，输入要找的字的编码。
2. 按屏幕上显示的标签跳转。
3. 继续输入可以匹配更长的文本，编码与普通 ASCII 可以混输。

输入 `terminal` 找“”，输入 `terminal with flash` 找“ with flash”。搜索 ASCII 时直接输入原文。

也可以输入 `term` 等前缀。终端需要使用 Nerd Font 才能显示图标；录制工作流会自行安装字体。

## 更多

- [flash-any 配置说明](https://github.com/dirichy/flash-any.nvim/blob/main/README.zh-CN.md)
- [更新码表与录制演示](docs/maintenance.md)

## 许可

项目代码采用 [MIT](LICENSE)，数据来源和上游条款见 [THIRD_PARTY.md](THIRD_PARTY.md)。
