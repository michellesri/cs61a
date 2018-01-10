(define (substitute s old new)
  (cond 
    ((null? s) 
      nil
    )
    
    ((pair? (car s)) 
      (cons (substitute (car s) old new) (substitute (cdr s) old new))
    )
    
    ((equal? (car s) old) 
      (cons new (substitute (cdr s) old new))
    )
    
    (else 
      (cons (car s) (substitute (cdr s) old new))
    )
  )
)

(define (get-index-of s lst index)
  (cond 
    ((null? lst) -1)
    ((pair? (car lst)) 
      (cond 
        ((= (get-index-of s (car lst) index) -1)
          (get-index-of s (cdr lst) (+ (length (car lst) index)))
        )
        (else (get-index-of s (car lst) index))
      )
    )
    ((equal? (car lst) s) 
      index
    )
    (else
      (get-index-of s (cdr lst) (+ index 1))
    )
  )
)

(define (get-item lst index)
  (cond
    ((null? lst) 
      nil
    )
    ((pair? (car lst))
      (cond
        ((> (length (car lst)) index)
          (get-item (car lst) index)
        )
        (else 
          (get-item (cdr lst) (- index (length (car lst))))
        )
      )
    )
    ((= index 0) (car lst))
    (else 
      (get-item (cdr lst) (- index 1))
    )
  )
)

(define (sub-all s olds news)
  (cond 
    ((null? s) nil)
    ((pair? (car s)) 
      (cons (sub-all (car s) olds news) (sub-all (cdr s) olds news))
    )
    ((= (get-index-of (car s) olds 0) -1)
      (cons (car s) (sub-all (cdr s) olds news))
    )
    (else
      (cons (get-item news (get-index-of (car s) olds 0)) (sub-all (cdr s) olds news))
    )
  )
)

(define (cadr s) (car (cdr s)))
(define (caddr s) (cadr (cdr s)))


; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond ((number? expr) 0)
        ((variable? expr) (if (same-variable? expr var) 1 0))
        ((sum? expr) (derive-sum expr var))
        ((product? expr) (derive-product expr var))
        ((exp? expr) (derive-exp expr var))
        (else 'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (sum? x)
  (and (list? x) (eq? (car x) '+)))
(define (addend s) (cadr s))
(define (augend s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
(cond ((or (=number? m1 0) (=number? m2 0)) 0)
      ((=number? m1 1) m2)
      ((=number? m2 1) m1)
      ((and (number? m1) (number? m2)) (* m1 m2))
      (else (list '* m1 m2))))
(define (product? x)
  (and (list? x) (eq? (car x) '*)))
(define (multiplier p) (cadr p))
(define (multiplicand p) (caddr p))

(define (derive-sum expr var)
  (make-sum (derive (cadr expr) var) (derive (caddr expr) var))
  
)

(define (derive-product expr var)
  (make-sum
    (make-product (derive (cadr expr) var) (caddr expr))
    (make-product (cadr expr) (derive (caddr expr) var))
  )
)

; Exponentiations are represented as lists that start with ^.
(define (make-exp base exponent)
  (cond
    ((= exponent 0) 1)
    ((= exponent 1) base)
    ((number? base) (expt base exponent))
    (else (list '^ base exponent))
  )
)

(define (base exp)
  (cadr exp)
)

(define (exponent exp)
  (caddr exp)
)

(define (exp? exp)
    (and (list? exp) (eq? (car exp) '^))
)

(define x^2 (make-exp 'x 2))
(define x^3 (make-exp 'x 3))

(define (derive-exp exp var)
  (make-product 
    (exponent exp) 
    (make-exp
      (base exp)
      (- (exponent exp) 1)
    )
  )
)
