use "./../assign01.sml";
use "assign01-01.sml";

fun xlist_sub(xs: 'a xlist, i0: int): 'a =
    case xs of
    xlist_nil => raise XlistSubscript exception
    |xlist_cons(x1, xs) => if (i0 = 0) then x1 
    else xlist_sub(xs, i0 - 1)
    |xlist_snoc(xs, x1) => if (i0 = xlist_size(xs)) then xlist_sub(xs, i0)
    else raise XlistSubscript exception
    |xlist_append(xs, ys) => if(i0 )
    |xlist_reverse(xs) => 