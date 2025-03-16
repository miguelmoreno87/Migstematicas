from manim import *


class Hiperbola(Scene):
    def construct(self):
        fondo = "#D1EDF2"
        rojo = "#FF0800"
        self.camera.background_color = fondo
        self.wait(2)

        ax = Axes(x_range=[-7, 7, 1], y_range=[-6, 6, 1], axis_config={'tip_shape': StealthTip}, x_length=9,
        x_axis_config={'include_ticks': False}, y_axis_config={'include_ticks': False})
        ax.set_color(BLACK)
        ejex = MathTex(r'x',color=GRAY).move_to(ax.coords_to_point(6,-0.5))
        ejey = MathTex(r'y',color=GRAY).move_to(ax.coords_to_point(-0.5,4.8))
        self.play(Write(ax), Write(ejex), Write(ejey), run_time=3)
        self.wait(2)

        eq1 = MathTex(r'y=\frac{1}{x}', color=BLACK).move_to(UP*2 + RIGHT*2.5)
        curva1 = ax.plot(lambda x: 1/x, color=rojo, x_range=[-6, -1/6])
        curva2 = ax.plot(lambda x: 1/x, color=rojo, x_range=[1/5, 6])
        texto1 = MathTex(r'\text{¿Hipérbola?}', color=BLACK).move_to(LEFT*3 + UP*2)
        self.play(Write(curva1), Write(eq1), Write(curva2), Write(texto1), run_time=2)
        self.wait(3)
        self.play(FadeOut(curva1), FadeOut(curva2), FadeOut(eq1), FadeOut(texto1))
        self.wait()

        eq2 = MathTex(r'\frac{x^2}{a^2}-\frac{y^2}{b^2}=1', color=BLACK).move_to(RIGHT*4.5 + UP*2)
        self.play(Write(eq2))
        self.wait(2)
        hiperbola1 = ParametricFunction(lambda t: np.array([np.sqrt(2)*np.cosh(t), np.sqrt(2)*np.sinh(t), 0]),
                                       color=rojo, t_range=np.array([-1.3,1.3,0.01]))
        hiperbola2 = ParametricFunction(lambda t: np.array([-np.sqrt(2)*np.cosh(t), np.sqrt(2)*np.sinh(t), 0]),
                                       color=rojo, t_range=np.array([-1.3,1.3,0.01]))
        self.play(Write(hiperbola1), Write(hiperbola2))
        self.wait(3)
        self.play(FadeOut(eq2))
        self.wait(2)
        self.play(Rotate(hiperbola1, angle=PI/4, about_point=ORIGIN, rate_func=smoothererstep),
                  Rotate(hiperbola2, angle=PI/4, about_point=ORIGIN, rate_func=smoothererstep), run_time=2)
        self.wait(2)
        self.play(FadeIn(eq1))
        self.wait(2)
        self.play(FadeOut(hiperbola1), FadeOut(hiperbola2), FadeOut(eq1), FadeOut(ejex), FadeOut(ejey), FadeOut(ax))
        self.wait(3)

        # Logo Migstemáticas
        mw = ImageMobject("5MW-Cian.png").scale(0.6).move_to(np.array([0, 1, 0])).scale(0.85)
        label = Text("Migstemáticas").move_to(np.array([0, -2, 0])).set_color(BLACK)
        self.play(FadeIn(mw), Write(label))
        self.wait(3)
        self.play(FadeOut(mw), FadeOut(label))
        self.wait(3)

class Deduccion(Scene):
    def construct(self):
        fondo = "#D1EDF2"
        rojo = "#FF0800"
        self.camera.background_color = fondo
        self.wait()

        # Rotación de los ejes. Desaparecen ejes antiguos y aparecen ejes nuevos.
        ax = Axes(x_range=[-7, 7, 1], y_range=[-6, 6, 1], axis_config={'tip_shape': StealthTip}, x_length=9,
        x_axis_config={'include_ticks': False}, y_axis_config={'include_ticks': False})
        ax.set_color(BLACK)
        ejex = MathTex(r'x',color=GRAY).move_to(ax.coords_to_point(6,-0.5))
        ejey = MathTex(r'y',color=GRAY).move_to(ax.coords_to_point(-0.5,4.8))   
        eq1 = MathTex(r'y=\frac{1}{x}', color=BLACK).move_to(LEFT*4 + UP*2)
        curva1 = ax.plot(lambda x: 1/x, color=rojo, x_range=[-6, -1/6])
        curva2 = ax.plot(lambda x: 1/x, color=rojo, x_range=[1/5, 6])
        self.play(FadeIn(ax), FadeIn(ejex), FadeIn(ejey), FadeIn(eq1), FadeIn(curva1), FadeIn(curva2))
        self.wait()
        self.play(Rotate(ax, angle=PI/4, about_point=ORIGIN, rate_func=smoothererstep),
                  Rotate(ejex, angle=PI/4, about_point=ORIGIN, rate_func=smoothererstep),
                  Rotate(ejey, angle=PI/4, about_point=ORIGIN, rate_func=smoothererstep),
                  run_time=2)
        ejex_new = MathTex(r"x'",color=GRAY).move_to(ax.coords_to_point(6,-0.5)).rotate(PI/4)
        ejey_new = MathTex(r"y'",color=GRAY).move_to(ax.coords_to_point(-0.6,4.8)).rotate(PI/4)
        self.play(Transform(ejex, ejex_new), Transform(ejey, ejey_new))
        self.wait()
        eq2 = MathTex(r"\Biggl(\frac{x'}{\sqrt{2}}\Biggr)^2-\Biggl(\frac{y'}{\sqrt{2}}\Biggr)^2=1", color=BLACK
                     ).move_to(LEFT*4.7 + UP*2).scale(0.75)
        self.play(Transform(eq1, eq2))
        self.wait(2)
        self.play(FadeOut(eq1))

        # Ejes nuevos se vuelven grises y aparecen ejes originales
        ax_new = Axes(x_range=[-7, 7, 1], y_range=[-6, 6, 1], axis_config={'tip_shape': StealthTip}, x_length=9,
        x_axis_config={'include_ticks': False}, y_axis_config={'include_ticks': False}).rotate(PI/4)
        ax_new.set_color(GRAY)
        ax2 = Axes(x_range=[-7, 7, 1], y_range=[-6, 6, 1], axis_config={'tip_shape': StealthTip}, x_length=9,
        x_axis_config={'include_ticks': True}, y_axis_config={'include_ticks': True})
        ax2.set_color(BLACK)
        ejex2 = MathTex(r'x',color=BLACK).move_to(ax2.coords_to_point(6,-0.5))
        ejey2 = MathTex(r'y',color=BLACK).move_to(ax2.coords_to_point(-0.5,4.8))
        self.play(Transform(ax, ax_new), Write(ax2), Write(ejex2), Write(ejey2), run_time=2)
        self.wait(2)

        # Vectores
        self.play(FadeOut(curva1), FadeOut(curva2), FadeOut(ax), FadeOut(ejex), FadeOut(ejey))
        self.wait(3)
        etiqueta_generica = MathTex(r'\begin{pmatrix} x\\ y \end{pmatrix}',
                                    r'\Rightarrow',
                                    r'x\hat{\imath} + y\hat{\jmath}').move_to(LEFT*3 + UP*2).set_color(BLACK)
        etiqueta1 = MathTex(r'\begin{pmatrix} 3\\ y \end{pmatrix}',
                            r'\Rightarrow',
                            r'3\hat{\imath} + y\hat{\jmath}').move_to(LEFT*3 + UP*2).set_color(BLACK)
        etiqueta2 = MathTex(r'\begin{pmatrix} 3\\ 2 \end{pmatrix}',
                            r'\Rightarrow',
                            r'3\hat{\imath} + 2\hat{\jmath}').move_to(LEFT*3 + UP*2).set_color(BLACK)
        vector1 = Vector(ax2.coords_to_point(3,2)).set_color(rojo)
        texto1 = MathTex(r'3', color = rojo).move_to(RIGHT*2 + DOWN*0.5)
        texto2 = MathTex(r'2', color=rojo).move_to(LEFT*0.5 + UP)
        self.play(Write(etiqueta_generica[0]))
        self.wait(2)
        self.play(Write(etiqueta_generica[1]))
        self.play(Write(etiqueta_generica[2]))
        self.wait()
        self.play(Write(vector1))
        self.wait()
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(etiqueta_generica, etiqueta1))
        self.wait()
        self.play(Write(texto2))
        self.wait()
        self.play(Transform(etiqueta_generica, etiqueta2))
        self.wait(2)
        self.play(FadeOut(ax2), FadeOut(ejex2), FadeOut(ejey2), FadeOut(etiqueta_generica), FadeOut(texto1), FadeOut(texto2))
        self.wait()

        # Ejes nuevos con marcas
        ax_new = Axes(x_range=[-7, 7, 2], y_range=[-6, 6, 2], axis_config={'tip_shape': StealthTip}, x_length=9,
        x_axis_config={'include_ticks': True}, y_axis_config={'include_ticks': True}).rotate(PI/4)
        ax_new.set_color(GRAY)
        ejex_new = MathTex(r"x'",color=GRAY).move_to(ax.coords_to_point(6,-0.5)).rotate(PI/4)
        ejey_new = MathTex(r"y'",color=GRAY).move_to(ax.coords_to_point(-0.6,4.8)).rotate(PI/4)
        self.play(Write(ax_new), Write(ejex_new), Write(ejey_new))
        self.wait(2)
        etiqueta_generica = MathTex(r"\begin{pmatrix} x'\\ y' \end{pmatrix}",
                                    r'\Rightarrow',
                                    r"x'\hat{\imath}' + y'\hat{\jmath}'").move_to(LEFT*3.7).set_color(BLACK).scale(0.8)
        etiqueta1 = MathTex(r"\begin{pmatrix} 3.536\\ y' \end{pmatrix}",
                                    r'\Rightarrow',
                                    r"3.536\hat{\imath}' + y'\hat{\jmath}'").move_to(LEFT*3.7).set_color(BLACK).scale(0.8)
        etiqueta2 = MathTex(r"\begin{pmatrix} 3.536\\ -0.707 \end{pmatrix}",
                                    r'\Rightarrow',
                                    r"3.536\hat{\imath}' - 0.707\hat{\jmath}'").move_to(LEFT*3.7).set_color(BLACK).scale(0.8)
        texto1 = MathTex(r'3.536', color=rojo).move_to(ax_new.coords_to_point(3.3,0.7)).rotate(PI/4).scale(0.75)
        texto2 = MathTex(r'-0.707', color=rojo).move_to(ax_new.coords_to_point(-1.1,-1.5)).rotate(PI/4).scale(0.75)
        linea1 = Line(start=ax_new.coords_to_point(3.3,0.2), end=ax_new.coords_to_point(3.3,-0.2), color=rojo)
        linea2 = Line(start=ax_new.coords_to_point(-0.2,-1.5), end=ax_new.coords_to_point(0.2,-1.5), color=rojo)
        self.play(Write(etiqueta_generica[0]))
        self.play(Write(etiqueta_generica[1]))
        self.play(Write(etiqueta_generica[2]))
        self.wait()
        self.play(Write(texto1), Write(linea1))
        self.wait()
        self.play(Transform(etiqueta_generica, etiqueta1))
        self.wait()
        self.play(Write(texto2), Write(linea2))
        self.wait()
        self.play(Transform(etiqueta_generica, etiqueta2))
        self.wait(3)
        self.play(FadeOut(ax_new), FadeOut(ejex_new), FadeOut(ejey_new), FadeOut(vector1), FadeOut(texto1),
                  FadeOut(texto2), FadeOut(linea1), FadeOut(linea2), FadeOut(etiqueta_generica))
        self.wait()

class Rotacion(Scene):
    def construct(self):
        fondo = "#D1EDF2"
        rojo = "#FF0800"
        self.camera.background_color = fondo
        
        # Ejes
        ax = Axes(x_range=[-2, 2, 0.5], y_range=[-2, 2, 0.5], axis_config={'tip_shape': StealthTip}, x_length=7, y_length=7,
        x_axis_config={'include_ticks': True, 'numbers_to_include': [-1,1]},
        y_axis_config={'include_ticks': True, 'numbers_to_include': [-1,1]})
        ax.set_color(BLACK)
        ejex = MathTex(r'x',color=BLACK).move_to(ax.coords_to_point(1.6,-0.2))
        ejey = MathTex(r'y',color=BLACK).move_to(ax.coords_to_point(-0.2,1.6))
        ax_new = Axes(x_range=[-3, 3, 0.5], y_range=[-3, 3, 0.5], axis_config={'tip_shape': StealthTip}, x_length=7, y_length=7,
        x_axis_config={'include_ticks': False}, y_axis_config={'include_ticks': False}).rotate(PI/4)
        ax_new.set_color(GRAY)
        ejex_new = MathTex(r"x'",color=GRAY).move_to(ax_new.coords_to_point(2.4,-0.2)).rotate(PI/4)
        ejey_new = MathTex(r"y'",color=GRAY).move_to(ax_new.coords_to_point(-0.2,2.4)).rotate(PI/4)
        self.play(FadeIn(ax), FadeIn(ejex), FadeIn(ejey), FadeIn(ax_new), FadeIn(ejex_new), FadeIn(ejey_new))   
        self.wait()

        # Vector unitario x'
        vector_x = Vector(ax.coords_to_point(1/np.sqrt(2),1/np.sqrt(2))).set_color(PURE_GREEN)
        etiqueta_x = MathTex(r"\hat{\imath}'").move_to(ax.coords_to_point(0.9,0.7)).set_color(PURE_GREEN).scale(0.8)
        self.play(Write(vector_x))
        self.play(Write(etiqueta_x))
        self.wait()
        arco = Arc(radius = 0.5, start_angle=0, angle=PI/4, arc_center=ORIGIN).set_color(BLACK)
        etiqueta_arco = MathTex(r'45^\circ').scale(0.75).set_color(BLACK).move_to(ax.coords_to_point(0.5,0.2))
        self.play(Write(arco))
        self.play(Write(etiqueta_arco))
        self.wait()
        linea1 = DashedLine(start=ax.coords_to_point(1/np.sqrt(2),1/np.sqrt(2)), end=ax.coords_to_point(0,1/np.sqrt(2)),
                            dash_length=0.05).set_color(PURE_GREEN)
        componente_x1 = MathTex(r"1\cdot\cos{45}").move_to(ax.coords_to_point(1/(2*np.sqrt(2)),0.8)).set_color(BLACK).scale(0.5)
        componente_x2 = MathTex(r"\frac{1}{\sqrt{2}}").move_to(ax.coords_to_point(1/(2*np.sqrt(2)),0.9)).set_color(BLACK).scale(0.5)
        linea2 = DashedLine(start=ax.coords_to_point(1/np.sqrt(2),1/np.sqrt(2)), end=ax.coords_to_point(1/np.sqrt(2),0),
                            dash_length=0.05).set_color(PURE_GREEN)
        componente_y1 = MathTex(r"1\cdot\sin{45}").move_to(ax.coords_to_point(1.1,1/(2*np.sqrt(2)))).set_color(BLACK).scale(0.5)
        componente_y2 = MathTex(r"\frac{1}{\sqrt{2}}").move_to(ax.coords_to_point(0.9,1/(2*np.sqrt(2)))).set_color(BLACK).scale(0.5)
        eq1 = MathTex(r"\hat{\imath}'=",
                      r"\Bigl(",
                      r"\hspace{1cm}",
                      r"\Bigr)",
                      r"\hat{\imath}+",
                      r"\Bigl(",
                      r"\hspace{1cm}",
                      r"\Bigr)",
                      r"\hat{\jmath}").move_to(RIGHT*4+UP*3).scale(0.75).set_color(BLACK)
        eq2 = MathTex(r"\hat{\imath}'=",
                      r"\Bigl(",
                      r"\frac{1}{\sqrt{2}}",
                      r"\Bigr)",
                      r"\hat{\imath}+",
                      r"\Bigl(",
                      r"\hspace{1cm}",
                      r"\Bigr)",
                      r"\hat{\jmath}").move_to(RIGHT*4+UP*3).scale(0.75).set_color(BLACK)
        eq3 = MathTex(r"\hat{\imath}'=",
                      r"\Bigl(",
                      r"\frac{1}{\sqrt{2}}",
                      r"\Bigr)",
                      r"\hat{\imath}+",
                      r"\Bigl(",
                      r"\frac{1}{\sqrt{2}}",
                      r"\Bigr)",
                      r"\hat{\jmath}").move_to(RIGHT*4+UP*3).scale(0.75).set_color(BLACK)
        self.play(Write(eq1), run_time=2)
        self.wait(2)
        self.play(Write(linea1))
        self.play(Write(componente_x1))
        self.wait()
        self.play(Transform(componente_x1, componente_x2))
        self.wait()
        self.play(Transform(eq1, eq2), FadeOut(componente_x1), FadeOut(linea1), run_time=3)
        self.wait(2)
        self.play(Write(linea2))
        self.play(Write(componente_y1))
        self.wait()
        self.play(Transform(componente_y1, componente_y2))
        self.wait()
        self.play(Transform(eq1, eq3), FadeOut(componente_y1), FadeOut(linea2), run_time=3)
        self.wait(3)
        self.play(FadeOut(vector_x), FadeOut(arco), FadeOut(etiqueta_arco), FadeOut(etiqueta_x))
        self.wait()

        # Vector unitario y'
        vector_y = Vector(ax.coords_to_point(-1/np.sqrt(2),1/np.sqrt(2))).set_color(PURE_BLUE)
        etiqueta_y = MathTex(r"\hat{\jmath}'").move_to(ax.coords_to_point(-0.8,1.1)).set_color(PURE_BLUE).scale(0.8)
        self.play(Write(vector_y))
        self.play(Write(etiqueta_y))
        self.wait()
        arco = Arc(radius = 0.5, start_angle=PI/2, angle=PI/4, arc_center=ORIGIN).set_color(BLACK)
        etiqueta_arco = MathTex(r'45^\circ').scale(0.75).set_color(BLACK).move_to(ax.coords_to_point(-0.2,0.5))
        self.play(Write(arco))
        self.play(Write(etiqueta_arco))
        self.wait()
        linea1 = DashedLine(start=ax.coords_to_point(-1/np.sqrt(2),1/np.sqrt(2)), end=ax.coords_to_point(0,1/np.sqrt(2)),
                            dash_length=0.05).set_color(PURE_BLUE)
        componente_x1 = MathTex(r"-1\cdot\cos{45}").move_to(ax.coords_to_point(-1/(2*np.sqrt(2)),0.8)).set_color(BLACK).scale(0.5)
        componente_x2 = MathTex(r"-\frac{1}{\sqrt{2}}").move_to(ax.coords_to_point(-0.55,0.9)).set_color(BLACK).scale(0.5)
        linea2 = DashedLine(start=ax.coords_to_point(-1/np.sqrt(2),1/np.sqrt(2)), end=ax.coords_to_point(-1/np.sqrt(2),0),
                            dash_length=0.05).set_color(PURE_BLUE)
        componente_y1 = MathTex(r"1\cdot\sin{45}").move_to(ax.coords_to_point(-1.1,1/(2*np.sqrt(2)))).set_color(BLACK).scale(0.5)
        componente_y2 = MathTex(r"\frac{1}{\sqrt{2}}").move_to(ax.coords_to_point(-0.9,1/(2*np.sqrt(2)))).set_color(BLACK).scale(0.5)
        eq4 = MathTex(r"\hat{\jmath}'=",
                      r"\Bigl(",
                      r"\hspace{1cm}",
                      r"\Bigr)",
                      r"\hat{\imath}+",
                      r"\Bigl(",
                      r"\hspace{1cm}",
                      r"\Bigr)",
                      r"\hat{\jmath}").move_to(RIGHT*4+UP*0.8).scale(0.75).set_color(BLACK)
        eq5 = MathTex(r"\hat{\jmath}'=",
                      r"\Bigl(",
                      r"-\frac{1}{\sqrt{2}}",
                      r"\Bigr)",
                      r"\hat{\imath}+",
                      r"\Bigl(",
                      r"\hspace{1cm}",
                      r"\Bigr)",
                      r"\hat{\jmath}").move_to(RIGHT*4+UP*0.8).scale(0.75).set_color(BLACK)
        eq6 = MathTex(r"\hat{\jmath}'=",
                      r"\Bigl(",
                      r"-\frac{1}{\sqrt{2}}",
                      r"\Bigr)",
                      r"\hat{\imath}+",
                      r"\Bigl(",
                      r"\frac{1}{\sqrt{2}}",
                      r"\Bigr)",
                      r"\hat{\jmath}").move_to(RIGHT*4+UP*0.8).scale(0.75).set_color(BLACK)
        self.play(Write(eq4), run_time=2)
        self.wait(2)
        self.play(Write(linea1))
        self.play(Write(componente_x1))
        self.wait()
        self.play(Transform(componente_x1, componente_x2))
        self.wait()
        self.play(Transform(eq4, eq5), FadeOut(componente_x1), FadeOut(linea1), run_time=3)
        self.wait(2)
        self.play(Write(linea2))
        self.play(Write(componente_y1))
        self.wait()
        self.play(Transform(componente_y1, componente_y2))
        self.wait()
        self.play(Transform(eq4, eq6), FadeOut(componente_y1), FadeOut(linea2), run_time=3)
        self.wait(3)
        self.play(FadeOut(vector_y), FadeOut(arco), FadeOut(etiqueta_arco), FadeOut(etiqueta_y), FadeOut(ax),
                  FadeOut(ejex), FadeOut(ejey), FadeOut(ax_new), FadeOut(ejex_new), FadeOut(ejey_new))
        self.wait()

        # Construcción matriz de rotación
        eq7 = MathTex(r"\hat{\imath}'=",
                      r"\Bigl(",
                      r"\frac{1}{\sqrt{2}}",
                      r"\Bigr)",
                      r"\hat{\imath}+",
                      r"\Bigl(",
                      r"\frac{1}{\sqrt{2}}",
                      r"\Bigr)",
                      r"\hat{\jmath}").move_to(RIGHT*3+UP*2).scale(0.75).set_color(BLACK)
        eq7p2 = MathTex(r"\hat{\imath}'=",
                      r"\Bigl(",
                      r"\frac{1}{\sqrt{2}}",
                      r"\Bigr)",
                      r"\hat{\imath}+",
                      r"\Bigl(",
                      r"\frac{1}{\sqrt{2}}",
                      r"\Bigr)",
                      r"\hat{\jmath}").move_to(RIGHT*3+UP*2).scale(1.25).set_color(rojo)
        eq8 = MathTex(r"\hat{\jmath}'=",
                      r"\Bigl(",
                      r"-\frac{1}{\sqrt{2}}",
                      r"\Bigr)",
                      r"\hat{\imath}+",
                      r"\Bigl(",
                      r"\frac{1}{\sqrt{2}}",
                      r"\Bigr)",
                      r"\hat{\jmath}").move_to(LEFT*3+UP*2).scale(0.75).set_color(BLACK)
        eq8p2 = MathTex(r"\hat{\jmath}'=",
                      r"\Bigl(",
                      r"-\frac{1}{\sqrt{2}}",
                      r"\Bigr)",
                      r"\hat{\imath}+",
                      r"\Bigl(",
                      r"\frac{1}{\sqrt{2}}",
                      r"\Bigr)",
                      r"\hat{\jmath}").move_to(LEFT*3+UP*2).scale(1.25).set_color(rojo)
        self.play(Transform(eq1, eq7), Transform(eq4, eq8))
        self.wait()
        eq9 = MathTex(r"\vec{v}=",
                      r"x'",
                      r" ",
                      r"\hat{\imath}'",
                      r" ",
                      r" ",
                      r" ",
                      r" ",
                      r"+y'",
                      r" ",
                      r" ",
                      r" ",
                      r" ",
                      r"\hat{\jmath}'",
                      r" ").set_color(BLACK)
        eq9p2 = MathTex(r"\vec{v}=",
                      r"x'",
                      r" ",
                      r"\hat{\imath}'",
                      r" ",
                      r" ",
                      r" ",
                      r" ",
                      r"+y'",
                      r" ",
                      r" ",
                      r" ",
                      r" ",
                      r"\hat{\jmath}'",
                      r" ").set_color(BLACK)
        eq9p2[3].set_color(rojo).scale(1.5)
        eq9p3 = MathTex(r"\vec{v}=",
                      r"x'",
                      r" ",
                      r"\hat{\imath}'",
                      r" ",
                      r" ",
                      r" ",
                      r" ",
                      r"+y'",
                      r" ",
                      r" ",
                      r" ",
                      r" ",
                      r"\hat{\jmath}'",
                      r" ").set_color(BLACK)
        eq10 = MathTex(r"\vec{v}=",
                      r"x'",
                      r"\Bigl(\frac{1}{\sqrt{2}}",
                      r"\hat{\imath}",
                      r"+",
                      r"\frac{1}{\sqrt{2}}",
                      r"\hat{\jmath}",
                      r"\Bigr)",
                      r"+y'",
                      r" ",
                      r" ",
                      r" ",
                      r" ",
                      r"\hat{\jmath}'",
                      r" ").set_color(BLACK)
        eq10p2 = MathTex(r"\vec{v}=",
                      r"x'",
                      r"\Bigl(\frac{1}{\sqrt{2}}",
                      r"\hat{\imath}",
                      r"+",
                      r"\frac{1}{\sqrt{2}}",
                      r"\hat{\jmath}",
                      r"\Bigr)",
                      r"+y'",
                      r" ",
                      r" ",
                      r" ",
                      r" ",
                      r"\hat{\jmath}'",
                      r" ").set_color(BLACK)
        eq10p2[13].set_color(rojo).scale(1.5)
        eq11 = MathTex(r"\vec{v}=",
                      r"x'",
                      r"\Bigl(\frac{1}{\sqrt{2}}",
                      r"\hat{\imath}",
                      r"+",
                      r"\frac{1}{\sqrt{2}}",
                      r"\hat{\jmath}",
                      r"\Bigr)",
                      r"+y'",
                      r"\Bigl(-",
                      r"\frac{1}{\sqrt{2}}",
                      r"\hat{\imath}",
                      r"+\frac{1}{\sqrt{2}}",
                      r"\hat{\jmath}",
                      r"\Bigr)").set_color(BLACK)
        self.play(Write(eq9))
        self.wait(2)
        self.play(Transform(eq1, eq7p2), Transform(eq9, eq9p2))
        self.play(Transform(eq1, eq7), Transform(eq9, eq9p3))
        self.wait(2)
        self.play(Transform(eq9, eq10), FadeOut(eq1))
        self.wait(2)
        self.play(Transform(eq4, eq8p2), Transform(eq9, eq10p2))
        self.play(Transform(eq4, eq8), Transform(eq9, eq10))
        self.wait(2)
        self.play(Transform(eq9, eq11), FadeOut(eq4))
        self.wait(2)
        eq12 = MathTex(r"\vec{v}=",
                       r"x'",
                       r"\Bigl(\frac{1}{\sqrt{2}}",
                       r"\hat{\imath}",
                       r"+",
                       r"\frac{1}{\sqrt{2}}",
                       r"\hat{\jmath}",
                       r"\Bigr)",
                       r"+y'",
                       r"\Bigl(-",
                       r"\frac{1}{\sqrt{2}}",
                       r"\hat{\imath}",
                       r"+\frac{1}{\sqrt{2}}",
                       r"\hat{\jmath}",
                       r"\Bigr)").set_color(BLACK).move_to(UP*1.5)
        eq12p2 = MathTex(r"\vec{v}=",
                       r"x'",
                       r"\Bigl(\frac{1}{\sqrt{2}}",
                       r"\hat{\imath}",
                       r"+",
                       r"\frac{1}{\sqrt{2}}",
                       r"\hat{\jmath}",
                       r"\Bigr)",
                       r"+y'",
                       r"\Bigl(-",
                       r"\frac{1}{\sqrt{2}}",
                       r"\hat{\imath}",
                       r"+\frac{1}{\sqrt{2}}",
                       r"\hat{\jmath}",
                       r"\Bigr)").set_color(BLACK).move_to(UP*1.5)
        eq12p3 = MathTex(r"\vec{v}=",
                       r"x'",
                       r"\Bigl(\frac{1}{\sqrt{2}}",
                       r"\hat{\imath}",
                       r"+",
                       r"\frac{1}{\sqrt{2}}",
                       r"\hat{\jmath}",
                       r"\Bigr)",
                       r"+y'",
                       r"\Bigl(-",
                       r"\frac{1}{\sqrt{2}}",
                       r"\hat{\imath}",
                       r"+\frac{1}{\sqrt{2}}",
                       r"\hat{\jmath}",
                       r"\Bigr)").set_color(BLACK).move_to(UP*1.5)
        eq13 = MathTex(r"\vec{v}=",
                       r"\Bigl(",
                       r"\frac{1}{\sqrt{2}}x'-\frac{1}{\sqrt{2}}y'",
                       r"\Bigr)",
                       r"\hat{\imath}",
                       r"+",
                       r"\Bigl(\frac{1}{\sqrt{2}}x'+\frac{1}{\sqrt{2}}y'\Bigr)",
                       r"\hat{\jmath}").set_color(BLACK).move_to(DOWN*1.5)
        eq12p2[3].set_color(rojo).scale(1.5)
        eq12p2[11].set_color(rojo).scale(1.5)
        eq12p3[6].set_color(rojo).scale(1.5)
        eq12p3[13].set_color(rojo).scale(1.5)
        self.play(Transform(eq9, eq12))
        self.wait()
        self.play(Write(eq13[:2]), Write(eq13[3:5]))
        self.wait()
        self.play(Transform(eq9, eq12p2))
        self.play(Transform(eq9, eq12))
        self.wait()
        self.play(Write(eq13[2]))
        self.wait(2)
        self.play(Write(eq13[5]), Write(eq13[7]))
        self.wait()
        self.play(Transform(eq9, eq12p3))
        self.play(Transform(eq9, eq12))
        self.wait()
        self.play(Write(eq13[6]))
        self.wait(2)
        self.play(FadeOut(eq9))
        self.wait()
        eq14 = MathTex(r"\vec{v}=x\hat{\imath}+y\hat{\jmath}").set_color(BLACK).move_to(UP*2)
        self.play(Write(eq14))
        self.wait()
        llave1 = Brace(mobject=eq13[1:4], direction=UP, buff=0.2, color=BLACK)
        llave2 = Brace(mobject=eq13[6], direction=UP, buff=0.2, color=BLACK)
        eq_x = llave1.get_tex(r"x=\frac{1}{\sqrt{2}}x'-\frac{1}{\sqrt{2}}y'").set_color(BLACK).scale(0.75)
        eq_y = llave2.get_tex(r"y=\frac{1}{\sqrt{2}}x'+\frac{1}{\sqrt{2}}y'").set_color(BLACK).scale(0.75)
        self.play(GrowFromCenter(llave1), Write(eq_x))
        self.wait()
        self.play(GrowFromCenter(llave2), Write(eq_y))
        self.wait()
        self.play(FadeOut(eq13), FadeOut(llave1), FadeOut(llave2), FadeOut(eq14))
        self.wait()
        eq15 = MathTex(r"x=\frac{1}{\sqrt{2}}x'-\frac{1}{\sqrt{2}}y'").set_color(BLACK).move_to(UP*2+LEFT*3)
        eq16 = MathTex(r"y=\frac{1}{\sqrt{2}}x'+\frac{1}{\sqrt{2}}y'").set_color(BLACK).move_to(UP*2+RIGHT*4)
        self.play(Transform(eq_x, eq15), Transform(eq_y, eq16))
        self.wait()

        # Forma matricial
        eq17 = MathTex(r"\begin{pmatrix} x\\ y \end{pmatrix}",
                       r"=\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & -1\\ 1 & 1\end{pmatrix}",
                       r"\begin{pmatrix} x'\\ y' \end{pmatrix}").set_color(BLACK)
        self.play(Write(eq17), run_time=2)
        self.wait(3)
        eq18 = MathTex(r"\begin{pmatrix} x'\\ y' \end{pmatrix}",
                       r"=\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1\\ -1 & 1\end{pmatrix}",
                       r"\begin{pmatrix} x\\ y \end{pmatrix}").set_color(BLACK)
        eq19 = MathTex(r"\begin{pmatrix} x'\\ y' \end{pmatrix}",
                       r"=\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1\\ -1 & 1\end{pmatrix}",
                       r"\begin{pmatrix} x\\ y \end{pmatrix}").set_color(BLACK).move_to(LEFT*3 + DOWN)
        self.play(Transform(eq17[0], eq18[0]), run_time=1.5)
        self.play(Transform(eq17[1], eq18[1]), run_time=1.5)
        self.play(Transform(eq17[2], eq18[2]), run_time=1.5)
        self.wait()
        self.play(FadeOut(eq_x), FadeOut(eq_y), Transform(eq17, eq19), run_time=1.5)
        self.wait()

        # Vuelve a aparecer la hipérbola
        ax = Axes(x_range=[-7, 7, 1], y_range=[-6, 6, 1], axis_config={'tip_shape': StealthTip}, x_length=9,
        x_axis_config={'include_ticks': False}, y_axis_config={'include_ticks': False})
        ax.set_color(BLACK)
        ejex = MathTex(r'x',color=BLACK).move_to(ax.coords_to_point(6,-0.5))
        ejey = MathTex(r'y',color=BLACK).move_to(ax.coords_to_point(-0.5,4.8))   
        curva1 = ax.plot(lambda x: 1/x, color=rojo, x_range=[-6, -1/6])
        curva2 = ax.plot(lambda x: 1/x, color=rojo, x_range=[1/5, 6])
        posicion = Dot(radius=0.08, color=PURE_BLUE)
        posicion2 = Dot(radius=0.08, color=PURE_BLUE)
        grafica = Group(ax, ejex, ejey, curva1, curva2)
        grafica.move_to(RIGHT*3 + UP).scale(0.75)
        self.play(FadeIn(grafica))
        self.wait()

        # Punto sobre la hipérbola
        eq20 = MathTex(r"\begin{pmatrix} x'\\ y' \end{pmatrix}",
                       r"=\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1\\ -1 & 1\end{pmatrix}",
                       r"\begin{pmatrix} x\\ y \end{pmatrix}").set_color(BLACK).move_to(LEFT*3 + DOWN)
        eq20[2].set_color(PURE_BLUE)
        eq21 = MathTex(r"\begin{pmatrix} x'\\ y' \end{pmatrix}",
                       r"=\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1\\ -1 & 1\end{pmatrix}",
                       r"\begin{pmatrix} x\\ \frac{1}{x} \end{pmatrix}").set_color(BLACK).move_to(LEFT*3 + DOWN)
        eq22 = MathTex(r"\begin{pmatrix} x'\\ y' \end{pmatrix}",
                       r"=\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1\\ -1 & 1\end{pmatrix}",
                       r"\begin{pmatrix} x\\ \frac{1}{x} \end{pmatrix}").set_color(BLACK).move_to(LEFT*3 + DOWN)
        eq21[2].set_color(PURE_BLUE)
        self.play(Transform(eq17, eq20))
        self.wait()
        self.play(Transform(eq17, eq21), MoveAlongPath(posicion, curva2), MoveAlongPath(posicion2, curva1),
                  rate_func=smoothererstep, run_time=4)
        self.play(FadeOut(posicion), FadeOut(posicion2))
        self.wait()
        self.play(Transform(eq17, eq22))
        self.wait()
        eq23 = MathTex(r"\begin{pmatrix} x'\\ y' \end{pmatrix}",
                       r"=\frac{1}{\sqrt{2}}",
                       r"\begin{pmatrix} x+\frac{1}{x}\vspace{0.25cm}\\x-\frac{1}{x} \end{pmatrix}").set_color(BLACK).move_to(LEFT*3 + DOWN)
        self.play(Transform(eq17, eq23))
        self.wait()
        eq24 = MathTex(r"x'=\frac{1}{\sqrt{2}}\Bigl(x+\frac{1}{x}\Bigr)").set_color(BLACK).move_to(LEFT*3 + UP*2.5).scale(0.75)
        eq25 = MathTex(r"y'=\frac{1}{\sqrt{2}}\Bigl(x-\frac{1}{x}\Bigr)").set_color(BLACK).move_to(LEFT*3 + UP).scale(0.75)
        self.play(Write(eq24), run_time=1.5)
        self.play(Write(eq25), run_time=1.5)
        self.wait()
        self.play(FadeOut(eq17))
        eq26 = MathTex(r"x'^2-y'^2",
                       r"=\frac{1}{2}\Bigl(x+\frac{1}{x}\Bigr)^2",
                       r"-",
                       r"\frac{1}{2}\Bigl(x-\frac{1}{x}\Bigr)^2",
                       r" ").set_color(BLACK).move_to(LEFT*2 + DOWN*1.5).scale(0.75)
        self.play(Write(eq26[0]), run_time=1.5)
        self.wait()
        self.play(Write(eq26[1]), run_time=1.5)
        self.wait()
        self.play(Write(eq26[2:]), run_time=1.5)
        self.wait()
        eq27 = MathTex(r"x'^2-y'^2",
                       r"=\frac{1}{2}\Bigl(x^2+2+\frac{1}{x^2}\Bigr)",
                       r"-",
                       r"\frac{1}{2}\Bigl(x^2-2+\frac{1}{x^2}\Bigr)",
                       r" ").set_color(BLACK).move_to(LEFT*2 + DOWN*1.5).scale(0.75)
        eq27p2 = MathTex(r"x'^2-y'^2",
                        r"=\frac{1}{2}2",
                        r"+",
                        r"\frac{1}{2}2",
                        r" ").set_color(BLACK).move_to(LEFT*2 + DOWN*1.5).scale(0.75)
        self.play(Transform(eq26, eq27))
        self.wait()
        flecha1 = Arrow(start=LEFT*3.25+DOWN*0.2, end=LEFT*3.25+DOWN*1.2, color=PURE_GREEN)
        flecha2 = Arrow(start=LEFT*0.1+DOWN*0.2, end=LEFT*0.1+DOWN*1.2, color=PURE_GREEN)
        flecha3 = Arrow(start=LEFT*1.8+DOWN*3, end=LEFT*1.8+DOWN*2, color=PURE_BLUE)
        flecha4 = Arrow(start=RIGHT*1.35+DOWN*3, end=RIGHT*1.35+DOWN*2, color=PURE_BLUE)
        self.play(Write(flecha1), Write(flecha2), Write(flecha3), Write(flecha4))
        self.wait(2)
        self.play(Transform(eq26, eq27p2), FadeOut(flecha1), FadeOut(flecha2), FadeOut(flecha3), FadeOut(flecha4))
        self.wait()
        eq28 = MathTex(r"x'^2-y'^2",
                       r"=1",
                       r"+",
                       r"1",
                       r"=2").set_color(BLACK).move_to(LEFT*2 + DOWN*1.5).scale(0.75)
        self.play(Transform(eq26[1:4], eq28[1:4]))
        self.wait()
        self.play(Transform(eq26, eq28))
        eq29 = MathTex(r"x'^2-y'^2",
                       r" ",
                       r" ",
                       r" ",
                       r"=2").set_color(BLACK).move_to(LEFT*2 + DOWN*1.5).scale(0.75)
        eq29p2 = MathTex(r"\frac{x'^2}{2}-\frac{y'^2}{2}",
                         r" ",
                         r" ",
                         r" ",
                         r"=1").set_color(BLACK).move_to(LEFT*2 + DOWN*1.5).scale(0.75)
        eq30 = MathTex(r"\frac{x'^2}{2}-\frac{y'^2}{2}",
                       r" ",
                       r" ",
                       r" ",
                       r"=1").set_color(GRAY).move_to(LEFT*3.7 + UP).scale(0.75)
        self.play(Transform(eq26, eq29))
        self.wait()
        self.play(Transform(eq26, eq29p2))
        self.wait(3)
        self.play(FadeOut(eq24), FadeOut(eq25), Transform(eq26, eq30), FadeOut(grafica))
        grafica.move_to(ORIGIN).scale(1.25)
        self.wait()

        # Ejes nuevos
        eq31 = MathTex(r"y=\frac{1}{x}").set_color(BLACK).move_to(RIGHT*3.5 + UP).scale(0.75)
        ax_new = Axes(x_range=[-7, 7, 2], y_range=[-6, 6, 2], axis_config={'tip_shape': StealthTip}, x_length=9,
        x_axis_config={'include_ticks': False}, y_axis_config={'include_ticks': False}).rotate(PI/4)
        ax_new.set_color(GRAY)
        ejex_new = MathTex(r"x'",color=GRAY).move_to(ax_new.coords_to_point(6,-0.5)).rotate(PI/4)
        ejey_new = MathTex(r"y'",color=GRAY).move_to(ax_new.coords_to_point(-0.6,4.8)).rotate(PI/4)
        self.play(FadeIn(ax_new), FadeIn(ejex_new), FadeIn(ejey_new), FadeIn(grafica))
        self.play(FadeIn(eq31))
        self.wait(3)
        self.play(FadeOut(ax_new), FadeOut(ejex_new), FadeOut(ejey_new), FadeOut(grafica), FadeOut(eq31), FadeOut(eq26))
        self.wait()


class Agradecimientos(Scene):
    def construct(self):
        fondo = "#D1EDF2"
        self.camera.background_color = fondo
        title = Text("Agradecimientos:").move_to(UP * 2.5).set_color(BLACK)
        self.wait(1)
        self.play(FadeIn(title))
        text2 = Text("David Saavedra Pastor").scale(0.75).set_color(BLACK)
        text1 = Text("Javier López Fernández").move_to(UP).scale(0.75).set_color(BLACK)
        text3 = Text("Julia Moreno Sánchez").move_to(DOWN).scale(0.75).set_color(BLACK)
        self.wait(2)
        self.play(FadeIn(text1))
        self.wait()
        self.play(FadeIn(text2))
        self.wait()
        self.play(FadeIn(text3))
        self.wait()
        self.wait(3)
        self.play(FadeOut(title), FadeOut(text1), FadeOut(text2), FadeOut(text3))
        self.wait()

class Logo(Scene):
    def construct(self):
        fondo = "#D1EDF2"
        self.camera.background_color = fondo

        # Logo Migstemáticas
        mw1 = ImageMobject("5MW-Cian.png").scale(0.6).move_to(np.array([0, 8, 0])).scale(0.85)
        mw2 = ImageMobject("5MW-Cian.png").scale(0.6).move_to(np.array([0, 1, 0])).scale(0.85)
        label1 = Text("Migstemáticas").move_to(np.array([0, -8, 0])).set_color(BLACK)
        label2 = Text("Migstemáticas").move_to(np.array([0, -2, 0])).set_color(BLACK)
        self.add(mw1, label1)
        self.wait(2)
        self.play(Transform(mw1, mw2), Transform(label1, label2), run_time=0.5)
        self.wait(3)
        self.play(FadeOut(mw1), FadeOut(label1))
        self.wait(2)
        