good = door = r"""      ______
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|
"""
bad = dragon = r"""
_.===._      ,"^^^^",
           /_\^^^/_\    /  ^ ,^  \     ,
           (0\ ^ /0)\  / ^  /  ^  \    /\
            \     /  ^^   ^ \ ^ \  ",." /
             )   (  ^  ^   ^ \   \    ,'
             (o_o)^    \ ^   ,)  /`^^`
              ^V^\ ^ \  \_,-"((((
      jgs     /  /`""/  /
             (((`   '(((
"""
has_key = True
if has_key:
    outcome = "Click: The door slowly swings open and the winding path continues."
    print(good)
else:
    outcome = "Doom: The door remains firmly locked and you hear something approaching behind you."
    print(bad)
print(outcome)