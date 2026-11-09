# Nerd Font icons for flash-any.nvim

[简体中文](README.zh-CN.md)

Search Nerd Font icons using their names and prefixes. Use it with
[flash-any.nvim](https://github.com/dirichy/flash-any.nvim/tree/main).

![Search and jump](https://github.com/dirichy/flash-any-nerdfont.nvim/releases/download/demos/table.gif)

[HD MP4](https://github.com/dirichy/flash-any-nerdfont.nvim/releases/download/demos/table.mp4)

## Install

Requires Neovim 0.11+, make and a C compiler. This package is prepared locally;
its remote repository and demo assets have not been published. Use a local dependency
until publication, then replace it with "dirichy/flash-any-nerdfont.nvim".
Add this to your lazy.nvim configuration:

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

## Use

1. Press `s` and enter a character's code.
2. Choose a displayed label to jump there.
3. Keep typing to match a longer phrase, mixing codes and ordinary ASCII text.

Type `terminal` to find “”, or `terminal with flash` to find “ with flash”. Ordinary ASCII text can also be searched directly.

Prefixes such as `term` work too. Your terminal must use a Nerd Font to display
the icons; the recording workflow installs its own font.

## More

- [flash-any configuration](https://github.com/dirichy/flash-any.nvim/blob/main/README.md)
- [Updating the table and recording demos](docs/maintenance.md)

## License

Code: [MIT](LICENSE). Data sources and upstream terms: [THIRD_PARTY.md](THIRD_PARTY.md).
