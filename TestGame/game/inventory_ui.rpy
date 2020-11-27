style inventory_label:
    xalign 0.2

style slot:
    background Frame("square", 0, 0)
    minimum(85, 85)
    maximum(85, 85)
    xalign 0.5

screen inventory_screen:
    style_prefix "inventory"

    add "white"
    hbox:
        #char details
        vbox:
            xmaximum 300
            spacing 10
            label "Character Stats" xalign 0.5 text_size 35
            label "Productivity: [player.prod]"
            label "Stress: [player.stress]"
            label "Technical Skills: [player.skills]"

            #equips
            frame:
                style "slot"
                if player.keyboard != None:
                    imagebutton idle player.keyboard.img action SetVariable("selected_item", player.keyboard) xalign 0.5 yalign 0.5
                else:
                    label "keyboard" xalign 0.5 yalign 0.5 text_size 15

            frame:
                style "slot"
                if player.mouse != None:
                    imagebutton idle player.mouse.img action SetVariable("selected_item", player.mouse) xalign 0.5 yalign 0.5
                else:
                    label "mouse" xalign 0.5 yalign 0.5 text_size 15

            frame:
                style "slot"
                if player.chair != None:
                    imagebutton idle player.chair.img action SetVariable("selected_item", player.chair) xalign 0.5 yalign 0.5
                else:
                    label "chair" xalign 0.5 yalign 0.5 text_size 15

            frame:
                style "slot"
                if player.monitor != None:
                    imagebutton idle player.monitor.img action SetVariable("selected_item", player.monitor) xalign 0.5 yalign 0.5
                else:
                    label "monitor" xalign 0.5 yalign 0.5 text_size 15

        #grid

        grid 7 7:
            for item in inventory:
                frame:
                    style "slot"
                    imagebutton idle item.img action SetVariable("selected_item", item) xalign 0.5 yalign 0.5
            for i in range(len(inventory), 49):
                frame:
                    style "slot"

        #item details
        vbox:
            spacing 10
            label "Item Details" xalign 0.5 text_size 35

            if selected_item != None:
                frame:
                    style "slot" xalign 0.5
                    add selected_item.img xalign 0.5 yalign 0.5

                label "[selected_item.name]" xalign 0.5 text_size 35

                label "Description: [selected_item.desc]" xalign 0.5 text_size 15

                if isinstance(selected_item, Consumable):
                    label "Type: Consumable" xalign 0.5 text_size 15
                    if selected_item.prod != 0:
                        label "Productivity: +[selected_item.prod]" xalign 0.5 text_size 15
                    if selected_item.skills != 0:
                        label "Technical: +[selected_item.skills]" xalign 0.5 text_size 15
                    if selected_item.stress != 0:
                        label "Stress: -[selected_item.stress]" xalign 0.5 text_size 15
                    label "Sell Price: $[selected_item.sell]" xalign 0.5 text_size 15
                    textbutton "Use" action Function(selected_item.use, player)
                if isinstance(selected_item, Keyboard):
                    label "Type: Keyboard" xalign 0.5 text_size 15
                    label "Productivity: +[selected_item.prod]" xalign 0.5 text_size 15
                    label "Sell Price: $[selected_item.sell]" xalign 0.5 text_size 15
                    if selected_item.is_equipped:
                        textbutton "Unequip" action [Function(selected_item.unequip), RemoveFromSet(equipped, selected_item), AddToSet(inventory, selected_item)]
                    else:
                        if player.keyboard is None:
                            textbutton "Equip" action [Function(selected_item.equip, player), RemoveFromSet(inventory, selected_item), AddToSet(equipped, selected_item)]
                if isinstance(selected_item, Mouse):
                    label "Type: Mouse" xalign 0.5 text_size 15
                    label "Productivity: +[selected_item.prod]" xalign 0.5 text_size 15
                    label "Sell Price: $[selected_item.sell]" xalign 0.5 text_size 15
                    if selected_item.is_equipped:
                        textbutton "Unequip" action [Function(selected_item.unequip), RemoveFromSet(equipped, selected_item), AddToSet(inventory, selected_item)]
                    else:
                        if player.mouse is None:
                            textbutton "Equip" action [Function(selected_item.equip, player), RemoveFromSet(inventory, selected_item), AddToSet(equipped, selected_item)]
                if isinstance(selected_item, Chair):
                    label "Type: Chair" xalign 0.5 text_size 15
                    label "Productivity: +[selected_item.prod]" xalign 0.5 text_size 15
                    label "Sell Price: $[selected_item.sell]" xalign 0.5 text_size 15
                    if selected_item.is_equipped:
                        textbutton "Unequip" action [Function(selected_item.unequip), RemoveFromSet(equipped, selected_item), AddToSet(inventory, selected_item)]
                    else:
                        if player.chair is None:
                            textbutton "Equip" action [Function(selected_item.equip, player), RemoveFromSet(inventory, selected_item), AddToSet(equipped, selected_item)]
                if isinstance(selected_item, Monitor):
                    label "Type: Monitor" xalign 0.5 text_size 15
                    label "Productivity: +[selected_item.prod]" xalign 0.5 text_size 15
                    label "Sell Price: $[selected_item.sell]" xalign 0.5 text_size 15
                    if selected_item.is_equipped:
                        textbutton "Unequip" action [Function(selected_item.unequip), RemoveFromSet(equipped, selected_item), AddToSet(inventory, selected_item)]
                    else:
                        if player.monitor is None:
                            textbutton "Equip" action [Function(selected_item.equip, player), RemoveFromSet(inventory, selected_item), AddToSet(equipped, selected_item)]

                if isinstance(selected_item, Equipment):
                    if not selected_item.is_equipped:
                        textbutton "Sell for $[selected_item.sell]" action [RemoveFromSet(inventory, selected_item), SetVariable("selected_item", None), Function(player.addMoney, selected_item.sell)]
                else:
                    textbutton "Sell for $[selected_item.sell]" action [RemoveFromSet(inventory, selected_item), SetVariable("selected_item", None), Function(player.addMoney, selected_item.sell)]

    textbutton "Return":
        #action [Return(), SetVariable("selected_item", None)]
        action Return()
        xalign 0.5
        yalign 0.95

screen show_inventory:
    vbox:
        spacing 5
        imagebutton idle "bag" action ShowMenu("inventory_screen")
        imagebutton idle "shop" action ShowMenu("shop_screen")