# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#--------------[Personajes]---------------
define i= Character('???', color="#a8a8a8")
define c= Character('Creator', color="#d7eceb")
define p= Character('Pereza', color="#3249a7")
define e= Character('Ellie', color="#f00707")
define g= Character('Gula', color="#a31097")
define h= Character('Hipatia', color="#b1179c")

#--------------[Sprites de pereza]----------------
image pereza_normal = "gui/Sprites/pereza_normal.png"
image pereza_serio = "gui/Sprites/Pereza_Serio.png"
image pereza_enojado = "gui/Sprites/Pereza_enojado.png"

#---------------[Sprites de Gula]--------------------
image gula_normal = "gui/Sprites/Gula_Normal.png"
image gula_normal_h = "gui/Sprites/Gula_Normal_H.png"

#-----------------[Creador]-----------------------
image Creador_indiferente = "gui/scenas/Creador_indiferente.png"
image Creador_feliz = "gui/scenas/Creador_feliz.png"
image Creador_insano = "gui/scenas/Creador_insano.png"
image Creador_insano_f = "gui/scenas/Creador_insano(f).png"
image Creador_serio = "gui/scenas/Creador_serio.png"

###---------------[Fondos]------------------------
image Fondo_negro = "gui/scenas/Fondo_negro.png"
image Fondo_surcos = "gui/scenas/Fondo_surcos.png"

# The game starts here.


label start:
    $ renpy.store.preferences.text_cps = 50
    c   "-Han cometido un gran error al entrar a este palacio y más aún.. intentar robarme-"

    scene Creador_indiferente
    with fade 
    pause 0.5

    scene Creador_serio

    p   "{color=#2fa27c}Era la voz más fría y sin alma que había escuchado a lo largo de mi existencia, no podía creer que 
        un ser con esa apariencia y título podría llegar a ponerme de los nervios.{/color}"

    scene Creador_feliz
    pause 0.5

    scene Creador_insano_f
    with fade

    p   "{color=#2fa27c}Después de esas palabras mi mente fue arrastrada a un plano extraño,  pronto solo fue despertar 
        dándome cuenta que me había perdido una parte de mi vida, como si hubiese sido borrada.{/color}"

    scene Fondo_negro
    with fade
    pause 0.5
    
    scene Creador_insano
    with fade

    c   "-¿Saben?, quizá sea mejor no malgastarlos -"

    scene Fondo_surcos
    with fade

    p "{color=#2fa27c}De inmediato supimos que eso nos llevaría a un trato, uno que no podríamos rechazar, por más en 
    desacuerdo que estuviésemos.{/color}"

    scene Fondo_negro
    with fade

    $ renpy.store.preferences.text_cps = 5

    "... "

    $ renpy.store.preferences.text_cps = 50

    i "-Des...erta- "

    p   "{color=#2fa27c}A lo lejos escuche una voz entre cortada, pronto lo que tenía en mi mente para de 
        reproducirse y poco a poco esta voz se hizo más clara.{/color}"

    i "-¡DESPIERTA!-"

    p   "{color=#2fa27c}Pronto me levanté un poco, solo para recibir un almohadazo en el rostro{/color}{w} -¡Mmhpm!- "

    i   "-¡Por fin ~!, pense que jamas despertarías jeje, vaya demonio perezoso, aunque es por eso que 
        estás aquí en el infierno ¿no es así?-"

    show gula_normal with dissolve
    show gula_normal at right
    with moveinleft

    show pereza_normal with dissolve
    show pereza_normal at left 
    with moveinright

    p   "{color=#2fa27c}De inmediato vi adelante, y ahí estaba nadie más ni nadie menos que [g.name], con su mirada 
        burlona en la cara, honestamente a veces me daban ganas de borrarle esa sonrisa del rostro.{/color}"

    hide gula_normal

    show gula_normal_h at right

    g "-¡Vamos!, no te lo tomes enserio, ¿porque no bajas de una vez?-" 

    hide gula_normal_h
    show gula_normal at right

    p "{color=#2fa27c}Dijo ensanchando aún más su
    sonrisa, solo pensé {b}{i}que fastidio tener tanta energía.{/i}{/b}{/color}"
    
    show pereza_normal with dissolve
    show pereza_normal at left 
    with moveinright

    menu:
        "Como reaccionar"

        "Enojarse porque lo han despertado":
            hide pereza_normal 

            show pereza_serio at left

            p   "-¿Tienes que ser tan ruidoso o solo te pones así de insoportable en las mañanas?
            -{color=#2fa27c}Dije bastante irritado, un poco apagado por la falta de ganas.{/color}"

            g   "- Vaya, con esa contestación pensaría que eres más un demonio de la ira que de la pereza,
            señor cascarrabias-"
            
            p "{color=#2fa27c}Dijo con una sonrisa más pequeña que la anterior, lo cuál me dio algo 
            de satisfacción por dentro.{/color}"

        "No hacer nada":
            p   "{color=#2fa27c}La verdad no tenía las ganas suficientes como para contestar a su actitud fastidiosa, así 
            que mejor pase de él, aunque su sonrisa bajó considerablemente, ¿Que acaso quería que 
            le contestara?{/color}"

    p "{color=#2fa27c}[g.name] termino por salir de la habitacion. Pronto me levante de la cama, solo tome la ropa que
    tenía más a la mano, me la puse, y no me moleste en arreglar mi cabello quedando exactamente 
    como me levanté.{/color}"

return
