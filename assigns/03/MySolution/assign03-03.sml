(* ****** ****** *)
(*
use "./../assign03.sml";
use "./../assign03-lib.sml";
*)
(* ****** ****** *)

(*
//
HX-2023-02-10: 10 points
The function list_tabulate takes an integer
[n] and a function [f] and returns a list that
equals [f(0), f(1), ..., f(n-1)]
//
list_tabulate(n: int, f: int -> 'a): 'a list
//
*)
fun list_tabulate(n: int, f: int -> 'a): 'a list=
    let
      fun helper(i, num) =
        if i < 0 then num
        else helper(i-1, f(i)::num)
    in
      helper(n-1, [])
    end



(* end of [CS320-2023-Spring-assign03-03.sml] *)
