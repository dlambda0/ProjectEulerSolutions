let int_sqrt n =
  float_of_int n
  |> sqrt
  |> int_of_float

let divisor_count n =
  let rec aux i acc =
    match i <= int_sqrt n with
    | true ->
      if n mod i = 0 then aux (i + 1) (acc + 2)
      else aux (i + 1) acc
    | false -> acc
    in
    aux 1 0

let divisors_in_tri d =
  let rec aux i acc =
    match divisor_count acc < d with
    | true -> aux (i + 1) (acc + i + 1)
    | false -> acc
  in
  aux 1 1

let () =
  divisors_in_tri 500
  |> print_int