import hashlib
from time import sleep


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Успешная авторизация под пользователем {nickname}")
                break
        else:
            print(f"Неверное имя пользователя или пароль")

    def register(self, nickname, password, age):
        hashed_password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        new_user = User(nickname=nickname, password=hashed_password, age=age)

        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        self.users.append(new_user)
        self.log_in(nickname, password)
        print(f"Регистрация прошла успешно! Вы вошли как {nickname}")

    def log_out(self):
        if self.current_user is not None:
            self.current_user = None
            print("Вы вышли из аккаунта")
        else:
            print("Вы не были авторизованы")

    def add(self, *videos):
        for video in videos:
            if not any(v.title.lower() == video.title.lower() for v in self.videos):
                self.videos.append(video)
            else:
                print(f"Видео '{video.title}' уже существует")

    def get_videos(self, search_word):
        search_results = [video.title for video in self.videos if search_word.lower() in video.title.lower()]
        return search_results

    def watch_video(self, video_title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        found_video = next((video for video in self.videos if video.title == video_title), None)

        if found_video is None:
            print(f"Видео '{video_title}' не найдено")
        elif found_video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            print(f"Воспроизведение видео: {video_title}")

            while found_video.time_now < found_video.duration:
                print(f"Секунда просмотра: {found_video.time_now}")
                found_video.time_now += 1
                sleep(1)

            print("Конец видео")
            found_video.time_now = 0


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.age = age
        self.password = password
        self.videos_uploaded = []

    def check_password(self, password):
        return self.password == int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def upload_video(self, urtube, video):
        if not isinstance(urtube, UrTube):
            raise TypeError("UrTube должен быть экземпляром класса UrTube")

        if not isinstance(video, Video):
            raise TypeError("Видео должно быть экземпляром класса Video")

        urtube.add(video)
        self.videos_uploaded.append(video)


class Video:
    def __init__(self, title, duration, author=None):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False
        self.author = author

    def set_adult_mode(self, mode=True):
        self.adult_mode = mode


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10)
v2.set_adult_mode(True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 8)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 32)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 99)
print(ur.current_user.nickname)