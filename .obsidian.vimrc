" Was having a lot of problems navigating across elements
"" Have j and k navigate visual lines rather than logical ones
"" noremap j gj
"" noremap k gk
"" noremap gj j
"" noremap gk k
""
"" use logical line navigation in visual mode
"" vnoremap j gj
"" vnoremap k gk
"" vnoremap gj j
"" vnoremap gk k

nmap j gj
nmap k gk

nmap <A-e> <C-e> " move one line down
nmap <A-y> <C-y> " move one line up
nmap <A-b> <C-b> " move page up
nmap <A-f> <C-f> " move page down
nmap <A-d> <C-d> " move 1/2 page down
nmap <A-u> <C-u> " move 1/2 page up

" Quickly remove search highlights
nmap <F9> :nohl<CR>

" Yank to system clipboard
set clipboard=unnamed

" Maps pasteinto to Alt-p
map <A-p> :pasteinto<CR>

unmap <Space>
exmap findfile obcommand switcher:open
exmap omnisearchvault obcommand omnisearch:show-modal
exmap omnisearchfile obcommand omnisearch:show-modal-infile
exmap savefile obcommand editor:save-file
map <Space>fF :findfile<CR>
map <Space>fv :omnisearchvault<CR>
map <Space>ff :omnisearchfile<CR>
map <Space>fs :savefile<CR>

exmap commandpalatte obcommand command-palette:open
map <A-x> :commandpalatte<CR>

exmap focusRight obcommand editor:focus-right
nmap <Space>wl :focusRight<CR>

exmap focusLeft obcommand editor:focus-left
nmap <Space>wh :focusLeft<CR>

exmap focusTop obcommand editor:focus-top
nmap <Space>wk :focusTop<CR>

exmap focusBottom obcommand editor:focus-bottom
nmap <Space>wj :focusBottom<CR>

exmap splitVertical obcommand workspace:split-vertical
nmap <Space>wv :splitVertical<CR>

exmap splitHorizontal obcommand workspace:split-horizontal
nmap <Space>ws :splitHorizontal<CR>

exmap closewindow obcommand workspace:close-tab-group
nmap <Space>wc :closewindow<CR>

" undo/redo consistently on one key
nnoremap U <C-r>

" Make o and O respect context (requires Code Editor Shortcuts Plugin)
" exmap blankAbove obcommand obsidian-editor-shortcuts:insertLineAbove
" nmap &a& :blankAbove
" nmap O &a&i
" 
" exmap blankBelow obcommand obsidian-editor-shortcuts:insertLineBelow
" nmap &b& :blankBelow
" nmap o &b&i

exmap toggleList obcommand editor:toggle-bullet-list
nnoremap <Space>- :toggleList<CR>

" so repeated "V" selects more lines
vnoremap V gj
