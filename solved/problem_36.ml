let to_base base n =
  let rec aux acc n =
    match n with
    | 0 -> acc
    | _ -> aux ((n mod base) :: acc) (n / base)
  in
  aux [] n

(* stolen from stack overflow, lol *)
let is_palindrome l =
  let rec aux l0 l1 =
    match (l0, l1) with
    | _, [] -> (true, [])
    | hd :: tl, [x] -> (hd = x, tl)
    | _, hdl :: tl1 -> let (pal, ll) = aux l0 tl1 in
      match ll with
      | [] -> (pal, [])
      | hd::tl -> (pal && hdl = hd, tl) in
  match l with
  | [] -> true
  | _ -> fst (aux l l)

let is_double_palindrome n =
  is_palindrome (to_base 10 n) && is_palindrome (to_base 2 n)

let ret_double_palindrome n =
  match is_double_palindrome n with
  | true -> n
  | false -> 0

let evaluate mx =
  let rec aux acc mx =
    match mx with
    | 0 -> acc
    | _ -> aux (acc + ret_double_palindrome mx) (mx - 1)
  in
  aux 0 mx

let () =
  print_int (evaluate 999999)