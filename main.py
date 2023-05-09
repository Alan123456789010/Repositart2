import arcade

window = arcade.Window(800, 600, "Drawing a Circle")
arcade.start_render()
arcade.draw_rectangle_filled(400, 300, 800, 700, arcade.color.BLUE)
arcade.draw_rectangle_filled(400, 100, 800, 200, arcade.color.BLIZZARD_BLUE)
arcade.draw_circle_filled(300, 200, 75, arcade.color.WHITE)
arcade.draw_circle_filled(300, 275, 60, arcade.color.WHITE)
arcade.draw_circle_filled(300, 350, 50, arcade.color.WHITE)
arcade.draw_circle_filled(280, 360, 7, arcade.color.BLACK)
arcade.draw_circle_filled(320, 360, 7, arcade.color.BLACK)
arcade.run()

