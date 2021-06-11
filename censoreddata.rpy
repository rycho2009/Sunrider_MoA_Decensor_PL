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
    kay "Nie mam pojęcia, dlaczego na Cerze zawsze jest tak zimno."
    kay "I hear Far Port has pretty good weather. Tropical year round."
    kay "Lots of beaches."
    ava "... ... ..."
    "Ava usiadła za Kayto."
    "Położyła dłonie na jego usta"
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
    "The tender tingling on their lips was too distant. Szukali głębiej."
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
    "Ich dłonie się spotkały. Their fingers intertwined."
    "Instead, he chose to waste his youth on indecision and false leads."
    "Musiał coś zrobić. Inaczej straciłby ją na zawsze."
    "Their bodies overheated."
    "With a final shove, Ava gasped for joy. She crumpled on top of him, her legs quivering."
    "He gasped as if death had him in its grasp, his world saturated white."
    ava "Haa... Haa.... haa..."
    "They were left breathing on top of each other for a moment."
    "She rolled off him."
    "They returned to being two."
    
    scene cg_avacg2 with dissolve
    
    ava "... ...  ..."
    "Kayto pogłaskał twarz Avy."
    kay "... ... ..."
    kay "Podjąłem decyzję. Ja też się zaciągnę."
    ava "Co?"
    kay "To nie jest koniec."
    kay "Będę rok za tobą. Kto wie co się wydarzy."
    kay "Ale pewnego dnia spotkamy się znowu. Obiecuję."
    ava "Ty...?"
    ava "Hahahaha!"
    ava "Ty... naprawdę jesteś idiotą."
    kay "To trochę zajmie. Ale polecimy naszym własnym statkiem razem."
    kay "Dumnym i potężnym okrętem Sił Kosmicznych Cery."
    kay "Będziemy mieć przygody w całej galaktyce. Będziemy pokonywać złych facetów. Będziemy bronić ludzkości."
    kay "Tylko ty i ja."
    kay "Kapitan Crescentia ai Pierwszy Oficer Shield."
    kay "Tak jak za starych czasów."
    ava "... ... ..."
    "Ava pstryknęła go w czoło."
    ava "Heh."
    ava "Idiota."
    
    jump goodbyemaray
