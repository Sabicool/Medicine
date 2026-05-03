;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "<none>"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("standalone" "tikz" "border=2pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("tikz" "") ("chemfig" "")))
   (TeX-run-style-hooks
    "latex2e"
    "standalone"
    "standalone10"
    "tikz"
    "chemfig"))
 :latex)

