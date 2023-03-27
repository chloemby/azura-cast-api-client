import json
from typing import List, Dict
from aiohttp import ClientSession


class AzuraCastApi:
    __host: str
    __api_key: str
    __client: ClientSession

    def __init__(self, host: str, api_key: str):
        self.__host = host
        self.__api_key = api_key
        self.__client = ClientSession(base_url=f"{host}/api", headers={"X-Auth-Key": api_key})

    async def now_playing(self) -> List[dict]:
        response = await self.__client.get('/nowplaying')

        return await response.json()

    async def now_playing_station(self, station_id: int) -> Dict:
        response = await self.__client.get(f"/nowplaying/{station_id}")

        return await response.json()

    async def upload_station_file(self, station_id: int, file_path: str, file_path_on_server: str) -> Dict:
        with open(file_path, 'r') as file:
            body = json.dumps({
                "path": file_path_on_server,
                "file": file
            })

            response = await self.__client.post(f"/station/{station_id}/file", body=body)

            return await response.json()

