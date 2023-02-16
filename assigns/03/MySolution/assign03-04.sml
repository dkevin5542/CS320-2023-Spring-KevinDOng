(* ****** ****** *)
(*
use "./../assign03.sml";
use "./../assign03-lib.sml";

*)
(* ****** ****** *)

(*
HX-2023-02-10: 20 points
Given a list of integers xs,
please implement a function that find
the longest ascending subsequences of [xs].
If there are more than one such sequences,
the left most one should be returned.

fun list_longest_ascend(xs: int list): int list
*)
use "./../../../mysmlib/mysmlib-cls.sml";

fun list_longest_ascend(xs: int list): int list =
    let
        fun helpfindmin(xs: int list): int =
            case xs of
            [] => raise Empty
            | [x] => x
            | x::rest =>
                let
                    val findmin = helpfindmin rest
                in
                    if x < findmin then x else findmin
                end

        fun test(xs: int list, prev: int): int list =
            
            case xs of
                [] => []
            |x::xs => if (x >= prev) then
                let
                    val keep = x :: test(xs, x)
                    val drop = test(xs, prev)
                in
                    if list_length(keep)>=list_length(drop) then keep 
                    else drop
                end
                    else test(xs, prev)

    in
        if xs = [] then []
        else test(xs, helpfindmin(xs))
    end

(* end of [CS320-2023-Spring-assign03-04.sml] *)
