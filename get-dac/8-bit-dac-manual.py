import RPi.GPIO as GPIO
GPIO.setmod(GPIO.BMC)
outp=[16, 5, 25, 17, 27, 23, 22, 24]
GPIO.setup(outp, GPIO.OUT)
dyn_range=float(input())
def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выход за динамический диапозон ЦАП (0.00-{dynamic_range:.2f} B)")
        print("Устанавливаем 0.0 B")
        return 0
    return int(voltage / dynamic_range * 255)

number_to_dac(value):
GPIO.output (outp, [int(element) for element in bin(value)[2:].zfill(8)])
try: 
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()



