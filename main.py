
from test import play_game

again = "yes"

while again == "yes" or again == "y":

    play_game()

    again = input("\nآیا می خواهی دوباره بازی کنی؟ (yes/no): ")

print("\nبازی به پایان رسید. خداحافظ!")
