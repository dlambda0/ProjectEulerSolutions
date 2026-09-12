
let (--) x y =
  let rec aux start stop =
    if start > stop then []
    else start :: aux (start + 1) stop
  in
  aux x y

(* Not Erathothenes Sieve :( *)
let sieve nums =
  let rec aux n_lst =
    match n_lst with
    | [] -> []
    | p :: rest ->
      p :: aux (List.filter (fun n -> n mod p <> 0) rest)
  in
  aux nums

let () = 
  print_int (List.nth (sieve (2 -- 300000)) 10000)
