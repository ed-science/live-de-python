from multiprocessing.dummy import Pool
from shutil import copyfileobj

from requests import get
from uteis import days

days = list(
    map(lambda day: str(day) if len(str(day)) > 1 else f'0{str(day)}', days)
)


base_url = 'http://www.tjms.jus.br/cdje/downloadCaderno.do'
full_url = f'{base_url}?dtDiario=DAY/10/2017&cdCaderno=3&tpDownload=D'

files_list = [full_url.replace('DAY', day) for day in days]


def download_file(name, url):
    xpto = get(url, stream=True)
    with open(name, 'wb') as f:
        copyfileobj(xpto.raw, f)
    return True


nodes = Pool(8)

xpto = nodes.map_async(
    lambda x: download_file(f'{x[0]}.pdf', x[1]), zip(days, files_list)
)


xpto.wait()
