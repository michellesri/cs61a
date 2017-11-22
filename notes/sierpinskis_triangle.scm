; Sierpinski

(define (repeat k fn)
  ; Repeat fn k times.
  (if (> k 1)
    (begin (fn) (repeat (- k 1) fn))
    (fn)))

(define (tri fn)
  ; Repeat fn 3 times, each followed by a 120 degree turn.
  (repeat 3 (lambda () (fn) (lt 120))))

(define (sier d j)
  ; Draw three legs of Sierpinski's triangle to depth d.
  (tri (lambda ()
    (if (= k 1)(fd d) (leg d k)))))
