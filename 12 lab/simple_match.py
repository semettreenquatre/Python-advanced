#!/usr/bin/env python3


# + a
# + ab
# - b
# - ba
REGEXP_1 = '^a'

# + aab
# + abb
# + acb
# - ab
# - aabc
REGEXP_2 = '^.{3}$'

# + sofia.mp3
# + sofia.mp4
# - sofia.mp7
# - sofia.mp34
REGEXP_3 = '[a-z]+\.mp[3-4]$'

# + taverna
# + versus
# + vera
# + zveri
# - zver
REGEXP_4 = '[a-z]*ver[a-z]+'

# - a
# - aa
# + aaa
# - aaaa
# - b
# - bb
# + bbb
# - bbbb
# - ccc
REGEXP_5 = '[ab]{3}$'

# - Ok
# - OkOk
# + OkOkOk
# - OkOkOkOk
# - ab
# - abab
# + ababab
# - abababab
REGEXP_6 = '(.{2}){3}$'

# - aaa
# - aaa aaa
# + aaa Aaa aaa
# + aaa aaa Aaa
# + Aaa aaa aaa
# - A
# - aaa A aaa
REGEXP_7 = '.*Aaa'

# + abc
# + abc03
# + a-b-c-3
# + a.b.c.0
# - Aabc
# - abc1
# - #abc
REGEXP_8 = '^a(.*)b(.*)c([^1]*)$'
