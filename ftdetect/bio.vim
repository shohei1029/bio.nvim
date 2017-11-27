augroup filetypedetect
    au BufNewFile,BufRead *.{fa,fasta}         setf fasta
    au BufNewFile,BufRead *.faa                setf fasta_aa
    au BufNewFile,BufRead *.{ffn,fna}          setf fasta_nt
    au BufNewFile,BufRead *.gff                setf gff
    au BufNewFile,BufRead *.{gb,gbk,genbank}   setf genbank
augroup END
