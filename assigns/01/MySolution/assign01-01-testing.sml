fun xlist_size(xs: 'a xlist): int =
    case xs of
       [] => 0
     | x :: xs => 1 + xlist_size;