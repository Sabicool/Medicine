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
nmap <F9> :nohl

" Yank to system clipboard
set clipboard=unnamed

" Maps pasteinto to Alt-p
map <A-p> :pasteinto

unmap <Space>
exmap findfile obcommand switcher:open
exmap omnisearchvault obcommand omnisearch:show-modal
exmap omnisearchfile obcommand omnisearch:show-modal-infile
exmap savefile obcommand editor:save-file
map <Space>fF :findfile
map <Space>fv :omnisearchvault
map <Space>ff :omnisearchfile
map <Space>fs :savefile

exmap commandpalatte obcommand command-palette:open
map <A-x> :commandpalatte

exmap focusRight obcommand editor:focus-right
nmap <Space>wl :focusRight

exmap focusLeft obcommand editor:focus-left
nmap <Space>wh :focusLeft

exmap focusTop obcommand editor:focus-top
nmap <Space>wk :focusTop

exmap focusBottom obcommand editor:focus-bottom
nmap <Space>wj :focusBottom

exmap splitVertical obcommand workspace:split-vertical
nmap <Space>wv :splitVertical

exmap splitHorizontal obcommand workspace:split-horizontal
nmap <Space>ws :splitHorizontal

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
nnoremap <Space>- :toggleList

" so repeated "V" selects more lines
vnoremap V gj
