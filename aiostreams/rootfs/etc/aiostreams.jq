def col: {"silly":"\u001b[90m","debug":"\u001b[37m","verbose":"\u001b[36m","http":"\u001b[94m",
    "info":"\u001b[32m","warn":"\u001b[33m","error":"\u001b[1;31m"}[.] // "";

(try fromjson catch null) as $l | if ($l|type) == "object" and ($l.msg != null) then
    "\u001b[90m[" + (($l.time|tostring)[11:19]) + "]\u001b[0m "
    + ($l.level|col) + ($l.level|ascii_upcase) + "\u001b[0m"
    + (if $l.module then " \u001b[35m[" + $l.module + "]\u001b[0m" else "" end)
    + ": " + $l.msg
    + (($l|del(.level,.time,.module,.msg)) as $x
       | if ($x|length) > 0 then " \u001b[90m" + ($x|tojson) + "\u001b[0m" else "" end)
else . end
