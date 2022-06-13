import dearpygui.dearpygui as dpg
import model

dpg.create_context()
dpg.create_viewport(title='Currency converter', width=600, height=300)

with dpg.window(label="Currency converter", width=600, height=300):
    dpg.add_text("Welcome to the currency converter.")
    dpg.add_input_float(label="amount", default_value=1.0, width=100)
    dpg.add_combo(model.currencies,
        default_value=model.default_from, label="from", width=250)
    dpg.add_combo(model.currencies,
        default_value=model.default_from, label="to", width=250)
    dpg.add_button(label="Convert")
    

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()