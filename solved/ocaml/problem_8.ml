let explode s =
  let rec aux i l = 
    if i < 0 then l 
    else aux (i - 1) (s.[i] :: l) 
  in
  aux (String.length s - 1) []


let rec num_lst char_list = List.map char_to_int char_list

and char_to_int char =
  int_of_char char - 48

let rec lst_slice lst first last =
  let rec aux i slice_lst =
    match i <= last with 
    | false -> slice_lst
    | true -> aux (i + 1) (List.nth lst i :: slice_lst)
  in
  aux first []

and slice_sum_prod lst first last =
  List.fold_left ( * ) 1 (lst_slice lst first last)

and largest_series_prod count lst =
  let rec aux ans first last =
    match first + count <= List.length lst with
    | false -> ans
    | true -> 
      let new_ans = slice_sum_prod lst first last in
      match ans < new_ans with
      | true -> aux new_ans (first + 1) (last + 1)
      | false -> aux ans (first + 1) (last + 1)
  in
  aux 0 0 (count - 1)

let () =
  open_in "input.txt" 
  |> input_line 
  |> explode 
  |> num_lst 
  |> largest_series_prod 13
  |> print_int