(* ****** ****** *)
use
"./../../../../mysmlib/mysmlib-cls.sml";
(* ****** ****** *)

(*
HX-2023-03-14: 20 points
Recall that a reference is precisely an array
of size 1. And it can be treated as a sequence.
For instance, we can define ref_foreach as follows
*)

(* ****** ****** *)

fun
ref_foreach
(r0: 'a ref, work: 'a -> unit): unit = work(!r0)

(* ****** ****** *)

(*
Please implement directly the following combinators
for for references. That is, your implementation should
not make use of any third-order functions defined in the
library for this class.
*)

(* ****** ****** *)


fun
ref_get_at
(ref0: 'a ref, i: int): 'a = !ref0


fun
ref_forall
(ref0: 'a ref, test: 'a -> bool): bool = test(!ref0)


fun
ref_map_list
(ref0: 'a ref, fopr: ('a) -> 'b): 'b list = [fopr(!ref0)]

fun
ref_foldleft
(ref0: 'a ref, res: 'r, fopr: ('r * 'a) -> 'r): 'r = fopr(res,!ref0)
fun

ref_ifoldleft
(ref0: 'a ref, res: 'r, fopr: ('r * int * 'a) -> 'r): 'r = fopr(res,0,!ref0)




(* end of [CS320-2023-Spring-assign05-01.sml] *)
