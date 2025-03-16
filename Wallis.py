from manim import *

class Presentacion(Scene):
    def construct(self):
        fondo = "#E9FFC7"
        rojo = "#FF0800"
        self.camera.background_color = fondo
        self.wait(2)

        # Título
        titulo = Tex(r"\underline{Fórmula de Wallis para integrales trigonométricas}").set_color(BLACK).move_to(UP*3)
        self.play(FadeIn(titulo))
        self.wait(2)

        # John Wallis
        wallis = ImageMobject("Wallis.png").scale(0.6).move_to(RIGHT*2.75+DOWN*0.35)
        etiqueta_wallis = Tex("John Wallis (1616-1703)").set_color(BLACK).scale(0.75).move_to(RIGHT*2.75 + DOWN*3.35)
        self.play(FadeIn(wallis), Write(etiqueta_wallis))
        self.wait(2)

        # Integrales
        eq_sen = MathTex(r"\int_0^{\frac{\pi}{2}}\sin^{\thinspace n}x\thinspace dx").set_color(BLACK).move_to(LEFT*3.75 + UP*0.5)
        eq_cos = MathTex(r"\int_0^{\frac{\pi}{2}}\cos^{\thinspace n}x\thinspace dx").set_color(BLACK).move_to(LEFT*3.75 + DOWN*1.5)
        self.play(Write(eq_sen), Write(eq_cos))
        self.wait(2)
        self.play(FadeOut(wallis), FadeOut(etiqueta_wallis))
        self.wait()

        # Stephen Wolfram
        wolfram1 = ImageMobject("Wolfram1.png").scale(0.6).move_to(RIGHT*2.75+DOWN*0.5)
        wolfram2 = ImageMobject("Wolfram2.png").scale(0.6).move_to(RIGHT*2.75+DOWN*0.5)
        wolfram3 = ImageMobject("Wolfram3.png").scale(0.6).move_to(RIGHT*2.75+DOWN*0.5)
        wolfram4 = ImageMobject("Wolfram4.png").scale(0.6).move_to(RIGHT*2.75+DOWN*0.5)
        wolfram1p2 = ImageMobject("Wolfram1.png").scale(0.6).move_to(RIGHT*2.75+DOWN*0.5)
        self.play(FadeIn(wolfram1))
        self.wait(2)
        self.play(Transform(wolfram1,wolfram2))
        self.wait(3)
        self.play(Transform(wolfram1,wolfram1p2))
        self.wait(2)
        self.play(Transform(wolfram1,wolfram3))
        self.play(Transform(wolfram1,wolfram4))
        self.play(Transform(wolfram1,wolfram3))
        self.play(Transform(wolfram1,wolfram4))
        self.play(Transform(wolfram1,wolfram3))
        self.play(Transform(wolfram1,wolfram1p2))
        self.wait()
        self.play(FadeOut(wolfram1))
        self.wait(3)

        # Elipse
        ax = Axes(x_range=[-7, 7, 1], y_range=[-6, 6, 1], axis_config={'tip_shape': StealthTip}, x_length=9,
        x_axis_config={'include_ticks': False}, y_axis_config={'include_ticks': False})
        ax.set_color(BLACK)
        ejex = MathTex(r'x',color=BLACK).move_to(ax.coords_to_point(6,-0.5))
        ejey = MathTex(r'y',color=BLACK).move_to(ax.coords_to_point(-0.5,4.8))
        eq_elipse = MathTex(r'\frac{x^2}{a^2}+\frac{y^2}{b^2}=1', color=BLACK).move_to(DOWN*5+RIGHT*0.2).scale(1.75)
        #curva_elipse = ParametricFunction(lambda t: np.array([1.75*np.sqrt(2)*np.cos(t), 1.75*np.sin(t), 0]),
                                       #color=rojo, t_range=np.array([0,2*np.pi,0.01]))
        a = 2.75*np.sqrt(2)
        b = 2.75
        curva_elipse1 = ax.plot(lambda x: b*np.sqrt(1-(x/a)**2), x_range=[-a,a], color=rojo)
        curva_elipse2 = ax.plot(lambda x: -b*np.sqrt(1-(x/a)**2), x_range=[-a,a], color=rojo)
        elipse = Group(ax,ejex,ejey,eq_elipse,curva_elipse1, curva_elipse2).move_to(RIGHT*2.5+DOWN*0.75).scale(0.5)
        area = ax.get_area(curva_elipse2, [-a, a], bounded_graph=curva_elipse1, color=rojo, opacity=0.5)
        self.play(FadeIn(elipse))
        self.wait(2)
        self.play(FadeIn(area))
        self.wait(2)
        self.play(FadeOut(elipse), FadeOut(area))
        self.wait()

        # Armónicos esféricos
        eq_arm = MathTex(r"Y_l^{-l}=C_l\sin^{\thinspace l}\theta e^{-il\phi}").set_color(BLACK).move_to(RIGHT*3+UP*0.5)
        eq_norm = MathTex(r"\int d\Omega |Y_l^{-l}|^2=1").set_color(BLACK).move_to(RIGHT*3+DOWN*1.5)
        flecha = Arrow(start=RIGHT*2.65+UP*2,end=RIGHT*2.65+UP*0.75,color=rojo)
        self.play(Write(eq_arm), Write(eq_norm))
        self.wait()
        self.play(Write(flecha))
        self.wait()
        self.play(FadeOut(eq_arm), FadeOut(eq_norm),FadeOut(flecha), FadeOut(eq_sen), FadeOut(eq_cos), FadeOut(titulo))
        self.wait()


class Logo(Scene):
    def construct(self):
        fondo = "#E9FFC7"
        self.camera.background_color = fondo

        # Logo Migstemáticas
        mw1 = ImageMobject("5MW-Verde.png").move_to(np.array([0, 8, 0])).scale(0.85)
        mw2 = ImageMobject("5MW-Verde.png").move_to(np.array([0, 1, 0])).scale(0.85)
        label1 = Text("Migstemáticas").move_to(np.array([0, -8, 0])).set_color(BLACK)
        label2 = Text("Migstemáticas").move_to(np.array([0, -2, 0])).set_color(BLACK)
        self.add(mw1, label1)
        self.wait(2)
        self.play(Transform(mw1, mw2), Transform(label1, label2), run_time=0.5)
        self.wait(3)
        self.play(FadeOut(mw1), FadeOut(label1))
        self.wait(2)


class Desarrollo(Scene):
    def construct(self):
        fondo = "#E9FFC7"
        self.camera.background_color = fondo
        rojo = "#FF0800"

        # n par
        eq_sen1_par = MathTex(r"\int_0^{\frac{\pi}{2}}\sin^{\thinspace n}x\thinspace dx").set_color(BLACK).move_to(UP+LEFT*3.5).scale(0.75)
        eq_cos1_par = MathTex(r"\int_0^{\frac{\pi}{2}}\cos^{\thinspace n}x\thinspace dx").set_color(BLACK).move_to(DOWN+LEFT*3.5).scale(0.75)
        eq_cos2_par = MathTex(r"\int_0^{\frac{\pi}{2}}\cos^{\thinspace n}x\thinspace dx").set_color(BLACK).move_to(UP+LEFT*0.9).scale(0.75)
        eq_ig1_par = MathTex(r"=").set_color(BLACK).move_to(UP+LEFT*2.15).scale(0.75)
        eq_nat = MathTex(r"n\in\mathbb{N}").set_color(BLACK)
        texto_par = MathTex(r"n \text{ par}").set_color(BLACK).scale(0.75).move_to(UP*2.5+RIGHT*0.4)
        eq_par = MathTex(r"=",
                         r"\frac{n-1}{n}\frac{n-3}{n-2}\cdots\frac{3}{4}\frac{1}{2}",
                         r"\frac{\pi}{2}").set_color(BLACK).move_to(UP+RIGHT*2.15).scale(0.75)
        eq_par2 = MathTex(r"=",
                         r"\frac{(n-1)!!}{n!!}",
                         r"\frac{\pi}{2}").set_color(BLACK).move_to(UP+RIGHT*2.15).scale(0.75)
        flecha1_par = Arrow(start=RIGHT*0.435+UP*1.05,end=RIGHT*0.435+UP*2.45).set_color(rojo)
        flecha2_par = Arrow(start=RIGHT*1.22+UP*1.05,end=RIGHT*1.22+UP*2.45).set_color(rojo)
        eq_sen2_par = MathTex(r"\int_0^{\frac{\pi}{2}}\sin^{\thinspace n}x\thinspace dx").set_color(BLACK).move_to(UP+LEFT*2.75).scale(0.75)
        eq_cos3_par = MathTex(r"\int_0^{\frac{\pi}{2}}\cos^{\thinspace n}x\thinspace dx").set_color(BLACK).move_to(UP+LEFT*0.15).scale(0.75)
        eq_ig2_par = MathTex(r"=").set_color(BLACK).move_to(UP+LEFT*1.4).scale(0.75)
        texto_par2 = MathTex(r"n \text{ par}").set_color(BLACK).scale(0.75).move_to(UP*2.5+RIGHT*1.2)
        self.wait(2)
        self.play(Write(eq_sen1_par), Write(eq_cos1_par))
        self.wait(2)
        self.play(Write(eq_nat))
        self.wait(2)
        self.play(FadeOut(eq_nat),Write(eq_ig1_par),Transform(eq_cos1_par,eq_cos2_par), run_time=2)
        self.wait(3)
        self.play(Write(texto_par), Write(flecha1_par), Write(eq_par[0]))
        self.wait(2)
        self.play(Write(eq_par[1]))
        self.wait(2)
        self.play(Write(eq_par[2]))
        self.wait(2)
        self.play(Transform(eq_par[1],eq_par2[1]))
        self.play(Transform(eq_par,eq_par2), Transform(eq_sen1_par,eq_sen2_par), Transform(flecha1_par,flecha2_par),
                  Transform(eq_ig1_par,eq_ig2_par), Transform(eq_cos1_par,eq_cos3_par), Transform(texto_par,texto_par2))
        self.wait(2)

        # n impar
        eq_sen1_impar = MathTex(r"\int_0^{\frac{\pi}{2}}\sin^{\thinspace n}x\thinspace dx").set_color(BLACK).move_to(DOWN+LEFT*3.5).scale(0.75)
        eq_cos1_impar = MathTex(r"\int_0^{\frac{\pi}{2}}\cos^{\thinspace n}x\thinspace dx").set_color(BLACK).move_to(DOWN+LEFT*0.9).scale(0.75)
        eq_ig1_impar = MathTex(r"=").set_color(BLACK).move_to(DOWN+LEFT*2.15).scale(0.75)
        texto_impar = MathTex(r"n \text{ impar}").set_color(BLACK).scale(0.75).move_to(DOWN*2.5+RIGHT*0.4)
        eq_impar = MathTex(r"=",
                         r"\frac{n-1}{n}\frac{n-3}{n-2}\cdots\frac{4}{5}\frac{2}{3}").set_color(BLACK).move_to(DOWN+RIGHT*2).scale(0.75)
        eq_impar2 = MathTex(r"=",
                         r"\frac{(n-1)!!}{n!!}").set_color(BLACK).move_to(DOWN+RIGHT*2).scale(0.75)
        flecha1_impar = Arrow(start=RIGHT*0.435+DOWN*1.05,end=RIGHT*0.435+DOWN*2.45).set_color(rojo)
        flecha2_impar = Arrow(start=RIGHT*1.22+DOWN*1.05,end=RIGHT*1.22+DOWN*2.45).set_color(rojo)
        eq_sen2_impar = MathTex(r"\int_0^{\frac{\pi}{2}}\sin^{\thinspace n}x\thinspace dx").set_color(BLACK).move_to(DOWN+LEFT*2.75).scale(0.75)
        eq_cos2_impar = MathTex(r"\int_0^{\frac{\pi}{2}}\cos^{\thinspace n}x\thinspace dx").set_color(BLACK).move_to(DOWN+LEFT*0.15).scale(0.75)
        eq_ig2_impar = MathTex(r"=").set_color(BLACK).move_to(DOWN+LEFT*1.4).scale(0.75)
        texto_impar2 = MathTex(r"n \text{ impar}").set_color(BLACK).scale(0.75).move_to(DOWN*2.5+RIGHT*1.2)
        self.wait(2)
        self.play(Write(eq_sen1_impar), Write(eq_cos1_impar), Write(eq_ig1_impar))
        self.wait(2)
        self.play(Write(texto_impar), Write(flecha1_impar), Write(eq_impar[0]))
        self.wait(2)
        self.play(Write(eq_impar[1]))
        self.wait(2)
        self.play(Transform(eq_impar[1],eq_impar2[1]))
        self.play(Transform(eq_impar,eq_impar2), Transform(eq_sen1_impar,eq_sen2_impar), Transform(flecha1_impar,flecha2_impar),
                  Transform(eq_ig1_impar,eq_ig2_impar), Transform(eq_cos1_impar,eq_cos2_impar), Transform(texto_impar,texto_impar2))
        self.wait(2)

        # Fórmula de Wallis
        wallis1 = Group(eq_sen1_par, eq_cos1_par, eq_ig1_par, eq_par, flecha1_par, texto_par,
                       eq_sen1_impar, eq_cos1_impar, eq_ig1_impar, eq_impar, flecha1_impar, texto_impar)
        wallis2 = wallis1.copy().scale(0.5).move_to(LEFT*4+UP*1.5)
        cuadro = Rectangle(color=BLACK, height=3, width=4.25).move_to(LEFT*4+UP*1.5)
        texto_wallis = Tex("Integrales de Wallis").set_color(BLACK).move_to(LEFT*4+DOWN*0.3).scale(0.75)
        self.play(Transform(wallis1, wallis2))
        self.play(Write(cuadro))
        self.play(Write(texto_wallis))
        self.wait(3)
        
        # Ejemplo 1
        ejemplo1p1 = MathTex(r"\int_0^{\frac{\pi}{2}}\sin^{\thinspace 4}x\thinspace dx",
                             r"=\frac{(n-1)!!}{n!!}",
                             r"\frac{\pi}{2}").set_color(BLACK).scale(0.75).move_to(RIGHT*2+DOWN)
        ejemplo1p2 = MathTex(r"\int_0^{\frac{\pi}{2}}\sin^{\thinspace 4}x\thinspace dx",
                             r"=\frac{(4-1)!!}{4!!}",
                             r"\frac{\pi}{2}").set_color(BLACK).scale(0.75).move_to(RIGHT*2+DOWN)
        ejemplo1p3 = MathTex(r"\int_0^{\frac{\pi}{2}}\sin^{\thinspace 4}x\thinspace dx",
                             r"=\frac{3\cdot 1}{4\cdot 2}",
                             r"\frac{\pi}{2}").set_color(BLACK).scale(0.75).move_to(RIGHT*2+DOWN)
        ejemplo1p4 = MathTex(r"\int_0^{\frac{\pi}{2}}\sin^{\thinspace 4}x\thinspace dx",
                             r"=\frac{3\pi}{16}",
                             r" ").set_color(BLACK).scale(0.75).move_to(RIGHT*2+DOWN)
        self.play(Write(ejemplo1p1[0]))
        self.wait()
        self.play(Write(ejemplo1p1[1]), Write(ejemplo1p1[2]))
        self.wait(2)
        self.play(Transform(ejemplo1p1,ejemplo1p2))
        self.wait()
        self.play(Transform(ejemplo1p1,ejemplo1p3))
        self.wait()
        self.play(Transform(ejemplo1p1,ejemplo1p4))
        self.wait(3)
        self.play(FadeOut(ejemplo1p1))
        self.wait(2)

        # Ejemplo 2
        ejemplo2p1 = MathTex(r"\int_0^{2\pi}\sin^{\thinspace 4}x\thinspace dx").set_color(BLACK).scale(0.75).move_to(RIGHT*2+DOWN)
        ejemplo2p2 = MathTex(r"\int_0^{2\pi}\sin^{\thinspace 4}x\thinspace dx").set_color(BLACK).scale(0.75).move_to(LEFT*4+DOWN*2.1)
        ejemplo2p3 = MathTex(r"\int_0^{2\pi}\sin^{\thinspace 4}x\thinspace dx").set_color(BLACK).scale(0.75).move_to(LEFT*4+DOWN*2.1)
        ejemplo2p3.set_color(rojo)
        ejemplo1p1 = MathTex(r"\int_0^{\frac{\pi}{2}}\sin^{\thinspace 4}x\thinspace dx",).set_color(PURE_BLUE).scale(0.75).move_to(RIGHT*3+DOWN*2.1)
        ejemplo1p2 = MathTex(r"\int_{\frac{\pi}{2}}^{\pi}\sin^{\thinspace 4}x\thinspace dx",).set_color(PURE_BLUE).scale(0.75).move_to(RIGHT*3+DOWN*2.1)
        ejemplo1p3 = MathTex(r"\int_{\pi}^{\frac{3\pi}{2}}\sin^{\thinspace 4}x\thinspace dx",).set_color(PURE_BLUE).scale(0.75).move_to(RIGHT*3+DOWN*2.1)
        ejemplo1p4 = MathTex(r"\int_{\frac{3\pi}{2}}^{2\pi}\sin^{\thinspace 4}x\thinspace dx",).set_color(PURE_BLUE).scale(0.75).move_to(RIGHT*3+DOWN*2.1)
        circulo = Circle(radius=0.2,color=rojo).move_to(RIGHT*1.43+DOWN*0.64)
        self.play(Write(ejemplo2p1))
        self.wait()
        self.play(Write(circulo))
        self.wait(2)
        self.play(Transform(ejemplo2p1,ejemplo2p2), FadeOut(circulo))
        self.wait()
        ax = Axes(
            x_range=[0, 2*PI, PI/2],
            y_range=[-1, 1, 0.5],
            axis_config={'tip_shape': StealthTip}
        ).scale(0.6).move_to(RIGHT*2.5+UP*1)
        ax.set_color(BLACK)
        p1 = MathTex(r"\frac{\pi}{2}").scale(0.5).set_color(BLACK).move_to(ax.coords_to_point(PI/2,-0.22))
        p2 = MathTex(r"\pi").scale(0.5).set_color(BLACK).move_to(ax.coords_to_point(PI,-0.18))
        p3 = MathTex(r"\frac{3\pi}{2}").scale(0.5).set_color(BLACK).move_to(ax.coords_to_point(1.5*PI,-0.22))
        p4 = MathTex(r"0.5").scale(0.5).set_color(BLACK).move_to(ax.coords_to_point(-0.32,0.5))
        p5 = MathTex(r"-0.5").scale(0.5).set_color(BLACK).move_to(ax.coords_to_point(-0.38,-0.5))
        p6 = MathTex(r"-1").scale(0.5).set_color(BLACK).move_to(ax.coords_to_point(-0.38,-1))
        curva_sen = ax.plot(lambda x: np.sin(x)**4, x_range=[0, 2*PI], color=GREY)
        eje_x = MathTex(r"x").scale(0.75).set_color(BLACK).move_to(ax.coords_to_point(2*PI-0.4,-0.1))
        eje_y = MathTex(r"y").scale(0.75).set_color(BLACK).move_to(ax.coords_to_point(0.3,1))
        area = ax.get_area(curva_sen, x_range=(0, 2*PI), color=rojo, opacity=0.5)
        area1 = ax.get_area(curva_sen, x_range=(0, PI/2), color=PURE_BLUE, opacity=0.5)
        self.play(Write(ax), Write(curva_sen), Write(eje_x), Write(eje_y), Write(p1), Write(p2), Write(p3), Write(p4),
                  Write(p5), Write(p6))
        self.wait(2)
        self.play(FadeIn(area), Transform(ejemplo2p1, ejemplo2p3))
        self.wait(3)
        self.play(FadeOut(area), Transform(ejemplo2p1, ejemplo2p2))
        self.play(FadeIn(area1), Write(ejemplo1p1))
        self.wait()
        self.play(Rotate(area1, axis=np.array([0,1,0]), angle=PI, rate_func=smoothererstep))
        area2 = area1.copy().move_to(ax.coords_to_point(0.75*PI,0.5))
        self.play(Transform(area1,area2), Transform(ejemplo1p1, ejemplo1p2))
        self.wait(2)
        self.play(Rotate(area1, axis=np.array([0,1,0]), angle=PI, rate_func=smoothererstep))
        area3 = area1.copy().move_to(ax.coords_to_point(1.25*PI,0.5))
        self.play(Transform(area1,area3), Transform(ejemplo1p1, ejemplo1p3))
        self.wait(2)
        self.play(Rotate(area1, axis=np.array([0,1,0]), angle=PI, rate_func=smoothererstep))
        area4 = area1.copy().move_to(ax.coords_to_point(1.75*PI,0.5))
        self.play(Transform(area1,area4), Transform(ejemplo1p1, ejemplo1p4))
        self.wait(2)
        self.play(FadeOut(area1), FadeOut(ejemplo1p1))
        self.wait(2)
        ejemplo2p4 = MathTex(r"=",
                             r"4",
                             r"\int_0^{\frac{\pi}{2}}\sin^{\thinspace 4}x\thinspace dx",
                             r"=",
                             r"4",
                             r"\frac{3\pi}{16}",
                             r"=\frac{3\pi}{4}").set_color(BLACK).scale(0.75).move_to(LEFT*0.3+DOWN*2.1)
        ejemplo2p4[2].set_color(PURE_BLUE)
        ejemplo2p4[5].set_color(PURE_BLUE)
        self.play(FadeIn(area), Transform(ejemplo2p1, ejemplo2p3))
        self.wait()
        self.play(Write(ejemplo2p4[0]), Write(ejemplo2p4[1]))
        self.wait(2)
        area1 = ax.get_area(curva_sen, x_range=(0, PI/2), color=PURE_BLUE, opacity=0.5)
        self.play(FadeIn(area1), Write(ejemplo2p4[2]))
        self.wait(2)
        self.play(Write(ejemplo2p4[3:6]))
        self.wait(2)
        self.play(Write(ejemplo2p4[6]))
        self.wait(3)
        self.play(FadeOut(area), FadeOut(area1), FadeOut(ejemplo2p1), FadeOut(ejemplo2p4), FadeOut(curva_sen))
        self.wait(2)

        # Ejemplo3
        ejemplo3p1 = MathTex(r"\int_0^{2\pi}\sin^{\thinspace 3}x\thinspace dx").set_color(BLACK).scale(0.75).move_to(LEFT*4+DOWN*2.1)
        ejemplo3p2 = MathTex(r"\int_0^{2\pi}\sin^{\thinspace 3}x\thinspace dx").set_color(rojo).scale(0.75).move_to(LEFT*4+DOWN*2.1)
        ejemplo3p3 = MathTex(r"\int_0^{2\pi}\sin^{\thinspace 3}x\thinspace dx").set_color(BLACK).scale(0.75).move_to(LEFT*4+DOWN*2.1)
        ejemplo3cero = MathTex(r"=0").set_color(BLACK).scale(0.75).move_to(LEFT*2.5+DOWN*2.1)
        ejemplo3aux1 = MathTex(r"\int_0^{\pi}\sin^{\thinspace 3}x\thinspace dx",
                               r"=",
                               r"-\int_{\pi}^{2\pi}\sin^{\thinspace 3}x\thinspace dx").set_color(BLACK).scale(0.75).move_to(RIGHT*2+DOWN*2.1)
        ejemplo3aux1[0].set_color(PURE_BLUE)
        ejemplo3aux1[2].set_color(rojo)
        curva_sen = ax.plot(lambda x: np.sin(x)**3, x_range=[0, 2*PI], color=GREY)
        area = ax.get_area(curva_sen, x_range=(0, 2*PI), color=rojo, opacity=0.5)
        area1 = ax.get_area(curva_sen, x_range=(0, PI), color=PURE_BLUE, opacity=0.5)
        area2 = ax.get_area(curva_sen, x_range=(PI, 2*PI), color=rojo, opacity=0.5)
        self.play(Write(ejemplo3p1))
        self.play(Write(curva_sen), run_time=1.5)
        self.wait()
        self.play(Transform(ejemplo3p1, ejemplo3p2), FadeIn(area))
        self.wait(3)
        self.play(FadeOut(area), Transform(ejemplo3p1, ejemplo3p3))
        self.wait()
        self.play(FadeIn(area1), Write(ejemplo3aux1[0]))
        self.wait(2)
        self.play(Rotate(area1, axis=np.array([1,0,0]), angle=PI, rate_func=smoothererstep))
        area1aux = area1.copy().move_to(ax.coords_to_point(1.5*PI,-0.5))
        self.play(Transform(area1, area1aux))
        self.play(Transform(area1, area2))
        self.play(Write(ejemplo3aux1[1:]))
        self.wait(2)
        self.play(Write(ejemplo3cero))
        self.wait(2)
        self.play(FadeOut(ejemplo3p1), FadeOut(ejemplo3cero), FadeOut(ejemplo3aux1), FadeOut(ax), FadeOut(curva_sen), FadeOut(eje_x),
                  FadeOut(p1), FadeOut(p2), FadeOut(p3), FadeOut(p4), FadeOut(p5), FadeOut(p6), FadeOut(wallis1), FadeOut(cuadro),
                  FadeOut(texto_wallis), FadeOut(eje_y), FadeOut(area1))
        self.wait(2)

        # Conclusión
        eq_final1 = MathTex(r"\int_0^{\frac{\pi}{2}}\sin^{\thinspace m}x\thinspace\cos^{\thinspace n}x\thinspace dx"
                           ).set_color(BLACK).move_to(UP*1.5)
        eq_final2 = MathTex(r"\int_0^1x^m(1-x)^n\thinspace dx"
                           ).set_color(BLACK).move_to(DOWN*1.5)
        self.play(Write(eq_final1))
        self.wait(2)
        self.play(Write(eq_final2))
        self.wait(3)
        self.play(FadeOut(eq_final1), FadeOut(eq_final2))
        self.wait()        


class Agradecimientos(Scene):
    def construct(self):
        fondo = "#E9FFC7"
        self.camera.background_color = fondo
        title = Text("Agradecimientos:").move_to(UP * 2.5).set_color(BLACK)
        self.wait(1)
        self.play(FadeIn(title))
        text1 = Text("David Saavedra Pastor").move_to(UP).scale(0.75).set_color(BLACK)
        text2 = Text("Daniel Martínez Lizán").scale(0.75).set_color(BLACK)
        self.wait(2)
        self.play(FadeIn(text1))
        self.wait()
        self.play(FadeIn(text2))
        self.wait()
        self.wait(3)
        self.play(FadeOut(title), FadeOut(text1), FadeOut(text2))
        self.wait()