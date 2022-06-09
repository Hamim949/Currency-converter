import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Currency converter', width=600, height=300)

with dpg.window(label="Currency converter", width=600, height=300):
    dpg.add_text("Welcome to the currency converter.")
    dpg.add_input_float(label="amount", default_value=1.0, width=100)
    dpg.add_combo(["USD - US dollar", "EUR - Euros"], label="From", width=200,
        default_value="USD - US Dollar")
    dpg.add_combo(["USD - US dollar", "EUR - Euros"], label="To", width=200,
        default_value="EUR - Euros")
    dpg.add_button(label="Convert")
    

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()