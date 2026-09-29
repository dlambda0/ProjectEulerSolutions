let rec factor_of_2 n =
  let rec aux n acc =
    match n mod 2 with
    | 0 -> aux (n / 2) 2
    | _ -> factor_of_3 n
  in
  aux n 0

and factor_of_3 n =
  let rec aux n acc =
    match n mod 3 with
    | 0 -> aux (n / 3) 3
    | _ -> check_odd_factors n
  in
  aux n 2

and check_odd_factors n =
  let rec aux n i acc =
    match n >= i with
    | false -> final_check n acc
    | true ->
      match n mod i with
      | 0 -> aux (n / i) (i + 6) (i)
      | _->
        match n mod (i + 2) with
        | 0 -> aux (n / (i + 2)) (i + 6) (i + 2)
        | _ -> aux n (i + 6) acc
  in
  aux n 5 3

and final_check n acc =
  match n > 4 with
  | true -> n
  | false -> acc

let largest_prime_factor n =
  factor_of_2 n

let () =
  print_int (largest_prime_factor 600851475143)
