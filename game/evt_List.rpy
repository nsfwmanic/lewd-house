init python:
    ########################################
    ########################################
    ## TODO Register events
    ## Register events
    ## example event("introduction", "act == 'day'", event.once(), event.only())
    event("intro", "act == 'night' and date <= startdate ", event.once(), event.only(), priority=101)
    event("empty", "act == 'morn'", event.once(), event.only(), priority=201)
    #event("N", "act == 'night'", event.once(), event.only(), priority=201)

    ##Gerneal Events
    #event("D", "act == 'day'", event.once(), priority=200)
    #event("N", "act == 'night'", priority=200)
    #event("M0002", "act == 'morn'", event.choose_one('morn'), priority=200)
    #event("M0003", "act == 'morn'", event.choose_one('morn'), priority=200)

    ##  Going places
    #event("p_home", "act == 'home'")
    #event("p_gym", "act == 'gym'")
    #event("pre_bat", "act == 'battle'")
    #event("act_sleep", "act == 'sleep'")
    #event("trainr", "act == 'trainr'")
    #event("train1", "act == 'train1'")
    #event("train2", "act == 'train2'")
    #event("train3", "act == 'train3'")

    ##  Action events
    #event("do_stuff", "act == 'stuff'")

    ##   House Map
    event("empty", "act == 'stuff'")
    event("room", "act == 'stuff'")

    ##  Meals
    #Breakfast, Lunch Dinner
    ## DayPhase = morning,afternoon,evening,night
    event("Breakfast", "act == 'morning' and DayPhase == 3", priority=201)
    event("Lunch", "act == 'afternoon' and DayPhase == 3", priority=201)
    event("Dinner", "act == 'evening' and DayPhase == 2", priority=201)
    event("room", "act == 'morning'", priority=200)
    event("room", "act == 'afternoon'", priority=200)
    event("room", "act == 'evening'", priority=200)

    #NightPhase
    event("NightPhase", "act == 'night'", priority=200)
    ########################################
    ########################################
