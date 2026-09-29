(* Just went with a brute force implementation *)

let reverse_number n = 
  let rec aux rev temp = 
    match temp != 0 with
    | true -> aux ((rev * 10) + (temp mod 10)) (temp / 10)
    | false -> rev
  in
  aux 0 n

let is_palindrome n =
  (reverse_number n) = n

let largest_palindrome =
  let rec aux num1 num2 =
    match is_palindrome (num1 * num2) with
    | true -> (num1 * num2)
    | false -> 
      match num2 = 0 with
      | true -> aux (num1 - 1) 999
      | false -> aux num1 (num2 - 1)
  in
  aux 999 999

let () =
  print_int largest_palindrome