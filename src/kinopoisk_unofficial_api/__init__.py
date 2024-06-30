from typing import Literal, List

from aiohttp import ClientSession

from .sch_awards import Awards
from .sch_box_office import BoxOffice
from .sch_collections import Collections
from .sch_distributions import Distributions
from .sch_external_sources import ExternalSources
from .sch_facts import Facts
from .sch_films import Films
from .sch_filters import Filters
from .sch_images import Images
from .sch_information import Information
from .sch_keys import Keys
from .sch_news import News
from .sch_person import Person
from .sch_premieres import Premieres
from .sch_releases import Release
from .sch_reviews import Reviews
from .sch_search_by_keyword import SearchByKeyword
from .sch_seasons import Seasons
from .sch_sequels_and_prequels import SequelsAndPrequels
from .sch_similars import Similars
from .sch_staff import Staff
from .sch_staffs import Staffs
from .sch_videos import Videos

MONTHS = {
    1: 'JANUARY', 2: 'FEBRUARY', 3: 'MARCH', 4: 'APRIL',
    5: 'MAY', 6: 'JUNE', 7: 'JULY', 8: 'AUGUST',
    9: 'SEPTEMBER', 10: 'OCTOBER', 11: 'NOVEMBER', 12: 'DECEMBER'
}


class KinopoiskAPIUnofficial:
    URL: str = 'https://kinopoiskapiunofficial.tech/api'
    API_VERSION: str = 'v2.2'

    def __init__(self, token: str):
        self.token = token
        self.headers = {
            'X-API-KEY': token,
            'Content-Type': 'application/json',
        }
        self.server = f'{self.URL}/{self.API_VERSION}'

    async def request(self, url: str) -> dict | None:
        async with ClientSession(headers=self.headers) as session:
            async with session.get(url=url) as response:
                if response.status != 200:
                    return None
                return await response.json()

    async def films_information(self, kip: int) -> Information | None:
        """
        Возвращает базовые данные о фильме.
        Поле lastSync показывает дату последнего обновления данных.
        """
        url: str = f'{self.server}/films/{kip}'
        response = await self.request(url=url)
        return Information(**response) if response else None

    async def films_seasons(self, kip: int) -> Seasons | None:
        """Возвращает данные о сезонах для сериала."""
        url: str = f'{self.server}/films/{kip}/seasons'
        response = await self.request(url=url)
        return Seasons(**response) if response else None

    async def films_facts(self, kip: int) -> Facts | None:
        """
        Возвращает список фактов и ошибок в фильме.
        FACT, обозначает интересный факт о фильме.
        BLOOPER, обозначает ошибку в фильме.
        """
        url: str = f'{self.server}/films/{kip}/facts'
        response = await self.request(url=url)
        return Facts(**response) if response else None

    async def films_distributions(self, kip: int) -> Distributions | None:
        """Возвращает данные о прокате в разных странах."""
        url: str = f'{self.server}/films/{kip}/distributions'
        response = await self.request(url=url)
        return Distributions(**response) if response else None

    async def films_box_office(self, kip: int) -> BoxOffice | None:
        """Возвращает данные о бюджете и сборах."""
        url: str = f'{self.server}/films/{kip}/box_office'
        response = await self.request(url=url)
        return BoxOffice(**response) if response else None

    async def films_awards(self, kip: int) -> Awards | None:
        """Возвращает данные о наградах и премиях фильма."""
        url: str = f'{self.server}/films/{kip}/awards'
        response = await self.request(url=url)
        return Awards(**response) if response else None

    async def films_videos(self, kip: int) -> Videos | None:
        """
        Возвращает трейлеры, тизеры, видео для фильма по kinopoisk id. В данный момент доступно три site:
        YOUTUBE - в этом случае url это просто ссылка на youtube видео.
        YANDEX_DISK - в этом случае url это ссылка на yandex disk.
        KINOPOISK_WIDGET - в этом случае url это ссылка на кинопоиск виджет.
        """
        url: str = f'{self.server}/films/{kip}/videos'
        response = await self.request(url=url)
        return Videos(**response) if response else None

    async def films_similars(self, kip: int) -> Similars | None:
        """получить список похожих фильмов по kinopoisk film id"""
        url: str = f'{self.server}/films/{kip}/similars'
        response = await self.request(url=url)
        return Similars(**response) if response else None

    async def films_images(self, kip: int, pg: int = 1,
                           _type: Literal['STILL', 'SHOOTING', 'POSTER',
                           'FAN_ART', 'PROMO', 'CONCEPT', 'WALLPAPER',
                           'COVER', 'SCREENSHOT'] = 'SCREENSHOT') -> Images | None:
        """
        Возвращает изображения фильма с пагинацией. Каждая страница содержит не более чем 20 фильмов.
        Доступные изображения:
        STILL - кадры
        SHOOTING - изображения со съемок
        POSTER - постеры
        FAN_ART - фан-арты
        PROMO - промо
        CONCEPT - концепт-арты
        WALLPAPER - обои
        COVER - обложки
        SCREENSHOT - скриншоты

        Default value: SCREENSHOT
        """
        url: str = f'{self.server}/films/{kip}/images?type={_type}&page={pg}'
        response = await self.request(url=url)
        return Images(**response) if response else None

    async def films_reviews(self, kip: int, pg: int = 1,
                            order: Literal['DATE_ASC', 'DATE_DESC', 'USER_POSITIVE_RATING_ASC',
                            'USER_POSITIVE_RATING_DESC', 'USER_NEGATIVE_RATING_ASC',
                            'USER_NEGATIVE_RATING_DESC',] = 'DATE_DESC') -> Reviews | None:
        """
        Возвращает список рецензии зрителей с пагинацией. Каждая страница содержит не более чем 20 рецензий.
        Тип сортировки
        Available values:   DATE_ASC
                            DATE_DESC
                            USER_POSITIVE_RATING_ASC
                            USER_POSITIVE_RATING_DESC
                            USER_NEGATIVE_RATING_ASC
                            USER_NEGATIVE_RATING_DESC

        Default value: DATE_DESC
        """
        url: str = f'{self.server}/films/{kip}/reviews?page={pg}&order={order}'
        response = await self.request(url=url)
        return Reviews(**response) if response else None

    async def films_external_sources(self, kip: int, pg: int = 1) -> ExternalSources | None:
        """Возвращает список сайтов с пагинацией. Каждая страница содержит не более чем 20 рецензий."""
        url: str = f'{self.server}/films/{kip}/external_sources?page={pg}'
        response = await self.request(url=url)
        return ExternalSources(**response) if response else None

    async def films_collections(self, pg: int = 1,
                                _type: Literal['TOP_POPULAR_ALL', 'TOP_POPULAR_MOVIES',
                                'TOP_250_TV_SHOWS', 'TOP_250_MOVIES', 'VAMPIRE_THEME',
                                'COMICS_THEME', 'CLOSES_RELEASES', 'FAMILY', 'OSKAR_WINNERS_2021',
                                'LOVE_THEME', 'ZOMBIE_THEME', 'CATASTROPHE_THEME', 'KIDS_ANIMATION_THEME',
                                'POPULAR_SERIES',] = 'TOP_POPULAR_ALL') -> Collections | None:
        """
        Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов.
        Тип топа или коллекции
        Available values:
                        TOP_POPULAR_ALL
                        TOP_POPULAR_MOVIES
                        TOP_250_TV_SHOWS
                        TOP_250_MOVIES
                        VAMPIRE_THEME
                        COMICS_THEME
                        CLOSES_RELEASES
                        FAMILY
                        OSKAR_WINNERS_2021
                        LOVE_THEME
                        ZOMBIE_THEME
                        CATASTROPHE_THEME
                        KIDS_ANIMATION_THEME
                        POPULAR_SERIES

        Default value: TOP_POPULAR_ALL
        """
        url: str = f'{self.server}/films/collections?type={_type}&page={pg}'
        response = await self.request(url=url)
        return Collections(**response) if response else None

    async def films_premieres(self, year: int, month: int = 1) -> Premieres | None:
        """
        Возвращает список кинопремьер.
        Available values:
                        1. JANUARY
                        2. FEBRUARY
                        3. MARCH
                        4. APRIL
                        5. MAY
                        6. JUNE
                        7. JULY
                        8. AUGUST
                        9. SEPTEMBER
                        10. OCTOBER
                        11. NOVEMBER
                        12. DECEMBER

        Default value: 1
        """

        url: str = f'{self.server}/films/premieres?year={year}&month={MONTHS.get(month)}'
        response = await self.request(url=url)
        return Premieres(**response) if response else None

    async def films_filters(self) -> Filters | None:
        """Возвращает список id стран и жанров, которые могут быть использованы в /api/v2.2/films"""
        url: str = f'{self.server}/films/filters'
        response = await self.request(url=url)
        return Filters(**response) if response else None

    async def films(self,
                    countries: int | List[int] = None,
                    genres: int | List[int] = None,
                    order: Literal['RATING', 'NUM_VOTE', 'YEAR'] = 'RATING',
                    _type: Literal['ALL', 'FILM', 'TV_SHOW', 'TV_SERIES', 'MINI_SERIES'] = 'ALL',
                    min_rating: int = 0,
                    max_rating: int = 10,
                    year_from: int = 1000,
                    year_to: int = 3000,
                    keyword: str = None,
                    pg: int = 1) -> Films | None:
        """
        Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов.
        Данный эндпоинт не возращает более 400 фильмов.
        Используй films/filters что-бы получить id стран и жанров.
        :param countries:
        :param genres:
        :param order:
        :param _type:
        :param min_rating:
        :param max_rating:
        :param year_from:
        :param year_to:
        :param keyword:
        :param pg:
        :return:
        """
        url: str = (f'{self.server}/films?order={order}&type={_type}&ratingFrom={min_rating}&ratingTo={max_rating}&'
                    f'yearFrom={year_from}&yearTo={year_to}&page={pg}')
        if countries:
            if type(countries) is list:
                country = ''.join([f'&countries={i}' for i in countries])
                url += country
            else:
                url += f'&countries={countries}'
        if genres:
            if type(genres) is list:
                g = ''.join([f'&genres={i}' for i in genres])
                url += g
            else:
                url += f'&genres={genres}'

        if keyword:
            url += f'&keyword={keyword}'

        response = await self.request(url=url)
        return Films(**response) if response else None

    async def films_sequels_and_prequels(self, kip: int) -> SequelsAndPrequels | None:
        """Возвращает сиквел/приквел по кинопоиск ид"""
        url: str = f'{self.URL}/v2.1/films/{kip}/sequels_and_prequels'
        response = await self.request(url=url)
        return SequelsAndPrequels(**response) if response else None

    async def films_search_by_keyword(self, keyword: str, pg: int = 1) -> SearchByKeyword | None:
        """Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов."""
        url: str = f'{self.URL}/v2.1/films/search-by-keyword?keyword={keyword}&page={pg}'
        response = await self.request(url=url)
        return SearchByKeyword(**response) if response else None

    async def films_releases(self, year: int, month: int = 1, pg: int = 1) -> Release | None:
        """
        Возвращает список цифровых релизов.
        Например: https://www.kinopoisk.ru/comingsoon/digital/
        """
        url: str = f'{self.URL}/v2.1/films/releases?year={year}&month={MONTHS.get(month)}&page={pg}'
        response = await self.request(url=url)
        return Release(**response) if response else None

    async def staffs(self, kip: int) -> Staff | None:
        """
        Набор методов для работы с данными об актерах, режиссерах и т.д.
        """
        url: str = f'{self.URL}/v1/staff?filmId={kip}'
        response = await self.request(url=url)
        return Staff(**response) if response else None

    async def staff(self, person_id: int) -> Staffs | None:
        """
        Данные об актере, режиссере и т.д.
        """
        url: str = f'{self.URL}/v1/staff/{person_id}'
        response = await self.request(url=url)
        return Staffs(**response) if response else None

    async def person(self, name: str, pg: int = 1) -> Person | None:
        """
        Данные об актере, режиссере и т.д.
        """
        url: str = f'{self.URL}/v1/persons?name={name}&page={pg}'
        response = await self.request(url=url)
        return Person(**response) if response else None

    async def news(self, pg: int = 1) -> News | None:
        """
        Получить медиа новости с сайта кинопоиск
        Одна страница может содержать до 20 элементов в items.
        :param pg: Page default 1
        :return:
        """
        url: str = f'{self.URL}/v1/media_posts?page={pg}'
        response = await self.request(url=url)
        return News(**response) if response else None

    async def api_keys(self, api_keys: str = None) -> Keys | None:
        """
        API keys details
        """
        api_keys = self.token if api_keys is None else api_keys
        url: str = f'{self.URL}/v1/api_keys/{api_keys}'
        response = await self.request(url=url)
        return Keys(**response) if response else None
