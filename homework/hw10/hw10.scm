(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (combiner (accumulate combiner start (- n 1) term) (term n))
  )
)

(define (accumulate-tail combiner start n term)
  (if (= n 0)
      start
      (accumulate-tail combiner (combiner start (term n)) (- n 1) term))
)

(define-macro (list-of expr for var in seq if filter-fn)
  'YOUR-CODE-HERE
)