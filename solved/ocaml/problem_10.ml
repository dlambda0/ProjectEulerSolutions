
let mark_multiples p primes n = 
  let rec aux p i = 
    match i < n + 1 with
    | true -> primes.(i) <- false; aux p (i + p)
    | false -> ()
  in
  aux p (p * p)


let arrbool_to_int primes n =
  let rec aux p acc =
    match p < n + 1 with
    | false -> acc
    | true ->
      if primes.(p) then
        aux (p + 1) (p :: acc)
      else
        aux (p + 1) acc
  in
  List.rev (aux 2 [])

(* As functional as possible, but still imperative -_- *)
let sieve n = 
  let primes = Array.make (n + 1) true in
  let rec aux p primes =
    match p * p <= n with
    | false -> primes
    | true -> 
      if primes.(p) then 
        mark_multiples p primes n; 
      aux (p + 1) primes 
  in
  arrbool_to_int (aux 2 primes) n


let () =
  print_int (List.fold_left ( + ) 0 (sieve 2000000))
