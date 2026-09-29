let rec range start stop =
  if start > stop then []
  else start :: range (start + 1) stop

let rec sieve nums =
  match nums with
  | [] -> [] 
  | p :: rest -> 
    p :: sieve (List.filter (fun n -> n mod p <> 0) rest)

let () =
  print_int 1