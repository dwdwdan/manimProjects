from manim import *
import math

a = 3
b = 4
angle = round(math.degrees(math.atan(a/b)))

class main(Scene):
    def construct(self):
        triangle = Polygon([0,0,0],[0,a,0], [b, 0, 0])
        right_angle = RightAngle(Line(DOWN, UP), Line(LEFT, RIGHT))

        a_brace = BraceBetweenPoints([0,a,0], [0,0,0])
        a_text = MathTex("a=",a).next_to(a_brace, LEFT)
        a_label = VGroup(a_brace, a_text)

        b_brace = BraceBetweenPoints([0,0,0], [b,0,0])
        b_text = MathTex("b=",b).next_to(b_brace, DOWN)
        b_label = VGroup(b_brace, b_text)

        # sohcahtoa has been split to allow for colouring of toa only
        sohcah = Text("SOHCAH")
        toa = Text("TOA").next_to(sohcah, RIGHT, buff=0.05)
        sohcahtoa = VGroup(sohcah, toa).move_to([4.2,3,0])

        ac_angle = Arc(1, 3*PI/2, math.atan(b/a), arc_center=[0,a,0])
        ac_theta = MathTex(r"\theta").move_to(ac_angle.get_arc_center() + DOWN*1.2 + 1.2*RIGHT/2)
        ac_angle_number = MathTex(str(angle) + r"^\circ").move_to(ac_theta)
        ac_angle_group_init = VGroup(ac_angle, ac_theta)
        ac_angle_group_end = VGroup(ac_angle, ac_angle_number)

        all_triangle = VGroup(triangle, a_label, b_label, ac_angle, ac_theta, ac_angle_number, right_angle)
        all_triangle.shift([-b-0.5, -a/2, 0])

        tan_text_1 = MathTex(r"\tan(\theta) = \frac{a}{b}").move_to([4, 0, 0])
        tan_text_2 = MathTex(r"\tan(\theta) = \frac{" + str(a) + "}{" + str(b) + "}").move_to([4, 0, 0])
        tan_text_3 = MathTex(r"\theta = \arctan\left(\frac{" + str(a) + "}{" + str(b) + r"}\right)").move_to([4, 0, 0])
        tan_text_4 = MathTex(r"\theta = " + str(angle) + r"^\circ").move_to([4, 0, 0])
        self.play(Create(triangle))
        self.play(Create(right_angle))
        self.play(Write(a_label))
        self.play(Write(b_label))

        self.wait(1)
        self.play(Write(ac_angle_group_init))

        self.wait(1)
        self.play(Write(sohcahtoa))

        self.wait(1)
        self.play(ApplyMethod(right_angle.scale, 1.5), run_time = 0.5)
        self.play(ApplyMethod(right_angle.scale, 2/3), run_time = 0.5)

        self.wait(1)
        self.play(ApplyMethod(toa.set_color, RED))

        self.wait(1)
        self.play(TransformFromCopy(toa, tan_text_1))
        self.play(ApplyMethod(toa.set_color, WHITE))

        self.wait(1)
        self.play(ReplacementTransform(tan_text_1, tan_text_2))

        self.wait(1)
        self.play(ReplacementTransform(tan_text_2, tan_text_3))

        self.wait(1)
        self.play(ReplacementTransform(tan_text_3, tan_text_4))

        self.wait(1)
        self.play(ReplacementTransform(ac_theta, ac_angle_number), ReplacementTransform(tan_text_4, ac_angle_number))

        self.wait(3)
        self.play(FadeOut(sohcahtoa, all_triangle, ac_angle_group_end, tan_text_4, a_label, b_label))
        self.wait(1)

        banner=ManimBanner().scale(0.7).shift(DOWN*0.75)
        made_with=Text("Made With").next_to(banner, UP, buff=0.5)
        self.play(Write(made_with), banner.create())
        self.play(banner.expand())
        self.wait(1)
