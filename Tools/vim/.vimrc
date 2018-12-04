" simple conf without any other extensions
set nu                                        "show line number
set pastetoggle=<F9>                          "good way to avoid paste trouble
autocmd BufWritePost $MYVIMRC source $MYVIMRC "enbale conf works right away.
syntax on
set autoindent                                "自动缩进
set smartindent                               "智能缩进
set hlsearch                                  "搜索高亮
set showmatch                                 "显示括号匹配
set ruler                                     "显示下方标识
set tabstop=4                                 "设置tab为4个空格
set smarttab

