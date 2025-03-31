from project import *
import schedule
import time

if __name__ == '__main__':
    tg = ProjectTelegram()
    vk = ProjectVk()

    def job(type, chat_id=None, group_id=None, tags=None):
        tg.send(type=type, chat_id=chat_id, tags=tags)
        if group_id is not None:
            vk.send(type=type, group_id=group_id, image_gen=False, text_gen=False, tags=tags)

    schedule.every().day.at("19:00",'Europe/Moscow').do(job, type="pisces", chat_id='@pisces_the', group_id='229837683', tags=['#гороскоп', '#таро', '#таронамесяц', '#рыбы'])
    schedule.every().day.at("19:01",'Europe/Moscow').do(job, type="aries", chat_id='@aries_the', group_id='229837854', tags=['#гороскоп', '#таро', '#таронамесяц', '#овен'])
    schedule.every().day.at("19:02",'Europe/Moscow').do(job, type="taurus", group_id='229860740', tags=['#гороскоп', '#таро', '#таронамесяц', '#телец'])
    schedule.every().day.at("19:03",'Europe/Moscow').do(job, type="gemini", chat_id='@gemini_the', group_id='229837895', tags=['#гороскоп', '#таро', '#таронамесяц', '#близнецы'])
    schedule.every().day.at("19:04",'Europe/Moscow').do(job, type="cancer", group_id='229860780', tags=['#гороскоп', '#таро', '#таронамесяц', '#рак'])
    schedule.every().day.at("19:05",'Europe/Moscow').do(job, type="leo", group_id='229860665', tags=['#гороскоп', '#таро', '#таронамесяц', '#лев'])
    schedule.every().day.at("19:06",'Europe/Moscow').do(job, type="virgo", group_id='229860810', tags=['#гороскоп', '#таро', '#таронамесяц', '#дева'])
    schedule.every().day.at("19:07",'Europe/Moscow').do(job, type="libra", group_id='229860834', tags=['#гороскоп', '#таро', '#таронамесяц', '#весы'])
    schedule.every().day.at("19:08",'Europe/Moscow').do(job, type="scorpio", group_id='229860866', tags=['#гороскоп', '#таро', '#таронамесяц', '#скорпион'])
    schedule.every().day.at("19:09",'Europe/Moscow').do(job, type="sagittarius", group_id='229860894', tags=['#гороскоп', '#таро', '#таронамесяц', '#стрелец'])
    schedule.every().day.at("19:10",'Europe/Moscow').do(job, type="capricorn", chat_id='@capricorn_the', group_id='229837876', tags=['#гороскоп', '#таро', '#таронамесяц', '#козерог'])
    schedule.every().day.at("19:11",'Europe/Moscow').do(job, type="aquarius", chat_id='@aquarius_the', group_id='229837930', tags=['#гороскоп', '#таро', '#таронамесяц', '#водолей'])

    fifteen_minutes = 15 * 60

    for i in range(fifteen_minutes):
        schedule.run_pending()
        time.sleep(1)

