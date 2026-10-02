type point = float * float
type shape =
  | Point of point
  | Circle of point * float
  | Rectangle of point * point

let p1 = Point (1., 1.)

let c1 = Circle ((1., 1.), 1.)
