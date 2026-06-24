let mult_3_or_5 lim = 
  let rec aux acc n = 
    match n with
    | n when n >= lim -> acc
    | n when n mod 3 = 0 ||n mod 5 = 0 -> aux (acc + n) (n + 1)
    | _ -> aux acc (n + 1)
  in
  aux 0 1

let () =
  print_int (mult_3_or_5 1000)