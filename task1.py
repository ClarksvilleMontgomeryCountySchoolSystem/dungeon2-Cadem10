good = torch = r"""/|
        /\/ |/\
        \  ^   | /\  /\
  (\/\  / ^   /\/  )/^ )
   \  \/^ /\       ^  /
    )^       ^ \     (
   (   ^   ^      ^\  )
    \___\/____/______/
    [________________]
     |              |
     |     //\\     |
     |    <<()>>    |
     |     \\//     |
      \____________/
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
"""
bad = dinosaur = r"""
  oo`'._..---.___..-
 (_,-.        ,..'`
      `'.    ;
         : :`
        _;_;
"""
torch_lit = True
if not torch_lit:
    outcome = "Doom: The room is covered in darkness as you hear something in the corner."
    print(bad)
else:
    outcome = "Flicker: The room glows softly and the path is revealed."
    print(good)
print(outcome)
