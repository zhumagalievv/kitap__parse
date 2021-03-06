from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        f'Сәлем, {message.from_user.username}!\n'
        f'5000-нан аса кітапты оқу және тыңдау платформасы, \n'
        f'толығырақ көру үшін /about командасын басыңыз')


@dp.message_handler(text='/about')
async def about_project(message: types.Message):
    await message.answer(
        text='Kitap.kz – қазақ және әлем әдебиетінің үздік шығармаларын оқу \n'
             'және тыңдау мүмкіндігін ұсынатын ауқымды онлайн платформа.\n'
             ' Мұнда ұлттық әдебиетіміз бен отандық ғылымның, өнеріміз бен \n'
             'сан-саладағы шығармашылық өкілдеріміздің жәдігерлері заңды \n'
             'негізде жинақталған.\n\n'
             'Бүгінгі таңда "Қазақстанның ашық кітапханасы" қорында түрлі'
             ' бағыттағы 500-ден аса автордың 5000-нан аса кітабы жинақталған.\n\n'
             '"Қазақстанның ашық кітапханасы" тек қазақ әдебиеті шығармаларымен ғана шектелмейді, '
             'осы кезеңге дейін қазақ тіліне аударылған шетел әдебиетінің де көрнекті туындылары '
             'оқырман назарына ұсынылып келеді. Қазір қорымызда 600-ден аса әлем әдебиетінің жауһарлары бар.\n'
             'Сондай-ақ, қазақ әдебиетінің шетел тілдеріне аударылған үздік шығармаларында да '
             'біздің кітапханадан таба аласыз. Балаларға арналған әңгіме, өлеңдермен қатар, түрлі '
             'тақырыптағы ертегілердің аудионұсқасы жасалды. Жобаның арқалаған жүгі салмақты: жаһандану '
             'дәуірінде ұлттың құндылықтарын сақтауға ұмтылу, сондай-ақ, интернет желісінде қазақтілді '
             'мазмұнды арттырып, тіліміздің қолданыс аясын кеңейтуге күш салу.'
    )
