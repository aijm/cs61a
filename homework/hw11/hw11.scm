(define (find s predicate)
  (cond ((null? s) #f)
        ((eq? (predicate (car s)) #t) (car s))
        (else (find (cdr-stream s) predicate)))
)

(define (scale-stream s k)
  (cons-stream (* (car s) k) (scale-stream (cdr-stream s) k))
)

(define (has-cycle s)
  'YOUR-CODE-HERE
 (define (in? lst s)  ;Check if stream s is in list lst
  (cond
   ((null? lst) #f)
   ((eq? (car lst) s) #t)
   (else (in? (cdr lst) s))))

 (define (has-cycle-helper memo s)
   (cond
    ((null? s) #f)
    ((in? memo s) #t)
    (else (has-cycle-helper (cons s memo) (cdr-stream s)))))

 (has-cycle-helper nil s)

)
(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)
