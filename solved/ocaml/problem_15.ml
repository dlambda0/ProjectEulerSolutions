let fact n =
  let rec aux n return = 
    match n with
    | 0 -> return 1
    | n -> return (aux (n-1) (fun x -> x * n)) 
  in
  aux n (fun x -> x)

let combinations n r =
  (fact n) / (fact (n-r)) * (fact r)

let () =
  print_int (combinations 40 20)