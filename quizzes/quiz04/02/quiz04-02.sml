(* ****** ****** *)
use "./../../../mysmlib/mysmlib-cls.sml";
(* ****** ****** *)

(*
Please put your implementation here for quiz04-02
*)

datatype 'a stream = Cons of 'a * (unit -> 'a stream)

fun stream_dupremov (fxs: int stream) =
    let
        fun helper prev str =
            case str of
                Cons(x, xs) =>
                    if x = prev then
                        helper x xs
                    else
                        Cons(x, fn () => helper x xs)
                | _ => "Empty"
    in
        case fxs of
            Cons(x, xs) => Cons(x, fn () => helper x xs)
            | _ => "Empty"
    end

(* end of [CS320-2023-Spring-quizzes-quiz04-02.sml] *)