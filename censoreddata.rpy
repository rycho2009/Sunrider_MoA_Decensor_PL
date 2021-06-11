init -5:
    
    image cg_avascene:
        "Censored/avasexcg.jpg"
        
    image cg_avacg2:
        "Censored/avasexcg2.jpg"

init 10:
    $ CENSOR = False

label censorscene1:
        
    scene bg avaroom with dissolve
    show ava hs handhair blushsmile with dissolve

    "Ava włączyła grzejnik."
    kay "I have no idea why it's always so cold on Cera."
    kay "I hear Far Port has pretty good weather. Tropical year round."
    kay "Lots of beaches."
    ava "... ... ..."
    "Ava usiadła za Kayto."
    "She put her hand on his mouth"
    ava "... ... ..."
    ava "Hej, idioto."
    ava "Zamknij się na moment."
    ava "... ... ..."
    "Ava's face flushed red as her heart pounded."

    play sound "sound/heartbeat.ogg"
    show white:
        alpha 0.0
        ease 0.5 alpha 1.0
        ease 0.5 alpha 0.0

    "She leaned in. Their lips met."
    "The tender tingling on their lips was too distant. They searched deeper."
    "Ava shoved him down onto her bed."
    ava "Dalej zimno?"
    "She climbed on top of him, her legs straddling his hips."
    "She leaned down to his face."
    
    scene cg_avascene with dissolve
    
    "Her scent was intoxicating as they kissed. He unwrapped her in a rush."
    "Their chests pounded as two became one."
    ava "A-ah...!"
    "Wonder came over him as he saw Ava merge with him."
    "As the two caressed each other, black regret cut into his dream."
    "He had longed for this moment longer than he could remember."
    "He closed his eyes and drowned in Ava's warmth."
    "But why had he not done this sooner."
    "Why had he wanted until the last second, only after it was too late?"
    "Their hands met. Their fingers intertwined."
    "Instead, he chose to waste his youth on indecision and false leads."
    "He had to do something. Or else he would lose her forever."
    "Their bodies overheated."
    "With a final shove, Ava gasped for joy. She crumpled on top of him, her legs quivering."
    "He gasped as if death had him in its grasp, his world saturated white."
    ava "Haa... Haa.... haa..."
    "They were left breathing on top of each other for a moment."
    "She rolled off him."
    "They returned to being two."
    
    scene cg_avacg2 with dissolve
    
    ava "... ...  ..."
    "Kayto stroked Ava's face."
    kay "... ... ..."
    kay "Podjąłem decyzję. I'm going to enlist too."
    ava "Co?"
    kay "To nie jest koniec."
    kay "I'll be a year behind you. Kto wie co się wydarzy."
    kay "But we'll meet again in space one day. I promise it."
    ava "Ty...?"
    ava "Hahahaha!"
    ava "Ty... naprawdę jesteś idiotą."
    kay "To trochę zajmie. But we'll fly our own ship together."
    kay "A proud and mighty vessel of the Cera Space Force."
    kay "Będziemy mieć przygody w całej galaktyce. Będziemy pokonywać złych facetów. Będziemy bronić ludzkości."
    kay "Just you and me."
    kay "Captain Crescentia and First Officer Shields."
    kay "Just like old times."
    ava "... ... ..."
    "Ava flicked him on his forehead."
    ava "Heh."
    ava "Idiota."
    
    jump goodbyemaray
