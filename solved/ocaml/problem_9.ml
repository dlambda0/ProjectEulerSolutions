let is_py a b c =
  (a * a) + (b * b) = (c * c)

let is_uneven_py a b c =
  (a * a) + (b * b) < (c * c)

let find_py_triplet n =
  let rec aux a b =
    let c = n - a - b in
    match is_py a b c with
    | true -> [a; b; c]
    | false -> 
      match is_uneven_py a b c with
      | true -> aux (b - 2) (b - 1)
      | false -> aux (a - 1) b
  in
  aux (n / 3) (n / 2 - 1)

let prod_sum int_lst =
  List.fold_left (fun x y -> x * y) 1 int_lst

let () =
  find_py_triplet 1000
  |> prod_sum
  |> print_int
