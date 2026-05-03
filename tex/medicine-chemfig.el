;;; tex/medicine-chemfig.el --- Chemfig diagram editor for the medicine vault -*- lexical-binding: t; -*-

(defconst medicine/vault-root
  (expand-file-name
   (pcase (intern (or (getenv "MEDICINE_PLATFORM") ""))
     ('linux "~/Documents/Areas/Medicine")
     (_      "~/Documents/02 areas/Medicine"))))

(defconst medicine/tex-dir         (expand-file-name "tex"         medicine/vault-root))
(defconst medicine/attachments-dir (expand-file-name "attachments" medicine/vault-root))

(defconst medicine/chemfig-template
  "\\documentclass[tikz, border=2pt]{standalone}
\\usepackage{tikz}
\\usepackage{chemfig}
\\setchemfig{
  atom sep=2.5em,         % bond length
  bond style={line width=0.8pt},
  double bond sep=2pt,
  baseline=(current bounding box.center)
}
\\begin{document}
\\chemfig{}
\\end{document}
")

;;; Buffer-local state

(defvar-local medicine/chemfig--name   nil "Diagram name (no extension).")
(defvar-local medicine/chemfig--source nil "Marker in the source markdown buffer, or nil.")

;;; Yequake bridge

(defvar medicine/chemfig--pending nil
  "The chemfig buffer prepared for the next yequake-toggle call.")

(defun medicine/chemfig--yequake-fn ()
  "Return the pending chemfig buffer; used as a yequake buffer-fn."
  (or (and (buffer-live-p medicine/chemfig--pending)
           medicine/chemfig--pending)
      (current-buffer)))

;;; Compile and dismiss

(defun medicine/chemfig--compile ()
  "Save, compile, post-process SVG, insert wikilink in source, close frame."
  (interactive)
  (let* ((name   medicine/chemfig--name)
         (source medicine/chemfig--source)
         (tex    (expand-file-name (concat name ".tex") medicine/tex-dir))
         (pdf    (expand-file-name (concat name ".pdf") medicine/tex-dir))
         (svg    (expand-file-name (concat name ".svg") medicine/attachments-dir))
         (fix    (expand-file-name "svg-colorfix.py"    medicine/tex-dir))
         (default-directory medicine/tex-dir)
         (cbuf (current-buffer)))
    (write-region (point-min) (point-max) tex)
    (message "medicine-chemfig: compiling %s…" name)
    (if (zerop (call-process "latexmk" nil "*medicine-chemfig*" nil
                             "-pdf" "-interaction=nonstopmode"
                             (concat name ".tex")))
        (if (zerop (call-process "pdf2svg" nil "*medicine-chemfig*" nil pdf svg))
            (progn
              (call-process "python3" nil nil nil fix svg)
              (message "medicine-chemfig: saved → attachments/%s.svg" name)
              (when (and source (marker-buffer source))
                (with-current-buffer (marker-buffer source)
                  (save-excursion
                    (goto-char source)
                    (insert (format "![[%s.svg]]" name)))))
              (medicine/chemfig--dismiss cbuf))
          (error "pdf2svg failed — see *medicine-chemfig* buffer"))
      (error "LaTeX failed — see *medicine-chemfig* buffer"))))

(defun medicine/chemfig--dismiss (&optional buf)
  "Close the chemfig frame and kill BUF (or current buffer) without compiling."
  (interactive)
  (let ((b (or buf (current-buffer))))
    (when (and (featurep 'yequake)
               (fboundp 'my/yequake-frame-visible-p)
               (my/yequake-frame-visible-p "medicine-chemfig"))
      (yequake-toggle "medicine-chemfig"))
    (when (buffer-live-p b)
      (kill-buffer b))))

;;; Minor mode

(define-minor-mode medicine-chemfig-mode
  "Minor mode for editing chemfig diagrams.
\\{medicine-chemfig-mode-map}"
  :lighter " ⬡"
  :keymap (let ((m (make-sparse-keymap)))
            (define-key m (kbd "C-c C-c") #'medicine/chemfig--compile)
            (define-key m (kbd "C-c C-k") #'medicine/chemfig--dismiss)
            m))

;;; Entry point

;;;###autoload
(defun medicine/new-chemfig (name)
  "Open a chemfig diagram buffer named NAME in a yequake popup.
When called interactively from a markdown buffer in the vault, inserts
![[NAME.svg]] at point after a successful compile."
  (interactive "sDiagram name: ")
  (let* ((in-vault (and buffer-file-name
                        (file-in-directory-p buffer-file-name medicine/vault-root)))
         (marker   (when (and in-vault (derived-mode-p 'markdown-mode))
                     (point-marker)))
         (buf      (get-buffer-create (format "*chemfig:%s*" name))))
    (with-current-buffer buf
      (erase-buffer)
      (insert medicine/chemfig-template)
      (goto-char (point-min))
      (re-search-forward "\\\\chemfig{" nil t)
      (setq-local medicine/chemfig--name   name
                  medicine/chemfig--source marker)
      (require 'latex nil t)
      (if (fboundp 'LaTeX-mode) (LaTeX-mode) (latex-mode))
      (medicine-chemfig-mode 1)
      (message "C-c C-c  compile + export   |   C-c C-k  discard"))
    (setq medicine/chemfig--pending buf)
    (if (and (featurep 'yequake)
             (assoc "medicine-chemfig" yequake-frames))
        (progn
          (when (and (fboundp 'my/yequake-frame-visible-p)
                     (my/yequake-frame-visible-p "medicine-chemfig"))
            (yequake-toggle "medicine-chemfig"))
          (yequake-toggle "medicine-chemfig"))
      (pop-to-buffer buf))))

(provide 'medicine-chemfig)
;;; medicine-chemfig.el ends here
