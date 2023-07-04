import random

def is_prime(num):
    """Перевірка, чи є число простим."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime():
    """Генерація випадкового простого числа."""
    while True:
        num = random.randint(2**10, 2**11)  # Генеруємо випадкове число з діапазону [2^10, 2^11]
        if is_prime(num):
            return num

def extended_euclidean(a, b):
    """Розширений алгоритм Евкліда."""
    if b == 0:
        return a, 1, 0
    gcd, x, y = extended_euclidean(b, a % b)
    return gcd, y, x - (a // b) * y

def generate_keys():
    """Генерація публічного та приватного ключів."""
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Вибір публічного ключа (експонента)
    e = random.randint(2, phi_n - 1)
    gcd, _, _ = extended_euclidean(e, phi_n)
    while gcd != 1:
        e = random.randint(2, phi_n - 1)
        gcd, _, _ = extended_euclidean(e, phi_n)

    # Обчислення приватного ключа
    _, d, _ = extended_euclidean(e, phi_n)
    d = d % phi_n

    return (e, n), (d, n)

def encrypt(message, public_key):
    """Шифрування повідомлення за публічним ключем."""
    e, n = public_key
    encrypted_message = []
    for block in message:
        encrypted_block = pow(block, e, n)
        encrypted_message.append(encrypted_block)
    return encrypted_message

def decrypt(encrypted_message, private_key):
    """Дешифрування повідомлення за приватним ключем."""
    d, n = private_key
    decrypted_message = []
    for block in encrypted_message:
        decrypted_block = pow(block, d, n)
        decrypted_message.append(decrypted_block)
    return decrypted_message

# Приклад використання
message = [211, 223]  # Список числових блоків повідомлення

public_key, private_key = generate_keys()
encrypted_message = encrypt(message, public_key)
decrypted_message = decrypt(encrypted_message, private_key)

print("Public key:", public_key)
print("Private key:", private_key)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)

"""
Запропонований код реалізує алгоритм RSA (Rivest-Shamir-Adleman) - один із найпопулярніших асиметричних алгоритмів шифрування. 
Він дозволяє забезпечити конфіденційність даних шляхом шифрування повідомлення за допомогою публічного ключа та дешифрування 
його за допомогою приватного ключа.

Основні кроки в роботі коду:

Функція is_prime(num) перевіряє, чи є число num простим. Вона використовує просту перевірку, перебираючи всі можливі дільники 
числа.

Функція generate_prime() генерує випадкове просте число шляхом виклику функції is_prime() для різних чисел, поки не 
буде знайдено просте число.

Функція extended_euclidean(a, b) реалізує розширений алгоритм Евкліда для обчислення найбільшого спільного дільника
 (НСД) чисел a і b, а також знаходження оберненого елемента d такого, що a*d ≡ 1 (mod b).

Функція generate_keys() генерує публічний та приватний ключі. Вона використовує функції generate_prime() для 
отримання двох простих чисел p і q, обчислює модуль n = p*q та значення функції Ойлера phi_n = (p-1)*(q-1). 
Далі вона вибирає випадкове число e, яке є публічним експонентом і менше за phi_n та незалежне від нього, і обчислює 
відповідний приватний експонент d, використовуючи розширений алгоритм Евкліда.

Функція encrypt(message, public_key) виконує шифрування повідомлення message за допомогою публічного ключа public_key. 
Вона розбиває повідомлення на числові блоки (в даному коді передбачається, що повідомлення представлене як список числових 
блоків), і кожен блок шифрує за допомогою операції піднесення до степеня за модулем pow(block, e, n).

Функція decrypt(encrypted_message, private_key) виконує дешифрування зашифрованого повідомлення encrypted_message за допомогою
 приватного ключа private_key. Вона розшифровує кожен блок зашифрованого повідомлення за допомогою операції піднесення 
 до степеня за модулем pow(block, d, n).

В прикладі використання коду створюється список числових блоків повідомлення [65, 66, 67]. Генеруються публічний 
та приватний ключі за допомогою функції generate_keys(). Повідомлення шифрується за допомогою encrypt() з використанням 
публічного ключа, а потім дешифрується за допомогою decrypt() з використанням приватного ключа. Результати виводяться на екран.
"""