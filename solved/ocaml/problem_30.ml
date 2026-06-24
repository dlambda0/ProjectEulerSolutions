let digitize n =
  let rec aux n acc = 
    match n with
    | 0 -> acc
    | _ -> aux (n / 10) ((n mod 10) :: acc)
  in
  aux n []

let int_pow base exp =
  let rec aux acc b e =
    match e with
    | 0 -> acc
    | _ -> aux (acc * b) b (e - 1)
  in
  aux 1 base exp

let exponentiate acc pow =
  List.map (fun x -> int_pow x pow) (digitize acc)

let power_sum n pow = 
  List.fold_left (fun x y -> x + y) 0 (exponentiate n pow)

let is_digit_power n =
  match power_sum n 5 with
  | x when x = n -> n
  | _ -> 0

let evaluate n = 
  let rec aux acc n =
    match n with
    | 999999 -> acc
    | _ -> aux (acc + (is_digit_power n)) (n + 1)
  in
  aux 0 n

let () =
  print_int (evaluate 2)