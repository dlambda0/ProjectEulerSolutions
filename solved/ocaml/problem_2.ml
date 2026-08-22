let fibonacci lim =
  let rec aux acc x y =
    match y <= lim with
    | true -> aux (y :: acc) y (x + y)
    | false -> acc
  in
  aux [] 1 2

let () =
  fibonacci 4000000
  |> List.fold_left (fun acc x -> 
      match x mod 2 with
      | 0 -> acc + x
      | _ -> acc
  ) 0
  |> print_int