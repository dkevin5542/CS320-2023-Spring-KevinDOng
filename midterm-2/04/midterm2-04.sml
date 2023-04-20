(* ****** ****** *)

use "./../../mysmlib/mysmlib-cls.sml";

(* ****** ****** *)

(*
//
// HX-2023-04-20: 20 points
//
// A non-empty sequence of numbers forms a
// "drawdown" if every number in the sequence does not
// exceed the first one. A maximal drawdown is one that
// is not contained in any longer drawdowns.
// Please implement a function stream_drawdowns that takes
// an infinite stream fxs of integers and returns a stream
// enumerating all the maximal drawdowns in fxs.
//
*)

(* ****** ****** *)

fun stream_drawdowns(fxs: int stream): int list stream =
  let
    fun helper(prev: int, s: int stream): int list stream =
      case s of
        Cons(x, xs) =>
          if x <= prev then
            (* start a new drawdown *)
            Cons([x], helper(x, xs))
          else
            (* continue the current drawdown or start a new one *)
            let
              val with_x = Cons(x, helper(x, xs))
              val without_x = helper(prev, xs)
            in
              append with_x without_x
            end
  in
    helper(hd fxs, fxs)
  end

(* end of [CS320-2023-Spring-midterm2-04.sml] *)
