a = input("Spielregeln: Gieb im Spiel immer 0 oder 1 ein um weiterzukommen. Aber verrate mir hier bitte deinen Alias(Name)")

print(f"Hallo {a} willst du in die Höhle gehen, oder den Pfad über den Berg wählen? \nWenn du in die Höhle willst schreibe 0, \nwenn du den Pfad nimmst, schreibe 1")

b = input("")

if b == "0":

    print("Du begegnest in der Höhle dem Goblin Richtelbicht. Er spricht zu dir: Fleisch, Fleisch, Fleisch. \nWas willst du tun, den Goblin erschlagen, oder mit ihm verhandeln?")
    print("Befehl 0: Du kämpfst mit dem Goblin")
    print("Befehl 1: Du verhandelst mit dem Goblin")
elif b == "1":
    print("Du wanderst den Pfad entlang und entdeckst eine Hängebrücke. \nWillst du sie überqueeren, oder den Graben durchklettern.") 
    print("Befehl Hängebrücke: 0, Befehl Graben: 1")

c= input("")

if b == "0" and c == "0":
    print("Der Goblin gewinnt und frisst dich")
    print(f"Du hast verloren {a}")
elif b == "0" and c == "1": 
    print("Der Goblin fragt dich: Was ist Frage, die keine Antwort kennen?")
    print("Befehl: Die Antwort, die keine Antwort ist, ist das Schweigen.: 0")
    print("Befehl: Die Antwort, die keine Antwort sein darf ist Gewalt.:1")

elif b == "1" and c == "0":
    print("Die Hängebrücke stürzt ein und du stürzt in die magische Welt Avalon. \nDort fällst du auf das Schwert Excalibur und es durchdringt deine Seele. \n(Du bist tod)")
    print(f"Du hast verloren {a}")
elif b == "1" and c == "1":
    print("Du gehst einen beschwerlichen Marsch und überwindest den Pfad. \nDann begegnest du Baumknospi in seiner Hütte. \nDu sprichst zu ihm:")
    print("Befehl 0: Hallo Werter Herr ist diese Gesellschaft inklusiv oder exclusiv?")
    print("Befehl 1: Hilfe bitte rette mich, ich habe Hunger.")

d = input("")

if b == "0" and c == "1" and d == "0":
    print("Ich haben gelernt, du nehmen Fleisch")
    print("Du gehst weiter und gelangst zügig durch die Höhle, da Richtelbicht dich zum Ausgang führt.")
    print("Du gehst ein Stück weiter und findest eine Hütte.")
    print("Befehl 0: Du klopfst an der Tür")
    print("Befehl 1: Du gehst in den Wald")
elif b == "0" and c == "1" and d == "1":
    print('Richtelbicht sagt:"Gewalt sein Recht der Starken." Der Goblin erschlägt dich und du bist tod.')
    print(f"Du hast verloren {a}")

elif b == "1" and c == "1" and d == "0":
    print("Baumknospi ladet dich auf Kaffe, Kuchen und eine Übernachtung ein.")
    print("Baumknospi fragt dich, was dich herführt.")
    print("Befehl 0: Ich möchte gerne das Wissen verstehen.")
    print("Befehl 1: Ich möchte gerne darüber diskutieren, warum ich so oft vor dem Anderen zu Wort komme und dann hinters Licht geführt werde.")
elif b == "1" and c == "1" and d == "1":
    print('Baumknospi sagt:"Du bist sicher Richtelbicht verschwinde und du verhungerst im Wald hinter der Hütte')
    print(f"Du hast verloren {a}")
e = input("")

if b == "0" and c == "1" and d == "0" and e == "0":
    print('Baumknospie öffnet die Tür und sieht dein Fleisch. \nEr schreit:"Hilfe Richtelbicht und ermordet dich."')
    print(f"Du hast verloren {a}")
elif b == "0" and c == "1" and d == "0" and e == "1":
    print("Du gehst in den Wald und findest einen Wolf. \nWas willst du tun?")
    print("Befehl 0: Du gibst dem Wolf das Fleisch.")
    print("Befehl 1: Du versuchst zu flüchten.")

elif b == "1" and c == "1" and d == "0" and e == "0":
    print('Baumknospi spricht zu dir:"Das Wissen ist als Fakt, also als anerkannter Messwert in Form einer Information definiert. Man kann es nicht verstehen, aber man kann es auswendig lernen. Aber ja es ist die Grundlage für das Assoziieren von Informationen. Wenn man durch Assoziationen miteinander verzweigte Informationen interpretiert, nennt man das Verständis."')
    print("Befehl 0: Du bewunderst Baumknospi und gehst schlafen.")
    print('Befehl 1: Du gibst zu bedenken, dass Messwerte nie ganz exakt sind und immer in einem Toleranzbereich liegen, der von der absoluten Exaktheit abweicht.')
elif b == "1" and c == "1" and d == "0" and e == "1":
    print('Baumknospi antwortet: Wer mit sich selbst im GLeichklang ist, steht vor dem Licht, wer korrigiert wird sollte lernen, wie man es richtig macht."')
    print("Danach schickt dich Baumknospi zu Bett")
    print("Klicke einfach die Entertaste")

f = input("")
if b == "0" and c == "1" and d == "0" and e == "1" and f == "0":
    print("Der Wolf wird dein Freund und führt dich aus dem Wald zum nächsten Dorf")
    print(f"Glückwunsch: Du gewinnst das Spielt {a}")
elif b == "0" and c == "1" and d == "0" and e == "1" and f == "1":
    print("Der Wolf holt dich ein und frisst dich und dein Fleisch")
    print(f"Du verlierst das Spiel {a}")

elif b == "1" and c == "1" and d == "0" and e == "0" and f == "1":
    print('Baumknospi antwortet:"Ganz genau, das hast du gut gemacht"')
    print("Er belohnt dich mit einer Karte, mit der du jederzeit zum nächsten Dorf findest")
    print(f"Du gewinnst das Spiel {a}")

if b == "1" and c == "1" and d == "0" and f == "0" or b == "1" and c == "1" and d == "0" and e == "1":
    print("Du wachst auf und Baumknospi hat ein Frühstück hergerichtet.")
    print("Ihr esst gemeinsam und kommt zum Philosophieren.")
    print("Baumknospi fragt dich: Was ist der Sinn des Lebens?")
    print("Befehl 0: Der Sinn des Lebens ist das Erreichen von Zufriedenheit")
    print("Befehl 1: Der Sinn des Lebens ist nicht dauerhaft festzuhalten.")

g = input("")

if b == "1" and c == "1" and d == "0" and f == "0" and g == "0" or b == "1" and c == "1" and d == "0" and e == "1" and g == "0":
    print('Baumknospi antwortet:"Ganz genau, das hast du gut gemacht"')
    print("Er belohnt dich mit einer Karte, mit der du jederzeit zum nächsten Dorf findest")
    print(f"Du gewinnst das Spiel {a}")
    exit()
elif b == "1" and c == "1" and d == "0" and f == "0" and g == "1" or b == "1" and c == "1" and d == "0" and e == "1" and g == "1":
    print('Baumknospi fragt:"Und deswegen ist der Sinn des Lebens immer das, was dir welche Geisteshaltung beschert?')
    x = input("Tippe die richtige Antwort ein.")


if x == "Zufriedenheit":
    print('Baumknospi antwortet:"Ganz genau, das hast du gut gemacht"')
    print("Er belohnt dich mit einer Karte, mit der du jederzeit zum nächsten Dorf findest")
    print(f"Du gewinnst das Spiel{a}")
else:
    print("Baumknospi will nicht weiter diskutieren und ladet dich aus.")
    print("Du gehst in den Düsterwald hinter der Hütte und wirst vom Wolf gefressen")
    print(f"Du hast verloren{a}")