VIM Markdown Preview
---

This is a vim markdown preview plugin.

####Installing

**Normal**

1. use `pip install mistune` to enable the markdown module works well.
2. then `vim plugin/markdown-preview.vim` to open the plugin file
3. use `source %`, to enable the plugin
4. use `<leader>m` to preview the markdown file in your default browser
5. or use `:MarkdownPreview` to preview your markdown docs

**Bundle or Vundle**

1. add `Bundle 'MikeCoder/markdown-preview.vim'` to your bundle file like vimrc or vimrc.bundle
2. and exec `BundleInstall` to install the plugin

####Custom
this theme is in the css folder, if you want to change it to your favorite theme. follow the steps.

1. open the **markdown-preview.vim**
2. find the line 26, change the css to your favorite css


####Thanks
1. mistune
2. vim

####LAST
wish you have a nice day

####TODO
see [TODO.md](https://github.com/MikeCoder/markdown-preview.vim/blob/master/TODO.md)
