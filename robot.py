from phoenix6 import hardware, controls, configs, unmanaged
import keyboard
import time

if __name__ == "__main__":
    # Use Talon FX ID 1 on the first available CAN interface
    fx = hardware.TalonFX(1, "*")

    # Factory-default it by applying an empty configuration
    fx.configurator.apply(configs.TalonFXConfiguration())
    # Change this to true to enable the robot. Otherwise press the "e" key to set this to true
    is_enabled = False

    while True:
        # Feed the enable if we want to be enabled
        # https://v6.docs.ctr-electronics.com/en/stable/docs/api-reference/api-usage/enabling-actuators.html#non-frc-applications
        if is_enabled:
            unmanaged.feed_enable(0.1)

        if keyboard.is_pressed('q'):
            print("Quitting")
            break
        elif keyboard.is_pressed('w'):
            print("Setting output to +0.1 duty cycle")
            fx.set_control(controls.DutyCycleOut(0.1))
        elif keyboard.is_pressed('s'):
            print("Setting output to neutral output")
            fx.set_control(controls.NeutralOut())
        elif keyboard.is_pressed('e'):
            print("Enabling output")
            is_enabled = True
        elif keyboard.is_pressed('d'):
            print("Disabling output")
            is_enabled = False

        # Run the loop at 50 milliseconds
        time.sleep(0.05)