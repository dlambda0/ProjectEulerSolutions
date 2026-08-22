(* for some reason,  ocaml only has support for float exponentiation *)

let sum_of_squares n =
  let rec aux i acc =
    match i = (n +. 1.0) with
    | true -> acc
    | false -> aux (i +. 1.0) (acc +. (i ** 2.0))
  in
  aux 1.0 0.0

let square_of_sum n =
  let rec aux i acc =
    match i = (n +. 1.0) with
    | true -> acc ** 2.0
    | false -> aux (i +. 1.0) (acc +. i)
  in
  aux 1.0 0.0

let sum_square_difference n =
  (square_of_sum n) -. (sum_of_squares n)

let () =
  print_float (sum_square_difference 100.0)