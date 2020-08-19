if !has("python3")
    echo "vim has to be compiled with +python3 to run this"
    finish 
endif

if exists('g:jsonformat_plugin_loaded')
    finish 
endif

let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3  << EOF
import sys 
import os.path
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
# print(plugin_root_dir)
python_root_dir = os.path.join(plugin_root_dir,'python')
# print(python_root_dir)
# python_root_dir = normpath(join(plugin_root_dir, '\\', 'python'))
# print(python_root_dir)
sys.path.insert(0, python_root_dir)
import jsonformat
EOF

function! PrintCountry()
    py3 jsonformat.print_country()
endfunction

function! InsertCountry()
    py3 jsonformat.insert_country()
endfunction

function! JsonFormat()
    py3 jsonformat.json_format()
endfunction

command! -nargs=0 InsertCountry call InsertCountry()
command! -nargs=0 PrintCountry call PrintCountry()
command! -nargs=0 JsonFormat call JsonFormat()

let g:jsonformat_plugin_loaded = 1
