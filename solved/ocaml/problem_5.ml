let check_divisibles n divs =
  let rec aux n i = 
  match i <= divs with
  | false -> n
  | true -> 
    match n mod i with
    | 0 -> aux n (i + 1)
    | _ -> aux (n + 2520) 1
  in
  aux n 1

let () =
  print_int (check_divisibles 2520 20)