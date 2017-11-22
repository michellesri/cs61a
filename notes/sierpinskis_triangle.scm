; Sierpinski

(define (repeat k fn)
  ; Repeat fn k times.
  (if (> k 1)
    (begin (fn) (repeat (- k 1) fn))
    (fn)))
