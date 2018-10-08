; Q1
(define (compose-all funcs)
  (if (null? funcs) 
      (lambda (x) x)
      (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x))))
)

; Q2
(define (tail-replicate x n)
; 若普通的递归，则(cons x (tail-replicate x (- n 1)))
; 需要记录上一个list的信息，再拼接，所以可以用辅助递归函数，将lst作为参数
  (define (inner x n lst)
    (if (= n 0)
        lst
        (inner x (- n 1) (cons x lst)))
  )
  (inner x n nil)
)