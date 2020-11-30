style inventory_label:
    xalign 0.2
style slot:
    background Frame("square", 0, 0)
    minimum(85, 85)
    maximum(85, 85)
    xalign 0.5
screen shop_screen:
    add "gray"
    #add "shop_bg" xalign 0.5 yalign 0.5
    hbox:
        #char details
        vbox:
            xmaximum 300
            spacing 10
            label "Welcome. How can I help you?" text_size 35 text_color "#000000"
            label "Balance: $[character.money]" text_color "#000000"
            add "shopkeeper" yanchor -.15

        #grid

        grid 7 5:
            for item in shop:
                frame:
                    style "slot"
                    imagebutton idle item.img action SetVariable("selected_shop_item", item) xalign 0.5 yalign 0.5
            for i in range(len(shop), 35):
                frame:
                    style "slot"

        #item details
        vbox:
            spacing 10
            label "Item Details" xalign 0.5 text_size 45 text_color "#000000"

            if selected_shop_item != None:
                frame:
                    style "slot" xalign 0.5
                    add selected_shop_item.img xalign 0.5 yalign 0.5

                label "[selected_shop_item.name]" xalign 0.5 text_size 45 text_color "#000000"

                label "Description: [selected_shop_item.desc]" xalign 0.5 text_size 15 text_color "#000000"

                if isinstance(selected_shop_item, Consumable):
                    label "Type: Consumable" xalign 0.5 text_size 15 text_color "#000000"
                    if selected_shop_item.prod != 0:
                        label "Productivity: +[selected_shop_item.prod]" xalign 0.5 text_size 15 text_color "#000000"
                    if selected_shop_item.skills != 0:
                        label "Technical: +[selected_shop_item.skills]" xalign 0.5 text_size 15 text_color "#000000"
                    if selected_shop_item.stress != 0:
                        label "Stress: -[selected_shop_item.stress]" xalign 0.5 text_size 15 text_color "#000000"
                    label "Price: $[selected_shop_item.buy]" xalign 0.5 text_size 15 text_color "#000000"
                    label "Sell Price: $[selected_shop_item.sell]" xalign 0.5 text_size 15 text_color "#000000"

                if isinstance(selected_shop_item, Keyboard):
                    label "Type: Keyboard" xalign 0.5 text_size 15 text_color "#000000"
                    label "Productivity: +[selected_shop_item.prod]" xalign 0.5 text_size 15 text_color "#000000"
                    label "Price: $[selected_shop_item.buy]" xalign 0.5 text_size 15 text_color "#000000"
                    label "Sell Price: $[selected_shop_item.sell]" xalign 0.5 text_size 15 text_color "#000000"

                if isinstance(selected_shop_item, Mouse):
                    label "Type: Mouse" xalign 0.5 text_size 15 text_color "#000000"
                    label "Productivity: +[selected_shop_item.prod]" xalign 0.5 text_size 15 text_color "#000000"
                    label "Price: $[selected_shop_item.buy]" xalign 0.5 text_size 15 text_color "#000000"
                    label "Sell Price: $[selected_shop_item.sell]" xalign 0.5 text_size 15 text_color "#000000"

                if isinstance(selected_shop_item, Chair):
                    label "Type: Chair" xalign 0.5 text_size 15 text_color "#000000"
                    label "Productivity: +[selected_shop_item.prod]" xalign 0.5 text_size 15 text_color "#000000"
                    label "Price: $[selected_shop_item.buy]" xalign 0.5 text_size 15 text_color "#000000"
                    label "Sell Price: $[selected_shop_item.sell]" xalign 0.5 text_size 15 text_color "#000000"

                if isinstance(selected_shop_item, Monitor):
                    label "Type: Monitor" xalign 0.5 text_size 15 text_color "#000000"
                    label "Productivity: +[selected_shop_item.prod]" xalign 0.5 text_size 15 text_color "#000000"
                    label "Price: $[selected_shop_item.buy]" xalign 0.5 text_size 15 text_color "#000000"
                    label "Sell Price: $[selected_shop_item.sell]" xalign 0.5 text_size 15 text_color "#000000"

                if isinstance(selected_shop_item, Equipment):
                    if selected_shop_item.buy <= character.money:
                        textbutton "Buy for $[selected_shop_item.buy]" action [AddToSet(inventory, selected_shop_item), Function(character.subMoney, selected_shop_item.buy), SetVariable("selected_shop_item", None)]
                    else:
                        label "You do not have enough $ to buy." text_size 25 text_color "#FF0000"
                elif isinstance(selected_shop_item, Book):
                    if selected_shop_item.buy <= character.money:
                        textbutton "Buy for $[selected_shop_item.buy]" action [AddToSet(inventory, selected_shop_item), RemoveFromSet(shop, selected_shop_item), Function(character.subMoney, selected_shop_item.buy), SetVariable("selected_shop_item", None)]
                    else:
                        label "You do not have enough $ to buy." text_size 25 text_color "#FF0000"
                else:
                    if selected_shop_item.buy <= character.money:
                        textbutton "Buy for $[selected_shop_item.buy]" action [Function(inventory.append, selected_shop_item), Function(character.subMoney, selected_shop_item.buy), SetVariable("selected_shop_item", None)]
                    else:
                        label "You do not have enough $ to buy." text_size 25 text_color "#FF0000"

    textbutton "Return":
        action Return()
        xalign 0.5
        yalign 0.95
        text_size 35
