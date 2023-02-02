fun str2int_opt (cs : string): int option =
  let
    fun checkNum (str: string, i: int): bool =
      if i >= String.size(str) then true
      else if ord(String.sub(str, i)) - ord(#"0") >= 0 andalso ord(String.sub(str, i)) - ord(#"0") <= 9 then checkNum(str, i+1)
      else false

    fun convert (i: int,k: int): int option =
      if i = String.size(cs) then SOME(k)
      else if i = 0 then convert(i+1, (ord(String.sub(cs, 0)) - ord(#"0")))
      else convert(i+1, 10*k + (ord(String.sub(cs, i)) - ord(#"0")))
  in
    if cs = "" orelse checkNum(cs, 0) = false then NONE
    else convert(0,0)
  end;
