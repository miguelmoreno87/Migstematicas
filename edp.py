from manim import *

class video1(Scene):
    def construct(self):
        # Presentación del vídeo
        title = Text("Interpretación geométrica de una EDP").move_to(UP*2)
        self.wait(1)
        self.play(FadeIn(title))
        eq1 = MathTex(r"(1) \hspace{0.5cm}a\frac{\partial f}{\partial x}+"
                      r"b\frac{\partial f}{\partial y}=0").move_to(LEFT*3+DOWN)
        eq1p2 = MathTex(r"(2) \hspace{0.5cm}y\frac{\partial f}{\partial x}-"
                      r"x\frac{\partial f}{\partial y}=0").move_to(LEFT * 3 + DOWN)
        eq1p3 = MathTex(r"(3) \hspace{0.5cm}x\frac{\partial f}{\partial x}+"
                        r"y\frac{\partial f}{\partial y}=0").move_to(LEFT * 3 + DOWN)
        eq1p4 = MathTex(r"a, b\in \mathbb{R}").move_to(RIGHT*2 + DOWN)
        eq1p5 = MathTex(r"f(x,y)").move_to(RIGHT * 2 + DOWN)
        texto1 = Text("i) Lineal").move_to(RIGHT*3).scale(0.5)
        texto2 = Text("ii) Primer orden").move_to(DOWN + RIGHT * 3).scale(0.5)
        texto3 = Text("iii) Homogénea").move_to(DOWN * 2 + RIGHT * 3).scale(0.5)
        self.wait()
        self.play(FadeIn(eq1))
        self.wait(2)
        self.play(FadeIn(eq1p4))
        self.wait(2)
        self.play(FadeOut(eq1p4))
        self.wait(2)
        self.play(FadeIn(eq1p5))
        self.wait(2)
        self.play(FadeOut(eq1p5))
        self.wait(2)
        self.play(Transform(eq1, eq1p2))
        self.wait(3)
        self.play(Transform(eq1, eq1p3))
        self.wait(3)
        self.play(FadeIn(texto1))
        self.wait()
        self.play(FadeIn(texto2))
        self.wait()
        self.play(FadeIn(texto3))
        self.wait()
        self.play(FadeOut(title), FadeOut(eq1), FadeOut(texto1),
                  FadeOut(texto2), FadeOut(texto3))
        self.wait(2)
        mw = ImageMobject("5MW.png").scale(0.25).move_to(np.array([0,1,0]))
        label = Text("Migsworld").move_to(np.array([0,-2,0]))
        self.play(FadeIn(mw), Write(label))
        self.wait(3)
        self.play(FadeOut(mw), FadeOut(label))
        self.wait(2)

        # EDP como producto escalar
        eq2 = MathTex(r"\vec{v}\cdot \nabla{f} =",
                      r" (a , b) \cdot \Bigl(\frac{\partial f}{\partial x} , \frac{\partial f}{\partial y} \Bigr) =",
                      r"a\frac{\partial f}{\partial x}+b\frac{\partial f}{\partial y} =",
                      r"0")
        eq3 = MathTex(r"\vec{v}\cdot \nabla{f} =",
                      r" 0",
                      r" \Longrightarrow \vec{v} \perp \nabla{f}")
        self.play(FadeIn(eq2[2]),FadeIn(eq2[3]))
        self.wait(2)
        self.play(FadeIn(eq2[1]))
        self.wait(2)
        self.play(FadeIn(eq2[0]))
        self.wait(3)
        self.play(FadeOut(eq2[1]),FadeOut(eq2[2]))
        self.play(Transform(eq2[3],eq3[1]),Transform(eq2[0],eq3[0]))
        self.wait(3)
        self.play(FadeIn(eq3[2]))
        self.wait(3)
        self.play(FadeOut(eq2[0]),FadeOut(eq2[3]),FadeOut(eq3[2]))
        self.wait()

class video2(VectorScene):
    def construct(self):
        self.wait(2)
        gris = "#C7C7C7"
        verde = "#02B126"
        rojo = "#CF010B"
        plane = NumberPlane(
            background_line_style={
                "stroke_color": gris,
                "stroke_opacity": 0.3,
                "stroke_width": 2
            },
            axis_config={
                "stroke_width": 4,
                "label_direction": DR,
                "include_ticks": True,
                "include_numbers": False
            }
        )
        self.play(FadeIn(plane))
        self.wait(2)

        #Primer ejemplo
        myVec = Vector([1, 0]).set_color(rojo)
        label1 = MathTex(r"\vec{v} = (a , b)", color=rojo).move_to(np.array([1, 0.5, 0]))
        label2 = MathTex(r"\vec{v} = (1 , 0)", color=rojo).move_to(np.array([1, 0.5, 0]))
        self.play(FadeIn(label1))
        self.wait(2)
        self.play(Transform(label1, label2))
        self.add_vector(myVec)
        self.wait(2)
        self.play(FadeOut(label1))
        grad1 = Vector([0, 3]).set_color(verde)
        grad2 = Vector([0, 3]).set_color(verde).shift(np.array([7, 0, 0]))
        grad3 = Vector([0, 3]).set_color(verde).shift(np.array([-7, 0, 0]))
        grad4 = Vector([0, 3]).set_color(verde)
        label_grad1 = MathTex(r"\nabla{f}", color=verde).move_to(np.array([-0.6, 1.5, 0]))
        label_grad2 = MathTex(r"\nabla{f}", color=verde).move_to(np.array([-0.6 + 7, 1.5, 0]))
        label_grad3 = MathTex(r"\nabla{f}", color=verde).move_to(np.array([-0.6 - 7, 1.5, 0]))
        label_grad4 = MathTex(r"\nabla{f}", color=verde).move_to(np.array([-0.6, 1.5, 0]))
        self.add_vector(grad1)
        self.play(FadeIn(label_grad1))
        self.wait(3)
        recta1 = Line(start=np.array([-10, 0, 0]), end=np.array([10, 0, 0])).set_color(rojo)
        recta2 = Line(start=np.array([-10, 0, 0]), end=np.array([10, 0, 0])).set_color(rojo).move_to(
            np.array([0,1,0]))
        recta3 = Line(start=np.array([-10, 0, 0]), end=np.array([10, 0, 0])).set_color(rojo).move_to(
            np.array([0, 2, 0]))
        recta4 = Line(start=np.array([-10, 0, 0]), end=np.array([10, 0, 0])).set_color(rojo).move_to(
            np.array([0, 3, 0]))
        recta5 = Line(start=np.array([-10, 0, 0]), end=np.array([10, 0, 0])).set_color(rojo).move_to(
            np.array([0, 4, 0]))
        recta6 = Line(start=np.array([-10, 0, 0]), end=np.array([10, 0, 0])).set_color(rojo).move_to(
            np.array([0, -1, 0]))
        recta7 = Line(start=np.array([-10, 0, 0]), end=np.array([10, 0, 0])).set_color(rojo).move_to(
            np.array([0, -2, 0]))
        recta8 = Line(start=np.array([-10, 0, 0]), end=np.array([10, 0, 0])).set_color(rojo).move_to(
            np.array([0, -3, 0]))
        recta9 = Line(start=np.array([-10, 0, 0]), end=np.array([10, 0, 0])).set_color(rojo).move_to(
            np.array([0, -4, 0]))
        self.play(FadeIn(recta1))
        self.play(FadeOut(myVec))
        self.wait(2)
        self.play(Transform(grad1, grad2), Transform(label_grad1,label_grad2), run_time=2)
        self.play(Transform(grad1, grad3), Transform(label_grad1,label_grad3), run_time=2)
        self.play(Transform(grad1, grad4), Transform(label_grad1,label_grad4), run_time=2)
        self.wait()
        self.play(FadeIn(recta2), FadeIn(recta3), FadeIn(recta4), FadeIn(recta5), FadeIn(recta6), FadeIn(recta7),
                  FadeIn(recta8), FadeIn(recta9))
        self.wait(3)

class video3(VectorScene):
    def construct(self):
        self.wait(2)
        gris = "#C7C7C7"
        verde = "#02B126"
        rojo = "#CF010B"
        plane = NumberPlane(
            background_line_style={
                "stroke_color": gris,
                "stroke_opacity": 0.3,
                "stroke_width": 2
            },
            axis_config={
                "stroke_width": 4,
                "label_direction": DR,
                "include_ticks": True,
                "include_numbers": False
            }
        )
        self.play(FadeIn(plane))
        self.wait(2)

        # Segundo ejemplo
        myVec = Vector([1, 2]).set_color(rojo)
        label1 = MathTex(r"\vec{v} = (a , b)", color=rojo).move_to(np.array([2, 2.5, 0]))
        label2 = MathTex(r"\vec{v} = (1 , 2)", color=rojo).move_to(np.array([2, 2.5, 0]))
        self.play(FadeIn(label1))
        self.wait(2)
        self.play(Transform(label1, label2))
        self.add_vector(myVec)
        self.wait(2)
        self.play(FadeOut(label1))
        grad1 = Vector([-3, 1.5]).set_color(verde)
        grad2 = Vector([-3, 1.5]).set_color(verde).shift(np.array([2, 4, 0]))
        grad3 = Vector([-3, 1.5]).set_color(verde).shift(np.array([-2, -4, 0]))
        grad4 = Vector([-3, 1.5]).set_color(verde)
        label_grad1 = MathTex(r"\nabla{f}", color=verde).move_to(np.array([-2, 1.5, 0]))
        label_grad2 = MathTex(r"\nabla{f}", color=verde).move_to(np.array([-2 + 2, 1.5 + 4, 0]))
        label_grad3 = MathTex(r"\nabla{f}", color=verde).move_to(np.array([-2 - 2, 1.5 - 4, 0]))
        label_grad4 = MathTex(r"\nabla{f}", color=verde).move_to(np.array([-2, 1.5, 0]))
        self.add_vector(grad1)
        self.play(FadeIn(label_grad1))
        self.wait(3)
        recta1 = Line(start=np.array([-8, -16, 0]), end=np.array([8, 16, 0])).set_color(rojo)
        recta2 = Line(start=np.array([-8, -16, 0]), end=np.array([8, 16, 0])).set_color(rojo).move_to(
            np.array([0, 2, 0]))
        recta3 = Line(start=np.array([-8, -16, 0]), end=np.array([8, 16, 0])).set_color(rojo).move_to(
            np.array([0, -2, 0]))
        recta4 = Line(start=np.array([-8, -16, 0]), end=np.array([8, 16, 0])).set_color(rojo).move_to(
            np.array([0, 4, 0]))
        recta5 = Line(start=np.array([-8, -16, 0]), end=np.array([8, 16, 0])).set_color(rojo).move_to(
            np.array([0, -4, 0]))
        recta6 = Line(start=np.array([-16, -32, 0]), end=np.array([16, 32, 0])).set_color(rojo).move_to(
            np.array([0, 6, 0]))
        recta7 = Line(start=np.array([-16, -32, 0]), end=np.array([16, 32, 0])).set_color(rojo).move_to(
            np.array([0, -6, 0]))
        recta8 = Line(start=np.array([-16, -32, 0]), end=np.array([16, 32, 0])).set_color(rojo).move_to(
            np.array([0, 8, 0]))
        recta9 = Line(start=np.array([-16, -32, 0]), end=np.array([16, 32, 0])).set_color(rojo).move_to(
            np.array([0, -8, 0]))
        recta10 = Line(start=np.array([-16, -32, 0]), end=np.array([16, 32, 0])).set_color(rojo).move_to(
            np.array([0, 10, 0]))
        recta11 = Line(start=np.array([-16, -32, 0]), end=np.array([16, 32, 0])).set_color(rojo).move_to(
            np.array([0, -10, 0]))
        recta12 = Line(start=np.array([-16, -32, 0]), end=np.array([16, 32, 0])).set_color(rojo).move_to(
            np.array([0, 12, 0]))
        recta13 = Line(start=np.array([-16, -32, 0]), end=np.array([16, 32, 0])).set_color(rojo).move_to(
            np.array([0, -12, 0]))
        recta14 = Line(start=np.array([-16, -32, 0]), end=np.array([16, 32, 0])).set_color(rojo).move_to(
            np.array([0, 14, 0]))
        recta15 = Line(start=np.array([-16, -32, 0]), end=np.array([16, 32, 0])).set_color(rojo).move_to(
            np.array([0, -14, 0]))
        recta16 = Line(start=np.array([-16, -32, 0]), end=np.array([16, 32, 0])).set_color(rojo).move_to(
            np.array([0, 16, 0]))
        recta17 = Line(start=np.array([-16, -32, 0]), end=np.array([16, 32, 0])).set_color(rojo).move_to(
            np.array([0, -16, 0]))
        recta18 = Line(start=np.array([-16, -32, 0]), end=np.array([16, 32, 0])).set_color(rojo).move_to(
            np.array([0, 18, 0]))
        recta19 = Line(start=np.array([-16, -32, 0]), end=np.array([16, 32, 0])).set_color(rojo).move_to(
            np.array([0, -18, 0]))
        self.play(FadeIn(recta1))
        self.play(FadeOut(myVec))
        self.wait(2)
        self.play(Transform(grad1, grad2), Transform(label_grad1,label_grad2), run_time=2)
        self.play(Transform(grad1, grad3), Transform(label_grad1,label_grad3), run_time=2)
        self.play(Transform(grad1, grad4), Transform(label_grad1,label_grad4), run_time=2)
        self.wait()
        self.play(FadeIn(recta2), FadeIn(recta3), FadeIn(recta4), FadeIn(recta5), FadeIn(recta6), FadeIn(recta7),
                  FadeIn(recta8), FadeIn(recta9), FadeIn(recta10), FadeIn(recta11), FadeIn(recta12),
                  FadeIn(recta13), FadeIn(recta14), FadeIn(recta15), FadeIn(recta16), FadeIn(recta17),
                  FadeIn(recta18), FadeIn(recta19))
        self.wait(3)

class video4(Scene):
    def construct(self):
        # Primer ejemplo
        eq1 = MathTex(r"\vec{v}=(a,b) \hspace{1cm}",
                      r"a\frac{\partial f}{\partial x}+b\frac{\partial f}{\partial y}=0")
        eq2 = MathTex(r"\vec{v}=(1,0) \hspace{1cm}",
                      r"\frac{\partial f}{\partial x}=0",
                      r"\Longrightarrow f(y)")
        self.wait()
        self.play(FadeIn(eq1))
        self.wait(2)
        self.play(Transform(eq1[0],eq2[0]),Transform(eq1[1],eq2[1]))
        self.wait(2)
        self.play(FadeIn(eq2[2]))
        self.wait(2)
        self.play(FadeOut(eq1),FadeOut(eq2[2]))
        eq3 = MathTex(r"\frac{df}{dt}=\nabla{f}\cdot \vec{v}", r"=0",
                      r"\Longrightarrow f=cte").move_to(DOWN)
        texto3 = MathTex(r"Si \hspace{0.15cm} \nabla{f} \perp \vec{v}:").move_to(UP)
        self.wait()
        self.play(FadeIn(texto3))
        self.wait()
        self.play(FadeIn(eq3[0]))
        self.wait()
        self.play(FadeIn(eq3[1]))
        self.wait()
        self.play(FadeIn(eq3[2]))
        self.wait(2)
        self.play(FadeOut(texto3), FadeOut(eq3))
        eq4 = MathTex(r"\frac{\partial f}{\partial x}=0",
                      r"\Leftrightarrow Curvas\hspace{0.15cm} de\hspace{0.15cm} nivel:\hspace{0.15cm} y = cte,"
                      r"\hspace{0.15cm} \forall x",
                      r"\Leftrightarrow f(y)")
        self.wait()
        self.play(FadeIn(eq4[0]))
        self.wait()
        self.play(FadeIn(eq4[1]))
        self.wait()
        self.play(FadeIn(eq4[2]))
        self.wait(2)
        self.play(FadeOut(eq4))
        self.wait(2)

        # Segundo ejemplo
        eq1 = MathTex(r"\vec{v}=(a,b) \hspace{1cm}",
                      r"a",
                      r"\frac{\partial f}{\partial x}",
                      r"+b",
                      r"\frac{\partial f}{\partial y}=0")
        eq2 = MathTex(r"\vec{v}=(1,2) \hspace{1cm}",
                      r"\hspace{0.25cm}",
                      r"\frac{\partial f}{\partial x}",
                      r"+2",
                      r"\frac{\partial f}{\partial y}=0")

        self.play(FadeIn(eq1))
        self.wait(2)
        self.play(Transform(eq1[0], eq2[0]), Transform(eq1[1], eq2[1]),
                  Transform(eq1[2], eq2[2]), Transform(eq1[3], eq2[3]),
                  Transform(eq1[4], eq2[4]))
        self.wait(2)
        self.play(FadeOut(eq1))
        self.wait(2)
        eq3 = MathTex(r"\vec{v}=(", r"1", r",", r"2", r")").move_to(LEFT * 3)
        eq4 = MathTex(r"\vec{v}=(", r"a", r",", r"b", r")").move_to(LEFT*3)
        eq5 = MathTex(r"\vec{v}=(", r"a", r",", r"b", r")").move_to(LEFT*3)
        eq5[1].set_color(YELLOW)
        eq5[3].set_color(YELLOW)
        eq6 = MathTex(r"y=", r"\frac{\Delta y}{\Delta x}", r"x+C").move_to(RIGHT*3)
        eq7 = MathTex(r"y=", r"\frac{b}{a}", r"x+C").move_to(RIGHT*3)
        eq7[1].set_color(YELLOW)
        self.play(FadeIn(eq6))
        self.wait()
        self.play(FadeIn(eq3))
        self.wait()
        self.play(Transform(eq3,eq4))
        self.wait()
        self.play(Transform(eq3, eq5))
        self.wait()
        self.play(Transform(eq6,eq7))
        self.wait()
        self.play(FadeOut(eq3), FadeOut(eq6))
        eq8 = MathTex(r"y=\frac{b}{a}x+C")
        eq9 = MathTex(r"ay=bx+aC")
        eq10 = MathTex(r"ay", r"-bx", r"=aC")
        eq11 = MathTex(r"ay", r"-bx", r"=cte")
        eq11p2 = MathTex(r"ay", r"-bx", r"=cte").move_to(UP)
        eq11p3 = MathTex(r"y", r"-2x", r"=cte").move_to(UP)
        self.wait()
        self.play(FadeIn(eq8))
        self.wait()
        self.play(Transform(eq8, eq9))
        self.wait()
        self.play(Transform(eq8, eq10))
        self.wait()
        self.play(Transform(eq8, eq11))
        self.wait()
        self.play(Transform(eq8,eq11p2))
        self.wait()
        eq12 = MathTex(r"f(x,y)", r"=", r"F(", r"ay-", r"b", r"x)").move_to(DOWN)
        eq13 = MathTex(r"f(x,y)", r"=", r"F(", r"y-", r"2", r"x)").move_to(DOWN)
        self.play(FadeIn(eq12[0]))
        self.wait()
        self.play(FadeIn(eq12[1]), FadeIn(eq12[2]), FadeIn(eq12[3]), FadeIn(eq12[4]), FadeIn(eq12[5]))
        self.wait(2)
        self.play(Transform(eq12, eq13), Transform(eq8, eq11p3))
        self.wait(2)
        self.play(FadeOut(eq12),FadeOut(eq8))
        self.wait()

        # Construcción de la transformación
        eq13 = MathTex(r"T: (x,y)\longrightarrow (u,v)").move_to(UP)
        eq14 = MathTex(r"\hat{u} \thinspace \| \thinspace \vec{v}",
                       r"\Longrightarrow \hat{u}=\frac{\vec{v}}{|\vec{v}|}",
                       r"\Longrightarrow \hat{u}=",
                       r"\frac{1}{\sqrt{a ^2+b ^2}}(a,b)").move_to(DOWN)
        eq14p2 = MathTex(r"\hat{u} \thinspace \| \thinspace \vec{v}",
                       r"\Longrightarrow \hat{u}=\frac{\vec{v}}{|\vec{v}|}",
                       r"\Longrightarrow \hat{u}=",
                       r"\frac{1}{|\vec{v}|}(a,b)").move_to(DOWN)
        eq14p3 = MathTex(r"\hat{u}=\frac{1}{|\vec{v}|}(a,b)").move_to(DOWN)
        self.play(FadeIn(eq13))
        self.wait()
        self.play(FadeIn(eq14[0]))
        self.wait()
        self.play(FadeIn(eq14[1]))
        self.wait()
        self.play(FadeIn(eq14[2]), FadeIn(eq14[3]))
        self.wait(2)
        self.play(Transform(eq14[3], eq14p2[3]))
        self.play(Transform(eq14, eq14p2))
        self.wait(2)
        self.play(Transform(eq14, eq14p3), FadeOut(eq13))
        self.wait()
        eq15 = MathTex(r"\hat{u}=\frac{1}{|\vec{v}|}(a,b)").move_to(UP*2+LEFT*3)
        eq16 = MathTex(r"\hat{v}=\frac{1}{|\vec{v}|}(-b,a)").move_to(UP*2+RIGHT*3)
        self.play(Transform(eq14, eq15))
        self.wait()
        self.play(FadeIn(eq16))
        self.wait(2)
        eq17 = MathTex(r"(\hat{u}, \hat{v}) = (\hat{x}, \hat{y}) \cdot", r"\thinspace", r"\begin{pmatrix}"
                       r"a_{11} & a_{12}\\ a_{21} & a_{22} \end{pmatrix}").move_to(DOWN)
        eq18 = MathTex(r"(\hat{u}, \hat{v}) = (\hat{x}, \hat{y})", r"\thinspace", r" \cdot \begin{pmatrix}"
                       r"\frac{a}{|\vec{v}|} & "
                       r"a_{12}\\ "
                       r"\frac{b}{|\vec{v}|} &"
                       r" a_{22} \end{pmatrix}").move_to(DOWN)
        eq19 = MathTex(r"(\hat{u}, \hat{v}) = (\hat{x}, \hat{y})", r"\thinspace", r" \cdot \begin{pmatrix}"
                       r"\frac{a}{|\vec{v}|} & "
                       r"\frac{-b}{|\vec{v}|}\\ "
                       r"\frac{b}{|\vec{v}|} &"
                       r" \frac{a}{|\vec{v}|} \end{pmatrix}").move_to(DOWN)
        eq20 = MathTex(r"(\hat{u}, \hat{v}) = (\hat{x}, \hat{y}) \cdot", r"\frac{1}{|\vec{v}|}",
                       r"\begin{pmatrix} a & -b\\ b &  a \end{pmatrix}").move_to(DOWN)
        self.play(FadeIn(eq17))
        self.wait(2)
        self.play(Transform(eq17, eq18))
        self.wait(2)
        self.play(Transform(eq17, eq19))
        self.wait(2)
        brace = Brace(mobject=eq17[2], direction=DOWN, buff=0.2)
        eq21 = MathTex(r"J^{-1}").move_to(DOWN * 2.5 + RIGHT*1.75)
        self.play(GrowFromCenter(brace), FadeIn(eq21))
        self.wait(3)
        self.play(FadeOut(brace), FadeOut(eq21))
        self.play(Transform(eq17, eq20))
        self.wait(2)
        self.play(FadeOut(eq14), FadeOut(eq16), FadeOut(eq17))
        self.wait()
        eq22 = MathTex(r"(\hat{u}, \hat{v}) = (\hat{x}, \hat{y}) J^{-1}",
                       r"\Longrightarrow \begin{pmatrix} u\\ v \end{pmatrix} = "
                       r"J \begin{pmatrix} x\\ y \end{pmatrix}").move_to(UP)
        self.play(FadeIn(eq22[0]))
        self.wait()
        self.play(FadeIn(eq22[1]))
        self.wait()
        eq23 = MathTex(r"\begin{pmatrix} u\\ v \end{pmatrix}",
                       r"= \frac{1}{|\vec{v}|} \begin{pmatrix} a & b\\ -b & a \end{pmatrix} "
                       r"\cdot \begin{pmatrix} x\\ y \end{pmatrix}",
                       r"= \frac{1}{|\vec{v}|} \begin{pmatrix} ax+by\\ -bx+ay \end{pmatrix}"
                       ).move_to(DOWN)
        eq24 = MathTex(r"\begin{pmatrix} u\\ v \end{pmatrix}",
                       r"= \frac{1}{|\vec{v}|} \begin{pmatrix} a & b\\ -b & a \end{pmatrix} "
                       r"\cdot \begin{pmatrix} a\\ b \end{pmatrix}",
                       r"= \frac{1}{|\vec{v}|} \begin{pmatrix} a^2+b^2\\ -ba+ab \end{pmatrix}"
                       ).move_to(DOWN)
        eq24p2 = MathTex(r"\begin{pmatrix} u\\ v \end{pmatrix}",
                       r"= \frac{1}{|\vec{v}|} \begin{pmatrix} a & b\\ -b & a \end{pmatrix} "
                       r"\cdot \begin{pmatrix} a\\ b \end{pmatrix}",
                       r"= \frac{1}{|\vec{v}|} \begin{pmatrix} |\vec{v}|^2\\ 0 \end{pmatrix}"
                       ).move_to(DOWN)
        eq25 = MathTex(r"\begin{pmatrix} u\\ v \end{pmatrix}",
                       r"= \frac{1}{|\vec{v}|} \begin{pmatrix} a & b\\ -b & a \end{pmatrix} "
                       r"\cdot \begin{pmatrix} a\\ b \end{pmatrix}",
                       r"= \begin{pmatrix} |\vec{v}|\\ 0 \end{pmatrix}").move_to(DOWN)
        self.play(FadeIn(eq23[0]))
        self.wait(2)
        self.play(FadeIn(eq23[1]))
        self.wait(2)
        self.play(FadeIn(eq23[2]))
        self.wait(2)
        self.play(Transform(eq23[1], eq24[1]))
        self.wait(2)
        self.play(Transform(eq23[2], eq24[2]))
        self.wait(2)
        self.play(Transform(eq23[2], eq24p2[2]))
        self.wait(2)
        self.play(Transform(eq23[2], eq25[2]))
        self.wait()
        self.play(Transform(eq23, eq25))
        self.wait(2)
        self.play(FadeOut(eq22), FadeOut(eq23))
        self.wait()

        eq26 = MathTex(r"\begin{pmatrix} u\\ v \end{pmatrix}",
                       r"= \frac{1}{|\vec{v}|} \begin{pmatrix} a & b\\ -b & a \end{pmatrix} "
                       r"\cdot \begin{pmatrix} x\\ y \end{pmatrix}",
                       r"= \frac{1}{|\vec{v}|} \begin{pmatrix} ax+by\\ -bx+ay \end{pmatrix}"
                       ).move_to(UP)
        self.play(FadeIn(eq26[0]))
        self.wait()
        self.play(FadeIn(eq26[1]))
        self.wait()
        self.play(FadeIn(eq26[2]))
        self.wait()
        eq27 = MathTex(r"(u,v)",
                       r"=T(x,y)",
                       r"=\frac{1}{|\vec{v}|}(ax+by,-bx+ay)").move_to(DOWN)
        self.play(FadeIn(eq27[0]))
        self.wait()
        self.play(FadeIn(eq27[1]))
        self.wait()
        self.play(FadeIn(eq27[2]))
        self.wait()
        self.play(FadeOut(eq26))
        eq28 = MathTex(r"(u,v)",
                       r"=T(x,y)",
                       r"=\frac{1}{|\vec{v}|}(ax+by,-bx+ay)").move_to(UP)
        self.play(Transform(eq27, eq28))
        self.wait()
        eq29 = MathTex(r"f(x,y)=g\circ T(x,y)").move_to(DOWN+LEFT*3)
        self.play(FadeIn(eq29))
        self.wait()
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage[all]{xy}")
        eq30 = Tex(r"$\xymatrix{(x,y) \ar[rr]^f & \hspace{0.8cm} & \mathbb{R}}$", tex_template=myTemplate
                   ).move_to(DOWN*0.5+RIGHT*3)
        eq31 = Tex(r"$\xymatrix{(x,y) \ar[r]^T & (u,v) \ar[r]^{\hspace{0.25cm} g} & \mathbb{R}}$",
                   tex_template=myTemplate).move_to(DOWN * 1.5 + RIGHT * 3)
        self.play(FadeIn(eq30))
        self.wait()
        self.play(FadeIn(eq31))
        self.wait(2)
        self.play(FadeOut(eq27), FadeOut(eq30), FadeOut(eq31))
        eq32 = MathTex(r"f(x,y)=g\circ T(x,y)").move_to(UP*2+LEFT*4)
        self.play(Transform(eq29, eq32))
        self.wait()
        eq33 = MathTex(r"(u,v)=T(x,y)",
                       r"\Longrightarrow u(x,y) \hspace{0.25cm} v(x,y)").move_to(UP*2+RIGHT*3)
        eq34 = MathTex(r"\frac{\partial{f}}{\partial{x}}",
                       r"=\frac{\partial{g}}{\partial{u}}\frac{\partial{u}}{\partial{x}}+"
                       r"\frac{\partial{g}}{\partial{v}}\frac{\partial{v}}{\partial{x}}",
                       r"=\frac{\partial{g}}{\partial{u}}\frac{a}{|\vec{v}|}-"
                       r"\frac{\partial{g}}{\partial{v}}\frac{b}{|\vec{v}|}")
        eq35 = MathTex(r"\frac{\partial{f}}{\partial{y}}",
                       r"=\frac{\partial{g}}{\partial{u}}\frac{\partial{u}}{\partial{y}}+"
                       r"\frac{\partial{g}}{\partial{v}}\frac{\partial{v}}{\partial{y}}",
                       r"=\frac{\partial{g}}{\partial{u}}\frac{b}{|\vec{v}|}+"
                       r"\frac{\partial{g}}{\partial{v}}\frac{a}{|\vec{v}|}").move_to(DOWN*2)
        self.play(FadeIn(eq34[0]))
        self.wait()
        self.play(FadeIn(eq33[0]))
        self.wait()
        self.play(FadeIn(eq33[1]))
        self.wait()
        self.play(Write(eq34[1]))
        self.wait()
        self.play(FadeIn(eq35[0]))
        self.wait()
        self.play(Write(eq35[1]))
        self.wait()
        eq36 = MathTex(r"(u,v)=\frac{1}{|\vec{v}|}(ax+by,-bx+ay)").move_to(UP*2+RIGHT*3)
        self.play(FadeOut(eq33))
        self.play(FadeIn(eq36))
        self.wait(2)
        self.play(Write(eq34[2]))
        self.wait()
        self.play(Write(eq35[2]))
        self.wait(2)
        self.play(FadeOut(eq29), FadeOut(eq36), FadeOut(eq34[2]), FadeOut(eq35[2]))
        eq36 = MathTex(r"\frac{\partial{f}}{\partial{x}}",
                       r"=\frac{\partial{g}}{\partial{u}}\frac{\partial{u}}{\partial{x}}+"
                       r"\frac{\partial{g}}{\partial{v}}\frac{\partial{v}}{\partial{x}}"
                       ).move_to(UP+LEFT*3)
        eq37 = MathTex(r"\frac{\partial{f}}{\partial{y}}",
                       r"=\frac{\partial{g}}{\partial{u}}\frac{\partial{u}}{\partial{y}}+"
                       r"\frac{\partial{g}}{\partial{v}}\frac{\partial{v}}{\partial{y}}"
                       ).move_to(UP + RIGHT * 3)
        self.play(Transform(eq34[0], eq36[0]), Transform(eq35[0], eq37[0]),
                  Transform(eq34[1], eq36[1]), Transform(eq35[1], eq37[1]))
        self.wait(2)
        eq38 = MathTex(r"\Bigl(\frac{\partial{f}}{\partial{x}},\frac{\partial{f}}{\partial{y}}\Bigr)",
                       r"=\Bigl(\frac{\partial{g}}{\partial{u}},\frac{\partial{g}}{\partial{v}}\Bigr)",
                       r"\cdot \begin{pmatrix} \frac{\partial{u}}{\partial{x}} &"
                       r"\frac{\partial{u}}{\partial{y}}\\"
                       r" \frac{\partial{v}}{\partial{x}} &"
                       r"\frac{\partial{v}}{\partial{y}} \end{pmatrix}").move_to(DOWN)
        self.play(FadeIn(eq38[0]))
        self.wait(2)
        self.play(FadeIn(eq38[1]))
        self.wait(2)
        self.play(FadeIn(eq38[2]))
        self.wait(2)
        eq39 = MathTex(r"\Bigl(\frac{\partial{f}}{\partial{x}},\frac{\partial{f}}{\partial{y}}\Bigr)",
                       r"=\Bigl(\frac{\partial{g}}{\partial{u}},\frac{\partial{g}}{\partial{v}}\Bigr)",
                       r"\cdot \frac{1}{|\vec{v}|} \begin{pmatrix} a &"
                       r"b \\ -b & a \end{pmatrix}").move_to(DOWN)
        self.play(Transform(eq38[2], eq39[2]))
        self.wait()
        self.play(Transform(eq38, eq39))
        self.wait()
        brace = Brace(mobject=eq39[2], direction=DOWN, buff=0.2)
        eq40 = MathTex(r"J").move_to(DOWN*2.5+RIGHT*2.55)
        self.play(GrowFromCenter(brace), FadeIn(eq40))
        self.wait()
        self.play(FadeOut(eq38), FadeOut(eq34[0]), FadeOut(eq35[0]),
                  FadeOut(eq34[1]), FadeOut(eq35[1]), FadeOut(brace), FadeOut(eq40))

        # Sustitución
        eq41 = MathTex(r"a",
                       r"\frac{\partial{f}}{\partial{x}}",
                       r"+",
                       r"b",
                       r"\frac{\partial{f}}{\partial{y}}",
                       r"=0").move_to(DOWN)
        eq41p2 = MathTex(r"\frac{\partial{f}}{\partial{x}}=\frac{a}{|\vec{v}|}"
                         r"\frac{\partial{g}}{\partial{u}}-\frac{b}{|\vec{v}|}\frac{\partial{g}}{\partial{v}}",
                         r"\hspace{1cm}",
                         r"\frac{\partial{f}}{\partial{y}}=\frac{b}{|\vec{v}|}"
                         r"\frac{\partial{g}}{\partial{u}}+\frac{a}{|\vec{v}|}\frac{\partial{g}}{\partial{v}}"
                         ).move_to(UP).scale(0.75)
        eq42 = MathTex(r"a",
                       r"\Bigl(\hspace{0.9cm}\frac{\partial{f}}{\partial{x}}\hspace{0.9cm}\Bigr)",
                       r"+",
                       r"b",
                       r"\Bigl(\hspace{0.9cm}\frac{\partial{f}}{\partial{y}}\hspace{0.9cm}\Bigr)",
                       r"=0").move_to(DOWN)
        self.play(FadeIn(eq41))
        self.wait()
        self.play(Transform(eq41, eq42))
        self.wait()
        eq43 = MathTex(r"a",
                       r"\Bigl(\frac{a}{|\vec{v}|}\frac{\partial{g}}{\partial{u}}-"
                       r"\frac{b}{|\vec{v}|}\frac{\partial{g}}{\partial{v}}\Bigr)",
                       r"+",
                       r"b",
                       r"\Bigl(\frac{b}{|\vec{v}|}\frac{\partial{g}}{\partial{u}}+"
                       r"\frac{a}{|\vec{v}|}\frac{\partial{g}}{\partial{v}}\Bigr)",
                       r"=0").move_to(DOWN)
        self.play(FadeIn(eq41p2[0]))
        self.wait()
        self.play(Transform(eq41[1], eq43[1]))
        self.wait()
        self.play(FadeIn(eq41p2[1]), FadeIn(eq41p2[2]))
        self.wait()
        self.play(Transform(eq41[4], eq43[4]))
        self.play(Transform(eq41, eq43))
        self.wait()
        self.play(FadeOut(eq41p2))
        self.wait()
        eq44 = MathTex(r"a",
                       r"\Bigl(\frac{a}{|\vec{v}|}\frac{\partial{g}}{\partial{u}}-"
                       r"\frac{b}{|\vec{v}|}\frac{\partial{g}}{\partial{v}}\Bigr)",
                       r"+",
                       r"b",
                       r"\Bigl(\frac{b}{|\vec{v}|}\frac{\partial{g}}{\partial{u}}+"
                       r"\frac{a}{|\vec{v}|}\frac{\partial{g}}{\partial{v}}\Bigr)",
                       r"=0")
        eq45 = MathTex(r"\frac{a^2}{|\vec{v}|}\frac{\partial{g}}{\partial{u}}-",
                       r"\frac{ab}{|\vec{v}|}\frac{\partial{g}}{\partial{v}}",
                       r"+",
                       r"\frac{b^2}{|\vec{v}|}\frac{\partial{g}}{\partial{u}}+",
                       r"\frac{ab}{|\vec{v}|}\frac{\partial{g}}{\partial{v}}",
                       r"=0")
        self.play(Transform(eq41, eq44))
        self.wait()
        self.play(Transform(eq41, eq45))
        self.wait()
        eq45[1].set_color(YELLOW)
        eq45[4].set_color(YELLOW)
        self.play(FadeIn(eq45))
        self.wait()
        eq46 = MathTex(r"\frac{a^2}{|\vec{v}|}\frac{\partial{g}}{\partial{u}}",
                       r"\hspace{1cm}",
                       r"+",
                       r"\frac{b^2}{|\vec{v}|}\frac{\partial{g}}{\partial{u}}",
                       r"\hspace{1cm}",
                       r"=0")
        self.play(FadeOut(eq45), Transform(eq41[1], eq46[1]), Transform(eq41[4], eq46[4]))
        self.play(Transform(eq41, eq46))
        self.wait()
        eq47 = MathTex(r"\frac{a^2}{|\vec{v}|}\frac{\partial{g}}{\partial{u}}",
                       r"",
                       r"+",
                       r"\frac{b^2}{|\vec{v}|}\frac{\partial{g}}{\partial{u}}",
                       r"",
                       r"=0")
        self.play(Transform(eq41, eq47))
        self.wait(2)
        eq48 = MathTex(r"(a^2",
                       r"+",
                       r"b^2)",
                       r"\frac{1}{|\vec{v}|}",
                       r"\frac{\partial{g}}{\partial{u}}",
                       r"=0")
        self.play(Transform(eq41, eq48))
        self.wait()
        eq49 = MathTex(r"(",
                       r"|\vec{v}|^2",
                       r")",
                       r"\frac{1}{|\vec{v}|}",
                       r"\frac{\partial{g}}{\partial{u}}",
                       r"=0")
        self.play(Transform(eq41, eq49))
        self.wait()
        eq50 = MathTex(r" ",
                       r"|\vec{v}|",
                       r" ",
                       r" ",
                       r"\frac{\partial{g}}{\partial{u}}",
                       r"=0")
        self.play(Transform(eq41, eq50))
        self.wait()
        eq51 = MathTex(r" ",
                       r" ",
                       r" ",
                       r" ",
                       r"\frac{\partial{g}}{\partial{u}}",
                       r"=0")
        self.play(Transform(eq41[1], eq51[1]))
        self.wait()
        self.play(FadeOut(eq41))

        # Solución
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{cancel}")
        eq52 = MathTex(r"\frac{\partial{g}}{\partial{u}}=0",
                       r"\Longrightarrow",
                       r"g(u,\cancel{v})", tex_template=myTemplate)
        self.play(FadeIn(eq52[0]))
        self.wait()
        self.play(FadeIn(eq52[1]), FadeIn(eq52[2]))
        self.wait()
        eq53 = MathTex(r"\frac{\partial{g}}{\partial{u}}=0",
                       r"\Longrightarrow",
                       r"g(u)")
        self.play(Transform(eq52[2], eq53[2]))
        self.play(Transform(eq52, eq53))
        self.wait()
        eq54 = MathTex(r"\frac{\partial{g}}{\partial{u}}=0",
                       r"\Longrightarrow",
                       r"g(u)").move_to(UP)
        self.play(Transform(eq52, eq54))
        eq55 = MathTex(r"f(x,y)=g\circ T(x,y)",
                       r"=g\bigl(",
                       r"v(x,y)",
                       r"\bigr)\\",
                       r"=g\Bigl(",
                       r"\frac{1}{|\vec{v}|}(ay-bx)",
                       r"\Bigr)",
                       r"=F(ay-bx)").move_to(DOWN)
        eq55[2].set_color(YELLOW)
        eq55[5].set_color(YELLOW)
        self.play(FadeIn(eq55[0]))
        self.wait()
        self.play(FadeIn(eq55[1]), FadeIn(eq55[2]), FadeIn(eq55[3]))
        self.wait()
        self.play(FadeIn(eq55[4]), FadeIn(eq55[5]), FadeIn(eq55[6]))
        self.wait()
        self.play(FadeIn(eq55[7]))
        self.wait()
        eq56 = MathTex(r"f(x,y)=",
                       r" ",
                       r" ",
                       r"\\",
                       r" ",
                       r" ",
                       r" ",
                       r"F(ay-bx)").move_to(DOWN)
        eq57 = MathTex(r"f(x,y)=F(ay-bx)").move_to(DOWN)
        self.play(Transform(eq55[1], eq56[1]), Transform(eq55[0], eq56[0]),
                  Transform(eq55[2], eq56[2]), Transform(eq55[3], eq56[3]),
                  Transform(eq55[4], eq56[4]), Transform(eq55[5], eq56[5]),
                  Transform(eq55[6], eq56[6]))
        self.wait()
        self.play(Transform(eq55, eq57))
        self.wait()

class video5(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            show_basis_vectors=False,
            include_background_plane=False,
            include_foreground_plane=True)

    def construct(self):
        rojo = "#CF010B"
        verde = "#02B126"
        self.setup()
        myVec = Vector([1,2]).set_color(rojo)
        ejex = MathTex("x").move_to(RIGHT*6.5+DOWN*0.5).scale(1.5)
        ejey = MathTex("y").move_to(LEFT*0.5+UP*3.5).scale(1.5)
        self.add(ejex, ejey)
        self.add_background_mobject(myVec)
        label1 = MathTex(r"\begin{pmatrix} 1 \\ 2 "
                         r"\end{pmatrix}").move_to(RIGHT * 1.75 + UP * 2.5)
        label1.set_color(rojo)
        self.add(label1)

        # Primera transformación
        self.wait(2)
        self.play(FadeOut(ejex), FadeOut(ejey))
        self.wait()
        self.apply_matrix([[1/np.sqrt(5), -2/np.sqrt(5)],
                           [2/np.sqrt(5), 1/np.sqrt(5)]])
        ejeu = MathTex("u").move_to(RIGHT * 2.47 + UP * 3.6).scale(1.5)
        ejew = MathTex("w").move_to(LEFT * 4.65 + UP * 3).scale(1.5)
        ejeu.rotate(TAU/5.68)
        ejew.rotate(TAU / 5.68)
        label2 = MathTex(r"\begin{pmatrix} \sqrt{5}\thinspace \\ 0\thinspace "
                          r"\end{pmatrix}").move_to(RIGHT * 1.75 + UP * 2.5)
        label2.set_color(rojo)
        self.play(FadeIn(ejeu))
        self.wait(3)
        self.play(FadeIn(ejew))
        self.wait(3)
        self.play(Transform(label1, label2))
        self.wait(3)

        recta1 = Line(start=np.array([-8, -16, 0]), end=np.array([8, 16, 0])).set_color(rojo)
        self.play(FadeIn(recta1), FadeOut(label1), FadeOut(myVec))
        self.wait(2)
        grad1 = Vector([-3, 1.5]).set_color(verde)
        grad2 = Vector([-3, 1.5]).set_color(verde).shift(np.array([2, 4, 0]))
        grad3 = Vector([-3, 1.5]).set_color(verde).shift(np.array([-2, -4, 0]))
        grad4 = Vector([-3, 1.5]).set_color(verde)
        label_grad1 = MathTex(r"\nabla{f}", color=verde).move_to(np.array([-2, 1.5, 0]))
        label_grad2 = MathTex(r"\nabla{f}", color=verde).move_to(np.array([-2 + 2, 1.5 + 4, 0]))
        label_grad3 = MathTex(r"\nabla{f}", color=verde).move_to(np.array([-2 - 2, 1.5 - 4, 0]))
        label_grad4 = MathTex(r"\nabla{f}", color=verde).move_to(np.array([-2, 1.5, 0]))
        self.add_vector(grad1)
        self.play(FadeIn(label_grad1))
        self.wait(2)
        self.play(Transform(grad1, grad2), Transform(label_grad1, label_grad2), run_time=2)
        self.play(Transform(grad1, grad3), Transform(label_grad1, label_grad3), run_time=2)
        self.play(Transform(grad1, grad4), Transform(label_grad1, label_grad4), run_time=2)
        self.wait(3)
        self.play(FadeOut(recta1), FadeOut(grad1), FadeOut(label_grad1))
        self.wait(2)

        self.add_vector(myVec)
        label_myVec = MathTex(r"\vec{v}").move_to(RIGHT + UP)
        label_myVec.set_color(rojo)
        self.play(FadeIn(label_myVec))
        self.wait(2)
        myVec2 = Vector([1 / np.sqrt(5), 2 / np.sqrt(5)]).set_color(YELLOW)
        label_myVec2 = MathTex(r"\hat{u}").move_to(LEFT * 0.15 + UP * 0.65)
        label_myVec2.set_color(YELLOW)
        self.add_vector(myVec2)
        self.play(FadeIn(label_myVec2))
        self.wait(2)
        myVec3 = Vector([-2 / np.sqrt(5), 1 / np.sqrt(5)]).set_color(BLUE)
        label_myVec3 = MathTex(r"\hat{w}").move_to(LEFT * 0.65 + DOWN * 0.15)
        label_myVec3.set_color(BLUE)
        self.add_vector(myVec3)
        self.play(FadeIn(label_myVec3))
        self.wait(2)

class video6(Scene):
    def construct(self):
        ax = Axes(x_range=[-5,5,1],
                  y_range=[-1.5,2,0.5],
                  x_length=14,
                  y_length=6)
        self.play(FadeIn(ax))
        self.wait()

        # Puntos destacados
        p1 = MathTex("1").move_to(ax.coords_to_point(-0.5, 1.1)).scale(0.5)
        p2 = MathTex("0.5").move_to(ax.coords_to_point(-0.5, 0.5)).scale(0.5)
        p3 = MathTex("-0.5").move_to(ax.coords_to_point(-0.5, -0.5)).scale(0.5)
        p4 = MathTex("-1").move_to(ax.coords_to_point(-0.5, -1)).scale(0.5)

        # Representación
        curva0 = ax.plot(lambda x: 1/(1+x**2), color = GREEN, x_range = [-10, 10])
        eq0 = MathTex(r"y=",
                      r"\frac{1}{1+x^2}").move_to(UP*2+RIGHT*3)
        ejex = MathTex("x").move_to(ax.coords_to_point(4.5, -0.25, 0))
        ejey = MathTex("y").move_to(ax.coords_to_point(-0.25, 1.5, 0))
        self.play(Write(curva0), Write(eq0), Write(p1),
                  Write(p2), Write(p3), Write(p4), Write(ejex), Write(ejey), run_time=2)
        self.wait(3)
        curva1 = ax.plot(lambda x: 1 / (1 + (x) ** 2), color=GREEN, x_range=[-10, 10]).move_to(
            ax.coords_to_point(3, 0.5)
        )
        eq1 = MathTex(r"y=",
                      r"\frac{1}{1+(x-vt)^2}").move_to(UP * 2 + RIGHT * 3)
        self.play(Transform(eq0[1], eq1[1]))
        self.play(Transform(eq0, eq1))
        self.wait(3)
        self.play(Transform(curva0, curva1), run_time=2)
        self.wait(3)
        curva2 = ax.plot(lambda x: 1 / (1 + (x) ** 2), color=GREEN, x_range=[-10, 10])
        eq2 = MathTex(r"y=",
                      r"\frac{1}{1+x^2}").move_to(UP * 2 + RIGHT * 3)
        self.play(Transform(eq0, eq2))
        self.wait(3)
        self.play(Transform(curva0, curva2), run_time=2)
        self.wait(3)
        curva3 = ax.plot(lambda x: 1 / (1 + (x) ** 2), color=GREEN, x_range=[-10, 10]).move_to(
            ax.coords_to_point(-3, 0.5)
        )
        eq3 = MathTex(r"y=",
                      r"\frac{1}{1+(x+vt)^2}").move_to(UP * 2 + RIGHT * 3)
        self.play(Transform(eq0, eq3))
        self.wait(3)
        self.play(Transform(curva0, curva3), run_time=2)
        self.wait(3)

class video7(Scene):
    def construct(self):
        # Ecuación de Transporte
        eq1 = MathTex(r"a",
                      r"\frac{\partial f}{\partial x}",
                      r"+b",
                      r"\frac{\partial f}{\partial y}=0").move_to(LEFT*3)
        eq2 = MathTex(r"a",
                      r"\frac{\partial f}{\partial t}",
                      r"+b",
                      r"\frac{\partial f}{\partial x}=0").move_to(LEFT*3)
        eq3 = MathTex(r"x \rightarrow t",
                      r"\hspace{0.25cm}",
                      r"y \rightarrow x").move_to(UP*2+LEFT*3)
        self.wait()
        self.play(FadeIn(eq1))
        self.wait()
        self.play(FadeIn(eq3[0]))
        self.wait()
        self.play(FadeIn(eq3[2]))
        self.wait()
        self.play(Transform(eq1, eq2))
        self.wait()
        self.play(FadeOut(eq3))
        eq4 = MathTex(r"\hspace{0.1cm}",
                      r"\frac{\partial f}{\partial t}",
                      r"+v",
                      r"\frac{\partial f}{\partial x}=0").move_to(LEFT*3)
        self.play(Transform(eq1, eq4))
        self.wait()
        eq5 = MathTex(r"\Longrightarrow \hspace{0.5cm}",
                        r"f(t,x)=",
                        r"F(ax-bt)").move_to(RIGHT * 2.75)
        eq5p2 = MathTex(r"\Longrightarrow \hspace{0.5cm}",
                      r"f(t,x)=",
                      r"F(x-vt)").move_to(RIGHT*2.75)
        self.play(FadeIn(eq5))
        self.wait(2)
        self.play(Transform(eq5[2], eq5p2[2]))
        self.play(Transform(eq5, eq5p2))
        self.wait(3)
        self.play(FadeOut(eq1), FadeOut(eq5))
        self.wait(2)

        # Familia infinita de soluciones
        eq6 = MathTex(r"\frac{df}{dx}=f(x)",
                      r"\Longrightarrow f(x)=",
                      r"C",
                      r"e^x").move_to(UP)
        eq6[2].set_color(YELLOW)
        self.play(FadeIn(eq6[0]))
        self.wait(2)
        self.play(FadeIn(eq6[1]), FadeIn(eq6[2]), FadeIn(eq6[3]))
        self.wait(3)
        eq7 = MathTex(r"\frac{d^2f}{dx^2}=-f(x)",
                      r"\Longrightarrow f(x)=",
                      r"A",
                      r"\cos(x)",
                      r"+",
                      r"B",
                      r"\sin(x)").move_to(DOWN)
        eq7[2].set_color(YELLOW)
        eq7[5].set_color(YELLOW)
        self.play(FadeIn(eq7[0]))
        self.wait(3)
        self.play(FadeIn(eq7[1]), FadeIn(eq7[2]), FadeIn(eq7[3]))
        self.wait(2)
        self.play(FadeIn(eq7[4]), FadeIn(eq7[5]), FadeIn(eq7[6]))
        self.wait(3)
        self.play(FadeOut(eq6), FadeOut(eq7))
        self.wait(2)

        # Problema de Cauchy
        eq8 = MathTex(r"\frac{\partial f}{\partial t}+v\frac{\partial f}{\partial x}=0",
                      r"\Longrightarrow f(x,y)=",
                      r"F(x-vt)").move_to(UP)
        eq8[2].set_color(YELLOW)
        eq9 = MathTex(r"f(x,",
                      r"t=0",
                      r")=\frac{1}{1+x^2}").move_to(DOWN)
        eq9[1].set_color(BLUE)
        self.play(FadeIn(eq8[0]))
        self.wait(2)
        self.play(FadeIn(eq8[1]), FadeIn(eq8[2]))
        self.wait(3)
        self.play(FadeIn(eq9))
        self.wait(3)
        self.play(FadeOut(eq8))
        eq10 = MathTex(r"f(x,",
                      r"t=0",
                      r")=\frac{1}{1+x^2}").move_to(LEFT*2)
        eq10[1].set_color(BLUE)
        self.play(Transform(eq9, eq10))
        self.wait()
        eq11 = MathTex(r"=F(x)").move_to(RIGHT*1.2)
        self.play(FadeIn(eq11))
        self.wait(2)
        eq12 = MathTex(r"f(x,",
                       r"t",
                       r")=\frac{1}{1+(x-vt)^2}").move_to(LEFT*2)
        eq13 = MathTex(r"=F(x-vt)").move_to(RIGHT*2)
        self.play(Transform(eq11, eq13))
        self.wait(2)
        self.play(Transform(eq9[2], eq12[2]))
        self.play(Transform(eq9, eq12))
        self.wait(3)
        eq14 = MathTex(r"f(x,",
                       r"t",
                       r")=\frac{1}{1+(x-vt)^2}").move_to(LEFT * 2 + UP)
        eq15 = MathTex(r"=F(x-vt)").move_to(RIGHT * 2 + UP )
        self.play(Transform(eq9, eq14), Transform(eq11, eq15))
        self.wait()
        eq16 = MathTex(r"\frac{\partial f}{\partial t}",
                       r"+",
                       r"v\frac{\partial f}{\partial x}=0").move_to(LEFT * 2 + DOWN)
        self.play(FadeIn(eq16))
        self.wait(2)
        eq17 = MathTex(r"\frac{\partial f}{\partial t}",
                       r"-",
                       r"v\frac{\partial f}{\partial x}=0").move_to(LEFT * 2 + DOWN)
        self.play(Transform(eq16, eq17))
        self.wait(2)
        eq18 = MathTex(r"f(x,",
                       r"t",
                       r")=\frac{1}{1+(x+vt)^2}").move_to(LEFT * 2 + UP)
        eq19 = MathTex(r"=F(x+vt)").move_to(RIGHT * 2 + UP)
        self.play(Transform(eq9, eq18), Transform(eq11, eq19))
        self.wait(3)
        self.play(FadeOut(eq9), FadeOut(eq11), FadeOut(eq16))

        # Ecuación de ondas
        eq20 = MathTex(r"\frac{\partial f}{\partial t}+v\frac{\partial f}{\partial x}=0",
                       r"\Longrightarrow f(t,x)=F(x-vt)").move_to(UP*2)
        eq21 = MathTex(r"\frac{\partial f}{\partial t}-v\frac{\partial f}{\partial x}=0",
                       r"\Longrightarrow f(t,x)=F(x+vt)")
        self.play(FadeIn(eq20[0]))
        self.wait()
        self.play(FadeIn(eq20[1]))
        self.wait()
        self.play(FadeIn(eq21[0]))
        self.wait()
        self.play(FadeIn(eq21[1]))
        self.wait()
        eq22 = MathTex(r"\Bigl(\frac{\partial}{\partial t}+v\frac{\partial }{\partial x}\Bigr)f(x,t)=0",
                       r"\Longrightarrow f(t,x)=F(x-vt)").move_to(UP * 2)
        eq23 = MathTex(r"\Bigl(\frac{\partial}{\partial t}-v\frac{\partial }{\partial x}\Bigr)f(x,t)=0",
                       r"\Longrightarrow f(t,x)=F(x+vt)")
        self.play(Transform(eq20[0], eq22[0]))
        self.wait()
        self.play(Transform(eq20, eq22))
        self.wait()
        self.play(Transform(eq21[0], eq23[0]))
        self.wait()
        self.play(Transform(eq21, eq23))
        self.wait()
        brace1 = Brace(mobject=eq22[0], direction=UP, buff=0.2)
        eq24 = MathTex(r"\hat{L}_{\rightarrow}f(t,x)=0").move_to(UP * 3.25 + LEFT * 2.55).scale(0.75)
        self.play(GrowFromCenter(brace1), FadeIn(eq24))
        self.wait(2)
        brace2 = Brace(mobject=eq23[0], direction=DOWN, buff=0.2)
        eq25 = MathTex(r"\hat{L}_{\leftarrow}f(t,x)=0").move_to(DOWN * 1.3 + LEFT * 2.55).scale(0.75)
        self.play(GrowFromCenter(brace2), FadeIn(eq25))
        self.wait(3)
        eq26 = MathTex(r"\hat{L}_{\rightarrow}",
                       r"\hat{L}_{\leftarrow}",
                       r"f(t,x)",
                       r"=\frac{\partial^2 f}{\partial x^2}-v^2\frac{\partial^2 f}{\partial t^2}=0"
                       ).move_to(DOWN * 2.5)
        eq27 = MathTex(r"\hat{L}_{\leftarrow}",
                       r"\hat{L}_{\rightarrow}",
                       r"f(t,x)",
                       r"=\frac{\partial^2 f}{\partial x^2}-v^2\frac{\partial^2 f}{\partial t^2}=0"
                       ).move_to(DOWN * 2.5)
        eq28 = MathTex(r"\frac{\partial^2 f}{\partial x\partial t}=\frac{\partial^2 f}{\partial t\partial x}"
                       ).move_to(DOWN * 2.5 + RIGHT * 2)
        eq28.set_color(YELLOW)
        self.play(FadeIn(eq26[0]), FadeIn(eq26[1]), FadeIn(eq26[2]))
        self.wait(2)
        self.play(FadeIn(eq28))
        self.wait()
        self.play(Transform(eq26[0], eq27[0]), Transform(eq26[1], eq27[1]))
        self.wait(2)
        self.play(FadeOut(eq28))
        self.play(FadeIn(eq26[3]))
        self.wait(3)

class video8(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            show_basis_vectors=False,
            include_background_plane=False,
            include_foreground_plane=True,
            foreground_plane_kwargs = {
                "x_range": np.array([-20, 20, 1]),
                "y_range": np.array([-20, 20, 1])
            })
    def construct(self):
        rojo = "#CF010B"
        verde = "#02B126"
        self.setup()
        myVec = Vector([1, 2]).set_color(rojo)
        ejex = MathTex("x").move_to(RIGHT * 6.5 + DOWN * 0.5).scale(1.5)
        ejey = MathTex("y").move_to(LEFT * 0.5 + UP * 3.5).scale(1.5)
        self.add(ejex, ejey)
        self.add_background_mobject(myVec)
        label1 = MathTex(r"\begin{pmatrix} 1 \\ 2 "
                         r"\end{pmatrix}").move_to(RIGHT * 1.75 + UP * 2.5)
        label1.set_color(rojo)
        self.add(label1)

        # Segunda transformación
        self.setup()
        self.add(ejex, ejey)
        self.add_background_mobject(myVec)
        self.add(label1)
        self.wait(2)
        self.play(FadeOut(ejex), FadeOut(ejey))
        self.wait()
        self.apply_matrix([[1, 0],
                           [2, 1]])
        ejeu = MathTex("u").move_to(RIGHT * 2.47 + UP * 3.6).scale(1.5)
        ejew = MathTex("w").move_to(LEFT * 0.5 + UP * 3.5).scale(1.5)
        ejeu.rotate(TAU / 5.68)
        label2 = MathTex(r"\begin{pmatrix} 1 \\ 0 "
                         r"\end{pmatrix}").move_to(RIGHT * 1.75 + UP * 2.5)
        label2.set_color(rojo)
        self.play(Transform(label1, label2), FadeIn(ejeu), FadeIn(ejew))
        self.wait(3)

class Introduccion(Scene):
    def construct(self):
        self.wait(2)
        mw = ImageMobject("5MW.png").scale(0.25).move_to(np.array([0,1,0]))
        label = Text("Migstemáticas").move_to(np.array([0,-2,0]))
        self.play(FadeIn(mw), Write(label))
        self.wait(3)
        self.play(FadeOut(mw), FadeOut(label))
        self.wait(2)

class CurvasNivel(VectorScene):
    def construct(self):
        self.wait(2)
        gris = "#C7C7C7"
        azul1 = "#90CAF9"
        azul2 = "#42A5F5"
        azul3 = "#1E88E5"
        azul4 = "#1565C0"
        verde = "#02B126"
        rojo = "#CF010B"
        plane = NumberPlane(
            background_line_style={
                "stroke_color": gris,
                "stroke_opacity": 0.3,
                "stroke_width": 2
            },
            axis_config={
                "stroke_width": 4,
                "label_direction": DR,
                "include_ticks": True,
                "include_numbers": False
            }
        )
        self.play(FadeIn(plane))
        self.wait(2)
        c1 = Circle(radius=1, color=azul1)
        label1 = MathTex("f = 1").move_to(np.array([0.4, 0.5, 0])).set_color(azul1).scale(0.5)
        self.play(FadeIn(c1), FadeIn(label1))
        self.wait()
        c2 = Circle(radius=2, color=azul2)
        label2 = MathTex("f = 2").move_to(np.array([1.1, 1.2, 0])).set_color(azul2).scale(0.5)
        self.play(FadeIn(c2), FadeIn(label2))
        self.wait()
        c3 = Circle(radius=3, color=azul3)
        label3 = MathTex("f = 3").move_to(np.array([1.85, 1.85, 0])).set_color(azul3).scale(0.5)
        self.play(FadeIn(c3), FadeIn(label3))
        self.wait()
        c4 = Circle(radius=4, color=azul4)
        label4 = MathTex("f = 4").move_to(np.array([2.6, 2.6, 0])).set_color(azul4).scale(0.5)
        self.play(FadeIn(c4), FadeIn(label4))
        self.wait()

        grad1 = Vector([-1/np.sqrt(2),1/np.sqrt(2)]).set_color(verde).shift(np.array([-1/np.sqrt(2), 1/np.sqrt(2), 0]))
        label_grad1 = MathTex(r"\nabla{f}").set_color(verde).move_to(np.array([-0.5, 0.5, 0])).scale(0.5)
        grad2 = Vector([-1/np.sqrt(2), -1/np.sqrt(2)]).set_color(verde).shift(np.array([-1 / np.sqrt(2), -1 / np.sqrt(2), 0]))
        grad3 = Vector([1/np.sqrt(2), -1/np.sqrt(2)]).set_color(verde).shift(np.array([1 / np.sqrt(2), -1 / np.sqrt(2), 0]))
        grad4 = Vector([1/np.sqrt(2), 1/np.sqrt(2)]).set_color(verde).shift(np.array([1 / np.sqrt(2), 1 / np.sqrt(2), 0]))
        grad5 = Vector([0, -1]).set_color(verde).shift(np.array([0, -1, 0]))
        grad6 = Vector([0, 1]).set_color(verde).shift(np.array([0, 1, 0]))
        grad7 = Vector([-1, 0]).set_color(verde).shift(np.array([-1, 0, 0]))
        grad8 = Vector([1, 0]).set_color(verde).shift(np.array([1, 0, 0]))
        self.play(FadeIn(grad1), FadeIn(label_grad1), FadeIn(grad2), FadeIn(grad3), FadeIn(grad4),
                  FadeIn(grad5), FadeIn(grad6), FadeIn(grad7), FadeIn(grad8))
        self.wait()

        grad9 = (Vector([np.cos(150*np.pi/180), np.sin(150*np.pi/180)]).set_color(verde)
                 .shift(np.array([2*np.cos(150*np.pi/180), 2*np.sin(150*np.pi/180), 0])))
        grad10 = (Vector([np.cos(240*np.pi/180), np.sin(240*np.pi/180)]).set_color(verde)
                  .shift(np.array([2*np.cos(240*np.pi/180), 2*np.sin(240*np.pi/180), 0])))
        grad11 = (Vector([np.cos(330*np.pi/180), np.sin(330*np.pi/180)]).set_color(verde)
                  .shift(np.array([2*np.cos(330*np.pi/180), 2*np.sin(330*np.pi/180), 0])))
        grad12 = (Vector([np.cos(60*np.pi/180), np.sin(60*np.pi/180)]).set_color(verde)
                  .shift(np.array([2*np.cos(60*np.pi/180), 2*np.sin(60*np.pi/180), 0])))
        grad13 = (Vector([np.cos(300*np.pi/180), np.sin(300*np.pi/180)]).set_color(verde)
                  .shift(np.array([2*np.cos(300*np.pi/180), 2*np.sin(300*np.pi/180), 0])))
        grad14 = (Vector([np.cos(120*np.pi/180), np.sin(120*np.pi/180)]).set_color(verde)
                  .shift(np.array([2*np.cos(120*np.pi/180), 2*np.sin(120*np.pi/180), 0])))
        grad15 = (Vector([np.cos(210*np.pi/180), np.sin(210*np.pi/180)]).set_color(verde)
                  .shift(np.array([2*np.cos(210*np.pi/180), 2*np.sin(210*np.pi/180), 0])))
        grad16 = (Vector([np.cos(30*np.pi/180), np.sin(30*np.pi/180)]).set_color(verde)
                  .shift(np.array([2*np.cos(30*np.pi/180), 2*np.sin(30*np.pi/180), 0])))
        self.play(FadeIn(grad9), FadeIn(grad10), FadeIn(grad11), FadeIn(grad12),
                  FadeIn(grad13), FadeIn(grad14), FadeIn(grad15), FadeIn(grad16))
        self.wait()

        grad17 = Vector([-1/np.sqrt(2), 1/np.sqrt(2)]).set_color(verde).shift(np.array([-3 / np.sqrt(2), 3 / np.sqrt(2), 0]))
        grad18 = Vector([-1/np.sqrt(2), -1/np.sqrt(2)]).set_color(verde).shift(np.array([-3 / np.sqrt(2), -3 / np.sqrt(2), 0]))
        grad19 = Vector([1/np.sqrt(2), -1/np.sqrt(2)]).set_color(verde).shift(np.array([3 / np.sqrt(2), -3 / np.sqrt(2), 0]))
        grad20 = Vector([1/np.sqrt(2), 1/np.sqrt(2)]).set_color(verde).shift(np.array([3 / np.sqrt(2), 3 / np.sqrt(2), 0]))
        grad21 = Vector([0, -1]).set_color(verde).shift(np.array([0, -3, 0]))
        grad22 = Vector([0, 1]).set_color(verde).shift(np.array([0, 3, 0]))
        grad23 = Vector([-1, 0]).set_color(verde).shift(np.array([-3, 0, 0]))
        grad24 = Vector([1, 0]).set_color(verde).shift(np.array([3, 0, 0]))
        self.play(FadeIn(grad17), FadeIn(grad18), FadeIn(grad19), FadeIn(grad20),
                  FadeIn(grad21), FadeIn(grad22), FadeIn(grad23), FadeIn(grad24))
        self.wait()

        grad25 = (Vector([np.cos(150*np.pi/180), np.sin(150*np.pi/180)]).set_color(verde)
                 .shift(np.array([4 * np.cos(150*np.pi/180), 4 * np.sin(150*np.pi/180), 0])))
        grad26 = (Vector([np.cos(240*np.pi/180), np.sin(240*np.pi/180)]).set_color(verde)
                  .shift(np.array([4 * np.cos(240*np.pi/180), 4 * np.sin(240*np.pi/180), 0])))
        grad27 = (Vector([np.cos(330*np.pi/180), np.sin(330*np.pi/180)]).set_color(verde)
                  .shift(np.array([4 * np.cos(330*np.pi/180), 4 * np.sin(330*np.pi/180), 0])))
        grad28 = (Vector([np.cos(60*np.pi/180), np.sin(60*np.pi/180)]).set_color(verde)
                  .shift(np.array([4 * np.cos(60*np.pi/180), 4 * np.sin(60*np.pi/180), 0])))
        grad29 = (Vector([np.cos(300*np.pi/180), np.sin(300*np.pi/180)]).set_color(verde)
                  .shift(np.array([4 * np.cos(300*np.pi/180), 4 * np.sin(300*np.pi/180), 0])))
        grad30 = (Vector([np.cos(120*np.pi/180), np.sin(120*np.pi/180)]).set_color(verde)
                  .shift(np.array([4 * np.cos(120*np.pi/180), 4 * np.sin(120*np.pi/180), 0])))
        grad31 = (Vector([np.cos(210*np.pi/180), np.sin(210*np.pi/180)]).set_color(verde)
                  .shift(np.array([4 * np.cos(210*np.pi/180), 4 * np.sin(210*np.pi/180), 0])))
        grad32 = (Vector([np.cos(30*np.pi/180), np.sin(30*np.pi/180)]).set_color(verde)
                  .shift(np.array([4 * np.cos(30*np.pi/180), 4 * np.sin(30*np.pi/180), 0])))
        self.play(FadeIn(grad25), FadeIn(grad26), FadeIn(grad27), FadeIn(grad28),
                  FadeIn(grad29), FadeIn(grad30), FadeIn(grad31), FadeIn(grad32))
        self.wait(3)

        self.play(FadeOut(grad1), FadeOut(grad2), FadeOut(grad3), FadeOut(grad4), FadeOut(grad5),
                  FadeOut(grad6), FadeOut(grad7), FadeOut(grad8), FadeOut(grad17), FadeOut(grad18),
                  FadeOut(grad19), FadeOut(grad20), FadeOut(grad21), FadeOut(grad22), FadeOut(grad23),
                  FadeOut(grad24), FadeOut(grad25), FadeOut(grad26), FadeOut(grad27), FadeOut(grad28),
                  FadeOut(grad29), FadeOut(grad30), FadeOut(grad31), FadeOut(grad32), FadeOut(label_grad1))

        label_grad = MathTex(r"\nabla{f}").set_color(verde).move_to(np.array([-1, 1, 0]))
        label_vec = MathTex(r"\vec{v}").set_color(rojo).move_to(np.array([1.3, 0.8, 0]))
        vec9 = (Vector([-np.sin(150 * np.pi / 180), np.cos(150 * np.pi / 180)]).set_color(rojo)
                 .shift(np.array([2 * np.cos(150 * np.pi / 180), 2 * np.sin(150 * np.pi / 180), 0])))
        vec10 = (Vector([-np.sin(240 * np.pi / 180), np.cos(240 * np.pi / 180)]).set_color(rojo)
                  .shift(np.array([2 * np.cos(240 * np.pi / 180), 2 * np.sin(240 * np.pi / 180), 0])))
        vec11 = (Vector([-np.sin(330 * np.pi / 180), np.cos(330 * np.pi / 180)]).set_color(rojo)
                  .shift(np.array([2 * np.cos(330 * np.pi / 180), 2 * np.sin(330 * np.pi / 180), 0])))
        vec12 = (Vector([-np.sin(60 * np.pi / 180), np.cos(60 * np.pi / 180)]).set_color(rojo)
                  .shift(np.array([2 * np.cos(60 * np.pi / 180), 2 * np.sin(60 * np.pi / 180), 0])))
        vec13 = (Vector([-np.sin(300 * np.pi / 180), np.cos(300 * np.pi / 180)]).set_color(rojo)
                  .shift(np.array([2 * np.cos(300 * np.pi / 180), 2 * np.sin(300 * np.pi / 180), 0])))
        vec14 = (Vector([-np.sin(120 * np.pi / 180), np.cos(120 * np.pi / 180)]).set_color(rojo)
                  .shift(np.array([2 * np.cos(120 * np.pi / 180), 2 * np.sin(120 * np.pi / 180), 0])))
        vec15 = (Vector([-np.sin(210 * np.pi / 180), np.cos(210 * np.pi / 180)]).set_color(rojo)
                  .shift(np.array([2 * np.cos(210 * np.pi / 180), 2 * np.sin(210 * np.pi / 180), 0])))
        vec16 = (Vector([-np.sin(30 * np.pi / 180), np.cos(30 * np.pi / 180)]).set_color(rojo)
                  .shift(np.array([2 * np.cos(30 * np.pi / 180), 2 * np.sin(30 * np.pi / 180), 0])))

        self.play(FadeIn(label_grad))
        self.wait()
        self.play(FadeIn(label_vec))
        self.add_vector(vec16)
        self.wait()
        self.add_vector(vec12)
        self.wait()
        self.add_vector(vec14)
        self.wait()
        self.add_vector(vec9)
        self.wait()
        self.add_vector(vec15)
        self.wait()
        self.add_vector(vec10)
        self.wait()
        self.add_vector(vec13)
        self.wait()
        self.add_vector(vec11)
        self.wait(3)

class video9(VectorScene):
    def construct(self):
        gris = "#C7C7C7"
        verde = "#02B126"
        rojo = "#CF010B"
        azul = "#42A5F5"
        v = lambda x: np.array([x[1], -x[0]])
        grad = lambda x: np.array([x[0], x[1]])
        field_v = ArrowVectorField(v).set_color(rojo)
        field_grad = ArrowVectorField(grad).set_color(verde)
        plane = NumberPlane(
            background_line_style={
                "stroke_color": gris,
                "stroke_opacity": 0.3,
                "stroke_width": 2
            },
            axis_config={
                "stroke_width": 4,
                "label_direction": DR,
                "include_ticks": True,
                "include_numbers": False
            }
        )

        label_x = MathTex(r"x").move_to(RIGHT * 6.5 + DOWN * 0.5)
        label_y = MathTex(r"y").move_to(LEFT * 0.5 + UP * 3.5)
        eq1 = MathTex(r"\vec{v}=(y,-x)").move_to(RIGHT*2 + UP*2.5).set_color(rojo)
        self.wait(2)
        self.play(FadeIn(plane), FadeIn(label_x), FadeIn(label_y))
        self.wait(2)
        self.play(FadeIn(eq1))
        self.wait(3)
        self.play(FadeOut(eq1))
        self.play([GrowArrow(vec) for vec in field_v], run_time=2)
        self.wait(2)
        self.play([GrowArrow(vec) for vec in field_grad], run_time=2)
        self.wait(3)
        self.play(FadeOut(field_v), FadeOut(field_grad))
        self.wait(2)

        vec1 = (Vector([np.sin(0 * np.pi / 180), -np.cos(0 * np.pi / 180)]).set_color(rojo)
                .shift(np.array([2 * np.cos(0 * np.pi / 180), 2 * np.sin(0 * np.pi / 180), 0])))
        vec2 = (Vector([np.sin(30 * np.pi / 180), -np.cos(30 * np.pi / 180)]).set_color(rojo)
                .shift(np.array([2 * np.cos(30 * np.pi / 180), 2 * np.sin(30 * np.pi / 180), 0])))
        vec3 = (Vector([np.sin(60 * np.pi / 180), -np.cos(60 * np.pi / 180)]).set_color(rojo)
                .shift(np.array([2 * np.cos(60 * np.pi / 180), 2 * np.sin(60 * np.pi / 180), 0])))
        vec4 = (Vector([np.sin(90 * np.pi / 180), -np.cos(90 * np.pi / 180)]).set_color(rojo)
                .shift(np.array([2 * np.cos(90 * np.pi / 180), 2 * np.sin(90 * np.pi / 180), 0])))
        vec5 = (Vector([np.sin(120 * np.pi / 180), -np.cos(120 * np.pi / 180)]).set_color(rojo)
                .shift(np.array([2 * np.cos(120 * np.pi / 180), 2 * np.sin(120 * np.pi / 180), 0])))
        vec6 = (Vector([np.sin(150 * np.pi / 180), -np.cos(150 * np.pi / 180)]).set_color(rojo)
                .shift(np.array([2 * np.cos(150 * np.pi / 180), 2 * np.sin(150 * np.pi / 180), 0])))
        vec7 = (Vector([np.sin(180 * np.pi / 180), -np.cos(180 * np.pi / 180)]).set_color(rojo)
                .shift(np.array([2 * np.cos(180 * np.pi / 180), 2 * np.sin(180 * np.pi / 180), 0])))
        vec8 = (Vector([np.sin(210 * np.pi / 180), -np.cos(210 * np.pi / 180)]).set_color(rojo)
                .shift(np.array([2 * np.cos(210 * np.pi / 180), 2 * np.sin(210 * np.pi / 180), 0])))
        vec9 = (Vector([np.sin(240 * np.pi / 180), -np.cos(240 * np.pi / 180)]).set_color(rojo)
                 .shift(np.array([2 * np.cos(240 * np.pi / 180), 2 * np.sin(240 * np.pi / 180), 0])))
        vec10 = (Vector([np.sin(270 * np.pi / 180), -np.cos(270 * np.pi / 180)]).set_color(rojo)
                .shift(np.array([2 * np.cos(270 * np.pi / 180), 2 * np.sin(270 * np.pi / 180), 0])))
        vec11 = (Vector([np.sin(300 * np.pi / 180), -np.cos(300 * np.pi / 180)]).set_color(rojo)
                .shift(np.array([2 * np.cos(300 * np.pi / 180), 2 * np.sin(300 * np.pi / 180), 0])))
        vec12 = (Vector([np.sin(330 * np.pi / 180), -np.cos(330 * np.pi / 180)]).set_color(rojo)
                 .shift(np.array([2 * np.cos(330 * np.pi / 180), 2 * np.sin(330 * np.pi / 180), 0])))

        grad1 = (Vector([np.cos(0 * np.pi / 180), np.sin(0 * np.pi / 180)]).set_color(verde)
                .shift(np.array([2 * np.cos(0 * np.pi / 180), 2 * np.sin(0 * np.pi / 180), 0])))
        grad2 = (Vector([np.cos(30 * np.pi / 180), np.sin(30 * np.pi / 180)]).set_color(verde)
                .shift(np.array([2 * np.cos(30 * np.pi / 180), 2 * np.sin(30 * np.pi / 180), 0])))
        grad3 = (Vector([np.cos(60 * np.pi / 180), np.sin(60 * np.pi / 180)]).set_color(verde)
                .shift(np.array([2 * np.cos(60 * np.pi / 180), 2 * np.sin(60 * np.pi / 180), 0])))
        grad4 = (Vector([np.cos(90 * np.pi / 180), np.sin(90 * np.pi / 180)]).set_color(verde)
                .shift(np.array([2 * np.cos(90 * np.pi / 180), 2 * np.sin(90 * np.pi / 180), 0])))
        grad5 = (Vector([np.cos(120 * np.pi / 180), np.sin(120 * np.pi / 180)]).set_color(verde)
                .shift(np.array([2 * np.cos(120 * np.pi / 180), 2 * np.sin(120 * np.pi / 180), 0])))
        grad6 = (Vector([np.cos(150 * np.pi / 180), np.sin(150 * np.pi / 180)]).set_color(verde)
                .shift(np.array([2 * np.cos(150 * np.pi / 180), 2 * np.sin(150 * np.pi / 180), 0])))
        grad7 = (Vector([np.cos(180 * np.pi / 180), np.sin(180 * np.pi / 180)]).set_color(verde)
                .shift(np.array([2 * np.cos(180 * np.pi / 180), 2 * np.sin(180 * np.pi / 180), 0])))
        grad8 = (Vector([np.cos(210 * np.pi / 180), np.sin(210 * np.pi / 180)]).set_color(verde)
                .shift(np.array([2 * np.cos(210 * np.pi / 180), 2 * np.sin(210 * np.pi / 180), 0])))
        grad9 = (Vector([np.cos(240 * np.pi / 180), np.sin(240 * np.pi / 180)]).set_color(verde)
                .shift(np.array([2 * np.cos(240 * np.pi / 180), 2 * np.sin(240 * np.pi / 180), 0])))
        grad10 = (Vector([np.cos(270 * np.pi / 180), np.sin(270 * np.pi / 180)]).set_color(verde)
                 .shift(np.array([2 * np.cos(270 * np.pi / 180), 2 * np.sin(270 * np.pi / 180), 0])))
        grad11 = (Vector([np.cos(300 * np.pi / 180), np.sin(300 * np.pi / 180)]).set_color(verde)
                 .shift(np.array([2 * np.cos(300 * np.pi / 180), 2 * np.sin(300 * np.pi / 180), 0])))
        grad12 = (Vector([np.cos(330 * np.pi / 180), np.sin(330 * np.pi / 180)]).set_color(verde)
                 .shift(np.array([2 * np.cos(330 * np.pi / 180), 2 * np.sin(330 * np.pi / 180), 0])))

        eq2 = MathTex(r"x^2+y^2=r^2").move_to(RIGHT * 4 + UP * 2.5)
        c2 = Circle(radius=2, color=azul)
        self.play(FadeIn(eq2), FadeIn(c2))
        self.wait(2)

        self.add_vector(vec1)
        self.add_vector(vec12)
        self.add_vector(vec11)
        self.add_vector(vec10)
        self.add_vector(vec9)
        self.add_vector(vec8)
        self.add_vector(vec7)
        self.add_vector(vec6)
        self.add_vector(vec5)
        self.add_vector(vec4)
        self.add_vector(vec3)
        self.add_vector(vec2)

        self.add_vector(grad1)
        self.add_vector(grad12)
        self.add_vector(grad11)
        self.add_vector(grad10)
        self.add_vector(grad9)
        self.add_vector(grad8)
        self.add_vector(grad7)
        self.add_vector(grad6)
        self.add_vector(grad5)
        self.add_vector(grad4)
        self.add_vector(grad3)
        self.add_vector(grad2)

        self.wait(2)

class Conclusiones(Scene):
    def construct(self):
        eq1 = MathTex(r"f(t,x)",
                      r"=C_1\cdot F(x-vt)",
                      r"+C_2\cdot F(x+vt)")
        self.wait()
        self.play(FadeIn(eq1[0]))
        self.wait()
        self.play(FadeIn(eq1[1]))
        self.wait()
        self.play(FadeIn(eq1[2]))
        self.wait(3)
        self.play(FadeOut(eq1))
        self.wait(2)

        eq2 = MathTex(r"(2) \hspace{0.5cm}y\frac{\partial f}{\partial x}-x\frac{\partial f}{\partial y}=0"
                     ).move_to(UP)
        eq3 = MathTex(r"(3) \hspace{0.5cm}x\frac{\partial f}{\partial x}+y\frac{\partial f}{\partial y}=0"
                     ).move_to(DOWN)
        self.play(FadeIn(eq2), FadeIn(eq3))
        self.wait(3)
        self.play(FadeOut(eq2), FadeOut(eq3))
        self.wait()


class Agradecimientos(Scene):
    def construct(self):
        title = Text("Agradecimientos:").move_to(UP * 2.5)
        self.wait(1)
        self.play(FadeIn(title))
        text1 = Text("David Saavedra Pastor").move_to(UP).scale(0.75)
        text2 = Text("Ignacio Moreno Soriano").scale(0.75)
        text3 = Text("María del Mar Sánchez López").move_to(DOWN).scale(0.75)
        text4 = Text("Javier López Fernández").move_to(DOWN * 2).scale(0.75)
        self.wait(2)
        self.play(FadeIn(text1))
        self.wait()
        self.play(FadeIn(text2))
        self.wait()
        self.play(FadeIn(text3))
        self.wait()
        self.play(FadeIn(text4))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(text1), FadeOut(text2),
                  FadeOut(text3), FadeOut(text4))
        self.wait()

class video10(Scene):
    def construct(self):
        # Presentación del vídeo
        title = Text("Interpretación geométrica de una EDP").move_to(UP * 2)
        self.wait(1)
        self.play(FadeIn(title))
        eq1 = MathTex(r"(1) \hspace{0.5cm}a\frac{\partial f}{\partial x}+"
                      r"b\frac{\partial f}{\partial y}=0").move_to(DOWN)
        eq2 = MathTex(r"(2) \hspace{0.5cm}y\frac{\partial f}{\partial x}-"
                        r"x\frac{\partial f}{\partial y}=0").move_to(DOWN)
        self.wait(2)
        self.play(FadeIn(eq1))
        self.wait(3)
        self.play(FadeOut(eq1))
        self.play(FadeIn(eq2))
        self.wait(3)
        self.play(FadeOut(eq2), FadeOut(title))
        self.wait(2)

        # Migstemáticas
        mw = ImageMobject("5MW.png").scale(0.25).move_to(np.array([0, 1, 0]))
        label = Text("Migstemáticas").move_to(np.array([0, -2, 0]))
        self.play(FadeIn(mw), Write(label))
        self.wait(3)
        self.play(FadeOut(mw), FadeOut(label))
        self.wait(2)

        # EDP (2)
        eq4 = MathTex(r"y\frac{\partial f}{\partial x}-x\frac{\partial f}{\partial y}",
                      r"=",
                      r"(y,-x)",
                      r"\cdot",
                      r"\Bigl(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\Bigr)",
                      r"=\vec{v}\cdot \nabla{f}=0")
        eq5 = MathTex(r"y\frac{\partial f}{\partial x}-x\frac{\partial f}{\partial y}",
                      r"=",
                      r"(y,-x)",
                      r"\cdot",
                      r"\Bigl(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\Bigr)",
                      r"=\vec{v}\cdot \nabla{f}=0")
        eq6 = MathTex(r"y\frac{\partial f}{\partial x}-x\frac{\partial f}{\partial y}",
                      r"=",
                      r"(y,-x)",
                      r"\cdot",
                      r"\Bigl(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\Bigr)",
                      r"=\vec{v}\cdot \nabla{f}=0")
        eq6p2 = MathTex(r"y\frac{\partial f}{\partial x}-x\frac{\partial f}{\partial y}",
                      r"=",
                      r"(y,-x)",
                      r"\cdot",
                      r"\Bigl(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\Bigr)",
                      r"=\vec{v}\cdot \nabla{f}=0").move_to(UP)
        eq5[4].set_color(YELLOW)
        eq5[2].set_color(YELLOW)
        self.play(FadeIn(eq4[0]))
        self.wait(3)
        self.play(FadeIn(eq4[1]), FadeIn(eq4[2]), FadeIn(eq4[3]), FadeIn(eq4[4]))
        self.wait()
        self.play(Transform(eq4[4], eq5[4]))
        self.wait(3)
        self.play(Transform(eq4[4], eq6[4]), Transform(eq4[2], eq5[2]))
        self.wait(3)
        self.play(Transform(eq4[2], eq6[2]), FadeIn(eq4[5]))
        self.wait(2)
        self.play(Transform(eq4, eq6p2))
        self.wait()
        eq7 = MathTex(r"\vec{v}=(y,-x)").move_to(DOWN)
        self.play(FadeIn(eq7))
        self.wait(3)
        self.play(FadeOut(eq4))
        self.wait()
        eq8 = MathTex(r"\vec{v}=(y,-x)").move_to(LEFT*2)
        eq9 = MathTex(r"\Longrightarrow \hspace{0.1cm} \nabla{f}\perp \vec{v}").move_to(RIGHT)
        self.play(Transform(eq7, eq8))
        self.wait(2)
        self.play(FadeIn(eq9))
        self.wait(3)
        self.play(FadeOut(eq7), FadeOut(eq9))
        self.wait()

class video11(Scene):
    def construct(self):
        # Resolución geométrica
        eq1 = MathTex(r"x^2+y^2=r^2").move_to(UP)
        eq2 = MathTex(r"f(x,y)",
                      r"=F(",
                      r"\hspace{1.2cm}",
                      r")").move_to(DOWN)
        eq3 = MathTex(r"f(x,y)",
                      r"=F(",
                      r"x^2+y^2",
                      r")").move_to(DOWN)
        eq4 = MathTex(r"f(x,y)",
                      r"=F(",
                      r"r^2",
                      r")").move_to(DOWN)
        eq5 = MathTex(r"f(x,y)",
                      r"=F(",
                      r"r",
                      r")").move_to(DOWN)
        self.wait()
        self.play(FadeIn(eq1))
        self.wait(2)
        self.play(FadeIn(eq2[0]))
        self.wait()
        self.play(FadeIn(eq2[1]), FadeIn(eq2[2]), FadeIn(eq2[3]))
        self.wait(2)
        self.play(Transform(eq2[2], eq3[2]))
        self.wait(2)
        self.play(Transform(eq2[2], eq4[2]))
        self.play(Transform(eq2, eq4))
        self.wait(2)
        self.play(Transform(eq2[2], eq5[2]))
        self.play(Transform(eq2, eq5))
        self.wait(2)

        eq6 = MathTex(r"f(x,y)",
                      r"=F(",
                      r"r",
                      r")")
        eq6p2 = MathTex(r"g(r,\theta)",
                      r"=F(",
                      r"r",
                      r")")
        self.play(FadeOut(eq1), Transform(eq2, eq6))
        self.wait(3)
        self.play(Transform(eq2, eq6p2))
        self.wait(3)
        self.play(FadeOut(eq2))
        self.wait()

        # Cambio a coordenadas polares
        eq7 = MathTex(r"T",
                      r":",
                      r"(x,y)\longrightarrow (r,\theta)").move_to(UP*2)
        eq7p2 = MathTex(r"(r,\theta )=T(x,y)=\Bigr(\sqrt{x^2+y^2}, \arctan\frac{y}{x}\Bigl)")
        self.play(FadeIn(eq7))
        self.wait(3)
        self.play(FadeIn(eq7p2))
        self.wait(3)
        eq7p3 = MathTex(r"J=",
                      r"\begin{pmatrix} \frac{\partial r}{\partial x} \vspace{0.1cm} &"
                      r"\frac{\partial r}{\partial y} \vspace{0.1cm} \\"
                      r"\frac{\partial \theta}{\partial x} &"
                      r"\frac{\partial \theta}{\partial y} \end{pmatrix}").move_to(DOWN*2)
        self.play(FadeIn(eq7p3))
        self.wait(3)
        eq8 = MathTex(r"T^{-1}",
                      r":",
                      r"(r,\theta)\longrightarrow (x,y)").move_to(UP*2)
        eq8p2 = MathTex(r"(x,y)=T^{-1}(r,\theta)=(r\cos\theta, r\sin\theta)")
        eq8p3 = MathTex(r"J^{-1}=",
                      r"\begin{pmatrix} \frac{\partial x}{\partial r} \vspace{0.1cm} &"
                      r"\frac{\partial x}{\partial \theta} \vspace{0.1cm} \\"
                      r"\frac{\partial y}{\partial r} &"
                      r"\frac{\partial y}{\partial \theta} \end{pmatrix}").move_to(DOWN*2)
        self.play(Transform(eq7, eq8))
        self.wait(2)
        self.play(Transform(eq7p2, eq8p2))
        self.wait(2)
        self.play(Transform(eq7p3, eq8p3))
        self.wait(3)
        eq9 = MathTex(r"J^{-1}=",
                      r"\begin{pmatrix} \frac{\partial x}{\partial r} \vspace{0.1cm} &"
                      r"\frac{\partial x}{\partial \theta} \vspace{0.1cm} \\"
                      r"\frac{\partial y}{\partial r} &"
                      r"\frac{\partial y}{\partial \theta} \end{pmatrix}").move_to(DOWN+LEFT * 3.5)
        eq10 = MathTex(r"J^{-1}=",
                       r"\begin{pmatrix} \cos\theta &"
                       r" -r\sin\theta \\"
                       r" \sin\theta &"
                       r" r\cos\theta \end{pmatrix}").move_to(DOWN + LEFT * 3.5)
        eq9p2 = MathTex(r"(x,y)=T^{-1}(r,\theta)=(r\cos\theta, r\sin\theta)").move_to(UP)
        self.play(FadeOut(eq7))
        self.wait(2)
        self.play(Transform(eq7p3, eq9), Transform(eq7p2, eq9p2))
        self.wait(2)
        self.play(Transform(eq7p3, eq10))
        self.wait(3)
        eq11 = MathTex(r"\Longrightarrow\hspace{0.1cm}",
                       r"J=\frac{1}{r}\begin{pmatrix} r\cos\theta & r\sin\theta \\"
                       r" -\sin\theta & \cos\theta \end{pmatrix}").move_to(DOWN + RIGHT * 2.75)
        self.play(FadeIn(eq11))
        self.wait(3)
        self.play(FadeOut(eq7p2), FadeOut(eq7p3), FadeOut(eq11))
        self.wait(2)

        # Regla de la cadena
        eq12 = MathTex(r"f(x,y)=g\circ T(x,y) \hspace{1cm}",
                       r"g(r,\theta)").move_to(UP*2)
        self.play(FadeIn(eq12[0]))
        self.wait(2)
        self.play(FadeIn(eq12[1]))
        self.wait(2)
        eq13 = MathTex(r"\Bigl(\frac{\partial{f}}{\partial{x}},\frac{\partial{f}}{\partial{y}}\Bigr)",
                       r"=\Bigl(\frac{\partial{g}}{\partial{r}},\frac{\partial{g}}{\partial{\theta}}\Bigr)",
                       r"J",
                       r"\\ \hspace{1cm}").move_to(DOWN)
        eq14 = MathTex(r"\Bigl(\frac{\partial{f}}{\partial{x}},\frac{\partial{f}}{\partial{y}}\Bigr)",
                       r"=\Bigl(\frac{\partial{g}}{\partial{r}},\frac{\partial{g}}{\partial{\theta}}\Bigr)",
                       r"\cdot \frac{1}{r}\begin{pmatrix} r\cos\theta & r\sin\theta \\"
                       r" -\sin\theta & \cos\theta \end{pmatrix}}",
                       r"\\ \hspace{1cm}").move_to(DOWN)
        eq15 = MathTex(r"\Bigl(\frac{\partial{f}}{\partial{x}},\frac{\partial{f}}{\partial{y}}\Bigr)",
                       r"=\Bigl(\frac{\partial{g}}{\partial{r}},\frac{\partial{g}}{\partial{\theta}}\Bigr)",
                       r"\cdot \frac{1}{r}\begin{pmatrix} r\cos\theta & r\sin\theta \\"
                       r" -\sin\theta & \cos\theta \end{pmatrix}}",
                       r"\\ =\Bigl(\cos\theta\frac{\partial{g}}{\partial{r}}-\frac{1}{r}"
                       r"\sin\theta\frac{\partial{g}}{\partial{\theta}},"
                       r"\sin\theta\frac{\partial{g}}{\partial{r}}+\frac{1}{r}"
                       r"\cos\theta\frac{\partial{g}}{\partial{\theta}}\Bigr)").move_to(DOWN)
        self.play(FadeIn(eq13))
        self.wait(3)
        self.play(Transform(eq13[2], eq14[2]))
        self.wait()
        self.play(Transform(eq13, eq14))
        self.wait(3)
        self.play(Transform(eq13[3], eq15[3]))
        self.wait()
        self.play(Transform(eq13, eq15))
        self.wait(2)
        eq16 = MathTex(r"\Bigl(\frac{\partial{f}}{\partial{x}},\frac{\partial{f}}{\partial{y}}\Bigr)",
                       r" ",
                       r" ",
                       r"\\ =\Bigl(\cos\theta\frac{\partial{g}}{\partial{r}}-\frac{1}{r}"
                       r"\sin\theta\frac{\partial{g}}{\partial{\theta}},"
                       r"\sin\theta\frac{\partial{g}}{\partial{r}}+\frac{1}{r}"
                       r"\cos\theta\frac{\partial{g}}{\partial{\theta}}\Bigr)").move_to(DOWN)
        eq17 = MathTex(r"\Bigl(\frac{\partial{f}}{\partial{x}},\frac{\partial{f}}{\partial{y}}\Bigr)",
                       r" ",
                       r" ",
                       r"=\Bigl(\cos\theta\frac{\partial{g}}{\partial{r}}-\frac{1}{r}"
                       r"\sin\theta\frac{\partial{g}}{\partial{\theta}},"
                       r"\sin\theta\frac{\partial{g}}{\partial{r}}+\frac{1}{r}"
                       r"\cos\theta\frac{\partial{g}}{\partial{\theta}}\Bigr)").move_to(DOWN)
        self.play(Transform(eq13, eq16))
        self.wait()
        self.play(Transform(eq13, eq17))
        self.wait(3)
        self.play(FadeOut(eq13), FadeOut(eq12))
        self.wait(2)

        # Cambio de variable
        eq12 = MathTex(r"y",
                       r"\frac{\partial f}{\partial x}",
                       r"-",
                       r"x",
                       r"\frac{\partial f}{\partial y}",
                       r"=0").move_to(DOWN)
        self.play(FadeIn(eq12))
        self.wait(2)
        eq13 = MathTex(r"y",
                       r"\Bigl(\hspace{1.35cm} \frac{\partial f}{\partial x} \hspace{1.35cm}\Bigr)",
                       r"-",
                       r"x",
                       r"\Bigl(\hspace{1.35cm} \frac{\partial f}{\partial y} \hspace{1.35cm}\Bigr)",
                       r"=0").move_to(DOWN)
        self.play(Transform(eq12, eq13))
        self.wait(2)
        eq14 = MathTex(r"\frac{\partial{f}}{\partial{x}}=\cos\theta\frac{\partial{g}}{\partial{r}}-\frac{1}{r}"
                       r"\sin\theta\frac{\partial{g}}{\partial{\theta}}").move_to(UP + LEFT*3.3).scale(0.75)
        eq15 = MathTex(r"\frac{\partial{f}}{\partial{y}}=\sin\theta\frac{\partial{g}}{\partial{r}}+\frac{1}{r}"
                       r"\cos\theta\frac{\partial{g}}{\partial{\theta}}").move_to(UP + RIGHT*2.7).scale(0.75)
        eq16 = MathTex(r"y",
                       r"\Bigl(\cos\theta\frac{\partial{g}}{\partial{r}}-\frac{1}{r}"
                       r"\sin\theta\frac{\partial{g}}{\partial{\theta}}\Bigr)",
                       r"-",
                       r"x",
                       r"\Bigl(\sin\theta\frac{\partial{g}}{\partial{r}}+\frac{1}{r}"
                       r"\cos\theta\frac{\partial{g}}{\partial{\theta}}\Bigr)",
                       r"=0").move_to(DOWN)
        self.play(FadeIn(eq14))
        self.wait(2)
        self.play(Transform(eq12[1], eq16[1]))
        self.wait(2)
        self.play(FadeIn(eq15))
        self.wait(2)
        self.play(Transform(eq12[4], eq16[4]))
        self.play(Transform(eq12, eq16))
        self.wait(3)
        self.play(FadeOut(eq14), FadeOut(eq15))
        self.wait(2)
        eq17 = MathTex(r"y=r\sin\theta").move_to(UP + LEFT * 3)
        eq18 = MathTex(r"x=r\cos\theta").move_to(UP + RIGHT * 2)
        eq19 = MathTex(r"r\sin\theta",
                       r"\Bigl(\cos\theta\frac{\partial{g}}{\partial{r}}-\frac{1}{r}"
                       r"\sin\theta\frac{\partial{g}}{\partial{\theta}}\Bigr)",
                       r"-",
                       r"r\cos\theta",
                       r"\Bigl(\sin\theta\frac{\partial{g}}{\partial{r}}+\frac{1}{r}"
                       r"\cos\theta\frac{\partial{g}}{\partial{\theta}}\Bigr)",
                       r"=0").move_to(DOWN)
        self.play(FadeIn(eq17))
        self.wait(2)
        self.play(Transform(eq12[0], eq19[0]))
        self.wait(2)
        self.play(FadeIn(eq18))
        self.wait(2)
        self.play(Transform(eq12[3], eq19[3]))
        self.play(Transform(eq12, eq19))
        self.wait(3)
        self.play(FadeOut(eq17), FadeOut(eq18))
        eq20 = MathTex(r"r\sin\theta",
                       r"\Bigl(\cos\theta\frac{\partial{g}}{\partial{r}}-\frac{1}{r}"
                       r"\sin\theta\frac{\partial{g}}{\partial{\theta}}\Bigr)",
                       r"-",
                       r"r\cos\theta",
                       r"\Bigl(\sin\theta\frac{\partial{g}}{\partial{r}}+\frac{1}{r}"
                       r"\cos\theta\frac{\partial{g}}{\partial{\theta}}\Bigr)",
                       r"=0")
        self.play(Transform(eq12, eq20))
        self.wait()
        eq21 = MathTex(r"r\sin\theta\cos\theta\frac{\partial{g}}{\partial{r}}",
                       r"-\sin^2\theta\frac{\partial{g}}{\partial{\theta}}",
                       r"-r\sin\theta\cos\theta\frac{\partial{g}}{\partial{r}}",
                       r"-\cos^2\theta\frac{\partial{g}}{\partial{\theta}}=0")
        self.play(Transform(eq12, eq21))
        self.wait(3)
        eq22 = MathTex(r"r\sin\theta\cos\theta\frac{\partial{g}}{\partial{r}}",
                       r"-\sin^2\theta\frac{\partial{g}}{\partial{\theta}}",
                       r"-r\sin\theta\cos\theta\frac{\partial{g}}{\partial{r}}",
                       r"-\cos^2\theta\frac{\partial{g}}{\partial{\theta}}=0")
        eq22[0].set_color(YELLOW)
        eq22[2].set_color(YELLOW)
        self.play(Transform(eq12, eq22))
        self.wait(2)
        eq23 = MathTex(r" ",
                       r"-\sin^2\theta\frac{\partial{g}}{\partial{\theta}}",
                       r" ",
                       r"-\cos^2\theta\frac{\partial{g}}{\partial{\theta}}=0")
        self.play(Transform(eq12, eq23))
        self.wait(2)
        eq24 = MathTex(r" ",
                       r"-\Bigl(\sin^2\theta+\cos^2\theta\Bigr)",
                       r" ",
                       r"\frac{\partial{g}}{\partial{\theta}}=0")
        self.play(Transform(eq12, eq24))
        self.wait(2)
        eq25 = MathTex(r" ",
                       r"-\Bigl(1\Bigr)",
                       r" ",
                       r"\frac{\partial{g}}{\partial{\theta}}=0")
        self.play(Transform(eq12, eq25))
        self.wait(2)
        eq26 = MathTex(r" ",
                       r" ",
                       r" ",
                       r"\frac{\partial{g}}{\partial{\theta}}=0")
        self.play(Transform(eq12, eq26))
        self.wait(2)
        self.play(FadeOut(eq12))
        self.wait(2)

        # Solución
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{cancel}")
        eq27 = MathTex(r"\frac{\partial{g}}{\partial{\theta}}=0",
                       r"\Longrightarrow",
                       r"g(r,\cancel{\theta})", tex_template=myTemplate)
        self.play(FadeIn(eq27[0]))
        self.wait()
        self.play(FadeIn(eq27[1]), FadeIn(eq27[2]))
        self.wait()
        eq28 = MathTex(r"\frac{\partial{g}}{\partial{\theta}}=0",
                       r"\Longrightarrow",
                       r"g(r)")
        self.play(Transform(eq27[2], eq28[2]))
        self.play(Transform(eq27, eq28))
        self.wait()
        eq29 = MathTex(r"\frac{\partial{g}}{\partial{\theta}}=0",
                       r"\Longrightarrow",
                       r"g(r)").move_to(UP)
        self.play(Transform(eq27, eq29))
        self.wait()
        eq30 = MathTex(r"f(x,y)=g\circ T(x,y)",
                       r"=g\Bigl(",
                       r"r(x,y)",
                       r"\Bigr)\\",
                       r"=g\Bigl(",
                       r"\sqrt{x^2+y^2}\thinspace",
                       r"\Bigr)",
                       r"=F(x^2+y^2)").move_to(DOWN)
        eq30[2].set_color(YELLOW)
        eq30[5].set_color(YELLOW)
        self.play(FadeIn(eq30[0]))
        self.wait(2)
        self.play(FadeIn(eq30[1]), FadeIn(eq30[2]), FadeIn(eq30[3]))
        self.wait(2)
        self.play(FadeIn(eq30[4]), FadeIn(eq30[5]), FadeIn(eq30[6]))
        self.wait(2)
        self.play(FadeIn(eq30[7]))
        self.wait(2)
        eq31 = MathTex(r"f(x,y)=",
                       r" ",
                       r" ",
                       r"\\",
                       r" ",
                       r" ",
                       r" ",
                       r"F(x^2+y^2)").move_to(DOWN)
        eq32 = MathTex(r"f(x,y)=F(x^2+y^2)").move_to(DOWN)
        self.play(Transform(eq30[1], eq31[1]), Transform(eq30[0], eq31[0]),
                  Transform(eq30[2], eq31[2]), Transform(eq30[3], eq31[3]),
                  Transform(eq30[4], eq31[4]), Transform(eq30[5], eq31[5]),
                  Transform(eq30[6], eq31[6]))
        self.wait()
        self.play(Transform(eq30, eq32))
        self.wait(3)
        self.play(FadeOut(eq30), FadeOut(eq27))
        self.wait()

class video12(VectorScene):
    def construct(self):
        gris = "#C7C7C7"
        verde = "#02B126"
        rojo = "#CF010B"
        azul = "#42A5F5"
        plane = NumberPlane(
            background_line_style={
                "stroke_color": gris,
                "stroke_opacity": 0.3,
                "stroke_width": 2
            },
            axis_config={
                "stroke_width": 4,
                "label_direction": DR,
                "include_ticks": True,
                "include_numbers": False
            }
        )

        label_x = MathTex(r"x").move_to(RIGHT * 6.5 + DOWN * 0.5)
        label_y = MathTex(r"y").move_to(LEFT * 0.5 + UP * 3.5)
        v = lambda x: np.array([x[0], x[1]])
        field_v = ArrowVectorField(v).set_color(rojo)
        eq1 = MathTex(r"\vec{v}=(x,y)").move_to(RIGHT * 2 + UP * 2.5).set_color(rojo)
        self.wait(2)
        self.play(FadeIn(plane), FadeIn(label_x), FadeIn(label_y))
        self.wait(2)
        self.play(FadeIn(eq1))
        self.wait(3)
        self.play(FadeOut(eq1))
        self.play([GrowArrow(vec) for vec in field_v], run_time=2)
        self.wait(3)
        self.play(FadeOut(field_v))
        self.wait(2)

        eq2 = MathTex(r"\nabla{f}").move_to(RIGHT * 2.7 + UP * 0.5).set_color(verde)
        eq3 = MathTex(r"\vec{v}=(\sqrt{3},1)").move_to(RIGHT * 1.8 + UP * 2.25).set_color(rojo)
        eq4 = MathTex(r"\vec{v}=(-1,\sqrt{3})").move_to(LEFT * 3 + UP * 2.25).set_color(YELLOW)
        eq5 = MathTex(r"\vec{v}=(-1.96,0.35)").move_to(LEFT * 2.7 + UP * 1.1).set_color(azul)
        vec1 = (Vector([2 * np.cos(30 * np.pi / 180), 2 * np.sin(30 * np.pi / 180)]).set_color(rojo)
               .shift(np.array([2 * np.cos(30 * np.pi / 180), 2 * np.sin(30 * np.pi / 180), 0])))
        vec2 = (Vector([2 * np.cos(120 * np.pi / 180), 2 * np.sin(120 * np.pi / 180)]).set_color(YELLOW)
                .shift(np.array([2 * np.cos(120 * np.pi / 180), 2 * np.sin(120 * np.pi / 180), 0])))
        vec3 = (Vector([2 * np.cos(170 * np.pi / 180), 2 * np.sin(170 * np.pi / 180)]).set_color(azul)
                .shift(np.array([2 * np.cos(170 * np.pi / 180), 2 * np.sin(170 * np.pi / 180), 0])))
        grad1 = (Vector([np.sin(30 * np.pi / 180), -np.cos(30 * np.pi / 180)]).set_color(verde)
                .shift(np.array([2 * np.cos(30 * np.pi / 180), 2 * np.sin(30 * np.pi / 180), 0])))
        grad1p2 = (Vector([0.9*np.sin(30 * np.pi / 180), -0.9*np.cos(30 * np.pi / 180)]).set_color(verde)
                 .shift(np.array([3.5 * np.cos(30 * np.pi / 180), 3.5 * np.sin(30 * np.pi / 180), 0])))
        grad1p3 = (Vector([0.8 * np.sin(30 * np.pi / 180), -0.8 * np.cos(30 * np.pi / 180)]).set_color(verde)
                   .shift(np.array([5 * np.cos(30 * np.pi / 180), 5 * np.sin(30 * np.pi / 180), 0])))
        grad1p4 = (Vector([0.7 * np.sin(30 * np.pi / 180), -0.7 * np.cos(30 * np.pi / 180)]).set_color(verde)
                   .shift(np.array([6.5 * np.cos(30 * np.pi / 180), 6.5 * np.sin(30 * np.pi / 180), 0])))
        grad1p5 = (Vector([0.6 * np.sin(30 * np.pi / 180), -0.6 * np.cos(30 * np.pi / 180)]).set_color(verde)
                   .shift(np.array([8 * np.cos(30 * np.pi / 180), 8 * np.sin(30 * np.pi / 180), 0])))
        grad1p6 = (Vector([-np.sin(30 * np.pi / 180), np.cos(30 * np.pi / 180)]).set_color(verde)
                 .shift(np.array([-2 * np.cos(30 * np.pi / 180), -2 * np.sin(30 * np.pi / 180), 0])))
        grad1p7 = (Vector([-0.9 * np.sin(30 * np.pi / 180), 0.9 * np.cos(30 * np.pi / 180)]).set_color(verde)
                   .shift(np.array([-3.5 * np.cos(30 * np.pi / 180), -3.5 * np.sin(30 * np.pi / 180), 0])))
        grad1p8 = (Vector([-0.8 * np.sin(30 * np.pi / 180), 0.8 * np.cos(30 * np.pi / 180)]).set_color(verde)
                   .shift(np.array([-5 * np.cos(30 * np.pi / 180), -5 * np.sin(30 * np.pi / 180), 0])))
        grad1p9 = (Vector([-0.7 * np.sin(30 * np.pi / 180), 0.7 * np.cos(30 * np.pi / 180)]).set_color(verde)
                   .shift(np.array([-6.5 * np.cos(30 * np.pi / 180), -6.5 * np.sin(30 * np.pi / 180), 0])))
        grad1p10 = (Vector([-0.6 * np.sin(30 * np.pi / 180), 0.6 * np.cos(30 * np.pi / 180)]).set_color(verde)
                   .shift(np.array([-8 * np.cos(30 * np.pi / 180), -8 * np.sin(30 * np.pi / 180), 0])))
        recta1 = (Line(start=np.array([-30, -10*np.sqrt(3), 0]), end=np.array([30, 10*np.sqrt(3), 0])
                       ).set_color(rojo))
        recta2 = (Line(start=np.array([-30, 30 * np.sqrt(3), 0]), end=np.array([30, -30 * np.sqrt(3), 0])
                       ).set_color(YELLOW))
        recta3 = (Line(start=np.array([-30, -30 * np.tan(170*np.pi / 180), 0]),
                       end=np.array([30, 30 * np.tan(170*np.pi / 180), 0])).set_color(azul))
        dot = Dot(point=ORIGIN, radius=0.25).set_color(verde)
        f1 = MathTex(r"f=0.25").set_color(rojo).move_to(RIGHT*6+UP*2.5)
        f2 = MathTex(r"f=0.75").set_color(YELLOW).move_to(LEFT*3.2+UP*3.5)
        f3 = MathTex(r"f=0.03").set_color(azul).move_to(LEFT*6+UP*0.5)

        self.add_vector(vec1)
        self.play(FadeIn(eq3))
        self.wait(2)
        self.add_vector(grad1)
        self.play(FadeIn(eq2))
        self.wait(2)
        self.play(FadeIn(recta1), FadeOut(vec1))
        self.wait(2)
        self.add_vector(grad1p2)
        self.add_vector(grad1p3)
        self.add_vector(grad1p4)
        self.add_vector(grad1p5)
        self.add_vector(grad1p6)
        self.add_vector(grad1p7)
        self.add_vector(grad1p8)
        self.add_vector(grad1p9)
        self.add_vector(grad1p10)
        self.wait(2)
        self.play(FadeIn(f1))
        self.wait(3)
        self.play(FadeOut(grad1p2), FadeOut(grad1p3), FadeOut(grad1p4), FadeOut(grad1p5), FadeOut(eq2),
                  FadeOut(grad1p6), FadeOut(grad1p7), FadeOut(grad1p8), FadeOut(grad1p9), FadeOut(grad1p10),
                  FadeOut(grad1), FadeOut(eq3))
        self.wait(2)
        self.add_vector(vec2)
        self.play(FadeIn(eq4))
        self.wait(2)
        self.play(FadeIn(recta2), FadeOut(vec2))
        self.wait()
        self.play(FadeIn(f2))
        self.wait(3)
        self.play(FadeOut(eq4))
        self.add_vector(vec3)
        self.play(FadeIn(eq5))
        self.wait(2)
        self.play(FadeIn(recta3), FadeOut(vec3))
        self.wait()
        self.play(FadeIn(f3))
        self.wait(3)
        self.play(FadeOut(eq5))
        self.play(FadeIn(dot))
        self.wait(3)

class video13(Scene):
    def construct(self):
        eq0 = MathTex(r"(3) \hspace{0.5cm} x\frac{\partial f}{\partial x}+y\frac{\partial f}{\partial y}=0")
        self.play(FadeIn(eq0))
        self.wait(3)
        self.play(FadeOut(eq0))
        eq1 = MathTex(r"x\frac{\partial f}{\partial x}+y\frac{\partial f}{\partial y}",
                      r"=",
                      r"(x,y)",
                      r"\cdot",
                      r"\Bigl(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \Bigr)",
                      r"=\vec{v}\cdot \nabla{f}=0")
        self.wait()
        self.play(FadeIn(eq1[0]))
        self.wait(2)
        self.play(FadeIn(eq1[1]), FadeIn(eq1[2]), FadeIn(eq1[3]), FadeIn(eq1[4]))
        self.wait()
        eq2 = MathTex(r"x\frac{\partial f}{\partial x}+y\frac{\partial f}{\partial y}",
                      r"=",
                      r"(x,y)",
                      r"\cdot",
                      r"\Bigl(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \Bigr)",
                      r"=\vec{v}\cdot \nabla{f}=0")
        eq2[4].set_color(YELLOW)
        eq2[2].set_color(YELLOW)
        eq3 = MathTex(r"x\frac{\partial f}{\partial x}+y\frac{\partial f}{\partial y}",
                      r"=",
                      r"(x,y)",
                      r"\cdot",
                      r"\Bigl(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \Bigr)",
                      r"=\vec{v}\cdot \nabla{f}=0")
        self.play(Transform(eq1[4], eq2[4]))
        self.wait(2)
        self.play(Transform(eq1[2], eq2[2]), Transform(eq1[4], eq3[4]))
        self.wait(2)
        self.play(Transform(eq1[2], eq3[2]), FadeIn(eq1[5]))
        self.wait(2)
        eq4 = MathTex(r"x\frac{\partial f}{\partial x}+y\frac{\partial f}{\partial y}",
                      r"=",
                      r"(x,y)",
                      r"\cdot",
                      r"\Bigl(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \Bigr)",
                      r"=\vec{v}\cdot \nabla{f}=0").move_to(UP)
        self.play(Transform(eq1, eq4))
        eq5 = MathTex(r"\vec{v}=(x,y)").move_to(DOWN)
        self.wait()
        self.play(FadeIn(eq5))
        self.wait(3)
        self.play(FadeOut(eq1))
        self.wait()
        eq6 = MathTex(r"\vec{v}=(x,y)").move_to(LEFT * 2)
        eq7 = MathTex(r"\Longrightarrow \hspace{0.2cm} \nabla{f}\perp \vec{v}").move_to(RIGHT)
        self.play(Transform(eq5, eq6))
        self.wait(2)
        self.play(FadeIn(eq7))
        self.wait(3)
        self.play(FadeOut(eq5), FadeOut(eq7))
        self.wait()

        eq8 = MathTex(r"(x,y)",
                      r"\cdot \nabla{f}\Bigl|",
                      r"_{(x,y)}",
                      r"=x\frac{\partial f}{\partial x}\Bigl|",
                      r"_{(x,y)}",
                      r"+\thinspace y\frac{\partial f}{\partial x}\Bigl|",
                      r"_{(x,y)}",
                      r"=0")
        self.play(FadeIn(eq8[0]), FadeIn(eq8[1]), FadeIn(eq8[2]))
        self.wait(2)
        eq9 = MathTex(r"(x,y)",
                      r"\cdot \nabla{f}\Bigl|",
                      r"_{(x,y)}",
                      r"=x\frac{\partial f}{\partial x}\Bigl|",
                      r"_{(x,y)}",
                      r"+\thinspace y\frac{\partial f}{\partial x}\Bigl|",
                      r"_{(x,y)}",
                      r"=0"
                      )
        eq9[2].set_color(YELLOW)
        self.play(Transform(eq8[2], eq9[2]))
        self.wait(3)
        eq10 = MathTex(r"(x,y)",
                       r"\cdot \nabla{f}\Bigl|",
                       r"_{(x,y)}",
                       r"=x\frac{\partial f}{\partial x}\Bigl|",
                       r"_{(x,y)}",
                       r"+\thinspace y\frac{\partial f}{\partial x}\Bigl|",
                       r"_{(x,y)}",
                       r"=0")
        self.play(Transform(eq8[2], eq10[2]))
        self.wait()
        self.play(FadeIn(eq8[3]), FadeIn(eq8[4]))
        self.wait()
        self.play(FadeIn(eq8[5]), FadeIn(eq8[6]))
        self.wait()
        self.play(FadeIn(eq8[7]))
        self.wait(3)
        eq11 = MathTex(r"(x,y)",
                       r"\cdot \nabla{f}\Bigl|",
                       r"_{(x,y)}",
                       r"=x\frac{\partial f}{\partial x}\Bigl|",
                       r"_{(x,y)}",
                       r"+\thinspace y\frac{\partial f}{\partial x}\Bigl|",
                       r"_{(x,y)}",
                       r"=0").move_to(UP)
        self.play(Transform(eq8, eq11))
        self.wait(2)
        eq12 = MathTex(r"(t,m\thinspace t)",
                       r"\cdot \nabla{f}\Bigl|",
                       r"_{(t,m\thinspace t)}",
                       r"=t\frac{\partial f}{\partial x}\Bigl|",
                       r"_{(t,m\thinspace t)}",
                       r"+\thinspace mt\frac{\partial f}{\partial x}\Bigl|",
                       r"_{(t,m\thinspace t)}",
                       r"=0").move_to(UP)
        eq13 = MathTex(r"(x,y)",
                       r"=(t,m\thinspace t)",
                       r"\Longrightarrow y=m\thinspace x").move_to(DOWN)
        self.play(FadeIn(eq13[0]))
        self.wait()
        self.play(FadeIn(eq13[1]))
        self.wait(2)
        self.play(FadeIn(eq13[2]))
        self.wait(3)
        self.play(Transform(eq8[0], eq12[0]))
        self.wait(2)
        self.play(Transform(eq8[2], eq12[2]))
        self.wait(2)
        self.play(Transform(eq8[3], eq12[3]))
        self.wait(2)
        self.play(Transform(eq8[4], eq12[4]))
        self.wait(2)
        self.play(Transform(eq8[5], eq12[5]))
        self.wait(2)
        self.play(Transform(eq8[6], eq12[6]))
        self.wait(2)
        self.play(Transform(eq8, eq12))
        self.wait(3)
        self.play(FadeOut(eq13))
        self.wait()

        eq14 = MathTex(r"(t,m\thinspace t)",
                       r"\cdot \nabla{f}\Bigl|",
                       r"_{(t,m\thinspace t)}",
                       r"=t\frac{\partial f}{\partial x}\Bigl|",
                       r"_{(t,m\thinspace t)}",
                       r"+\thinspace mt\frac{\partial f}{\partial x}\Bigl|",
                       r"_{(t,m\thinspace t)}",
                       r"=0")
        self.play(Transform(eq8, eq14))
        self.wait(2)
        eq15 = MathTex(r"(t,m\thinspace t)",
                       r"\cdot \nabla{f}\Bigl|",
                       r"_{(t,m\thinspace t)}",
                       r" ",
                       r" ",
                       r" ",
                       r" ",
                       r"=0")
        self.play(Transform(eq8, eq15))
        self.wait(2)
        eq16 = MathTex(r"t(1,m)",
                       r"\cdot \nabla{f}\Bigl|",
                       r"_{(t,m\thinspace t)}",
                       r" ",
                       r" ",
                       r" ",
                       r" ",
                       r"=0")
        self.play(Transform(eq8[0], eq16[0]))
        self.play(Transform(eq8, eq16))
        self.wait(2)
        eq17 = MathTex(r"(1,m)",
                       r"\cdot \nabla{f}\Bigl|",
                       r"_{(t,m\thinspace t)}",
                       r" ",
                       r" ",
                       r" ",
                       r" ",
                       r"=0")
        eq18 = MathTex(r"(1,m)",
                       r"\cdot \nabla{f}\Bigl|",
                       r"_{(t,m\thinspace t)}",
                       r" ",
                       r" ",
                       r" ",
                       r" ",
                       r"=0").move_to(UP)
        self.play(Transform(eq8, eq17))
        self.wait(2)
        self.play(Transform(eq8, eq18))
        self.wait(3)
        eq19 = MathTex(r"\nabla{f}\perp (1,m)",
                       r"\Longrightarrow y=m\thinspace x \hspace{0.25cm} \text{Curva de nivel}").move_to(DOWN)
        self.play(FadeIn(eq19[0]))
        self.wait(2)
        self.play(FadeIn(eq19[1]))
        self.wait(3)
        self.play(FadeOut(eq8), FadeOut(eq19))
        self.wait()

        eq20 = MathTex(r"f(x,y)",
                       r"=F\Bigl(",
                       r"\hspace{0.2cm}",
                       r"\Bigr)").move_to(UP)
        self.play(FadeIn(eq20))
        eq21 = MathTex(r"y=m\thinspace x",
                       r"\Longrightarrow \frac{y}{x}=m",
                       r"=cte").move_to(DOWN)
        self.play(FadeIn(eq21[0]))
        self.wait()
        self.play(FadeIn(eq21[1]))
        self.wait()
        self.play(FadeIn(eq21[2]))
        self.wait()
        eq22 = MathTex(r"f(x,y)",
                       r"=F\Bigl(",
                       r"\frac{y}{x}",
                       r"\Bigr)").move_to(UP)
        self.play(Transform(eq20[2], eq22[2]))
        self.play(Transform(eq20, eq22))
        self.wait(3)
        self.play(FadeOut(eq20), FadeOut(eq21))
        self.wait()

class video14(Scene):
    def construct(self):
        eq1 = MathTex(r"x\frac{\partial f}{\partial x}+y\frac{\partial f}{\partial y}=0"
                      r"\hspace{0.3cm}",
                      r"\Longrightarrow \hspace{0.3cm}",
                      r"a",
                      r"\frac{\partial f}{\partial x} +",
                      r" b",
                      r"\frac{\partial f}{\partial y}=0")
        eq2 = MathTex(r"x\frac{\partial f}{\partial x}+y\frac{\partial f}{\partial y}=0"
                      r"\hspace{0.3cm}",
                      r"\Longrightarrow \hspace{0.3cm}",
                      r" ",
                      r"\frac{\partial f}{\partial x} +",
                      r" ",
                      r"\frac{\partial f}{\partial y}=0")
        self.wait()
        self.play(FadeIn(eq1[0]))
        self.wait()
        self.play(FadeIn(eq1[1]), FadeIn(eq1[2]), FadeIn(eq1[3]), FadeIn(eq1[4]),
                  FadeIn(eq1[5]))
        self.wait(2)
        self.play(Transform(eq1, eq2))
        self.wait(3)
        self.play(FadeOut(eq1))
        self.wait()
        eq3 = MathTex(r"f(x,y)=g\circ T(x,y)").move_to(UP + LEFT*3)
        eq4 = MathTex(r"g(u,w)").move_to(UP + RIGHT*2)
        self.play(FadeIn(eq3))
        self.wait(2)
        self.play(FadeIn(eq4))
        self.wait(3)
        eq5 = MathTex(r"u(x)",
                      r"=",
                      r"\ln |x|",
                      r"\hspace{0.2cm} w(y)",
                      r"=",
                      r"\ln |y|").move_to(UP + RIGHT*3)
        eq5[2].set_color(YELLOW)
        eq5[5].set_color(BLUE)
        eq6 = MathTex(r"x \hspace{0.2cm}",
                      r"\frac{\partial f}{\partial x}",
                      r"\hspace{0.2cm}",
                      r"+\hspace{0.2cm}",
                      r"y \hspace{0.2cm}",
                      r"\frac{\partial f}{\partial y}",
                      r"\hspace{0.2cm}",
                      r"=0"
                      ).move_to(DOWN)
        self.play(FadeIn(eq6))
        self.wait()
        self.play(FadeOut(eq4))
        self.wait()
        self.play(FadeIn(eq5[0]), FadeIn(eq5[3]))
        self.wait(3)
        eq7 = MathTex(r"x",
                      r"\frac{\partial g}{\partial u}",
                      r"\frac{du}{dx}",
                      r"+\thinspace ",
                      r"y",
                      r"\frac{\partial g}{\partial w}",
                      r"\frac{dw}{dy}",
                      r"=0"
                      ).move_to(DOWN)
        self.play(Transform(eq6[1], eq7[1]))
        self.wait()
        self.play(Transform(eq6[2], eq7[2]))
        self.wait()
        self.play(Transform(eq6[5], eq7[5]))
        self.wait()
        self.play(Transform(eq6[6], eq7[6]))
        self.play(Transform(eq6, eq7))
        self.wait(3)
        eq8 = MathTex(r"x",
                      r"\frac{\partial g}{\partial u}",
                      r"\frac{1}{x}",
                      r"+\thinspace ",
                      r"y",
                      r"\frac{\partial g}{\partial w}",
                      r"\frac{1}{y}",
                      r"=0"
                      ).move_to(DOWN)
        eq8[2].set_color(YELLOW)
        eq8[6].set_color(BLUE)
        self.play(Transform(eq6[2], eq8[2]))
        self.wait(3)
        self.play(FadeIn(eq5[1]), FadeIn(eq5[2]))
        self.wait(3)
        self.play(Transform(eq6[6], eq8[6]))
        self.wait(3)
        self.play(FadeIn(eq5[4]), FadeIn(eq5[5]))
        self.wait(3)
        self.play(Transform(eq6, eq8))
        self.wait()
        eq9 = MathTex(r" ",
                      r"\frac{\partial g}{\partial u}",
                      r" ",
                      r"+\thinspace ",
                      r" ",
                      r"\frac{\partial g}{\partial w}",
                      r" ",
                      r"=0"
                      ).move_to(DOWN)
        eq10 = MathTex(r" ",
                      r"\frac{\partial g}{\partial u}",
                      r" ",
                      r"+\thinspace ",
                      r" ",
                      r"\frac{\partial g}{\partial w}",
                      r" ",
                      r"=0"
                      ).move_to(LEFT*2.2)
        self.play(Transform(eq6, eq9))
        self.wait(2)
        self.play(FadeOut(eq3), FadeOut(eq5), Transform(eq6, eq10))
        self.wait(2)
        eq11 = MathTex(r"\Longrightarrow g(u,w)=G(u-w)").move_to(RIGHT*2.2)
        self.play(FadeIn(eq11))
        self.wait()
        eq12 = MathTex(r" ",
                       r"\frac{\partial g}{\partial u}",
                       r" ",
                       r"+\thinspace ",
                       r" ",
                       r"\frac{\partial g}{\partial w}",
                       r" ",
                       r"=0"
                       ).move_to(LEFT * 2.2 + UP)
        eq13 = MathTex(r"\Longrightarrow g(u,w)=G(u-w)").move_to(RIGHT * 2.2 + UP)
        self.play(Transform(eq6, eq12), Transform(eq11, eq13))
        self.wait()
        eq14 = MathTex(r"f(x,y)",
                       r"=g\circ T(x,y)",
                       r"= g\Bigl(u(x),w(y)\Bigr)",
                       r"=G\Bigl(",
                       r"u(x)-w(y)",
                       r"\Bigr)"
                       ).move_to(DOWN)
        self.play(FadeIn(eq14[0]))
        self.wait(2)
        self.play(FadeIn(eq14[1]))
        self.wait(2)
        self.play(FadeIn(eq14[2]))
        self.wait(2)
        self.play(FadeIn(eq14[3]), FadeIn(eq14[4]), FadeIn(eq14[5]))
        self.wait(2)
        eq15 = MathTex(r"f(x,y)",
                       r"=g\circ T(x,y)",
                       r"= g\Bigl(u(x),w(y)\Bigr)",
                       r"=G\Bigl(",
                       r"\ln |x|-\ln |y|",
                       r"\Bigr)",
                       ).move_to(DOWN)
        self.play(Transform(eq14[4], eq15[4]))
        self.play(Transform(eq14, eq15))
        self.wait(2)
        eq16 = MathTex(r"f(x,y)",
                       r"=g\circ T(x,y)",
                       r"= g\Bigl(u(x),w(y)\Bigr)",
                       r"=G\Bigl(",
                       r"\ln\frac{|x|}{|y|}",
                       r"\Bigr)",
                       ).move_to(DOWN)
        self.play(Transform(eq14, eq16))
        self.wait(2)
        eq17 = MathTex(r"f(x,y)",
                       r"=g\circ T(x,y)",
                       r"= g\Bigl(u(x),w(y)\Bigr)",
                       r"=F\Bigl(",
                       r"\frac{x}{y}",
                       r"\Bigr)",
                       ).move_to(DOWN)
        self.play(Transform(eq14[3], eq17[3]), Transform(eq14[4], eq17[4]))
        self.play(Transform(eq14, eq17))
        self.wait(2)
        eq18 = MathTex(r"f(x,y)",
                       r"=g\circ T(x,y)",
                       r"= g\Bigl(u(x),w(y)\Bigr)",
                       r"=F\Bigl(",
                       r"\frac{y}{x}",
                       r"\Bigr)",
                       ).move_to(DOWN)
        self.play(Transform(eq14, eq18))
        self.wait(2)
        eq19 = MathTex(r"f(x,y)",
                       r" ",
                       r" ",
                       r"=F\Bigl(",
                       r"\frac{y}{x}",
                       r"\Bigr)",
                       ).move_to(DOWN)
        self.play(Transform(eq14, eq19))
        self.wait(3)
        self.play(FadeOut(eq14), FadeOut(eq6), FadeOut(eq11))
        self.wait()

class video15(Scene):
    def construct(self):
        # Problema de Cauchy 1
        eq1 = MathTex(r"f(",
                      r"x=1",
                      r",y)",
                      r"=\frac{1}{1+y^2}",
                      r"=F\Bigl(",
                      r"\frac{y}{1}",
                      r"\Bigr)")
        eq1[1].set_color(BLUE)
        eq1[5].set_color(BLUE)
        self.play(FadeIn(eq1[0]), FadeIn(eq1[1]), FadeIn(eq1[2]))
        self.wait(2)
        self.play(FadeIn(eq1[3]))
        self.wait(3)
        self.play(FadeIn(eq1[4]), FadeIn(eq1[5]), FadeIn(eq1[6]))
        self.wait(3)
        eq2 = MathTex(r"f(",
                      r"x=1",
                      r",y)",
                      r"=\frac{1}{1+y^2}",
                      r"=F\Bigl(",
                      r"\frac{y}{x}",
                      r"\Bigr)")
        eq3 = MathTex(r"f(",
                      r"x",
                      r",y)",
                      r"=\frac{1}{1+(\frac{y}{x})^2}",
                      r"=F\Bigl(",
                      r"\frac{y}{x}",
                      r"\Bigr)")
        self.play(Transform(eq1[5], eq2[5]))
        self.wait()
        self.play(Transform(eq1[3], eq3[3]))
        self.play(Transform(eq1, eq3))
        self.wait()
        eq4 = MathTex(r"f(",
                      r"x",
                      r",y)",
                      r"=\frac{x^2}{x^2+y^2}",
                      r"=F\Bigl(",
                      r"\frac{y}{x}",
                      r"\Bigr)")
        self.play(Transform(eq1[3], eq4[3]))
        self.wait()
        self.play(Transform(eq1, eq4))
        self.wait(3)
        self.play(FadeOut(eq1))
        self.wait(2)

        # Problema de Cauchy 2
        eq5 = MathTex(r"f(",
                      r"x=1",
                      r",y)",
                      r"=\frac{1}{y-1}",
                      r"=F\Bigl(",
                      r"\frac{y}{1}",
                      r"\Bigr)")
        eq5[1].set_color(BLUE)
        eq5[5].set_color(BLUE)
        self.play(FadeIn(eq5[0]), FadeIn(eq5[1]), FadeIn(eq5[2]))
        self.wait()
        self.play(FadeIn(eq5[3]))
        self.wait(2)
        self.play(FadeIn(eq5[4]), FadeIn(eq5[5]), FadeIn(eq5[6]))
        self.wait(2)
        eq6 = MathTex(r"f(",
                      r"x=1",
                      r",y)",
                      r"=\frac{1}{y-1}",
                      r"=F\Bigl(",
                      r"\frac{y}{x}",
                      r"\Bigr)")
        eq7 = MathTex(r"f(",
                      r"x",
                      r",y)",
                      r"=\frac{1}{\frac{y}{x}-1}",
                      r"=F\Bigl(",
                      r"\frac{y}{x}",
                      r"\Bigr)")
        self.play(Transform(eq5[5], eq6[5]))
        self.wait()
        self.play(Transform(eq5[3], eq7[3]))
        self.play(Transform(eq5, eq7))
        self.wait()
        eq8 = MathTex(r"f(",
                      r"x",
                      r",y)",
                      r"=\frac{x}{y-x}",
                      r"=F\Bigl(",
                      r"\frac{y}{x}",
                      r"\Bigr)")
        self.play(Transform(eq5[3], eq8[3]))
        self.wait()
        self.play(Transform(eq5, eq8))
        self.wait(3)
        self.play(FadeOut(eq5))
        self.wait()

class video16(Scene):
    def construct(self):
        gris = "#C7C7C7"
        rojo = "#CF010B"
        plane = NumberPlane(
            background_line_style={
                "stroke_color": gris,
                "stroke_opacity": 0.3,
                "stroke_width": 2
            },
            axis_config={
                "stroke_width": 4,
                "label_direction": DR,
                "include_ticks": True,
                "include_numbers": False
            }
        )

        label_x = MathTex(r"x").move_to(RIGHT * 6.5 + DOWN * 0.5)
        label_y = MathTex(r"y").move_to(LEFT * 0.5 + UP * 3.5)
        self.wait(2)
        self.play(FadeIn(plane), FadeIn(label_x), FadeIn(label_y))
        self.wait(2)

        label_recta = MathTex(r"y=x").move_to(RIGHT * 4 + UP * 2.5).set_color(rojo)
        recta = (Line(start=np.array([-10, -10, 0]), end=np.array([10, 10, 0])
                       ).set_color(rojo))
        self.play(Write(recta), Write(label_recta))
        self.wait(3)

class video17(Scene):
    def construct(self):
        eq1 = MathTex(r"f(",
                      r"x",
                      r",y",
                      r")",
                      r" ")
        self.wait()
        self.play(FadeIn(eq1))
        self.wait()
        eq2 = MathTex(r"f(",
                      r"\lambda x",
                      r",y",
                      r")",
                      r" ")
        eq3 = MathTex(r"f(",
                      r"\lambda x",
                      r",\lambda y",
                      r")",
                      r" ")
        eq4 = MathTex(r"f(",
                      r"\lambda x",
                      r",\lambda y",
                      r")",
                      r"=\lambda^mf(x,y)")
        self.play(Transform(eq1[1], eq2[1]))
        self.play(Transform(eq1, eq2))
        self.wait()
        self.play(Transform(eq1[2], eq3[2]))
        self.play(Transform(eq1, eq3))
        self.wait(2)
        self.play(Transform(eq1, eq4), run_time=1.5)
        self.wait(2)
        eq5 = MathTex(r"f(",
                      r"\lambda x",
                      r",\lambda y",
                      r")",
                      r"=\lambda^mf(x,y)").move_to(UP * 2)
        self.play(Transform(eq1, eq5))
        self.wait(2)
        eq5p2 = MathTex(r"f(",
                        r"x,",
                        r"y",
                        r")",
                        r"=x^2",
                        r"+3xy\sin\Bigl(\frac{x}{y}\Bigr)",
                        r"-7y^2",
                        r" ")
        eq5p3 = MathTex(r"f(",
                        r"\lambda x,",
                        r"y",
                        r")",
                        r"=x^2",
                        r"+3xy\sin\Bigl(\frac{x}{y}\Bigr)",
                        r"-7y^2",
                        r" ")
        eq5p4 = MathTex(r"f(",
                        r"\lambda x,",
                        r"\lambda y",
                        r")",
                        r"=x^2",
                        r"+3xy\sin\Bigl(\frac{x}{y}\Bigr)",
                        r"-7y^2",
                        r" ")
        eq5p5 = MathTex(r"f(",
                        r"\lambda x,",
                        r"\lambda y",
                        r")",
                        r"=(\lambda x)^2",
                        r"+3xy\sin\Bigl(\frac{x}{y}\Bigr)",
                        r"-7y^2",
                        r" ")
        eq5p6 = MathTex(r"f(",
                        r"\lambda x,",
                        r"\lambda y",
                        r")",
                        r"=(\lambda x)^2",
                        r"+3\lambda x\lambda y\sin\Bigl(\frac{\lambda x}{\lambda y}\Bigr)",
                        r"-7y^2",
                        r" ")
        eq5p7 = MathTex(r"f(",
                        r"\lambda x,",
                        r"\lambda y",
                        r")",
                        r"=(\lambda x)^2",
                        r"+3\lambda^2 xy\sin\Bigl(\frac{x}{y}\Bigr)",
                        r"-7y^2",
                        r" ")
        eq5p8 = MathTex(r"f(",
                        r"\lambda x,",
                        r"\lambda y",
                        r")",
                        r"=(\lambda x)^2",
                        r"+3\lambda^2 xy\sin\Bigl(\frac{x}{y}\Bigr)",
                        r"-7(\lambda y)^2",
                        r" ")
        eq5p9 = MathTex(r"f(",
                        r"\lambda x,",
                        r"\lambda y",
                        r")",
                        r"=\lambda^2\Bigl( x^2",
                        r"+3xy\sin\Bigl(\frac{x}{y}\Bigr)",
                        r"-7y^2\Bigr)",
                        r" ")
        eq5p10 = MathTex(r"f(",
                        r"\lambda x,",
                        r"\lambda y",
                        r")",
                        r"=\lambda^2\Bigl( x^2",
                        r"+3xy\sin\Bigl(\frac{x}{y}\Bigr)",
                        r"-7y^2\Bigr)",
                        r"=\lambda^2 f(x,y)")
        self.play(FadeIn(eq5p2[0]), FadeIn(eq5p2[1]), FadeIn(eq5p2[2]), FadeIn(eq5p2[3]))
        self.wait()
        self.play(FadeIn(eq5p2[4]))
        self.wait()
        self.play(FadeIn(eq5p2[5]))
        self.wait()
        self.play(FadeIn(eq5p2[6]))
        self.wait(3)
        self.play(Transform(eq5p2[1], eq5p3[1]))
        self.play(Transform(eq5p2, eq5p3))
        self.wait()
        self.play(Transform(eq5p2[2], eq5p4[2]))
        self.play(Transform(eq5p2, eq5p4))
        self.wait()
        self.play(Transform(eq5p2[4], eq5p5[4]))
        self.play(Transform(eq5p2, eq5p5))
        self.wait(2)
        self.play(Transform(eq5p2[5], eq5p6[5]))
        self.play(Transform(eq5p2, eq5p6))
        self.wait(2)
        self.play(Transform(eq5p2[5], eq5p7[5]))
        self.play(Transform(eq5p2, eq5p7))
        self.wait(2)
        self.play(Transform(eq5p2[6], eq5p8[6]))
        self.play(Transform(eq5p2, eq5p8))
        self.wait(2)
        self.play(Transform(eq5p2, eq5p9))
        self.wait(2)
        self.play(Transform(eq5p2, eq5p10))
        self.wait(3)
        self.play(FadeOut(eq5p2))
        self.wait(2)
        eq6 = MathTex(r"(x,y)\cdot \nabla{f}",
                      r"=x\frac{\partial f}{\partial x}",
                      r"+ y\frac{\partial f}{\partial y}",
                      r"=m\thinspace f(x,y)")
        text = Text("Teorema de Euler de las funciones homogéneas").move_to(DOWN * 2).scale(0.75)
        self.play(FadeIn(eq6[0]))
        self.wait()
        self.play(FadeIn(eq6[1]), FadeIn(eq6[2]))
        self.wait()
        self.play(FadeIn(eq6[3]))
        self.wait()
        self.play(FadeIn(text))
        self.wait(3)
        self.play(FadeOut(eq6), FadeOut(text))
        self.wait(2)
        eq7 = MathTex(r"\frac{d}{d\lambda}\Bigl[\hspace{3.5cm} \Bigr]").move_to(UP * 2 + LEFT * 0.3)
        self.play(FadeIn(eq7))
        self.wait(3)
        eq8 = MathTex(r"\frac{\partial f}{\partial(\lambda x)}",
                      r"\frac{d(\lambda x)}{d\lambda}",
                      r"+ \frac{\partial f}{\partial(\lambda y)}",
                      r"\frac{d(\lambda y)}{d\lambda}",
                      r"=m\lambda^{m-1}",
                      r"f(x,y)")
        self.play(Write(eq8[0]), Write(eq8[1]))
        self.wait(2)
        self.play(Write(eq8[2]), Write(eq8[3]))
        self.wait(2)
        self.play(Write(eq8[4]))
        self.wait(2)
        self.play(Write(eq8[5]))
        self.wait(3)
        eq9 = MathTex(r"\frac{\partial f}{\partial(\lambda x)}",
                      r"x",
                      r"+ \frac{\partial f}{\partial(\lambda y)}",
                      r"\frac{d(\lambda y)}{d\lambda}",
                      r"=m\lambda^{m-1}",
                      r"f(x,y)")
        eq10 = MathTex(r"\frac{\partial f}{\partial(\lambda x)}",
                      r"x",
                      r"+ \frac{\partial f}{\partial(\lambda y)}",
                      r"y",
                      r"=m\lambda^{m-1}",
                      r"f(x,y)")
        self.play(Transform(eq8[1], eq9[1]))
        self.play(Transform(eq8, eq9))
        self.wait()
        self.play(Transform(eq8[3], eq10[3]))
        self.play(Transform(eq8, eq10))
        self.wait(2)
        eq11 = MathTex(r"\frac{\partial f}{\partial x}",
                       r"x",
                       r"+ \frac{\partial f}{\partial(\lambda y)}",
                       r"y",
                       r"=m\lambda^{m-1}",
                       r"f(x,y)")
        self.play(Transform(eq8[0], eq11[0]))
        self.play(Transform(eq8, eq11))
        self.wait(2)
        eq12 = MathTex(r"\frac{\partial f}{\partial x}",
                       r"x",
                       r"+ \frac{\partial f}{\partial y}",
                       r"y",
                       r"=m\lambda^{m-1}",
                       r"f(x,y)")
        self.play(Transform(eq8[2], eq12[2]))
        self.play(Transform(eq8, eq12))
        self.wait(2)
        eq13 = MathTex(r"\frac{\partial f}{\partial x}",
                       r"x",
                       r"+ \frac{\partial f}{\partial y}",
                       r"y",
                       r"=m",
                       r"f(x,y)")
        self.play(Transform(eq8[4], eq13[4]))
        self.play(Transform(eq8, eq13))
        self.wait(2)
        eq14 = MathTex(r"x",
                       r"\frac{\partial f}{\partial x}",
                       r"+ y",
                       r"\frac{\partial f}{\partial y}",
                       r"=m",
                       r"f(x,y)")
        self.play(Transform(eq8, eq14))
        self.wait(3)
        self.play(FadeOut(eq1), FadeOut(eq7))
        self.wait()
        eq15 = MathTex(r"x",
                       r"\frac{\partial f}{\partial x}",
                       r"+ y",
                       r"\frac{\partial f}{\partial y}",
                       r"=0",
                       r"f(x,y)")
        eq16 = MathTex(r"x",
                       r"\frac{\partial f}{\partial x}",
                       r"+ y",
                       r"\frac{\partial f}{\partial y}",
                       r"=0",
                       r" ")
        self.play(Transform(eq8[4], eq15[4]))
        self.wait()
        self.play(Transform(eq8, eq16))
        self.wait()
        eq17 = MathTex(r"x",
                       r"\frac{\partial f}{\partial x}",
                       r"+ y",
                       r"\frac{\partial f}{\partial y}",
                       r"=0",
                       r" ").move_to(UP)
        self.play(Transform(eq8, eq17))
        eq18 = MathTex(r"f(x,y)",
                       r"=F\Bigl(\frac{y}{x}\Bigr)").move_to(DOWN)
        self.wait()
        self.play(FadeIn(eq18[0]))
        self.wait()
        self.play(FadeIn(eq18[1]))
        self.wait(3)
        self.play(FadeOut(eq8), FadeOut(eq18))
        self.wait(2)

        eq19 = MathTex(r"U",
                       r"=f(",
                       r"S",
                       ",",
                       r"V",
                       ",",
                       r"N",
                       r")",
                       r" ")
        self.play(FadeIn(eq19))
        self.wait(3)
        eq20 = MathTex(r"U",
                       r"=f(",
                       r"S",
                       ",",
                       r"V",
                       ",",
                       r"N",
                       r")",
                       r" ")
        eq20[0].set_color(YELLOW)
        self.play(Transform(eq19, eq20))
        self.wait(2)
        eq21 = MathTex(r"U",
                       r"=f(",
                       r"S",
                       ",",
                       r"V",
                       ",",
                       r"N",
                       r")",
                       r" ")
        eq21[2].set_color(YELLOW)
        self.play(Transform(eq19, eq21))
        self.wait(2)
        eq22 = MathTex(r"U",
                       r"=f(",
                       r"S",
                       ",",
                       r"V",
                       ",",
                       r"N",
                       r")",
                       r" ")
        eq22[4].set_color(YELLOW)
        self.play(Transform(eq19, eq22))
        self.wait(2)
        eq23 = MathTex(r"U",
                       r"=f(",
                       r"S",
                       ",",
                       r"V",
                       ",",
                       r"N",
                       r")",
                       r" ")
        eq23[6].set_color(YELLOW)
        self.play(Transform(eq19, eq23))
        self.wait(2)
        eq24 = MathTex(r"U",
                       r"=f(",
                       r"S",
                       ",",
                       r"V",
                       ",",
                       r"N",
                       r")",
                       r" ")
        self.play(Transform(eq19, eq24))
        self.wait(2)
        eq25 = MathTex(r"U",
                       r"=f(",
                       r"\lambda S",
                       ",",
                       r"V",
                       ",",
                       r"N",
                       r")",
                       r" ")
        self.play(Transform(eq19, eq25))
        self.wait()
        eq26 = MathTex(r"U",
                       r"=f(",
                       r"\lambda S",
                       ",",
                       r"\lambda V",
                       ",",
                       r"N",
                       r")",
                       r" ")
        self.play(Transform(eq19, eq26))
        self.wait()
        eq27 = MathTex(r"U",
                       r"=f(",
                       r"\lambda S",
                       ",",
                       r"\lambda V",
                       ",",
                       r"\lambda N",
                       r")",
                       r" ")
        self.play(Transform(eq19, eq27))
        self.wait()
        eq28 = MathTex(r"U",
                       r"=f(",
                       r"\lambda S",
                       ",",
                       r"\lambda V",
                       ",",
                       r"\lambda N",
                       r")",
                       r"=\lambda f(S,V,N)")
        self.play(Transform(eq19, eq28), run_time=1.5)
        self.wait(3)
        eq29 = MathTex(r"U",
                       r"=f(",
                       r"\lambda S",
                       ",",
                       r"\lambda V",
                       ",",
                       r"\lambda N",
                       r")",
                       r"=\lambda f(S,V,N)").move_to(UP)
        self.play(Transform(eq19, eq29))
        self.wait()
        eq30 = MathTex(r"S",
                       r"\frac{\partial f}{\partial S}",
                       r"+V",
                       r"\frac{\partial f}{\partial V}",
                       r"+N",
                       r"\frac{\partial f}{\partial N}",
                       r"=U").move_to(DOWN)
        self.play(FadeIn(eq30[0]), FadeIn(eq30[1]))
        self.wait()
        self.play(FadeIn(eq30[2]), FadeIn(eq30[3]))
        self.wait()
        self.play(FadeIn(eq30[4]), FadeIn(eq30[5]))
        self.wait()
        self.play(FadeIn(eq30[6]))
        self.wait(2)
        eq31 = MathTex(r"S",
                       r"\frac{\partial U}{\partial S}",
                       r"+V",
                       r"\frac{\partial f}{\partial V}",
                       r"+N",
                       r"\frac{\partial f}{\partial N}",
                       r"=U").move_to(DOWN)
        self.play(Transform(eq30, eq31))
        self.wait()
        eq32 = MathTex(r"S",
                       r"\frac{\partial U}{\partial S}",
                       r"+V",
                       r"\frac{\partial U}{\partial V}",
                       r"+N",
                       r"\frac{\partial f}{\partial N}",
                       r"=U").move_to(DOWN)
        self.play(Transform(eq30, eq32))
        self.wait()
        eq33 = MathTex(r"S",
                       r"\frac{\partial U}{\partial S}",
                       r"+V",
                       r"\frac{\partial U}{\partial V}",
                       r"+N",
                       r"\frac{\partial U}{\partial N}",
                       r"=U").move_to(DOWN)
        self.play(Transform(eq30, eq33))
        self.wait()
        eq34 = MathTex(r"S",
                       r"\frac{\partial U}{\partial S}",
                       r"+V",
                       r"\frac{\partial U}{\partial V}",
                       r"+N",
                       r"\frac{\partial U}{\partial N}",
                       r"=U").move_to(DOWN)
        eq34[1].set_color(YELLOW)
        self.play(Transform(eq30, eq34))
        self.wait()
        eq35 = MathTex(r"S",
                       r"T",
                       r"+V",
                       r"\frac{\partial U}{\partial V}",
                       r"+N",
                       r"\frac{\partial U}{\partial N}",
                       r"=U").move_to(DOWN)
        eq35[1].set_color(YELLOW)
        self.play(Transform(eq30, eq35))
        self.wait(2)
        eq36 = MathTex(r"S",
                       r"T",
                       r"+V",
                       r"\frac{\partial U}{\partial V}",
                       r"+N",
                       r"\frac{\partial U}{\partial N}",
                       r"=U").move_to(DOWN)
        eq36[3].set_color(YELLOW)
        self.play(Transform(eq30, eq36))
        self.wait()
        eq37 = MathTex(r"S",
                       r"T",
                       r"+V",
                       r"(-P)",
                       r"+N",
                       r"\frac{\partial U}{\partial N}",
                       r"=U").move_to(DOWN)
        eq37[3].set_color(YELLOW)
        self.play(Transform(eq30, eq37))
        self.wait(2)
        eq38 = MathTex(r"S",
                       r"T",
                       r"+V",
                       r"(-P)",
                       r"+N",
                       r"\frac{\partial U}{\partial N}",
                       r"=U").move_to(DOWN)
        eq38[5].set_color(YELLOW)
        self.play(Transform(eq30, eq38))
        self.wait()
        eq39 = MathTex(r"S",
                       r"T",
                       r"+V",
                       r"(-P)",
                       r"+N",
                       r"\mu",
                       r"=U").move_to(DOWN)
        eq39[5].set_color(YELLOW)
        self.play(Transform(eq30, eq39))
        self.wait(2)
        eq40 = MathTex(r"S",
                       r"T",
                       r"+V",
                       r"(-P)",
                       r"+N",
                       r"\mu",
                       r"=U").move_to(DOWN)
        self.play(Transform(eq30, eq40))
        self.wait()
        eq41 = MathTex(r"U=",
                       r"S",
                       r"T",
                       r"-P",
                       r"V",
                       r"+\mu",
                       r"N").move_to(DOWN)
        self.play(Transform(eq30, eq41))
        self.wait(3)
        self.play(FadeOut(eq30), FadeOut(eq19))
        self.wait()

class Nocursiva(Scene):
    def construct(self):
        eq3 = MathTex(r"\frac{df}{dt}=\nabla{f}\cdot \vec{v}", r"=0",
                      r"\Longrightarrow f=cte").move_to(DOWN)
        texto3 = MathTex(r"\text{Si} \hspace{0.15cm} \nabla{f} \perp \vec{v}:").move_to(UP)
        self.wait()
        self.play(FadeIn(texto3))
        self.wait()
        self.play(FadeIn(eq3[0]))
        self.wait()
        self.play(FadeIn(eq3[1]))
        self.wait()
        self.play(FadeIn(eq3[2]))
        self.wait(2)
        self.play(FadeOut(texto3), FadeOut(eq3))
        eq4 = MathTex(r"\frac{\partial f}{\partial x}=0",
                      r"\Leftrightarrow \text{Curvas de nivel:}\hspace{0.15cm} y = cte,"
                      r"\hspace{0.15cm} \forall x",
                      r"\Leftrightarrow f(y)")
        self.wait()
        self.play(FadeIn(eq4[0]))
        self.wait()
        self.play(FadeIn(eq4[1]))
        self.wait()
        self.play(FadeIn(eq4[2]))
        self.wait(2)
        self.play(FadeOut(eq4))
        self.wait(2)

class Intro3(Scene):
    def construct(self):
        # Presentación del vídeo
        title = Text("Interpretación geométrica de una EDP").move_to(UP * 2)
        self.wait(1)
        self.play(FadeIn(title))
        eq1 = MathTex(r"(1) \hspace{0.3cm}a\frac{\partial f}{\partial x}+"
                      r"b\frac{\partial f}{\partial y}=0").move_to(DOWN + LEFT * 3)
        eq2 = MathTex(r"(2) \hspace{0.3cm}y\frac{\partial f}{\partial x}-"
                      r"x\frac{\partial f}{\partial y}=0").move_to(DOWN + RIGHT * 3)
        eq3 = MathTex(r"(3) \hspace{0.3cm}x\frac{\partial f}{\partial x}+"
                      r"y\frac{\partial f}{\partial y}=0").move_to(DOWN)
        self.wait(2)
        self.play(FadeIn(eq1), FadeIn(eq2))
        self.wait(3)
        self.play(FadeOut(eq1), FadeOut(eq2))
        self.play(FadeIn(eq3))
        self.wait(3)
        self.play(FadeOut(eq3), FadeOut(title))
        self.wait(2)

        # Migstemáticas
        mw = ImageMobject("5MW.png").scale(0.25).move_to(np.array([0, 1, 0]))
        label = Text("Migstemáticas").move_to(np.array([0, -2, 0]))
        self.play(FadeIn(mw), Write(label))
        self.wait(3)
        self.play(FadeOut(mw), FadeOut(label))
        self.wait(2)