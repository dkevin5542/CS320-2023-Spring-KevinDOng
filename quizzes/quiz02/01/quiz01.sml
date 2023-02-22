use
"./../../../mysmlib/mysmlib-cls.sml"

val = strlen = foreach_to_length(string_foreach)
val = strsub = foreach_to_get_at(string_foreach)

fun quiz02-01 (word: string): char -> int =
    fn (c: char) =>
    let
        val len = strlen(word)
        val count = ref 0
      fun counter (i: int) =
        if i = len then !count
        else
        let
          val letter = strsub(word, i)
        in
          if letter = c then (count := !count + 1)
          counter (i + 1)
        end
    in
      counter(0)
    end