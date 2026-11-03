
import random


def play_game():
    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 5
    win = False

    print("\nبازی حدس اعداد شروع شد!")
    print("یک عدد بین 1 تا 100 حدس بزن.")

    while attempts < max_attempts:

        print("\nتلاش", attempts + 1, "از", max_attempts)
        print("فرصت باقی مانده:", max_attempts - attempts)

        guess = input("حدس خود را وارد کنید: ")

        # بررسی معتبر بودن ورودی
        if not guess.isdigit():
            print("ورودی نامعتبر است! لطفاً عدد وارد کنید.")
            continue

        guess = int(guess)

        if guess < 1 or guess > 100:
            print("عدد باید بین 1 تا 100 باشد.")
            continue

        # ثبت تلاش معتبر
        attempts += 1

        # بررسی حدس
        if guess == secret_number:
            print("\nآفرین! درست حدس زدی!")
            win = True

            if attempts == 1:
                print("رتبه: نمونه ای")
            elif attempts == 2:
                print("رتبه: بسیار خوب")
            elif attempts == 3:
                print("رتبه: خوب")
            elif attempts == 4:
                print("رتبه: قبول")
            elif attempts == 5:
                print("رتبه: با شانس بردی!")

            break

        else:
            difference = abs(secret_number - guess)

            if guess > secret_number:
                print("عدد کوچک تر وارد کن.")
            else:
                print("عدد بزرگ تر وارد کن.")

            # راهنمای نزدیک یا دور
            if difference <= 5:
                print("خیلی نزدیکی!")
            elif difference <= 15:
                print("نزدیکی، ولی هنوز فاصله داری!")
            else:
                print("خیلی دوری!")

    # بررسی باخت
    if win == False:
        print("\nفرصت هایت تمام شد!")
        print("متأسفانه باختی!")
        print("عدد مخفی این بود:", secret_number)
