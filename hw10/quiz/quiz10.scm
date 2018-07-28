(define (how-many-dots s dot-count)
  (cond
    ((null? s)
      nil
    )
    ((pair? (car s))
      (how-many-dots (cdr s) dot-count)
    )
    ((number? (cdr s)
      (how-many-dots (cdr s) (+ dot-count 1))
    ))
  )
)

// if it's not a pair, but there is
a number after that, call fn again and increment dot-count

;;; Tests

(how-many-dots '(1 2 3))
; expect 0
(how-many-dots '(1 2 . 3))
; expect 1
(how-many-dots '((1 . 2) 3 . 4))
; expect 2
(how-many-dots '((((((1 . 2) . 3) . 4) . 5) . 6) . 7))
; expect 6
(how-many-dots '(1 . (2 . (3 . (4 . (5 . (6 . (7)))))))
; expect 0
