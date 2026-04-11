(* Useful functions I use across code samples! *)

let digitize n =
  let rec aux n acc = 
    match n with
    | 0 -> acc
    | _ -> aux (n / 10) ((n mod 10) :: acc)
  in
  aux n []