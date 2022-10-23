from PIL import Image

img = Image.open('elephant_image.jpg')
# img.show(print(img.size, img.mode, sep='\n'))  # открываем изображение и выводим его размеры и тип в консоль

new_img = img.crop((50, 20, 200, 100))  # Обрезаем нужную часть изображения
# new_img.show(print(img.size, img.mode, sep='\n'))

glasses = Image.open('glasses.jpg').resize((100, 50))  # открываем еще одну картинку и меняем ее размер
glasses.putalpha(200)  # Меняем прозрачность картинки
# glasses.show(print(glasses.size, glasses.mode, sep='\n'))

created_img = Image.new('RGBA', new_img.size, (255, 255, 255, 0))  # Создаем шаблон нового изображения
created_img.paste(new_img)  # Поверх шаблона вставляем одно изображение
created_img.paste(glasses, (20, 15), mask=glasses)  # а затем второе поверх первого
created_img.show()
