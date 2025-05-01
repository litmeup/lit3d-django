from django.core.management.base import BaseCommand
from lit3d.models import Slogans, ContactInfo

class Command(BaseCommand):
    help = "Заполняет базу начальными данными"

    def handle(self, *args, **kwargs):
        if not Slogans.objects.exists():
            Slogans.objects.create(
            main_heading= '<div class="main-title__title a-fade js-reveal-intro" style="translate: none; rotate: none; scale: none; transform: translate(0px, 0px); opacity: 1; visibility: inherit;">Новейшие технологии</div>',
            main_subheading= '<div class="main-title__subtitle">в&nbsp;мультимедийных выставках и&nbsp;экспозиционных павильонах</div>',
            about_heading= '<h2 class="section-title a-fade js-reveal-about" style="translate: none; rotate: none; scale: none; opacity: 1; visibility: inherit; transform: translate(0px, 0px);">Мы&nbsp;— команда амбициозных профессионалов, преданных своему делу и&nbsp;вдохновленных идеями техношаманизма</h2>',
            about_text= '<p>За&nbsp;нами более 30&nbsp;успешно реализованных выставочных проектов, участие в&nbsp;государственных контрактах и&nbsp;прямые договоры с&nbsp;ведущими производителями мультимедийного оборудования. Мы&nbsp;создаем уникальные проекты, не&nbsp;имеющие аналогов в&nbsp;мире, сочетая технологии и&nbsp;креативные решения, чтобы воплотить ваши самые смелые идеи в&nbsp;реальность!</p>',
            slogan= '<h2 class="section-title section-title--size_small section-title--align_center a-fade js-reveal-outro" style="translate: none; rotate: none; scale: none; opacity: 1; visibility: inherit; transform: translate(0px, 0px);">Невозможное мы&nbsp;сделаем сразу, а&nbsp;для чуда понадобится немного подготовки</h2>',
            contact_heading= '<h2 class="section-title section-title--size_small">Готовы к&nbsp;успеху?</h2>',
            contact_subheading= '<h3 class="section-title section-title--size_small"> Свяжитесь с&nbsp;нами и&nbsp;мы&nbsp;вместе создадим <nobr>что-то</nobr> выдающееся!</h3>'
            )
            self.stdout.write(self.style.SUCCESS("Данные для Slogans добавлены"))

        if not ContactInfo.objects.exists():
            ContactInfo.objects.create(
                phone_number= "8 800 250 39 76",
                email= "main@lit3d.io",
                instagram_url= "https://www.instagram.com/lit3dmap/",
                vk_url= "https://vk.com/lit3dmap",
                pinterest_url= "https://ru.pinterest.com/lit3d/",
                behance_url= "https://www.behance.net/lit3dteam"                      
            )
            self.stdout.write(self.style.SUCCESS("Данные для ContactInfo добавлены"))
