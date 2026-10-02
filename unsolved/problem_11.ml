let read_file filename = 
  try
    In_channel.with_open_text filename In_channel.input_all
  with Sys_error msg -> 
    failwith ("Failed to read file: " ^ msg)

let input_to_intlst s =
  String.split_on_char '\n' s
  |> List.concat_map (String.split_on_char ' ')
  |> List.filter (fun x -> x <> "")
  |> List.map int_of_string


let () =
  read_file "input.txt"
  |> input_to_intlst
  |> List.iter print_int
