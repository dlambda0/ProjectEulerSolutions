
let string_to_numslice str stop = 
  int_of_string (String.sub str 0 stop)

let load_first_n_digits file n =
  let ic = open_in file in
  let rec aux acc =
    try
      let line = input_line ic in
      aux (string_to_numslice (line) (n) :: acc)
    with End_of_file ->
      close_in ic;
      acc
  in
  aux []

let () =
  load_first_n_digits "input.txt" 15
  |> List.fold_left ( + ) 0
  |> print_int