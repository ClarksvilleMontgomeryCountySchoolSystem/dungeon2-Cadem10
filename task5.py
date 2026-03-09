good = money = r"""
 $$ $             
             \O/$            
            $ |              
             /_\             
           _|___|_           
         _|___|___|_         
       _|___|___|___|_       
     _|___|___|___|___|_     
   _|___|___|___|___|___|_   
 _|___|___|___|___|___|___|_ 
|___|___|___|___|___|___|___|
 \o/ \o/ \o/ \o/ \o/ \o/ \o/ 
  |   |   |   |   |   |   |  
 / \ / \ / \ / \ / \ / \ / \ 
"""
bad = mosquito = r"""
,-.
         `._        /  |        ,
            `--._  ,   '    _,-'
     _       __  `.|  / ,--'
      `-._,-'  `-. \ : /
           ,--.-.-`'.'.-.,_-
         _ `--'-'-;.'.'-'`--
     _,-' `-.__,-' / : \
                _,'|  \ `--._
  jrei     _,--'   '   .     `-.
         ,'         \  |        `

"""
escaped = False
if escaped:
    outcome = "Legend: You successfully escaped and are on your journey home."
    print(good)
else:
    outcome = "Doom: You were not able to escape and were caught by the guards and thrown in prison forever."
    print(bad)
print(outcome)
